### Sample eval function using python

def function_creator():

    # expression to be evaluated
    expr = input("Enter the function(in terms of x):")

    # variable used in expression
    x = int(input("Enter the value of x:"))

    # evaluating expression
    y = eval(expr)

    # printing evaluated result
    print("y =", y)


if __name__ == "__main__":
    function_creator()


## OUTPUT: 

```output
Enter the function(in terms of x):x*(x+1)*(x+2)
Enter the value of x:3
y = 60