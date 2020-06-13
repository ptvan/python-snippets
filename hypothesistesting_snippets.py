from scipy.stats import normaltest, anderson, chi2_contingency
import random

dat = [random.randrange(1,50,1) for i in range(50)]

# D'Agostino's test for normality
stat, p = normaltest(dat)
print('stat=%.3f, p=%.3f' % (stat, p)) 

# Anderson-Darling test for normality
result = anderson(dat)
print('stat=%.3f' % (result.statistic))

# Chi-Squared test
table = [[10, 20, 30],[6,  9,  17]]
stat, p, dof, expected = chi2_contingency(table)