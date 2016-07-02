import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def test_run():

    # LOAD data
    start_date = '1994-01-01'
    end_date = '2016-01-01'

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

    df1 = df1.iloc[::-1]  # reverse data frame in date


    df1 = df1.pct_change() # convert  close to percent change

    df1['BaySignal'] = 0

    df1['SelSignal'] = 0

    df1['Result'] = 0

    df1['Total'] = 0

    df1 = df1.dropna()

    arr = df1.values

    #print df1
    #print arr
    prv = 0

    arr[:, 0] = arr[:, 0]*100

    #print arr

    for i in range(len(arr)):
        if i == 0:
            continue
        prv = arr[i-1, 0]

        # BUY signal
        if prv < 0:
            arr[i, 1] = 1
        else:
            arr[i, 1] = 0

    # day results
    arr[:, 3]  =  arr[:, 0] *  arr[:, 1]

    # calculate total sum
    sum = 0
    for i in range(len(arr)):
        if i == 0:
            continue
        sum = sum + arr[i, 3]
        arr[i, 4] = sum


    print arr[-10:, :]


    df = pd.DataFrame(arr, index=df1.index, columns=list('ABCDE'))

    df.ix[: ,['E']].plot()
    plt.xlabel('Time')
    plt.ylabel('Percent')
    plt.title('Simulation of SPY  - Long Only')
    plt.show()  # show plot

    '''
    plt.plot(arr[:,4])
    plt.ylabel('Portfolio')
    plt.show()
    '''
    # PLOT
    '''
    df1.plot(title='Stocks', fontsize=12)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    '''

if __name__ == "__main__":
    test_run()
