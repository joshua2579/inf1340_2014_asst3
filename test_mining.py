#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
from mining import *
import pytest

# Tests to add:
# What if there is a tie for the sixth ****st month? (show most recent one or something)
#


def test_goog():
    read_stock_data("GOOG", "data/GOOG.json")
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                 ('2008/05', 576.29), ('2008/06', 555.34)]
    assert six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09),
                                   ('2004/12', 181.01), ('2005/03', 181.18)]

def test_tseso():
    read_stock_data("TSE-SO", "data/TSE-SO.json")
    assert six_best_months() == [('2007/12', 20.98), ('2007/11', 20.89), ('2013/05', 19.96), ('2013/06', 19.94),
                                 ('2013/04', 19.65), ('2007/10', 19.11)]
    assert six_worst_months() == [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/02', 2.41),
                                  ('2009/04', 2.75), ('2009/01', 3.14)]

def test_less_than_five():
    read_stock_data("lt5", "data/only_five_months.json")
    assert six_best_months() == [('2008/09', 449.15), ('2008/12', 442.93), ('2008/10', 439.08),
                                 ('2008/08', 433.86), ('2008/11', 414.49)]
    assert six_worst_months() == [('2008/11', 414.49), ('2008/08', 433.86), ('2008/10', 439.08),
                                  ('2008/12', 442.93), ('2008/09', 449.15)]


def test_files():
    with pytest.raises(FileNotFoundError):
        read_stock_data("GOOG", "data/LOLZ.json")


def test_no_volume():
    with pytest.raises(ValueError):
        read_stock_data("NoV", "data/volume_is_missing.json")


def test_missing_date():
    with pytest.raises(ValueError):
        read_stock_data("dateic", "data/date_is_corrupt.json")


def test_close_missing():
    with pytest.raises(ValueError):
        read_stock_data("cis", "data/close_missing.json")

def test_data_corrupt():
    with pytest.raises(ValueError):
        read_stock_data("dcorrupt", "data/data_is_corrupt.json")

def test_bad_date_format():
    with pytest.raises(ValueError):
        read_stock_data("bad_date", "data/date_is_incorrect")
        


