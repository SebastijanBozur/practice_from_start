# def fuck_you(greeting, name='you'):
#     return '{}, {} Function'.format(greeting, name)
#
# print(fuck_you('go fuck yourselfe', name='Ivice'))
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(**kwargs)

# Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""
#
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
#
# def days_in_month(year, month):
#     """Return number of days in that month in that year."""
#
#     if not 1 <= month <= 12:
#         return 'Invalid Month'
#
#     if month == 2 and is_leap(year):
#         return 29
#
#     return month_days[month]

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'biology', 'physics', 'english']
info = {'fname':'milan','lname':'jakic','age':'26','year':'7'}

student_info(*courses,**info)