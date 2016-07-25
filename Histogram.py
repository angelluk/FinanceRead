
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn


'''
    read some stocks
'''


def get_data(symbols, dates):

    # create empty data frame
    df1 = pd.DataFrame(index=dates)

    for symbol in symbols:

        df_temp = pd.read_csv("{}.csv".format(symbol), index_col="Date",
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])

        # rename Adj Close to symbol name
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # LEFT join df1 and dfSPY and drop NA
        df1 = df1.join(df_temp)

        df1 = df1.dropna()

        df1 = df1.iloc[::-1]  # reverse data frame in data

    return df1


'''
    plot data
'''


def plot_data(df,title='Stocks', ylabel='Price'):

    # PLOT
    df.plot(title=title, fontsize=12)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.show()


'''
    return daily return
'''


def compute_daily_returns(df):

    df = df.fillna(0)
    tmp = (df / df.shift(periods=1))-1
    tmp.ix[0, :] = 0  # fill first value to 0
    return tmp




def test_run():

    # LOAD data
    start_date = '1994-01-01'
    end_date = '2016-05-01'

    # create datetime range
    dates = pd.date_range(start_date, end_date)

    symbols = ['SPY', 'RTS', 'USO', 'GLD', 'AAPL','GOOG']

    df = get_data(symbols, dates)

    # daily return
    daily_return = compute_daily_returns(df)

    daily_return['RTS'].hist(bins=200, label='RTS')
    daily_return['USO'].hist(bins=200, label='USO')
    daily_return['SPY'].hist(bins=200, label='SPY')

    plt.legend(loc='upper right')
    plt.show()

    mean = daily_return['SPY'].mean()
    print "mean - ", mean

    std = daily_return['SPY'].std()
    print "std - ", std

    # KURTOSIS
    print '\n\nKurtosys (Normal=3): \n', daily_return.kurtosis()

    # CORRELATIONS
    print '\n\nCorrelations: \n', daily_return.corr(method='pearson')

    #plt.axvline(mean, color='w', linestyle='dashed',linewidth=2)
    #plt.axvline(std, color='r', linestyle='dashed',linewidth=2)
    #plt.axvline(-std, color='r', linestyle='dashed',linewidth=2)

    #plt.show()

    # SCATTER PLOT
    #daily_return.plot(kind='scatter', x='SPY', y='RTS')
    #daily_return.plot(kind='scatter', x='USO', y='RTS')
    #daily_return.plot(kind='scatter', x='USO', y='GLD')
    #daily_return.plot(kind='scatter', x='SPY', y='AAPL')

    daily_return.plot(kind='scatter', x='SPY', y='GOOG')
    # get regression coefficients
    beta_GOOG, alpha_GOOG = np.polyfit(daily_return['SPY'], daily_return['GOOG'], 1)
    # plot the regression line
    plt.plot(daily_return['SPY'], beta_GOOG * daily_return['SPY'] + alpha_GOOG, '-', color='r')
    plt.show()

    daily_return.plot(kind='scatter', x='RTS', y='USO')
    # get regression coefficients
    beta_USO, alpha_USO= np.polyfit(daily_return['RTS'],daily_return['USO'], 1)
    # plot the regression line
    plt.plot(daily_return['RTS'], beta_USO * daily_return['RTS'] + alpha_USO, '-', color='r')
    plt.show()

if __name__ == "__main__":
    test_run()
