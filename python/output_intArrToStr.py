def output_intArrToStr(intArr):
    if intArr == []:
        return ""
    string = str(intArr[0])
    if len(intArr) >= 2:
        for i in range(1,len(intArr)):
            string = string + " " + str(intArr[i])
    return string 