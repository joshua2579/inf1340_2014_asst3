__author__ = 'Alex Goel, Joshua Liben, Kristina Mitova'


import json


class StockMiner:
    """

    """
    def __init__(self, name, stock_file_name):
        """

        :param name:
        :param stock_file_name:
        :return:
        """
        self.name = name
        self.stock_file_name = stock_file_name
        self.monthly_averages = {}

    def read_json_from_file(self):
        try:
            with open(self.stock_file_name) as file_handle:
                file_contents = file_handle.read()
        except FileNotFoundError:
            raise FileNotFoundError("Cannot find file:" + self.stock_file_name)

        return json.loads(file_contents)

    def month_averages(self):
        """

        :return:
        """
        stock_info = self.read_json_from_file()
        for day in stock_info:
            #Parse date into list of 3 strings for Year, Month, Day.
            stock_date_split = day["Date"].split("-")
            stock_year_month = stock_date_split[0]+"/"+stock_date_split[1]

            if stock_year_month in self.monthly_averages:
                total_sales = self.monthly_averages[stock_year_month][0]
                total_volume = self.monthly_averages[stock_year_month][1]
                self.monthly_averages[stock_year_month] = \
                    (total_sales + day["Volume"]*day["Close"], total_volume + day["Volume"])
            else:
                self.monthly_averages[stock_year_month] = ((day["Volume"] * day["Close"]), day["Volume"])

        for year_month, sales_and_volume in self.monthly_averages.items():
            self.monthly_averages[year_month] = float("%.2f" % float(sales_and_volume[0]/sales_and_volume[1]))

        return
