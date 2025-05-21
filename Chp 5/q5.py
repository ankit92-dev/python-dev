#Waf a recursive functon to print all element in a list
#Hint: use list & index as parameters
def func_name(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    func_name(list,idx + 1)
        
#Call
digit=[1,2,4,2,43,5,242,2423]
func_name(digit)