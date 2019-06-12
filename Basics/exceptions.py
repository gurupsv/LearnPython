def divide(x,y):
    try:
        res=x/y
    except ZeroDivisionError:
        print("Division by zero!")
    except :
        print ("Some other error!!")
    else:
        print("Result is -> ",res)
    finally:
        print("Running Finally block!")

divide(2,1)
divide(2,0)
divide('2','2')