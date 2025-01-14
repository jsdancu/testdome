import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    """
    :param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the new campaign.
    :returns: (float) Required amount of money to be invested.
    """
    plt.plot(units_sold, marketing_expenditure, '.')
    plt.xlabel("Units sold")
    plt.ylabel("Marketing expenditure")
    plt.title("Sold vs marketing")
    #plt.show()
    plt.savefig("marketing_costs.pdf")

    reg = linear_model.LinearRegression().fit(np.array(units_sold).reshape(-1, 1), np.array(marketing_expenditure).reshape(-1, 1))
    predicted = reg.predict([[desired_units_sold]])
    return predicted[0][0]

#For example, with the parameters below, the function should return 250000.0
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))