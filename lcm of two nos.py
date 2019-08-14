a=int(input("Enter the number = "))
b=int(input("Enter the second number = "))
if b>a :
    c=b
    b=a
    a=c
lcm=1
while True:
          c=0
          for i in range (2,a):
              if a%i==0 and b%i==0 :
                c=c+1
                a=a//i
                b=b//i
                lcm=lcm*i
                break
          if c==0:
             print("The lcm of the given two numbers = ",lcm*a*b)
             break

