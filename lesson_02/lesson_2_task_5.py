def month_to_season(month):
    if month < 1 or month > 12:
        return "Некорректный номер месяца"

    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"


month_number = 5
season = month_to_season(month_number)

print(f"{month_number} месяц  относится к сезону: {season}.")
