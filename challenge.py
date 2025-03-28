print("CALCULATING LARGE POWER")

def large_power(base,exponent):
    result= base ** exponent
    print(result)
    if result > 5000:
    #     return True 
    # else:
    #     return False
    # OORRRR
        return True
    return False
    

print(large_power(2,13))
print(large_power(5,3))

print("DIVISIBLITY BY TEN")
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
    

print(divisible_by_ten(24)) 
print(divisible_by_ten(15))     
print(divisible_by_ten(100))     