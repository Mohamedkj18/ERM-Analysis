In this project, I studed the hypothesis class of a finite
union of disjoint intervals, and the properties of the ERM algorithm for this class.

In this repository provided two files:
1. intervals.py:
   The file intervals.py includes a function that implements an ERM algorithm for H_k.
Given a sorted list xs = [x1, . . . , xn], the respective labeling ys = [y1, . . . , yn] and k, the
given function find best interval returns a list of up to k intervals and their error
count on the given sample. These intervals have the smallest empirical error count
possible from all choices of k intervals or less.

2. Experiment.py:
   In this section I preformed multiple experiments:
   - Wrote a function that, given a list of intervals I, calculates the true
error eP(hI). Then, for k = 3, n = 10, 15, 20, . . . , 100, performe T = 100 times:
(i) Draw a sample of size n and run the ERM algorithm on it;
(ii) Calculate the empirical error for the returned hypothesis;
(iii) Calculate the true error for the returned hypothesis. Plot the empirical and true errors,
averaged across the T runs, as a function of n.

- Drew a sample of size n = 1500. And then found an ERM hypothesis for
k = 1, 2, . . . , 10, and plotted the empirical and true errors as a function of k. 

- Draw a data set of n = 1500 samples, preformed the previous experiment again, but
now plotted two additional lines as a function of k: 1) the penalty, and 2) the
sum of penalty and empirical error.

- Drew a data set of n = 1500 samples and used 20% for a holdout-validation.

