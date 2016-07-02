
import pandas as pd
import matplotlib.pyplot as plt


def test_run():

    # LOAD data
    start_date = '2010-01-01'
    end_date = '2010-12-31'

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
    symbols = ['GOOG', 'IBM', 'GLD']

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

    #
    # SLICING

    # slice by rows
    print df1.ix['2010-01-31':'2010-01-01']

    # slice by column
    print df1['GOOG']
    print df1[['GOOG', 'GLD']]

    # slice by rows and cols
    print df1.ix['2010-01-31':'2010-01-01', ['SPY', 'IBM']]

    ##
    # NORMALIZE DATA
    df1 = df1.iloc[::-1]  # reverse data frame in date
    df1 = df1 / df1.ix[0]  # normalize



    ###################################

    # PLOT
    df1.plot(title='Stocks', fontsize=12)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

if __name__ == "__main__":
    test_run()
