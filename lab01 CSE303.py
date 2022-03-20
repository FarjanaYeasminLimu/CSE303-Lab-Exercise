print("problem no-1")
print("2019-1-60-174")
x = int(input("Enter a value: "))
y = int(input("Enter a value: "))
if x*y>1000:
  print(x+y)
else:
  print(x*y)
  
  print("problem no-2")
print("2019-1-60-174")
r = float(input("Enter a value: "))
x=3.141592654
a=x*(r*r)
p=2*x*r
print("Area is %.2f and perimeter is %.2f"%(a,p))


print("problem no-3")
print("2019-1-60-174")
p = int(input("Enter a value: "))
r = float(input("Enter a value: "))
t = int(input("Enter a value: "))

def compound_interest_2019_1_60_174(p,r,t):
    return p * (1 + r/100)**t
print("Interest is = %.2f"%(compound_interest_2019_1_60_174(p,r,t)))


print("problem no-4")
print("2019-1-60-174")
sum = 0
n = int(input("Enter a value : "))
for i in range(1,n+1):
  sum=sum+i**2
print(sum)


print("problem no-5")
print("2019-1-60-174")
n = int(input("Enter the number: "))
def prime_find_2019_1_60_174(n):
    for i in range(2, int(n+1/2)):
        if(n%i==0):
             return 1
    else:
      return 0
if(prime_find_2019_1_60_174(n)==0):
   print("It is a Prime number")
else:
   print("It is Not a Prime number")          
    
	 
	
	
	print("problem no-6")
print("2019-1-60-174")
n = int(input("Enter the number: "))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fibonacci(n)


print("problem no-7")
print("2019-1-60-174")
sum = 0
list=[202,34,2212,323,4343,223,32,2,423,432,323,2,2,31,3,23,2,4343,43,434,34,343]
for i in range(22):
  sum = sum + list[i]
print(sum)


print("problem no-8")
print("2019-1-60-174")
sum = 0
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(1,20):
   if list[i]%2==0:
    sum = sum + list[i]
print(sum)


print("problem no-9")
print("2019-1-60-174")
List = [11,34,22,45,200,-45,-3,-45,-100,-90,65,90,70,0,-90,-31,1000]

def largest_number_2019_1_60_174():
    a=0
    for i in range(17):
          if List[i]>a:
              a=List[i]           
    
    print(a)

def smallest_number_2019_1_60_174():
    a=3000
    for i in range(17):
          if List[i]<a:
              a=List[i]
    
    print(a)
    
largest_number_2019_1_60_174()
smallest_number_2019_1_60_174()



print("problem no-10")
print("2019-1-60-174")
a=0
b=0
List = [12,23,98,25,78,-67,-45,-89,-12,0]
for i in range(10):
    for j in range(i+1,10):
        if List[j]<List[i]:
            temp=List[i]
            List[i]=List[j]
            List[j]=temp
for i in range(10):
    if a<List[i]:
        a=List[i]
        b=i
print(List[b-1])


print("problem no-11")
print("2019-1-60-174")
a = input("Enter the string: ")
for i in range(0,len(a),2):
    print(a[i])
	
	
	
	print("problem no-12")
print("2019-1-60-174")
m = input("Enter the string: ")
n = int(input("Enter the number: "))
a = ""
for i in range(n,len(m)):
    a = a + m[i]
print(a) 




print("problem no-13")
print("2019-1-60-174")
a = input("Enter the String: ")
sum=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i:j] =='CSE303':
            sum=sum+1
print(f'CSE303 comes in {sum} times.')
          
		  
		  
	print("problem no-14")
print("2019-1-60-174")
str1 = input("Enter the String: ")
c=len(str1)
def palindrome_checker_2019_1_60_174():
    for i in range(0,c,1):
        if str1[i] == str1[c-(1+i)]:
            return 1
        else:
            return 0
        
if(palindrome_checker_2019_1_60_174()):
    print("Palindrome")
else:
    print("Not palindrome")


print("problem no-15")
print("2019-1-60-174")
List1 = [12,56,78,32,1,9,5,45,32,34]

List2 = [65,78,21,34,58,98,51,45,67,0,35]

List3 = []

List4 = []

for i in range(len(List1)):
       if List1[i]%2==0:
         List3.append(List1[i])

for i in range(len(List2)):
       if List2[i]%2!=0:
        List4.append(List2[i])
       
print(List3)
print(List4)	