# century: a century leap year is a year that is exactly divisible by 100. A century is 100 years

# leap Century: leap century is divited by 400 that is divided by 4 also bre divided by 100 so dividet by 400
  
# leap year: What is a leap year? To be a leap year, 
#            the year number must be divisible by four – except for end-of-century years,
#            which must be divisible by 400. This means that the year 2000 was a leap year,
#            although 1900 was not. 2020, 2024 and 2028 are all leap years.

# Syntex: 
         #if (condition1):      # Executes when condition1 is true
             #if (condition2):  # Executes when condition2 is true
                                # if Block is end here
                                # if Block is end here



year=int(input("Enter a year"))
 
if year%4==0:
    print("{0} is a leap year".format(year))
    if year%100==0:
        print("{0} is a Century year".format(year))
        if year%400==0:
            print("{0} is a leap Century year".format(year))

        else:
            print("{0} is not a leap Century year".format(year))

    else:
        print("{0} is not a Century year".format(year))
else:
    print("{0} is not leap year".format(year))
