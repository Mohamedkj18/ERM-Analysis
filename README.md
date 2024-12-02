# Hypothesis Class of Finite Union of Disjoint Intervals and ERM Algorithm

In this project, I studied the hypothesis class of a finite union of disjoint intervals, focusing on the properties of the Empirical Risk Minimization (ERM) algorithm for this class.

## Repository Overview

This repository contains two main files:

### 1. **`intervals.py`**:
This file implements the ERM algorithm for the hypothesis class \( H_k \). Given a sorted list `xs = [x1, x2, ..., xn]` and the respective labeling `ys = [y1, y2, ..., yn]`, the function `find_best_interval` returns a list of up to `k` intervals and their error counts on the given sample. These intervals minimize the empirical error count from all possible choices of `k` intervals or fewer.

### 2. **`experiment.py`**:
This file contains multiple experiments conducted to analyze the performance of the ERM algorithm. Specifically:
- **Experiment 1**: 
  - A function calculates the true error \( e_P(h_I) \) for a given list of intervals \( I \).
  - For \( k = 3 \) and \( n = 10, 15, 20, ..., 100 \), we perform \( T = 100 \) runs:
    1. Draw a sample of size \( n \) and run the ERM algorithm.
    2. Calculate the empirical error for the returned hypothesis.
    3. Calculate the true error for the returned hypothesis.
  - The results of empirical and true errors are plotted, averaged across \( T \) runs, as a function of \( n \).
  
- **Experiment 2**:
  - A sample of size \( n = 1500 \) is drawn.
  - ERM hypotheses are found for \( k = 1, 2, ..., 10 \), and empirical and true errors are plotted as a function of \( k \).
  
- **Experiment 3**:
  - A data set of size \( n = 1500 \) is drawn.
  - The previous experiment is repeated, but two additional lines are plotted as a function of \( k \):
    1. The penalty.
    2. The sum of the penalty and empirical error.

- **Experiment 4**:
  - A data set of size \( n = 1500 \) is drawn and split into training (80%) and holdout-validation (20%).

## Requirements

To run the experiments and code, you need Python 3 with the following dependencies:

- `numpy`
- `matplotlib`

You can install the necessary dependencies using pip:

```bash
pip install numpy matplotlib
