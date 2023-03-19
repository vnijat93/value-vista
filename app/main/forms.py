from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from value_investing_strategy.strategy_system.StrategySystem import StrategySystem


class SelectStockForm(FlaskForm):
    stock_list = StrategySystem.get_available_stocks()

    stock = SelectField("Stock", choices=stock_list)
    submit = SubmitField("submit")
