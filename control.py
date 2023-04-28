#Write a function that uses while, if and continue statements to print all
#the even numbers between 0 and 50. 

def even_numbers():
    x=1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)
    
    
#Write a function that takes an integer argument and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.
def prime_numbers(num):
 if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "Not prime")
            break
    else:
        print("Prime")
 else:
    print("Not prime")

                
    
#Write a function that takes a list of integers as input and prints the sum of all the even numbers
#in the list.    

def even_integers(nums):
    count = 0
    for i in nums:
        if i%2==0:
            count+=i
            print(count)
        
        
#Write a function that takes any two integers as input, and prints the sum of all the numbers
# between the two integers (inclusive) that are divisible by 3.  
def sum_inclusive(a,b):
    sum=0
    for x in range(a,b+1):
        if x%3==0:
            sum+=x
            print(sum)
    
   
            

        
    
      
                   
    
                    
            
         
            
            