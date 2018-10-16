## Citibike Review
### Reviewer: Tiancheng(Gabriel) Yin - ty1045

### 1. Null Hypothesis 
Your null hypothesis is fairly interesting since comparing those two groups can help us learn a lot about the riders. You expressed it correctly in both the words and the formula. 

### 2. Data
You did an excellent job creating features and selecting data that you need. I believe the data you choose and the features you create can be used effectively to test whether or not your hypothesis is correct. Your bar graph clearly display the two groups that you're trying to compare and their respective mean. The data you provided is sufficient in testing the hypothesis.

### 3. Tests 
#### Z-Test
A Z-test is any statistical test for which the distribution of the test statistic under the null hypothesis can be approximated by a normal distribution. Because of the central limit theorem, many test statistics are approximately normally distributed for large samples. For each significance level, the Z-test has a single critical value (for example, 1.96 for 5% two tailed) which makes it more convenient than the Student's t-test which has separate critical values for each sample size. Therefore, many statistical tests can be conveniently performed as approximate Z-tests if the sample size is large or the population variance is known. If the population variance is unknown (and therefore has to be estimated from the sample itself) and the sample size is not large (n < 30), the Student's t-test may be more appropriate.  -- Wiki & Lecture Slides

In this case, we can use a one-tail two sample z-test, under a = 0.05, to test whether or not our null hypothesis is robost.

#### T-Test

The t-test is any statistical hypothesis test in which the test statistic follows a Student's t-distribution under the null hypothesis. A t-test is most commonly applied when the test statistic would follow a normal distribution if the value of a scaling term in the test statistic were known. When the scaling term is unknown and is replaced by an estimate based on the data, the test statistics (under certain conditions) follow a Student's t distribution. The t-test can be used, for example, to determine if two sets of data are significantly different from each other. -- Wiki & Lecture Slides

Even though a t-test is more suitable for cases in which the sample size, n, is less than 30, when the sample size is large enough, a t-test's result will converge to a z-test's result. Therefore, in this case, since our sample size is large enough, we can also conduct a one-tail two sample t-test to calculate the t-statistics and use it to test whether or not our null hypothesis is robost.

#### Chi-Square Test

A chi-squared test, also written as χ2 test, is any statistical hypothesis test where the sampling distribution of the test statistic is a chi-squared distribution when the null hypothesis is true. Without other qualification, 'chi-squared test' often is used as short for Pearson's chi-squared test. The chi-squared test is used to determine whether there is a significant difference between the expected frequencies and the observed frequencies in one or more categories. In the standard applications of the test, the observations are classified into mutually exclusive classes, and there is some theory, or say null hypothesis, which gives the probability that any observation falls into the corresponding class. The purpose of the test is to evaluate how likely the observations that are made would be, assuming the null hypothesis is true.  -- Wiki

This test is used to determine the differences between the expected values and the observed values. Therefore, it is more useful in a two tailed test. For instance, if the author's null hypothesis is that the mean riding time of age 40+ people are equal to those who are under 40, then we can apply the chi square test. However, since we're interested in a one-tailed test, this test might not be particularly useful in testing the robostness of our null hypothesis. 
