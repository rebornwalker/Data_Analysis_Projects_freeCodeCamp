import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', delimiter=',', index_col='date')

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025)) & 
        (df['value']<=df['value'].quantile(0.975))]

df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    df_line = df.copy()

    import matplotlib.dates as mdates

    fig, axes = plt.subplots(figsize=(16,6))
    axes.plot(df_line.index, df_line.value, color='red')
    
    axes.xaxis.set_major_locator(mdates.MonthLocator(interval=6))  
    axes.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  

    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.resample('M').mean()
    df_bar['year'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.strftime('%B')

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

    df_bar['Months'] = pd.Categorical(df_bar['Months'], categories=month_order, ordered=True)

    # Draw bar plot
    fig = sns.catplot(df_bar, x='year', y='value', hue='Months', kind='bar', palette='bright', legend='brief', legend_out=False)
    fig.set_xlabels('Years')
    fig.set_ylabels('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,6))
    sns.boxplot(data=df_box, x='year', y='value',  ax=axes[0])
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
