# ----------------------------------
# @author GIFO ---------------------
# ----------------------------------

# ----------------------------------
# Imports
# ----------------------------------

import random

# ----------------------------------
# Global variable declarations
# ----------------------------------

companies = []
buyers = []

# ----------------------------------
# Classes
# ----------------------------------

class Company(object):

    def __init__(self, _name, _owner, _company_value): # string, string, float
        self.name = _name
        self.owner = _owner
        self.company_value = _company_value
        self.number_of_changes_positive_or_negative = 0


class Buyer(object):

    def __init__(self, _name, _money): # string
        self.name = _name
        self.money = _money
        self.percentages_bought = []


class Percentage(object):

    def __init__(self, _company, _company_part_bought): # string, float
        self.which_company = _company
        self.company_part_bought = _company_part_bought


# ----------------------------------
# Necessary Functions
# ----------------------------------

def Create_Company(_name, _owner, _company_value):  # string, float

    method_temporary_company = Company(_name, _owner, _company_value)
    companies[len(companies)] = method_temporary_company


def Varies_companies_value(_max_times_increase_or_decrease_company_value):  # int

    for current_company_in_array in companies:
        random_percentage = random.uniform(0, 10)

        if current_company_in_array.number_of_changes_of_same_type <= _max_times_increase_or_decrease_company_value and current_company_in_array.number_of_changes_of_same_type >= -_max_times_increase_or_decrease_company_value:
            random_percentage = random.uniform(-10, 10)
            current_company_in_array.company_value += random_percentage * 100 / current_company_in_array.company_value

            if current_company_in_array.number_of_changes_positive_or_negative <= 0 and random_percentage < 0:
                current_company_in_array.number_of_changes_positive_or_negative -= 1

            elif current_company_in_array.number_of_changes_positive_or_negative >= 0 and random_percentage > 0:
                current_company_in_array.number_of_changes_positive_or_negative += 1

        elif current_company_in_array.number_of_changes_of_same_type > _max_times_increase_or_decrease_company_value:
            current_company_in_array.company_value -= random_percentage * 100 / current_company_in_array.company_value
            current_company_in_array.number_of_changes_positive_or_negative -= 1

        elif current_company_in_array.number_of_changes_of_same_type < -_max_times_increase_or_decrease_company_value:
            current_company_in_array.company_value += random_percentage * 100 / current_company_in_array.company_value
            current_company_in_array.number_of_changes_positive_or_negative += 1


def Buy_percentage_of_company(_percentage, _company_name, _buyer_name):  # float, string, string

    for company in companies:

        if company.name == _company_name:
            company_part_bought = company.company_value * _percentage / 100

            for buyer in buyers:

                if buyer.name == _buyer_name:

                    try:
                        buyer.money -= company_part_bought

                    except:
                        print('Not enough money to buy')

                    percentage = Percentage(_company_name, company_part_bought)
                    buyer.percentages_bought[len(buyer.percentages_bought)] = percentage


def Sell_company(_company_name, _buyer_name):

    for company in companies:

        if company.name == _company_name:

            for seller in buyers:

                if seller.name == company.owner:

                    for buyer in buyers:

                        if buyer.name == _buyer_name:

                            for percentage in seller.percentages_bought:

                                if percentage.which_company == _company_name:

                                    try:
                                        buyer.money -= percentage.company_part_bought
                                        seller.money += percentage.company_part_bought
                                        seller
