
import pandas as pd
import matplotlib.pyplot as plt

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


def hurst(ts):
    """Returns the Hurst Exponent of the time series vector ts"""
    # Create the range of lag values
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0]*2.0


def test_run():

    # LOAD data
    start_date = '1994-01-01'
    end_date = '2016-05-01'

    # create datetime range
    dates = pd.date_range(start_date, end_date)

    # create empty data frame
    df1 = pd.DataFrame(index=dates)

    # read SPY
    dfSPY = pd.read_csv("SPY.csv", index_col="Date", parse_dates=True,
                        usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    # rename Adj Close to SPY
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

    # LEFT join df1 and dfSPY and drop NA
    df1 = df1.join(dfSPY, how='inner')

    # read more stocks
    symbols = ['GOOG', 'IBM', 'GLD', 'RTS', 'USO']

    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol), index_col="Date",
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])

        # rename Adj Close to symbol name
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        # LEFT join df1 and dfSPY and drop NA
        df1 = df1.join(df_temp)

        df1 = df1.dropna()

    print df1



    # NORMALIZE DATA
    df1 = df1.iloc[::-1]  # reverse data frame in date
    #df1 = df1 / df1.ix[0]  # normalize


    # Create a Gometric Brownian Motion, Mean-Reverting and Trending Series
    gbm = log(cumsum(randn(100000))+1000)
    mr = log(randn(100000)+1000)
    tr = log(cumsum(randn(100000)+1)+1000)

    # Output the Hurst Exponent for each of the above series
    # and the price of Google (the Adjusted Close price) for
    # the ADF test given above in the article
    print "Gussian(GBM):   %s" % hurst(gbm)
    print "Contratrend(MR):    %s" % hurst(mr)
    print "Trend(TR):    %s" % hurst(tr)

    print "Hurst(SPY):  %s" % hurst(df1['SPY'])
    print "Hurst(GOOG):  %s" % hurst(df1['GOOG'])
    print "Hurst(IBM):  %s" % hurst(df1['IBM'])
    print "Hurst(GLD):  %s" % hurst(df1['GLD'])
    print "Hurst(RTS):  %s" % hurst(df1['RTS'])
    print "Hurst(USO):  %s" % hurst(df1['USO'])

if __name__ == "__main__":
    test_run()
