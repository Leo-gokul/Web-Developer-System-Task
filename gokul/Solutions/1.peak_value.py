def check_array (arr):
    leng = len(arr)
    if n== 0 : # check th elist for null
        peak = None
        print("There is no array")
    for i in range (leng ): # chech the values in the list one by one for greast number
        if (arr[i-1]<arr[i]& arr[i]>=arr[i+1]):
            peak= arr[i]
        elif (arr[i+1]>arr[i]):
            peak = arr[i+1]
        elif (arr[i-1]>arr[i]):
            peak = arr[i-1]
    return peak
# input for user
list_value = input("number=" )
array = list(map(int, list_value.split()))
peak = check_array(array)
# prit output
print("Output=", peak)
