'''ord(character) returns an integer between 0...127 from a single unicode character'''


def are_all_chars_unique(s):
    all_chars = [0 for i in range(128)]
    for character in s:
        if not all_chars[ord(character)]:
            all_chars[ord(character)]=1
        else:
            return False
    return True

test1 = "mihaela"
test2 = "zlatko"

print(are_all_chars_unique(test1))
print(are_all_chars_unique(test2))
