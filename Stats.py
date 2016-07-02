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

        df1 = df1.iloc[::-1]  # reverse data frame in date

        #df1 = df1 / df1.ix[0]  # normalize


    return df1

'''
    plot data
'''

def plot_data(df):

    # PLOT
    df.plot(title='Stocks', fontsize=12)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()



def test_run():

    dates = pd.date_range('2000-01-01', '2016-01-01')

    symbols = ['SPY', 'IBM', 'GOOG', 'GLD']

    df = get_data(symbols, dates)


    print "\n  Mean: \n", df.mean()

    print "\n  Median: \n", df.median()

    print "\n  Standard deviation: \n", df.std()

    # plot all stocks
    #plot_data(df)

    df1 = get_data(['SPY'], dates)

    ax = df1['SPY'].plot(title='SPY rolling mean', label='SPY')

    #rm_SPY = pd.rolling_mean(df1['SPY'], window=252)
    rm_SPY =  pd.Series.rolling(df1['SPY'], window=252, center=False).mean()

    rm_SPY.plot(label='Rolling mean', ax=ax)

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')

    plt.show()



if __name__ == "__main__":

    test_run()
