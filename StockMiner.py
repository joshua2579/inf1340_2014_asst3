__author__ = 'Alex Goel, Joshua Liben, Kristina Mitova'

import json
import datetime


class StockMiner:
    """
    This class creates a stockminer object that is used to calculate the monthly averages of a stock file.
    """

    def __init__(self, name, stock_file_name):
        """
        Initializes the stockminer object
        :param name: The name of the stock
        :param stock_file_name: The filepath of the stock information
        :return: A stockminer Object
        """
        self.name = name
        self.stock_file_name = stock_file_name
        self.monthly_averages = {}

    def valid_date_format(self, date_string):
        """
        Checks whether a date has the format YYYY-mm-dd in numbers
        :param date_string: date to be checked
        :return: Boolean True if the format is valid, False otherwise
        """
        try:
            datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def read_json_from_file(self):
        """
        Reads the contents of the JSON file
        :return: The loaded JSON object
        """
        try:
            with open(self.stock_file_name) as file_handle:
                file_contents = file_handle.read()
        except FileNotFoundError:
            raise FileNotFoundError("Cannot find file:" + self.stock_file_name)
        except ValueError:
            raise ValueError("File format is incorrect.")

        return json.loads(file_contents)

    def month_averages(self):
        """
        Calculates the monthly averages for the JSON file object.
        :return: A dictionary of key: month to value: average.
        """
        stock_info = self.read_json_from_file()
        for day in stock_info:
            # Parse date into list of 3 strings for Year, Month, Day.
            if "Date" in day:
                if self.valid_date_format(day["Date"]):
                    stock_date_split = day["Date"].split("-")
                    stock_year_month = stock_date_split[0] + "/" + stock_date_split[1]
                else:
                    raise ValueError("Date is incorrect format")
            else:
                raise ValueError("Date is missing from the JSON file")

            # Update an existing month in the dictionary
            if "Close" in day:
                if "Volume" in day:
                    if stock_year_month in self.monthly_averages:
                        total_sales = self.monthly_averages[stock_year_month][0]
                        total_volume = self.monthly_averages[stock_year_month][1]
                        self.monthly_averages[stock_year_month] = \
                            (total_sales + day["Volume"] * day["Close"], total_volume + day["Volume"])
                    else:
                        self.monthly_averages[stock_year_month] = ((day["Volume"] * day["Close"]), day["Volume"])
                else:
                    raise ValueError("Volume is missing from the JSON file")
            else:
                raise ValueError("Close is missing from the JSON file")

        # Calculate the averages based on sales and volume and convert to two decimal float.
        for year_month, sales_and_volume in self.monthly_averages.items():
            self.monthly_averages[year_month] = float("%.2f" % float(sales_and_volume[0] / sales_and_volume[1]))
        return
