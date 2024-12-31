# декораторы

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result == 1:
           print('Не простое и не составное')
        else:
            weh_ = 1
            for i in range(2, result):
                if result % i == 0 :
                    weh_ = 0
            if weh_ :
                print('простое')
            else:
                print('составное')
        return result
    return wrapper

@ is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2,3,7)
print(result)
