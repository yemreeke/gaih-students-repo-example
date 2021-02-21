def prime_first(number):
    for i in range(2,int((number**0.5)+1)):
        if(number%i==0):
            return False
    if(number==1 or number==0):
        return False
    return True
def prime_second(number):
    for i in range(2,int((number**0.5)+1)):
        if(number%i==0):
            return False
    if(number==1 or number==0):
        return False
    return True

for i in range(0,1000+1):
    if(i<500):
        if(prime_first(i)):
            print(i)
    else:
        if(prime_second(i)):
            print(i)
