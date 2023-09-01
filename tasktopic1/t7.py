#wap to take number of days as input now display year,weeks and days.E.g.if userinput375 days then output willbe 1 years,1 weeks and 3 days.in this program ignore leap year.
days=int(input("enter the days "))
year=int(days/365)
weeks=int((days%365)/7)
days=int((days%365)%7)
print(year, weeks,days)
