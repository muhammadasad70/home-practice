# def main():
#     x=int(input("enter a  number:\n"))
#     y=int(input("enter a  number:\n"))
#     z=max(x,y)
#     print("the larger number is ",z)
# main()
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# def Grade(number):
#     if number>=90:
#         return ('A')
#     elif number>=80:
#          return ('B')
#     elif number >= 70:
#         return ('C')
#     else:
#         return ('F')
# def main():
#     number=eval(input("enter your number"))
#     grade=Grade(number)
#     print("the grade is",grade)
#     # Grade(number)
# main()
# def order(num1,num2):
#     if num1>num2:
#         return num2 ,num1
#     else:
#         return num1,num2
# def isEven(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# #
# def main():
#     num=int(input("enter a number"))
#     num=isEven(num)
#     if num==True:
#         print("this is even number")
#     else:
#         print("this is odd number")
# main()
# def isPositive(num):
#     if num>0:
#         return True
#     else:
#         return False
# def main():
#     num=eval(input("enter a number"))
#     num=isPositive(num)
#     if num==True:
#         print("this is positive number")
#     else:
#         print("this is not positive number")
# main()
# def Factorial(num):
#     c=1
#     f=1
#     while c<=num:
#         f=f*c
#         c=c+1
#         factorial=f
#     return factorial
# def main():
#     num=eval(input("enter a number"))
#     factorial=Factorial(num)
#     print("the factorial of ",num,"=",factorial)
# main()
def increment(n):
    n+=1
    print(n)
def main():
    x=1
    print(x)
    increment(x)
    print(x)
main()