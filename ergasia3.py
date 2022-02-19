a_file = open("random_file.txt", "r")
list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
a_file.close()
flat_list = [item for sublist in list_of_lists for item in sublist]
import string
list1 = []
for word in flat_list:
    for letter in word:
        if letter in string.punctuation:
            word = word.replace(letter,"")   
    list1.append(word)
list2 = []
for item in list1:
	list2.append(len(item))
i=-1
for item in list1:
  i=i+1
  if i%2 == 0:
    a=item
  elif i%2==1:
    b=item
    if len(a)+len(b)==20:
      list1.remove(a)
      list1.remove(b)
w1=w2=w3=w3=w4=w5=w6=w7=w8=w9=w10=w11=0
for item in list1:
  if len(item)==1:
    w1=w1+1
  if len(item)==2:
    w2=w2+1
  if len(item)==3:
    w3=w3+1
  if len(item)==4:
    w4=w4+1
  if len(item)==5:
    w5=w5+1
  if len(item)==6:
    w6=w6+1
  if len(item)==7:
    w7=w7+1
  if len(item)==8:
    w8=w8+1
  if len(item)==9:
    w9=w9+1
  if len(item)==10:
    w10=w10+1 
  if len(item)==11:
    w11=w11+1   
print(w1,"words of one letter") 
print(w2,"words of two letters")
print(w3,"words of three letters")
print(w4,"words of four letters")
print(w5,"words of five letters")
print(w6,"words of six letters")
print(w7,"words of seven letters")
print(w8,"words of eight letters")
print(w9,"words of nine letters")
print(w10,"words of ten letters")
print(w11,"words of eleven letters")

  


    
    
    



