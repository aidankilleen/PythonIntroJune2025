import datetime as dt

start_of_year = dt.date(2025,1,1)

now = dt.date.today()

difference = (now - start_of_year).days
print (f"difference:{difference}")