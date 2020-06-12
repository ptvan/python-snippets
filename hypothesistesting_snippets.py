from scipy.stats import normaltest
import random

# D'Agostino's test for normality
dat = [random.randrange(1,50,1) for i in range(50)]
stat, p = normaltest(dat)
print('stat=%.3f, p=%.3f' % (stat, p)) 