
# 1

def calculate(min,max,step):
    s = sum(range(min,max+1,step))
    print(s)
calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

# 2
def avg(data):
    salaryAll=0
    for i in data["employees"]:
        if i["manager"]==False:
            salaryAll+=i["salary"]
    print(salaryAll)
            
avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) 

# 3
def func(a):
    def total(b,c):
        print(a+b*c)
    return total    
func(2)(3, 4) 
func(5)(1, -5) 
func(-3)(2, 9) 


# 4
def maxProduct(nums):
    max = nums[0] * nums[1]
    for x in nums:
        for y in nums:
            num=x*y
            if num > max and x!=y:
                max=num
    print(max)

maxProduct([5, 20, 2, 6]) 
maxProduct([10, -20, 0, 3]) 
maxProduct([10, -20, 0, -3]) 
maxProduct([-1, 2]) 
maxProduct([-1, 0, 2]) 
maxProduct([5,-1, -2, 0]) 
maxProduct([-5, -2]) 

def twoSum(nums, target):
    for i in nums:
        for j in nums:
            if i!=j and i+j==target:
                return[nums.index(i),nums.index(j)]
result=twoSum([2, 11, 7, 15], 9)
print(result) 


# 6
def maxZeros(nums):
    max=0
    sum=0
    for i in nums:
        if i==0:
            sum+=1
        else:
            sum=0
        if sum>max:
            max=sum
    print(max)
maxZeros([0, 1, 0, 0]) 
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) 
maxZeros([1, 1, 1, 1, 1]) 
maxZeros([0, 0, 0, 1, 1]) 





