a_file = open("random_file.txt", "r")
list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
a_file.close()
flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list)
text = ' '.join([str(element) for element in flat_list])
print(85)
import math
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m 
list1=toBinary(text)
list2=[]
for s in list1:
  f = str(s)
  list2.append(f[:2])
  list2.append(f[-2:])
list3=[]
for i in range(0,len(list2),8):
    if i<len(list2)-8:
       c=list2[i]+list2[i+1]+list2[i+2]+list2[i+3]+list2[i+4]+list2[i+5]+list2[i+6]+list2[i+7]
       list3.append(c)
list4=[]
for i in list3:
    list4.append(int(i,2))
per_even=sum_even=0
per_div3=sum_div3=0
per_div5=sum_div5=0
per_div7=sum_div7=0
j=0
for item in list4:
    j=j+1
    if item%2==0:
        sum_even=sum_even+1
    if item%3==0:
        sum_div3=sum_div3+1
    if item%5==0:
        sum_div5=sum_div5+1
    if item%7==0:
        sum_div7=sum_div7+1
per_even=(sum_even/(j)*100)
per_div3=(sum_div3/(j)*100)
per_div5=(sum_div5/(j)*100)
per_div7=(sum_div7/(j)*100)
print("The percentage of numbers that are even are:",per_even)
print("The percentage of numbers that can be divided with 3 is",per_div3)
print("The percentage of numbers that can be divided with 5 is",per_div5)        
print("The percentage of numbers that can be divided with 7 is",per_div7)




