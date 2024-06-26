# This code calculates and tracks the daily and total revenue generated by a camping site over a specified number of days.
# Based on user input for the occupancy of different types of camping lots and their respective rates.

# Входираме данните за обекта "Къмпинг"
# Брой дни на летният сезон, можем да ги изчислим на база 1 май - 30 септември
# Приемаме, че дните на активният сезон от 15.05 до 15.09.2022 година дните са 153!

camping_name = input("Въведете името на Вашият къмпинг: ")

days_of_season = int(input("Въведете за колко дни ще въвеждате информация в системата: "))

tent_without_parking_lots = int(input("Места за палатки без личен паркинг: "))
tent_with_parking_lots = int(input("Места за палатки с личен паркинг: "))
caravans_lots = int(input("Места за каравани: "))
camper_lots = int(input("Места за кемпери: "))
tent_without_parking_lots_today = tent_without_parking_lots
tent_with_parking_lots_today = tent_with_parking_lots
caravans_lots_today = caravans_lots
camper_lots_today = camper_lots

price_tent = 25
price_tent_car = 35
price_caravan = 70
price_camper = 55

total_sum = 0


def price_of_the_day(people_in_tent, people_in_tent_cars, people_in_caravan, people_in_camper):
    return people_in_tent * price_tent + people_in_tent_cars * price_tent_car + people_in_caravan * price_caravan + people_in_camper * price_camper


for current_day in range(1, days_of_season + 1):
    print(f"Въвеждане на данните на гостите на {camping_name} за ден {current_day}: ")

    tent_lots_today = int(
        input(f"Заети места на палатките без личен паркинг, но не повече от {tent_without_parking_lots} : "))
    tent_without_parking_lots -= tent_lots_today

    tent_lots_cars_today = int(
        input(f"Заети места на палатките с личен паркинг, но не повече от {tent_with_parking_lots}: "))
    tent_with_parking_lots -= tent_lots_cars_today

    caravans_lots_today = int(input(f"Заети места с каравaни, но не повече от {caravans_lots}: "))
    caravans_lots -= caravans_lots_today

    campers_lots_today = int(input(f"Заети места с кемпери, но не повече от {camper_lots}: "))
    camper_lots -= campers_lots_today

    if current_day % 7 == 0:
        tent_without_parking_lots_today = tent_without_parking_lots
        tent_with_parking_lots_today = tent_with_parking_lots
        caravans_lots_today = caravans_lots
        camper_lots_today = camper_lots

    total_sum += (price_of_the_day(tent_lots_today, tent_lots_cars_today, caravans_lots_today, campers_lots_today))
    print(
        f"За днес Вие реализирахте печалба от {price_of_the_day(tent_lots_today, tent_lots_cars_today, caravans_lots_today, campers_lots_today)} лв.")

print(f"Вие реализирахте печалба от {total_sum} лв. за периодът от {days_of_season} дни!")
