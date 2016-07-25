import pandas as pd
import matplotlib.pyplot as plt


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
    return rolling mean
'''


def get_rolling_mean(values, window):
    return pd.Series.rolling(values, window=window, center=True).mean()


'''
    return rolling sd
'''


def get_rolling_sd(values, window):
    return pd.Series.rolling(values, window=window, center=True).std()


'''
    return upper and lower bands
'''


def get_bollinger_bands(rm, sd):
    return rm + 2 * sd, rm - 2 * sd

'''
    return daily return
'''

def compute_daily_returns(df):

    df = df.fillna(0)
    tmp = (df / df.shift(periods=1))-1
    tmp.ix[0, :] = 0 # fill first value to 0
    return tmp


'''
    TEST ROLLING MEAN
'''


def test_run():

    dates = pd.date_range('2000-01-01', '2016-05-20')

    symbols = ['SPY', 'IBM', 'GOOG', 'GLD']

    df = get_data(symbols, dates)

    print "\n  Mean: \n", df.mean()

    print "\n  Median: \n", df.median()

    print "\n  Standard deviation: \n", df.std()

    # get stock data
    df1 = get_data(['SPY'], dates)

    # plot of SPY
    ax = df1['SPY'].plot(title='SPY rolling mean', label='SPY')

    # get rolling mean
    rm_spy = pd.Series.rolling(df1['SPY'], window=252, center=True).mean()

    # plot rolling mean with graph of SPY (ax=ax)
    rm_spy.plot(label='Rolling mean', ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')

    plt.show()



'''
    TEST BB
'''


def test_Bollinder_Band():

    dates = pd.date_range('2000-01-01', '2016-05-20')

    # get stack data
    df = get_data(['SPY'], dates)

    # 1 compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=200)

    # 2 compute rolling standart deviation
    rm_sd = get_rolling_sd(df['SPY'], window=200)

    # 3 compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rm_sd)

    # Plot SPY, mean and Bollinger Bands
    ax = df['SPY'].plot(title='Bollinger Band', label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()

'''
    TEST DAILY RETURN
'''
def test_daily_return():

    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')  # one month only
    symbols = ['SPY','IBM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

if __name__ == "__main__":

    #test_run()
    #test_Bollinder_Band()
    test_daily_return()
