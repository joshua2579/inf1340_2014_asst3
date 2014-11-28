#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
from StockMiner import StockMiner


def read_stock_data(stock_name, stock_file_name):
    """

    :param stock_name:
    :param stock_file_name:
    :return:
    """

    global stock
    stock = StockMiner(stock_name, stock_file_name)
    stock.month_averages()


def six_months(sort_order):
    """

    :param sort_order:
    :return:
    """

    results = []
    list_of_averages = []
    if sort_order == "descending":
        sort_order = False
    elif sort_order == "ascending":
        sort_order = True
    else:
        raise ValueError("Unexpected sort order.")

    for sales_average in stock.monthly_averages.values():
        list_of_averages.append(sales_average)
    list_of_averages.sort(reverse=sort_order)
    for this_average in list_of_averages[:6]:
        for year_month, sales_average in stock.monthly_averages.items():
            if this_average == sales_average:
                results.append((year_month, sales_average))
    return results


def six_best_months():
    return six_months("ascending")


def six_worst_months():
    return six_months("descending")

read_stock_data("TSE-SO", "data/only_five_months.json")
print(six_months("ascending"))
print(six_months("descending"))





