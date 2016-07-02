import pandas as pd
import matplotlib.pyplot as plt


def get_max_close(symbol):
    '''
    Return the maximum closing price
    '''
    df = pd.read_csv("{}.csv".format(symbol))
    return df['Close'].max()    # get max close price for symbol


def get_mean_volume(symbol):
    '''
    Return the maximum closing price
    '''
    df = pd.read_csv("{}.csv".format(symbol))
    return df['Volume'].mean()    # get mean volume for symbol


def read_stocks():

    '''
    df = pd.read_csv("IBM.csv")
    print df.head(4)        # print first n rows
    print df.tail(4)        # print last n rows
    print df[10:21]
    '''

    for symbol in ['AAPL','IBM']:
        print "Max close price"
        print symbol, get_max_close(symbol)
        print "Mean volume"
        print symbol, get_mean_volume(symbol)


def plot_stocks():

    '''
    plot price
    '''

    df = pd.read_csv("AAPL.csv")
    print df['Adj Close']
    df = df.iloc[::-1]  # reverse data frame in date
    df[['Close', 'Adj Close']].plot()   # plot two columns of df
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Price if AAPL')
    plt.show()  # show plot




if __name__ == "__main__":
    read_stocks()
    plot_stocks()