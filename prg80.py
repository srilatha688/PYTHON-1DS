def sum(*numbers):
    print('\n datatype of argumentsn is:',type(numbers))
    s=0
    for n in numbers:
        s=s+n
    print('sum is:',s)
sum(1,2,3)
