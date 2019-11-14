import numpy

''' all_chars_1 = [0 for i in range(128)]
 all_chars_2 = [0  for i in range(128)]

 for character1, character2 in zip(in_str1, in_str2):
     all_chars_1[ord(character1)]+=1
     all_chars_2[ord(character2)]+=1

 return all_chars_1==all_chars_2'''


# better way




def is_permutation(in_str1, in_str2):
   all_chars = [0 for i in range(128)]
   for c2 in in_str2:
       all_chars[ord(c2)]+=1
   for c1 in in_str1:
       all_chars[ord(c1)]-=1
       if all_chars[ord(c1)]<0:
           return False
   return True






test1 = "miha"
test2 = "hami"
test3 = "haam"

print(is_permutation(test1, test2))
print(is_permutation(test2, test3))