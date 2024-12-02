import numpy as np
import matplotlib.pyplot as plt
import intervals



class Experiment(object):

    def sample_from_D(self, m):
        
        """Sample m data samples from D.
        Input: m - an integer, the size of the data sample.

        Returns: np.ndarray of shape (m,2) :
                A two dimensional array of size m that contains the pairs where drawn from the distribution P.
        """
        x_values = np.random.uniform(0, 1, size=m)
        x_values.sort()
        y_values = [0 for i in range(m)]
        for i, x in enumerate(x_values):
            if 0.2 < x < 0.4 or  0.6 < x < 0.8:
                yZeroProb = 0.9
                yOneProb = 0.1
            else:
                yZeroProb = 0.2
                yOneProb = 0.8
            y = np.random.choice([0,1], p = [yZeroProb, yOneProb])
            y_values[i] = y
                
        
        return np.array([np.array([x_values[i] , y_values[i]]) for i in range(m)])


    def experiment_m_range_erm(self, m_first, m_last, step, k, T):
        """Runs the ERM algorithm.
        Calculates the empirical error and the true error.
        Plots the average empirical and true errors.
        Input: m_first - an integer, the smallest size of the data sample in the range.
               m_last - an integer, the largest size of the data sample in the range.
               step - an integer, the difference between the size of m in each loop.
               k - an integer, the maximum number of intervals.
               T - an integer, the number of times the experiment is performed.

        Returns: np.ndarray of shape (n_steps,2).
            A two dimensional array that contains the average empirical error
            and the average true error for each m in the range accordingly.
        """
        n_s = []
        emp = []
        true = []
        for m in range(m_first, m_last + step, step):
            n_s.append(m)
            emp_error = []
            true_error = []
            for i in range(T):
                samples = self.sample_from_D(m)
                xs , ys = [sample[0] for sample in samples] , [sample[1] for sample in samples]
                J , error_count = intervals.find_best_interval(xs, ys, k)
                emp_error.append(error_count/m)
                true_error.append(self.true_error(J))
            emp.append(np.mean(emp_error))
            true.append(np.mean(true_error))
        plt.figure()
        plt.plot(n_s, emp, label= "emperical erorr")
        plt.plot(n_s, true, label= "true erorr")
        plt.xlabel('n')
        plt.ylabel('Erorr')
        plt.legend()
        plt.show()
        return np.array(np.array([emp[i], true[i]]) for i in range(m))
        
            
            
            
        

    def experiment_k_range_erm(self, m, k_first, k_last, step):
        """Finds the best hypothesis for k= 1,2,...,10.
        Plots the empirical and true errors as a function of k.
        Input: m - an integer, the size of the data sample.
               k_first - an integer, the maximum number of intervals in the first experiment.
               m_last - an integer, the maximum number of intervals in the last experiment.
               step - an integer, the difference between the size of k in each experiment.

        Returns: The best k value (an integer) according to the ERM algorithm.
        """
        samples = self.sample_from_D(m)
        xs , ys = samples[:, 0] , samples[:, 1]
        k_s = []
        emp = []
        true = []
        for k in range(k_first, k_last+step, step):
            print(k)
            k_s.append(k)
            emp_error = []
            true_error = []
            J , error_count = intervals.find_best_interval(xs, ys, k)
            emp_error.append(error_count/m)
            true_error.append(self.true_error(J))
            emp.append(np.mean(emp_error))
            true.append(np.mean(true_error))
        
        plt.figure()
        plt.plot(k_s, emp, label= "emperical erorr")
        plt.plot(k_s, true, label= "true erorr")
        plt.xlabel('k')
        plt.ylabel('Erorr')
        plt.legend()
        plt.show()
        return k_s[emp.index(min(emp))]
            
            
            

    def experiment_k_range_srm(self, m, k_first, k_last, step):
        """Run the experiment in (c).
        Plots additionally the penalty for the best ERM hypothesis.
        and the sum of penalty and empirical error.
        Input: m - an integer, the size of the data sample.
               k_first - an integer, the maximum number of intervals in the first experiment.
               m_last - an integer, the maximum number of intervals in the last experiment.
               step - an integer, the difference between the size of k in each experiment.

        Returns: The best k value (an integer) according to the SRM algorithm.
        """
        samples = self.sample_from_D(m)
        xs , ys = samples[:, 0] , samples[:, 1]
        k_s = []
        emp = []
        true = []
        panalties = []
        panAndEmp = []
        for k in range(k_first, k_last+step, step):
            print(k)
            panalty = 2*np.sqrt((2*k + np.log(20*(k**2)))/m)
            panalties.append(panalty)
            k_s.append(k)
            emp_error = []
            true_error = []
            J , error_count = intervals.find_best_interval(xs, ys, k)
            emp_error.append(error_count/m)
            true_error.append(self.true_error(J))
            emp.append(np.mean(emp_error))
            true.append(np.mean(true_error))
            panAndEmp.append(panalty + emp_error)
        
        plt.figure()
        plt.plot(k_s, emp, label= "emperical erorr")
        plt.plot(k_s, true, label= "true erorr")
        plt.plot(k_s, panalties, label= "panalty")
        plt.plot(k_s, panAndEmp, label= "sum of panalty and emperical error")
        plt.xlabel('k')
        plt.ylabel('Erorr')
        plt.legend()
        plt.show()
        return k_s[panAndEmp.index(min(panAndEmp))]

    def cross_validation(self, m):
        """Finds a k that gives a good test error.
        Input: m - an integer, the size of the data sample.

        Returns: The best k value (an integer) found by the cross validation algorithm.
        """
        samples = self.sample_from_D(m)
        indecies = [i for i in range(m)]
        indecies_s1 = np.random.choice(indecies, size=int(0.2*m), replace=False)
        indecies_s2 = [i for i in range(m) if not i in indecies_s1]
        indecies_s1.sort()
        indecies_s2.sort()
        s1 = np.array([samples[i] for i in indecies_s1])
        xs, ys = s1[:, 0] , s1[:, 1]
        s2  = np.array([samples[i] for i in indecies_s2])
        error_s2 = []
        hypo = []
        for k in range(1, 11):
            J , error_count_s1 = intervals.find_best_interval(xs, ys, k)
            hypo.append(J)
            s2_empErr = self.emperical_error(J, s2)
            error_s2.append(s2_empErr)
            
        i = error_s2.index(min(error_s2)) + 1          
        return i 
        
        

    #################################
    def true_error(self, J):
        """given a lists of intervals  we calculates the true erorr"""
        I = [[0,0.2],[0.4,0.6], [0.8,1]]
        I_c = self.find_complement(I)
        J_c = self.find_complement(J)
        return 0.2*self.interval_intersection(I, J) +0.8*self.interval_intersection(I, J_c) + 0.9*self.interval_intersection(I_c, J) + 0.1*self.interval_intersection(I_c, J_c)
    
    
    def emperical_error(self, J, s):
        cnt = 0 
        for sample in s:
            x  = sample[0]
            y = sample[1]
            inUnion = False
            for interval in J:
                if  interval[0] <= x <= interval[1]:
                    inUnion = True
                    
            if (y == 1 and not inUnion) or (y == 0 and inUnion):
                cnt += 1
        return cnt/len(s)
    
        
                    
    def find_complement(self, intervals):
        """given a lists of intervals I we find the complement in the interval [0,1]"""
        res = []
        curr = 0
        for l, r in intervals:
            if l > curr:
                res.append([curr, l])
            curr = max(curr, r)
        
        if curr < 1:
            res.append([curr, 1])
        
        return res   

              
    def interval_intersection(self, I, J):
        """given two lists of intervals I , J we calculate the propbality of 
        thr intervals intersection"""
        intersections = []
        for a, b in I:
            for c, d in J:
                start = max(a, c)
                end = min(b, d)
                if start <= end:
                    intersections.append([start, end])
        return sum([interval[1]- interval[0] for interval in intersections])
            
        
        


    #################################


if __name__ == '__main__':
    e = Experiment()
    e.experiment_m_range_erm(10, 100, 5, 3, 100)
    e.experiment_k_range_erm(1500, 1, 10, 1)
    e.experiment_k_range_srm(1500, 1, 10, 1)
    e.cross_validation(1500)

