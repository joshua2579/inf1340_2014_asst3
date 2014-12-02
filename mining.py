#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim, Joshua Liben, Alex Goel, Kristina Mitova'

# imports one per line
from StockMiner import StockMiner


def read_stock_data(stock_name, stock_file_name):
    """
    Reads the stock data from the stock files and runs the function for
    Calculating monthly averages.
    :param stock_name: The name of the stock
    :param stock_file_name: The filename of the stock information
    """

    global stock
    stock = StockMiner(stock_name, stock_file_name)
    stock.month_averages()
    return


def six_months(sort_order):
    """
    Sorts the monthly averages into a list based on sort_order
    :param sort_order: Tells whether to sort ascending or descending
    :return: The list of the six worst or best months (depending on sort_order)
    """

    results = []
    list_of_averages = []

    # Prepares sort_order for function use
    if sort_order == "descending":
        sort_order = False
    elif sort_order == "ascending":
        sort_order = True
    else:
        raise ValueError("Unexpected sort order.")

    # Gets six worst or best months from the dictionary of averages
    for sales_average in stock.monthly_averages.values():
        list_of_averages.append(sales_average)
    list_of_averages.sort(reverse=sort_order)
    for this_average in list_of_averages[:6]:
        for year_month, sales_average in stock.monthly_averages.items():
            if this_average == sales_average:
                results.append((year_month, sales_average))
    return results


def six_best_months():
    """
    Gets the six best monthly averages
    :return: the six_months in ascending order (six best months)
    """
    return six_months("ascending")


def six_worst_months():
    """
    Gets the six worst monthly averages
    :return: the six_months in descending order (six best months)
    """
    return six_months("descending")