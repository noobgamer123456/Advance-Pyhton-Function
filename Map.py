number = [1,2,3,4,5,6]
even = [x for x in number if x%2 ==0]
print(even)
#=============
n1=[1,2,3]
n2=[4,5,6]
n3=[7,8,9]

nSum = map( lambda x,y,z: x+y+z,  n1,n2,n3)

print(list(nSum))
#=============

def sq(n):
    return n*n

num = [5,6,5,4,7,8,9,55]
res = map (sq,num)

print(list(res))


