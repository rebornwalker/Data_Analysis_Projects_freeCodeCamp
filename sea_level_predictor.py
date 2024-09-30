import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np

def draw_plot():
    
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', delimiter=',')

    # Create scatter plot
    plt.figure(figsize=(14,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlim(xmax=2060)
    
    year_extended = np.arange(df['Year'].min(), 2051)
    plt.plot(year_extended, res.intercept + res.slope*year_extended, color='red')

    # Create second line of best fit
    new_df = df[df['Year']>=2000]
    new_res = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    new_year_extended = np.arange(new_df['Year'].min(), 2051)
    plt.plot(new_year_extended, new_res.intercept + new_res.slope*new_year_extended, color='blue')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
