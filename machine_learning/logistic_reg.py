import math

# NOTE WE would like to predict whether or not a human breast mass is likely to be benign or malignant, given just two features. This is inspired by real-world data, but we have simplified our training.

x_train = [[0.5, 1.5], [1, 1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]]
y_train = [0, 0, 0, 1, 1, 1]


class LogisticRegressor:
    def __init__(self, w, b, alpha):
        self.w = w
        self.b = b
        self.alpha = alpha

    def fit(self, x_train, y_train):
        for _ in range(10000):
            delta_w = self._d_cost_func_w(x_train, y_train)
            delta_b = self._d_cost_func_b(x_train, y_train)
            for i in range(len(self.w)):
                self.w[i] = self.w[i] - delta_w[i] * self.alpha
            self.b = self.b - delta_b

    def cost(self, x_examples, y_labels):
        cost = 0
        for i in range(len(x_examples)):
            cost += self._loss(x_examples[i], y_labels[i])
        return cost / len(x_examples)

    def _loss(self, x, y):
        z = self._dot_product(self.w, x) + self.b
        return -y * math.log(self._sigmoid(z)) - (1 - y) * math.log(
            1 - self._sigmoid(z)
        )

    def _d_cost_func_w(self, x_train, y_train):
        delta_w = [0] * len(x_train[0])
        for i in range(len(x_train)):
            error = (
                self._sigmoid(self._dot_product(self.w, x_train[i]) + self.b)
                - y_train[i]
            )
            for j in range(len(delta_w)):
                delta_w[j] += error * x_train[i][j]
        for i in range(len(delta_w)):
            delta_w[i] = delta_w[i] / len(x_train)
        return delta_w

    def _d_cost_func_b(self, x_train, y_train):
        delta_b = 0
        for i in range(len(x_train)):
            delta_b += (
                self._sigmoid(self._dot_product(self.w, x_train[i]) + self.b)
                - y_train[i]
            )
        return delta_b / len(x_train)

    def predict(self, x):
        return 1 if self._sigmoid(self._dot_product(self.w, x) + self.b) >= 0.5 else 0

    def _dot_product(self, a, b):
        return sum(pair[0] * pair[1] for pair in zip(a, b))

    def _sigmoid(self, exponent):
        return 1 / (1 + math.exp(-exponent))


# NOTE what we want to do:
regressor = LogisticRegressor(w=[0, 0], b=0, alpha=0.1)
regressor.fit(x_train, y_train)

for example in x_train:
    print(f"Prediction for {example} is {regressor.predict(example)}")

print(regressor.cost(x_train, y_train))
