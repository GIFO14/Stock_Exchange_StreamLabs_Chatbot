# ----------------------------------
# @author GIFO ---------------------
# ----------------------------------

# ----------------------------------
# Imports
# ----------------------------------

import random
import datetime

# ----------------------------------
# Global variable declarations
# ----------------------------------

g_companies = []
g_buyers = []
g_percentage_of_bank_interest_per_real_life_month = 7

# ----------------------------------
# Classes
# ----------------------------------

class Loan(object):

    def __init__(self, _money_quantity, _bank_interest, date): # float, float
        self.money_quantity = _money_quantity
        self.bank_interest = _bank_interest


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
        self.loan = []
        self.percentages_bought = []


class Percentage(object):

    def __init__(self, _company, _company_part_bought): # string, float
        self.which_company = _company
        self.company_part_bought = _company_part_bought

class Bank:

    number_of_loan_given = 0
    money = 9*10**9 # 9 000 000 000


# ----------------------------------
# Necessary Functions
# ----------------------------------

def Create_Company(_name, _owner, _company_value):  # string, float

    method_temporary_company = Company(_name, _owner, _company_value)
    g_companies[len(g_companies)] = method_temporary_company


def Varies_companies_value(_max_times_increase_or_decrease_company_value):  # int

    for current_company_in_array in g_companies:
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

    for company in g_companies:

        if company.name == _company_name:
            company_part_bought = company.company_value * _percentage / 100

            for buyer in g_buyers:

                if buyer.name == _buyer_name:

                    try:
                        buyer.money -= company_part_bought

                    except:
                        print('Not enough money to buy')

                    percentage = Percentage(_company_name, company_part_bought)
                    buyer.percentages_bought[len(buyer.percentages_bought)] = percentage


def Sell_company(_company_name, _buyer_name): # string, string

    index_percentage_array = 0

    for company in g_companies:

        if company.name == _company_name:

            for seller in g_buyers:

                if seller.name == company.owner:

                    for buyer in g_buyers:

                        if buyer.name == _buyer_name:

                            for percentage in seller.percentages_bought:

                                if percentage.which_company == _company_name:

                                    try:
                                        buyer.money -= percentage.company_part_bought
                                        seller.money += percentage.company_part_bought
                                        del seller.percentages_bought[index_percentage_array]
                                        company.owner = _buyer_name

                                    except:
                                        print('Error in selling company')

                                index_percentage_array += 1


def Provide_loan(_buyer_name, _loan_quantity): # string, float

    for buyer in g_buyers:

        if buyer.name == _buyer_name:

            Bank.money -= _loan_quantity
            Bank.number_of_loan_given += 1

            loan = Loan(_loan_quantity, Create_bank_interest(_loan_quantity), datetime.datetime.now())
            buyer.loan[len(buyer.loan)] = loan
            buyer.money += _loan_quantity


def Create_bank_interest(loan): # float

    return loan * g_percentage_of_bank_interest_per_real_life_month / 100