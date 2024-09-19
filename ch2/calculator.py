num1=int(input("enter num1"))
num2=int(input("enter num2:"))
operator=input("enter the operator")

match operator:
    case"+":
        print("sum is ",num1+num2)
    case"-":
        print("difference is ",num1-num2)
    case"*":
        print("product is ",num1*num2)
    case"/":
        print("division is ",num1/num2)
    case "%":
        print("modulo is ",num1%num2)
    case _:
        print("enter a valid operator")
