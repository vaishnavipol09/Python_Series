def sum_all(*args):
    return sum(args)

print(sum_all(1 , 2))
print(sum_all(1 , 2 , 3 , 4))
print(sum_all(1 , 2 , 3 , 4 , 5 , 6))

# when we use args without * then only 1 parameter passed not multiple

# when we use args with * then we can pass multiple parameters