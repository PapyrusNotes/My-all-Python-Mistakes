import numpy as np

x = np.random.randint(100, size=20)

print("array x : ", x)
print("len of x : ", len(x))

print("mean of x : ", np.mean(x))
print("variance of x : ", np.var(x))
print("standard deviation of x : ", np.std(x))

print("max value in x : ", np.max(x))
print("min value in x : ", np.min(x))
print("median value in x : ", np.median(x))

print("first quartile value of x : ", np.percentile(x, 25))
print("second quartile value of x : ", np.percentile(x, 50))
print("third quartile value of x : ", np.percentile(x, 75))
