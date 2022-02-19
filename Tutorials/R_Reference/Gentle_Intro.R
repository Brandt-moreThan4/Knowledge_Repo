
## 
# Load one of R's built-in data sets about cars
data(mtcars)

# Fit a straight line for mpg vs hp and plot the result.

mpg_model = lm(mpg ~ hp, data=mtcars) # Fit Linera Model
plot(mtcars$hp, mtcars$mpg) # Plot Linear Model
abline(mpg_model) # Draw the best fit line
print(coef(mpg_model)) # Print the coefficients to command line
