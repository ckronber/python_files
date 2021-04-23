from datetime import datetime

birthday = datetime(1987,11,17,9,25,30)

days = datetime.now() - datetime(1987,11,17)

parsed_date = datetime.strptime('Jul 4, 2011', '%b %d, %Y')

print(parsed_date.month)
print(parsed_date.year)

datestring = datetime.strftime(datetime.now(),'%b %d, %Y')

print(datestring)

#pipenv to do cool stuff in python
#Installing pipenv and working with virtual environments
#