#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import datetime
from StockMiner import StockMiner


def read_stock_data(stock_name, stock_file_name):
    """

    :param stock_name:
    :param stock_file_name:
    :return:
    """

    global stock
    stock = StockMiner(stock_name, stock_file_name)
    stock.monthly_averages()


def six_months(sort_order):
    """

    :param sort_order:
    :return:
    """

    results = []
    list_averages = []
    if sort_order == "descending":
        sort_order = False
    elif sort_order == "ascending":
        sort_order = True
    else:
        raise ValueError("Unexpected sort order.")

    for sales_average in stock.monthly_averages.values():
        list_averages.append(sales_average)
    list_averages.sort(reverse=sort_order)

def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]




