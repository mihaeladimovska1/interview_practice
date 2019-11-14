
nums=0

def num_ways(N,step_size, nums):
    if N==0:
        nums+=1
        return nums
    else:
        N=N-step_size
        num_ways(N, 1, nums)
        num_ways(N,2,nums)

print(4,1,nums)
