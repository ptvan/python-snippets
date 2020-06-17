from scipy.stats import normaltest, anderson, chi2_contingency, ttest_ind, ttest_rel, wilcoxon, kruskal
import random

dat = [random.randrange(1,1000,1) for i in range(100)]
dat2 = [random.randrange(1,1000,1) for i in range(100)]


# D'Agostino's test for normality
stat, p = normaltest(dat)
print('stat=%.3f, p=%.3f' % (stat, p)) 

# Anderson-Darling test for normality
result = anderson(dat)
print('stat=%.3f' % (result.statistic))

# Chi-Squared test
table = [[10, 20, 30],[6,  9,  17]]
stat, p, dof, expected = chi2_contingency(table)

# Student's t-test, independent samples
stat, p = ttest_ind(dat, dat2)

# Student's t-test, paired samples
stat, p = ttest_rel(dat, dat2)

# Wilcoxon signed-rank test
stat, p = wilcoxon(dat, dat2)

# Kruskal-Wallis test
stat, p = kruskal(dat, dat2)