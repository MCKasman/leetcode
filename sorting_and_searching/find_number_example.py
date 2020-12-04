def find_number(nums):
    start = 0
    end = len(nums)
    target = 2

    while(start<end):
        mid=(start+end)//2

        if(target==nums[mid]):
            print(mid)
            break
        elif(target>nums[mid]):
            start=mid+1
        else:
            end = mid

nums=[1,2,3,4,5,6,7,8]

find_number(nums)
