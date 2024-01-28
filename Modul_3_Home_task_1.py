from datetime import datetime

def get_days_from_today():
    user_input = input('Enter date in format: YYYY-MM-DD --->')
    try:
        user_date = datetime.strptime(user_input, "%Y-%m-%d")
        print(user_date)
        current_date = datetime.today()
        delta_days = current_date.toordinal() - user_date.toordinal()
        print(delta_days)
    except Exception:
        print("Invalid date format")

get_days_from_today()
    
# date_input = input('Enter date in format: YYYY-MM-DD --->')
# date = datetime.strptime(date_input, "%Y-%m-%d")
# current_date = datetime.today()
# get_days_from_today = current_date.toordinal() - date.toordinal()

# print(get_days_from_today)

# Код все розраховує вірно, але не була створена функція. Чи вважається завдання виконаним?