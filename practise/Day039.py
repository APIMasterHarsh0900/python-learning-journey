def returntheListofindices(arr,element,index):
    if (len(arr)==index):
        return []
    smalllist=returntheListofindices(arr,element,index+1)
    if (arr[index]==element):
        ans=[index]+smalllist
        return ans
    else:
        return smalllist
print(returntheListofindices([3,3,3,3,3,3,3,3,3,3,3,3],9,0))