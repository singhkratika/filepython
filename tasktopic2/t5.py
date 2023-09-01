#wap to compute gross salary
bs=int(input("basic salary:"))
if bs<=4000:
 hra=bs*10/100
 da=bs*50/100
elif bs>4000 and bs<=8000:
 hra=bs*15/100
 da=bs*60/100
elif bs>8000 and bs<=12000:
  hra=bs*20/100 
  da=bs*70/100
else:
 hra=bs*25/100
 da=bs*80/100
gs=bs+hra+da
print("basic salary = ",bs)
print("HRA = ",hra)
print("DA = ",da)
print("Gross Salary = ",gs)