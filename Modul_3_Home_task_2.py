import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1000 or min>=max or quantity<min or quantity>(max-min+1):
        print('Invalid parameters')
        return[]
    return sorted(random.sample(list(range(min, max+1)), quantity))
print("These numbers won the lottery", get_numbers_ticket(1, 49, 6))
print("These numbers won the lottery", get_numbers_ticket(1, 36, 5))