from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DecimalField
from value_investing_strategy.strategy_system.StrategySystem import StrategySystem


class SelectStockForm(FlaskForm):
    stock_list = StrategySystem.get_available_stocks()
    stock = SelectField("Stock", choices=stock_list)
    submit = SubmitField("submit")


class SelectFundamentalAnalysis(SelectStockForm):

    options = SelectField(
        "Analysis",
        choices=["Company Overview", "Earnings", "Cash Flow", "Balance Sheet"]
    )
    submit = SubmitField("submit")


class RebalancePortfolio(FlaskForm):

    stock_list = StrategySystem.get_available_stocks()

    stock_1 = SelectField("Stock", choices=stock_list)
    num_shares_1 = DecimalField("Number of Shares")
    target_weight_1 = DecimalField("Target Weight")

    stock_2 = SelectField("Stock", choices=stock_list)
    num_shares_2 = DecimalField("Number of Shares")
    target_weight_2 = DecimalField("Target Weight")
    submit = SubmitField("submit")

    stock_3 = SelectField("Stock", choices=stock_list)
    num_shares_3 = DecimalField("Number of Shares")
    target_weight_3 = DecimalField("Target Weight")

    submit = SubmitField("submit")
