#wap to create a list of ten nos taking input from user named AR.now copy even nos in list EAR and odd nos in list OAR.now display elements of EAR and OAR.
l=[9,8,7,6,5,4,12,23,54,61]
even_count, odd_count = 0,0
for num in l:
  if num% 2 == 0:
    even_count += 1
  else:
    odd_count += 1
print("even nos in the l: ",even_count)
print("odd nos in the l: ",odd_count)