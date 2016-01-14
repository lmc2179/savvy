import numpy as np
from explain_sklearn import regression_diagnostic
from matplotlib import pyplot as plt
from sklearn import linear_model
# This is a demo of the diagnostic tool being used where the assumptions of the linear regression model are met.

DATA_POINTS = 5000
X = np.random.uniform(0, 10, DATA_POINTS).reshape(DATA_POINTS, 1)
TRUE_SLOPE = 0.5
TRUE_BIAS = 2
y = TRUE_SLOPE*X.reshape(DATA_POINTS) + TRUE_BIAS + np.random.normal(size=DATA_POINTS)
lr = linear_model.LinearRegression()
lr.fit(X, y)

diag = regression_diagnostic.RegressionDiagnostic(lr, X, y)
diag.get_residual_histogram()
plt.show()