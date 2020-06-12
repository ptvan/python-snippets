from scipy.stats import normaltest
import random

dat = [random.randrange(1,50,1) for i in range(50)]

# D'Agostino's test for normality
stat, p = normaltest(dat)
print('stat=%.3f, p=%.3f' % (stat, p)) 

# Anderson-Darling test for normality
result = anderson(data)
print('stat=%.3f' % (result.statistic))