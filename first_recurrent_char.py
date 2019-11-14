def get_first_recurrent(in_string):
    all_chars = [0 for i in range(128)]
    for c in in_string:
        if not all_chars[ord(c)]:
            all_chars[ord(c)]=1
        else:
            return c
    return False

test1="abba"
test2 = "abc"
print(get_first_recurrent(test1))
print(get_first_recurrent(test2))

