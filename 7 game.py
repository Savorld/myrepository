print(filter(lambda n:n%7==0 or ('7' in str(n)),range(100)))
print([i for i in range(100) if i%7==0 or ('7' in str(i))])