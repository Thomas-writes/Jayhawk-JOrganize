import csv

lst = []



with open("matrix (2).csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    for line in csvreader:
        if line != []:
            lst.append(line)

    for element in lst[1:]:
        for item in range(len(element)):
            if isinstance(element[item], str):
                element[item] = element[item].replace("$","")
                element[item] = element[item].replace("%","")
                element[item] = element[item].replace(",","")
                element[item] = element[item].replace("+","")

    date_index = 0
    gross_index = 8
    title_index = 0
    date_index = 0



    headers = lst[0]
    title_headers = ["titles", "#1 release", "title", "video game", "movie"]
    for i in range(len(headers)):
        for j in title_headers:
            if headers[i].lower() == j:
                headers[i] = "title1"
                title_index = i

    date_headers = ["dates", "days", "year", "month", "date", "months", "years"]
    for i in range(len(headers)):
        for j in date_headers:
            if headers[i].lower() == j:
                headers[i] = "date1"
                date_index = i
    
    values = lst[1]
    tempValues = []
    for i in range(len(values)):
        if "1" in values[i] or "2" in values[i] or "3" in values[i] or "4" in values[i] or "5" in values[i] or "6" in values[i] or "7" in values[i] or "8" in values[i] or "9" in values[i]:
            try:
                tempValues.append(int(values[i]))
            except:
                pass
            
    #print(tempValues)
    max = 0
    for i in tempValues:
        if i > max:
            max = i
    changei = values.index(str(max))

    headers[changei] = "maxVal"

    #print(headers)
    values = lst[1::]

    title_lst = []
    maxVal_lst = []
    date_lst = []

    #print(title_index)

    for i in range(len(lst[1:])):
        maxVal_lst.append(lst[i+1][changei])
    for i in range(len(lst[1:])):
        title_lst.append(lst[i+1][title_index])
    for i in range(len(lst[1:])):
        date_lst.append(lst[i+1][date_index])

    #print(maxVal_lst)
    #print(title_lst)
    #print(date_lst)

    

    
    #print(lst[0][0])
    """for element in lst[1:]:
        date = element[date_index]
        gross = element[gross_index]

        try:
            gross = float(gross)
        except ValueError:
            gross = 0.0

        myDict[date] = gross
"""
    #print(myDict)





    #for item in sorted_data:
        #print(item)
    key_list = date_lst[1:]
    values_list = maxVal_lst[1:]
    date_val_dict = {}
    for i in range(len(key_list)):
        date_val_dict[key_list[i]]= values_list[i]

    print(date_val_dict)
    print(title_lst)