#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:13:47 2023

@author: mukeshavudaiappan
"""

#Importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Variable to store selected countries

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


#Function to filter out 5 countries to perform the analysis into bar plot

def filter_barplot_data(df):
    """
    Parameters
    ----------
    df : dataframe with years as columns
    Returns
    -------
    df : filtered dataframe to plot bar graph of the below mentioned countries
    """
    df = df[['Country Name', 'Indicator Name', '2010', '2015', '2020']]
    df = df[(df["Country Name"] == "Pakistan") |
            (df["Country Name"] == "Sri Lanka") |
            (df["Country Name"] == "India") |
            (df["Country Name"] == "Afghanistan") |
            (df["Country Name"] == "Vietnam")]
    return df


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

# Function to calculate the mean of CO2 emission in 5 selected countries

def co2_emission_mean():
    """
    Returns
    -------
    mean : dataframe with average CO2 emission of 5 countries
    """
    # reading dataframes from CO2 emission dataset
    df1, df2 = read_file("CSV_Files/co2_emission.csv")
    # processing the dataframe to calculate mean of CO2 eimssion over the years
    data = df1.set_index('Country Name')
    transpose = data.transpose()
    # dropping irrelevent coloumns
    transpose = transpose.drop(index='Indicator Name')
    transpose = transpose.drop(index='Country Code')
    transpose = transpose.drop(index='Indicator Code')
    # replacing NaN values with 0 for calculating average emission
    cleaned_data = transpose.fillna(0)
    mean = cleaned_data[['Pakistan', 'Sri Lanka', 'India', 'Afghanistan', 'Vietnam']].mean()
    return mean


#Reading data from csv file to two dataframes using the function read_file(filename)

forest_area, forest_area_transpose = read_file('CSV_Files/forest_area.csv')
forest_area = filter_barplot_data(forest_area)

population_growth, population_growth_transpose = read_file('CSV_Files/population_growth.csv')
population_growth = filter_barplot_data(population_growth)

CO2_emission, CO2_emission_transpose = read_file('CSV_Files/co2_emission.csv')
CO2_emission = filter_lineplot_data(CO2_emission)

access_to_electricity, access_to_electricity_transpose = read_file('CSV_Files/access_to_electricity.csv')
access_to_electricity = filter_lineplot_data(access_to_electricity)


#Function to plot bar graph

def barplot(df, label1, label2):
    """
    Parameters
    ----------
    df : filtered dataframe to plot bar graph of the selected countries
    label1 : string to label y-axis
    label2 : string to display the title of bar graph
    Returns
    -------
    None.
    """
    plt.figure(figsize=(35, 25), layout = 'constrained')
    plt.rcParams['font.size'] = 20
    ax = plt.subplot(1, 1, 1)
    x = np.arange(5)
    width = 0.2

    bar1 = ax.bar(x, df["2010"], width, label = 2010, color = "lightseagreen")
    bar2 = ax.bar(x + width, df["2015"], width, label = 2015, color = "lightsteelblue")
    bar3 = ax.bar(x + width * 2, df["2020"], width, label = 2020, color = "slategrey")

    ax.set_xlabel("Country", fontsize = 40)
    ax.set_ylabel(label1, fontsize = 40)
    ax.set_title(label2, fontsize = 40)
    ax.set_xticks(x, countries, fontsize = 30, rotation = 45)
    ax.legend(fontsize = 30)

    ax.bar_label(bar1, padding = 2, rotation = 90, fontsize = 25)
    ax.bar_label(bar2, padding = 2, rotation = 90, fontsize = 25)
    ax.bar_label(bar3, padding = 2, rotation = 90, fontsize = 25)
    plt.savefig("barplot.png")
    plt.show()
    plt.close()


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

    plt.figure(figsize = (20, 15), layout = 'constrained')
    plt.rcParams['font.size'] = 20
    data = df.set_index('Country Name')
    transpose = data.transpose()
    transpose = transpose.drop(index = ['Indicator Name'])
    for i in range(len(countries)):
        plt.plot(transpose.index, transpose[countries[i]], label = countries[i])
    plt.title(label2, size = 20)
    plt.xlabel("Year", size = 20)
    plt.ylabel(label1, size = 20)
    plt.grid('True')
    plt.xticks(rotation = 50)
    plt.legend(fontsize = 25)
    plt.savefig("lineplot.png")
    plt.show()
    plt.close()


# Plotting bar graph for forest area and population growth to analyse

barplot(forest_area, 
        "Forest Area (% of land area)", "Forest Area")
barplot(population_growth, 
        "Population growth (annual %)", "Population Growth")

# Plotting line graph for forest area and population growth to analyse

line_plot(CO2_emission,
          "CO2 Emission in KT", "CO2 Emissions")
line_plot(access_to_electricity,
          "Access to electricity (% of population)", "Access to electricity")

# Statistical function to return the mean of CO2 emission of the countries

mean = co2_emission_mean()

# Writing the data to a csv file

mean = mean.to_csv("mean_of_co2_emission.csv")