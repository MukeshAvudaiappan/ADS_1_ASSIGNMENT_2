#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:37:07 2023

@author: mukeshavudaiappan
"""

#Importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Global variable to store selected countries
countries = ['Pakistan', 'Sri Lanka', 'India', 'Afghanistan', 'Vietnam']


#Functions
#Function to read the csv file to the dataframe

def read_file(filename):
    """
    Parameters
    ----------
    filename : csv file
    Returns
    -------
    df : dataframe with years as columns
    df_transpose : dataframe with countries as columns
    """
    df = pd.read_csv(filename)
    # transposing the dataframe keeping 'Country Name' as index
    df_transpose = df.set_index('Country Name').transpose()
    return df, df_transpose

#Function to filter out 5 countries to perform the analysis into line plot

def filter_lineplot_data(df):
    """
    Parameters
    ----------
    df : dataframe with years as columns
    Returns
    -------
    df : filtered dataframe to plot line graph of the below mentioned countries
    """
    df = df[['Country Name', 'Indicator Name',
             '2000', '2005', '2010', '2015', '2020']]
    df = df[(df["Country Name"] == "Pakistan") |
            (df["Country Name"] == "Sri Lanka") |
            (df["Country Name"] == "India") |
            (df["Country Name"] == "Afghanistan") |
            (df["Country Name"] == "Vietnam")]
    return df

#Reading data from csv file to two dataframes using the function read_file(filename)

CO2_emission, CO2_emission_transpose = read_file("co2_emission.csv")
CO2emission = filter_lineplot_data(CO2_emission)
CO2emission.iloc[:,2:] = CO2emission.iloc[:,2:]/1000000
CO2_emission = CO2emission

access_to_ele, access_to_ele_trans = read_file('access_to_electricity.csv')
access_to_ele = filter_lineplot_data(access_to_ele)

# Function to plot line graph

def line_plot(df, label1, label2):
    """
    Parameters
    ----------
    df : filtered dataframe to plot line graph of the selected countries
    label1 : string to label y-axis
    label2 : string to display the title of line graph
    Returns
    -------
    None.
    """

    plt.figure(figsize=(20, 15), layout = 'constrained')
    plt.rcParams['font.size'] = 20
    data = df.set_index('Country Name')
    transpose = data.transpose()
    transpose = transpose.drop(index=['Indicator Name'])
    for i in range(len(countries)):
        plt.plot(transpose.index, transpose[countries[i]], label=countries[i])
    plt.title(label2, size=20)
    plt.xlabel("Year", size=20)
    plt.ylabel(label1, size=20)
    plt.grid('True')
    plt.xticks(rotation=50)
    plt.legend(fontsize=25)
    plt.savefig("lineplot.png")
    plt.show()
    plt.close()
    
# Plotting line graph for forest area and population growth to analyse

line_plot(CO2_emission,
          "CO2 Emission in KT", "CO2 Emissions")
line_plot(access_to_ele,
          "Access to electricity (% of population)", "Access to electricity")
    