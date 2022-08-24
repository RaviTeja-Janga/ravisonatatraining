def age(n):
    if (n==0):
        return 'not born'
    elif n==100:
        return 'you have 100 years'

    else:
        x=100-n
        return x,'years needed to get 100 year'

n=int(input('enter n value:'))
ag=age(n)
print(ag)