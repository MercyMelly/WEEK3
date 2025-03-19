def calculate_discount(price,discount_percent):
    if discount_percent>=20:
        discount_amount = (discount_percent/100)*price
        final_price  = price - discount_amount
        return final_price
    else:
        return price
    
print(calculate_discount(1700,35))
print(calculate_discount(4500,10))    