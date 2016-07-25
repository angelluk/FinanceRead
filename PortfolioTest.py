
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


def plot_data(df,title='Portfolio', ylabel='Price'):

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

'''
    calculate Sharp Ratio
'''


def calculate_sharp_ratio(portf):

    # average return
    average_return = portf.mean()
    print '\n\nAverage return :\n', average_return

    # std deviation
    std_return = portf.std()
    print '\n\nStd :\n', std_return

    # Sharpe ratio
    SR = sqrt(252) * average_return / std_return
    print '\n\nSharp ratio :\n', SR


def test_run():

    # LOAD data
    start_date = '1994-01-01'
    end_date = '2016-05-01'

    # capital
    start_val = 1000000

    # create datetime range
    dates = pd.date_range(start_date, end_date)

    symbols = ['GOOG', 'AAPL', 'IBM', 'SPY']

    df = get_data(symbols, dates)

    # daily return
    daily_return = compute_daily_returns(df)

    # allocation : minus mean short position
    alloc = [0.25, 0.25, 0.0, -0.5]

    # get allocated
    alloced = daily_return * alloc

    # value of positions
    pos_val = alloced * start_val

    # portfolio total values
    port_val = pos_val.sum(axis=1)


    portf = port_val[1:]
    print portf.tail()

    #statistics
    cum_ret = portf.cumsum()

    print '\n\nTotal Portfolio return :\n', cum_ret[len(cum_ret) - 1]

    # Calculate Sharp Ratio Portfolio
    calculate_sharp_ratio(portf)

    # show the Portfolio
    #portf.hist(bins=200, label='Portfolio')


    SPY_daily = daily_return['SPY'].cumsum() * start_val    # compare with all money invest to SPY

    # Calculate Sharp Ratio SPY
    calculate_sharp_ratio(daily_return['SPY'])

    # Plot
    ax = SPY_daily.plot(title='SPY', label='SPY')           # plot SPY return
    cum_ret.plot(label='Portfolio', ax=ax)                  # plot Portfolio return

    ax.set_xlabel('Date')
    ax.set_ylabel('Return')
    ax.legend(loc='upper left')
    plt.show()



if __name__ == "__main__":
    test_run()

