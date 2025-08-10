def hasPowerOfTwo(arr):
    crntInt = 1
    n_dig = len(arr)

    while crntInt<=10**9:
        # get dig array for current number
        crntDigArr = convertToDig(crntInt)

        if len(crntDigArr) > n_dig:
            break

        if crntDigArr == arr:
            return True
        
        crntInt *= 2

    return False

def convertToDig(n):
    # convert n in to chars
    temp = n
    digits = []
    while temp!=0:
        digits.append(str(temp%10))
        temp //= 10
    digits.sort()
    return digits

def reorderedPowerOf2(n):
    digitsReq = convertToDig(n)
    
    
        
    print(hasPowerOfTwo(digitsReq))

    

reorderedPowerOf2(46)

