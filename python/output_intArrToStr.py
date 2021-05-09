def output_intArrToStr(intArr):
    string = str(intArr[0])
    for i in range(1,len(intArr)):
        string = string + " " + str(intArr[i])
    return string 
