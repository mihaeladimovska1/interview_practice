def is_interleaved(s1,s2,s3):
    if len(s1)+len(s2)!=len(s3):
        return False
    ind1=0
    ind2=0
    for i in range(len(s3)):
        if ind1<len(s1) and s3[i]==s1[ind1]:
            ind1+=1
            print(s1)
        elif ind2<len(s2) and s3[i]==s2[ind2]:
            ind2+=1
        else:
            return False

    return True

def is_interleaved_with_overlap(s1,s2,s3):
    if len(s1)+len(s2)!=len(s3):
        return False


s1='pump'
s2='kni'
s3='pumpkin'
print(is_interleaved(s1, s2, s3))