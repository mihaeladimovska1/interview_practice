import numpy
import string

def word_pattern(pattern, in_string):
   pattern_dict = dict()
   string_dict = dict()
   for i in range(len(pattern)):
      if pattern[i] in pattern_dict:
         pattern_dict[pattern[i]].append(i)
      else:
         pattern_dict[pattern[i]]=[i]
   print(pattern_dict)
   keys = in_string.split(' ')
   for i in range(len(keys)):
      if keys[i] in string_dict:
          string_dict[keys[i]].append(i)
      else:
          string_dict[keys[i]] = [i]
   #now iterate over the lists of values and see if they match
   for (k1,k2) in zip(pattern_dict.keys(), string_dict.keys()):
      if pattern_dict[k1]!= string_dict[k2]:
          return False
   return True



test1 = "abba"
test2 = "cat dog dog cat"
test3 = "cat cat dog dog"
print(word_pattern(test1, test2))
print(word_pattern(test1, test3))