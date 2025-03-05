from datetime import date

r_day, r_month, r_year = map(int, input().split())
d_day, d_month, d_year = map(int, input().split())


r_date = date(r_year, r_month, r_day)
d_date = date(d_year, d_month, d_day)


if r_date <= d_date:
    fine = 0
elif r_date.year == d_date.year:
    if r_date.month == d_date.month:
        fine = 15 * (r_day - d_day)
    else:
        fine = 500 * (r_month - d_month)
else:
    fine = 10000

print(fine)