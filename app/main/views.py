from flask import render_template, abort
from . import main
from ..models import User
from .forms import SelectStockForm, SelectFundamentalAnalysis
from .utils import snake_to_regular_dict, sort_by_date
from value_investing_strategy.strategy_system.stocks.stock.Stock import Stock


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/user/<username>")
def user(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404)

    print(user.member_since)

    return render_template("user.html", user=user)


@main.route("/cgn", methods=["GET", "POST"])
def calculate_graham_number():
    form = SelectStockForm()

    if form.validate_on_submit():
        stock_ticker = form.stock.data
        stock = Stock.from_alpha_vantage_data(stock_ticker)
        graham_number = stock.graham_number
        return render_template(
            "display_cgn.html", stock=stock_ticker, graham_number=graham_number
        )

    return render_template("cgn.html", form=form)


@main.route("/fund_analysis", methods=["GET", "POST"])
def fundamental_analysis():
    form = SelectFundamentalAnalysis()

    if form.validate_on_submit():
        stock_ticker = form.stock.data
        stock = Stock.from_alpha_vantage_data(stock_ticker)
        option = form.options.data

        if option == "Company Overview":

            company_overview = snake_to_regular_dict(vars(stock.company_overview))
            return render_template(
                "display_fund_analysis.html",
                company_overview=company_overview
            )
        elif option == "Balance Sheet":
            reports = []
            for annual_report in stock.balance_sheet.annual_reports:
                reports.append(vars(annual_report))
            headers = list(reports[0].keys())
            clean_headers = [header.replace('_', ' ').title() for header in headers]
            dates = [report["fiscal_date_ending"] for report in reports]
            return render_template(
                "display_balance_sheet.html",
                reports=reports,
                dates=dates,
                all_header=zip(headers[1:], clean_headers[1:])
            )
        elif option == "Cash Flow":
            anual_reports = []
            quaterly_reports = []

            for annual_report in stock.balance_sheet.annual_reports:
                anual_reports.append(vars(annual_report))

            for quaterly_report in stock.cash_flow.quarterly_reports:
                quaterly_reports.append(vars(quaterly_report))

            anual_reports = sort_by_date(anual_reports, "fiscal_date_ending")
            quaterly_reports = sort_by_date(quaterly_reports, "fiscal_date_ending")

            headers = list(anual_reports[0].keys())
            clean_headers = [header.replace('_', ' ').title() for header in headers]

            q_headers = list(quaterly_reports[0].keys())
            q_clean_headers = [header.replace('_', ' ').title() for header in q_headers]

            anual_dates = [ar["fiscal_date_ending"] for ar in anual_reports]
            quaterly_dates = [qa["fiscal_date_ending"] for qa in quaterly_reports]

            return render_template(
                "display_cash_flow.html",
                anual_reports=anual_reports,
                quaterly_reports=quaterly_reports,
                anual_dates=anual_dates,
                quaterly_dates=quaterly_dates,
                all_header=zip(headers[1:], clean_headers[1:]),
                quaterly_header=zip(q_headers[1:], q_clean_headers[1:]),
                stock=stock.ticker
            )

    return render_template("fund_analysis.html", form=form)
