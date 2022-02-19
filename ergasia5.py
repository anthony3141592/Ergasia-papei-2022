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
for i in range(len(list1)):
    list1[i] = list1[i].lower()
text = ' '.join([str(element) for element in list1]) 
from collections import Counter
import re
words = re.findall('\w+',text)
print(Counter(words).most_common(10))
f=""
text2=""
for string in list1:
 f=string[:2]   
 text2=text2+" "+f
words = re.findall('\w+',text2)
print(Counter(words).most_common(3))
c=""
text3=""
for string in list1:
  c=string[:3]
  text3=text3+" "+c
words = re.findall('\w+',text3)
print(Counter(words).most_common(3))











 

