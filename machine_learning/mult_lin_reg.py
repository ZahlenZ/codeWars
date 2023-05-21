import logging

logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


class MultipleLinearRegressor:
    def __init__(self, w=[], b=0, alpha=0.01):
        self.w = w
        self.b = b
        self.alpha = alpha
        self.n = len(self.w)

    def fit(self, x_train, y_train):
        run = True
        iter = 0
        while run:
            iter += 1
            for j in range(len(self.w)):
                delta_w = self.alpha * self._d_cost_function_w(x_train, y_train, j)
                delta_b = self.alpha * self._d_cost_function_b(x_train, y_train)
                self.w[j] = self.w[j] - delta_w
                self.b = self.b - delta_b
                if abs(delta_w) < 1e-8:
                    run = False
                    break

    def _d_cost_function_w(self, x_train, y_train, dex):
        calc = 0.0
        for x, y in zip(x_train, y_train):
            calc += (self.predict(x) - y) * x[dex]
        return calc / self.n

    def _d_cost_function_b(self, x_train, y_train):
        calc = 0
        for x, y in zip(x_train, y_train):
            calc += self.predict(x) - y
        return calc / self.n

    def predict(self, x):
        return self._dot_product(self.w, x) + self.b

    def _dot_product(self, a, b):
        return sum(pair[0] * pair[1] for pair in zip(a, b))


x_train = [
    [2104.0, 5.0, 1.0, 45.0],
    [1416.0, 3.0, 2.0, 40.0],
    [1534.0, 3.0, 2.0, 30.0],
    [852.0, 2.0, 1.0, 36.0],
]
y_train = [460.0, 232.0, 315.0, 178.0]

regressor = MultipleLinearRegressor([0, 0, 0, 0], 0, 1e-9)
regressor.fit(x_train, y_train)

## Prints out the different tests
first_house_price = regressor.predict([2104.0, 5.0, 1.0, 45.0])
print(
    f"The predicted price of a 2,104 sqft house with 5 bedrooms, 1 floor, that is 45-years old is {first_house_price}, the actual house price is 460"
)

second_house_price = regressor.predict([1416.0, 3.0, 2.0, 40.0])
print(
    f"The predicted price of a 1,416 sqft house with 3 bedrooms, 2 floors, that is 40 years old is {second_house_price} thousand dollars, the actual house price is 232"
)

third_house_price = regressor.predict([1534.0, 3.0, 2.0, 30.0])
print(
    f"The predicated price of a 1,534 sqft house with 3 bedrooms, 2 floors, that is 30 years old is {third_house_price} thousand dollars, the actual house price is 315"
)

small_house_price = regressor.predict([852.0, 2.0, 1.0, 36.0])
print(
    f"The predicted price of the final house is {small_house_price}, the actual price is 178"
)
