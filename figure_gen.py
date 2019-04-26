import GPy
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 2.2, 6]).reshape(-1, 1)

Y = np.array([0.3, 1., 1.1, 0.6]).reshape(-1, 1)
# Y += np.random.randn(*Y.shape) * 1e-6

# m = GPy.models.GPRegression(X, Y, normalizer=True)
# m.optimize_restarts(num_restarts=100)
# print(m.param_array)

plt.figure(figsize=(16, 5))
ax = plt.subplot(121)

m = GPy.models.GPRegression(X, Y)
m.optimize()
m.plot(ax=ax, legend=False)

ax = plt.subplot(122)

m = GPy.models.GPRegression(X, Y)
m.optimize()
m.Gaussian_noise.variance = 0.03
m.plot(ax=ax, legend=False)

plt.tight_layout()
plt.savefig("images/gp-noise.png")


### RBF params

plt.figure(figsize=(16, 5))
ax = plt.subplot(121)

m = GPy.models.GPRegression(X, Y)
m.optimize()
m.kern.lengthscale = 0.2
m.plot(ax=ax, legend=False)

ax = plt.subplot(122)

m = GPy.models.GPRegression(X, Y)
m.optimize()
m.kern.lengthscale = 2.
m.plot(ax=ax, legend=False)

plt.savefig("images/gp-lengthscale.png")


### Parameter optimization


plt.figure(figsize=(16, 5))
ax = plt.subplot(121)

m = GPy.models.GPRegression(X, Y)
m.optimize()
m.kern.lengthscale = 4.
m.kern.variance = .1
m.plot(ax=ax, legend=False)

ax = plt.subplot(122)

m = GPy.models.GPRegression(X, Y)
m.optimize()
m.plot(ax=ax, legend=False)

plt.savefig("images/gp-kernel-param-optimization.png")

