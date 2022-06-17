def hotel_cost(nights):
    return 140*nights
def plane_ride(city):
    if city=="Charlotte" or city=="charlotte":
        return 183
    elif city=="Tampa" or city=="tampa":
        return 220
    elif city=="Pittsburgh"or city=="pittsburgh":
        return 222
    elif city=="Los Angeles" or city=="los angeles":
        return 475

def rental_car_cost(days):
    cost=40*days
    if(days>=3 and days<7):
        cost-=20
    elif(days>=7):
        cost-=50
    return cost

def trip_cost(city,days,spending_money):
    sum=0
    hotelcost=hotel_cost(days)
    planecost=plane_ride(city)
    carcost=rental_car_cost(days)
    sum=hotelcost+planecost+carcost+spending_money
    return sum
print("Cities")
print("1.Charlotte")
print("2.Tampa")
print("3.Pittsburgh")
print("4.Los Angeles")
city=str(input("Enter the city name from the list above : "))
days=int(input("Enter the number of days: "))
spendingMoney=int(input("Enter the money spent: "))
print("The total money spent on trip is : ")
print(trip_cost(city,days,spendingMoney))