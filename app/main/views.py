from pathlib import Path
from flask import render_template, abort
from . import main
from ..models import User
from .forms import SelectStockForm
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
def fundamental_analysis():
    form = SelectStockForm()

    if form.validate_on_submit():
        data_path = Path("scripts/SimpleAlphaVantageCacher/output/json_cache/DATA")
        stock_ticker = form.stock.data
        stock = Stock.from_alpha_vantage_data(stock_ticker, data_path)
        graham_number = stock.graham_number
        return render_template(
            "display_cgn.html", stock=stock_ticker, graham_number=graham_number
        )

    return render_template("cgn.html", form=form)
