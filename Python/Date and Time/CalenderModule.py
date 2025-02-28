# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, day, year = map(int, input().split())
week_day = calendar.weekday(year, month, day)
match week_day:
    case 0: print("MONDAY")
    case 1: print("TUESDAY")
    case 2: print("WEDNESDAY")
    case 3: print("THURSDAY")
    case 4: print("FRIDAY")
    case 5: print("SATURDAY")
    case 6: print("SUNDAY")