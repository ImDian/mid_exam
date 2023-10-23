number_of_cities = int(input())

total_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    money_earned = float(input())
    money_spent = float(input())

    if city % 5 == 0:
        money_spent += money_earned * 0.10

    elif city % 3 == 0:
        money_spent += money_spent * 0.50

    profit = money_earned - money_spent
    total_profit += profit

    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

