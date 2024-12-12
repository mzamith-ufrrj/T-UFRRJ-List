#!/opt/anaconda/bin/python
from scipy.stats import beta
import matplotlib.pyplot as plt
import sys
#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "sans-serif",
#    "font.sans-serif": ["Helvetica"]})
# for Palatino and other serif fonts use:
#plt.rcParams.update({
#"text.usetex": True,
#    "font.family": "serif",
#    "font.serif": ["Palatino"],
#})
plt.rc('text', usetex=True)
import numpy as np
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / (a + b)
    save = int(sys.argv[3])
    #st = 'Beta pdf B(a = {:.1f}, b = {:.1f})'.format(alpha, beta)
    #print(st)
    st = 'beta.{:.1f}.{:.1f}.eps'.format(a, b)

    x = np.linspace(beta.ppf(0.0000001, a, b), beta.ppf(0.9999999, a, b), 100)
    rv = beta(a, b)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, rv.pdf(x), 'k-', lw=2, label=r'$\alpha = {:.1f} / \beta = {:.2f}$'.format(a, b))
    plt.xticks(np.arange(0, 1, 0.1))
    plt.axvline(x=c, label=r'$\mu = {:.4f}$'.format(c))
    ax.legend(loc='best', frameon=False)
    if save == 0:
        plt.show()
    else:
        plt.savefig(st, format='eps')
        print('File: ', st, ' saved')

    #x = np.linspace(beta.ppf(0.01, alpha, beta), beta.ppf(0.99, alpha, beta), 100)
    #ax.plot(x, beta.pdf(x, alpha, beta), 'r-', lw=5, alpha=0.6, label='beta pdf')
