import sys
x = 69

def my_display(x):
    print("out: "+str(x))

sys.displayhook = my_display

print(x)
my_display(x)
sys.displayhook(x)