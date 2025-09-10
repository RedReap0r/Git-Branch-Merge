from myfunc import calculate
from myfunc2 import subtract

def result_number():
    a = 11
    b = 12

    print("บวก:", calculate(a, b))
    print("ลบ:", subtract(a, b))

if __name__ == "__main__":
    result_number()
