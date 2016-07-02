import numpy as np
import time


def manual_mean(arr):
    sum = 0
    for i in xrange(0, arr.shape[0]):
        for j in xrange(0, arr.shape[1]):
            sum = sum + arr[i, j]
    return sum / arr.size


def numpy_mean(arr):
    return arr.mean()


def how_long(func, *args):
    t0 = time.time()
    result = func(*args)
    t1 = time.time()
    return result, t1 - t0


def test_run():

    #  List of 1D array
    print np.array([2, 3, 4])

    #  List of 2D array
    print np.array([(2, 3, 4), (5, 6, 7)])

    # Empty array
    print np.empty(5)

    print np.empty([5, 4])

    # array of 1
    print np.ones([2, 3], dtype=np.int)

    # array of zeros
    print np.zeros([5, 4], dtype=np.int)

    # random values [0.0, 1.0]
    print np.random.random((5, 4))

    # random values Gaussian
    print np.random.normal(size=(2, 3))  # mean =0, sd = 1

    # random values Gaussian mean  = 50 sd = 10
    print np.random.normal(50, 10, size=(2, 3))

    # random integers
    print np.random.randint(0, 10, size=(2, 20))

    a = np.random.random((5, 4))

    print a
    print a.shape  # dimensional of array

    print a.shape[0]  # number of rows
    print a.shape[1]  # number of columns

    print len(a.shape)  # number of dimensions

    print a.size  # number of total elements

    print a.dtype  # type of elements

    # random array
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))
    print a

    print "Sum of all elements:", a.sum()

    print "Sum of each column: \n", a.sum(axis=0)
    print "Sum of each row: \n", a.sum(axis=1)

    print "Minimum of each column: \n", a.min(axis=0)
    print "Maximum of each row: \n", a.max(axis=1)

    print "Mean of all elements:", a.mean()

    print 'Max value is ', a.max(), ',index is ', a.argmax()

    # fast operations
    t1 = time.time()
    print "Some text"
    t2= time.time()
    print 'Time for printing text is ', t2 - t1,' seconds'

    nd1 = np.random.random((1000, 1000))  # large array
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)

    print 'manual time - {:.6f} vs numpy time {:.6f}'.format(t_manual, t_numpy)
    print 'Numpy faster is ', str(t_manual/t_numpy), ' times'

    # access using indices
    a = np.random.random(5)

    indices = np.array([1, 1, 2, 3])

    print a
    print a[indices]

    # boolean access
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print a

    mean = a.mean()
    print mean

    a[a < mean] = mean
    print a

if __name__ == "__main__":
    test_run()