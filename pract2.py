num=int(input("Enter the number: "))
# temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10

if(rev==num):
    print("palindrome")
else:
    print("Not palindrome")

# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# n=int(input("Enter number:"))
# temp=n
# rev=0
# tot=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
#     tot=tot+dig
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")
#
#     print("The number isn't a palindrome!")
# print("The reverse num is:", rev)  #to get reverse of a number
# print("The sum of digits:", tot)   # to print sum of digits
