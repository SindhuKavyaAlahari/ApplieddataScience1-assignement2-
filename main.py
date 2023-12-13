#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:54:07 2023
@author: Sindhu Kavya Alahari
"""

"""
# Importing Required Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

def Ingest_and_manipulate_data(filepath):
    """
        Load a CSV file into a pandas DataFrame,
        create a reversed DataFrame, and clean the data by dropping NaN values.

        Parameters:
        - filepath (str): The file path to the CSV file.

        Returns:
        - df (pd.DataFrame): Original DataFrame loaded from the CSV file.
        - transposed (pd.DataFrame): Reversed DataFrame with 'Country Name' and
        'Time' columns swapped.
        - cleanedDataset (pd.DataFrame): DataFrame with NaN values dropped.
    """
    df = pd.read_csv(filepath)
    transposed = df.copy()
    transposed[['Country Name' , 'Time']] = transposed[['Time' , 'Country Name']]
    transposed = transposed.rename(columns={'Country Name': 'Time' , 'Time': 'Country Name'})
    cleanedDataset = transposed.dropna()
    return df , transposed , cleanedDataset


def centralGovernementDebt(data):
    """
        Create a line graph to visualize the central government debt as a percentage of
        GDP over time for different countries.

        Parameters:
        - data (pd.DataFrame): DataFrame containing data for central government debt,
        GDP percentage, and time for different countries.

        Returns:
        None
    """
    # Set Seaborn style
    sns.set(style="whitegrid")
    # Plotting a line graph for each country using Seaborn
    plt.figure(figsize=(10 , 6))
    sns.lineplot(x='Time' , y='Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]' ,
                 hue='Country Name' ,
                 data=data , marker='o')

    plt.title('Central Government Debt (% of GDP) Over Time' , fontsize=17)
    plt.xlabel('Year')
    plt.ylabel('Central Government Debt (% of GDP)')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


def IntrestPayments(corrMat):
    """
        Create a heatmap to visualize the correlation matrix between Interest
        Payments (% of Expense) and Interest Payments (% of Revenue).

        Parameters:
        - corrMat (pd.DataFrame): Correlation matrix DataFrame.

        Returns:
        None
    """
    # Set Seaborn style
    sns.set(style="white")

    # Create a heatmap for the correlation matrix
    plt.figure(figsize=(8 , 6))
    sns.heatmap(corrMat , annot=True , cmap='coolwarm' , fmt=".2f" , linewidths=.5)

    plt.title('Correlation Matrix: Interest Payments (% of Expense) vs. Interest Payments (% of Revenue)' ,
              fontsize=17)
    plt.show()


def compenstaionOfEmployee(data):
    """
        Create a pie chart to visualize the distribution of Compensation of
        Employees as a percentage of expense by country.

        Parameters:
        - data (pd.DataFrame): DataFrame containing data for Compensation of
        Employees, country names, and other relevant information.

        Returns:
        None
    """
    sns.set(style="whitegrid")
    # Plotting a pie chart for the distribution of compensation of employees by country
    plt.figure(figsize=(8 , 8))
    plt.pie(data['Compensation of employees (% of expense) [GC.XPN.COMP.ZS]'] ,
            labels=data['Country Name'] , autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart: Compensation of Employees (% of Expense) by Country' , fontsize=17)
    plt.show()


def goodsAndGrantsGraph(data):
    """
        Create a grouped bar graph to compare Goods and Services Expense (% of Expense)
        and Grants and Other Revenue (% of Revenue) over time.

        Parameters:
        - data (pd.DataFrame): DataFrame containing data for Goods and
        Services Expense, Grants and Other Revenue, and time information.

        Returns:
        None
    """

    bar_width = 0.35
    bar_positions_goods = data['Time'] - bar_width / 2
    bar_positions_grants = data['Time'] + bar_width / 2

    # Plotting bar graph
    plt.figure(figsize=(12, 8))
    plt.bar(bar_positions_goods ,
            data['Goods and services expense (% of expense) [GC.XPN.GSRV.ZS]'] ,
            width=bar_width ,
            label='Goods and services expense', color='pink')
    plt.bar(bar_positions_grants ,
            data['Grants and other revenue (% of revenue) [GC.REV.GOTR.ZS]'] ,
            width=bar_width ,
            label='Grants and other revenue' , color='red')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title('Goods and services expense Vs Grants and other revenue' , fontsize=17)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()


def IntrestPaymentsExpense(data):
    """
        Create a line graph to visualize Interest Payments (% of Expense)
        by country over time.

        Parameters:
        - data (pd.DataFrame): DataFrame containing data for Interest Payments
        (% of Expense) and time information.

        Returns:
        None
    """
    # Plotting a line graph for customs and other import duties by country
    # over time using Matplotlib
    plt.figure(figsize=(10 , 6))

    for country , group in data.groupby('Country Name'):
        plt.plot(group['Time'] , group['Interest payments (% of expense)'] ,
                 label=country , marker='o')

    plt.title('Interest payments (% of expense)' , fontsize=17)
    plt.xlabel('Year')
    plt.ylabel('Interest payments (% of expense)')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


def IntrestPaymentrevenue(data):
    """
        Create a pie chart to visualize Interest Payments (% of Revenue) in 2020 by country.

        Parameters:
        - data (pd.DataFrame): DataFrame containing data for Interest Payments (
        % of Revenue) and country information.

        Returns:
        None
    """
    plt.figure(figsize=(8 , 8))
    plt.pie(data['Interest payments (% of revenue)'] , labels=data['Country Name'] ,
            autopct='%1.1f%%' , startangle=140)
    plt.title('Interest Payments (% of Revenue) in 2020 by Country' , fontsize=17)
    plt.show()


TimeColumnData , CountryColumnData , cleanedData = \
    Ingest_and_manipulate_data('sindhuData.csv')
print("Year as column Data")
print(TimeColumnData.head())
print("Country as column data")
print(CountryColumnData.head())
print("cleaned dataset")
print(cleanedData.head())

"Exploring the statistical properties"
print("1. Describe ")
CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'] = \
    pd.to_numeric(CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'] ,
                  errors='coerce')
describeStats = CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'].\
    describe()
print(describeStats)

print("2. Mode")
mode = CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'].\
    mode()
print("mode of Central government debt, total is " , mode)

print("3. Skewness")
skewness = CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'].\
    skew()
print("skewness of Central government debt, total is" , skewness)

#Visualizations
# Central Governement Debt
CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'] = \
    pd.to_numeric(CountryColumnData['Central government debt, total (% of GDP) [GC.DOD.TOTL.GD.ZS]'] ,
                  errors='coerce')

centralGovernementDebt(CountryColumnData)

# Convert columns to numeric (replace '..' with NaN)
CountryColumnData['Interest payments (% of expense)'] = \
    pd.to_numeric(CountryColumnData['Interest payments (% of expense)'] ,
                  errors='coerce')
CountryColumnData['Interest payments (% of revenue)'] = \
    pd.to_numeric(CountryColumnData['Interest payments (% of revenue)'] ,
                  errors='coerce')

# Select relevant columns for correlation matrix
correlation_data = CountryColumnData[['Interest payments (% of expense)',
                                      'Interest payments (% of revenue)']]

# Compute the correlation matrix
correlation_matrix = correlation_data.corr()
IntrestPayments(correlation_matrix)

IntrestedCountries = ['Canada' , 'India' , 'Switzerland' , 'Sweden' , 'Spain' ,
                      'Finland' , 'France']
compenstaionData = CountryColumnData[CountryColumnData['Time'] == '2017']
compenstaionData = compenstaionData[compenstaionData['Country Name']
.isin(IntrestedCountries)]
print(compenstaionData)

compenstaionOfEmployee(compenstaionData)

CountryColumnData['Goods and services expense (% of expense) [GC.XPN.GSRV.ZS]'] = \
    pd.to_numeric(CountryColumnData['Goods and services expense (% of expense) [GC.XPN.GSRV.ZS]'] ,
                  errors='coerce')
CountryColumnData['Grants and other revenue (% of revenue) [GC.REV.GOTR.ZS]'] = \
    pd.to_numeric(CountryColumnData['Grants and other revenue (% of revenue) [GC.REV.GOTR.ZS]'] ,
                  errors='coerce')
CountryColumnData['Time'] = pd.to_numeric(CountryColumnData['Time'] ,
                                          errors='coerce')
goodsAndGrantsData = CountryColumnData[(CountryColumnData['Time'] >= 2015) &
                                       (CountryColumnData['Time'] <= 2020)]
goodsAndGrantsGraph(goodsAndGrantsData)

# Convert 'Customs and other import duties (current LCU)' to numeric (replace None with NaN)
CountryColumnData['Interest payments (% of expense)'] = \
    pd.to_numeric(CountryColumnData['Interest payments (% of expense)'] ,
                  errors='coerce')
IntrestPaymentsExpense(CountryColumnData)

pieData = CountryColumnData[CountryColumnData['Time'] == 2020]
IntrestPaymentrevenue(pieData)



