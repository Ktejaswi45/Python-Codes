a=list(map(int,input().split()))
n= len(a)+1
n_sum=n*(n+1)//2
a_sum=sum(a)
miss_val=n_sum-a_sum
print(miss_val)