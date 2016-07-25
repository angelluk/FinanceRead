import math
from matplotlib import pyplot as plt


def normal_pdf(x, mu = 0, sigma = 1 ):
    '''
        calculate x for normal distribution
    '''
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2 ) / (sqrt_two_pi * sigma))
    
    
# plot example of Normal Distributions
    
xs = [x / 10.0  for x  in range (-50,50)]

plt.plot(xs,[normal_pdf(x, sigma = 1) for x in xs] , '-', label = 'mu = o, sigma = 1')
plt.plot(xs,[normal_pdf(x, sigma = 2) for x in xs] , '--', label = 'mu = o, sigma = 2')    
plt.plot(xs,[normal_pdf(x, sigma = 0.5) for x in xs] , ':', label = 'mu = o, sigma = 0.5')
plt.plot(xs,[normal_pdf(x, mu = -1) for x in xs] , '-.', label = 'mu = -1, sigma = 1')

plt.legend()
plt.title("Varios Normal pdfs")  
plt.show()
