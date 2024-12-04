# Sample Eval Functions using python
def eval_function():

    # expression to be evaluated
    expr = input("Enter the function(in terms of x):")

    # variable used in expression
    x = int(input("Enter the value of x:"))

    # evaluating expression
    y = eval(expr)

    # printing evaluated result
    print("y =", y)


if __name__ == "__main__":
    eval_function()