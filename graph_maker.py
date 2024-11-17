from data_analysis import data
#------------------------------------------------
#Table 1 good!
mydict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, 
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

import os

def clear_old_graphs():
    folder = "static/images/"
    for file_name in os.listdir(folder):
        if file_name.startswith("graph_") and file_name.endswith(".png"):
            os.remove(os.path.join(folder, file_name))

def trends(pList): # assumes that you have a list of percentages (like apples/farm) and tells you if the trend is positive, negative or "Stable" (not sure if thats the right word)
    n=(len(pList))-1
    if pList[n] > pList[0]:
        trend_word="Positive"
    elif pList[n] < pList[0]:
        trend_word="Negative"
    else:
        trend_word="Stable"
    return trend_word
    

def analysis_1(np,plt,numDict,yearList,graph_title="Money x Time",x_title="Date",y_title=""): #assumes that you have a dictionary with the two things you want to compare [i.e apples(value) per farm (key)] LISTS MUST BE PROPORTIONAL!!
    monthsAsNumsList = []
    monthslist = list(numDict.keys())
    try:
        for month in monthslist:
            month = str(month)
            month = month.split(" ")
            shortMonth = month[0]    
            num =int(month[1])
            monthsAsNumsList.append(mydict[shortMonth] * 30 + num)
        x1=monthsAsNumsList
    except:
        newlist = []
        for year in yearList:
            newlist.append(int(year))
        x1 = newlist
    pDict=dict()
    pList=[]
    yearCounter=0
    for num in numDict.values():
        percent=int(num/(len(list(numDict.keys())))*100)
        pList.append(percent)
        pDict[num] = num
        yearCounter+=1
    table_1_trend=(f"$Trend:$ ${trends(pList)}$")
    y1=[]
    for value in pDict.values():
        y1.append(value)
    
    change_x=(x1[1]-x1[0])
    plt.figure(figsize=(20, 20))
    plt.plot(x1,y1, color=((120/225),0,0,1))
    x2=[x1[0],x1[(len(x1))-1]] 
    y2=[y1[0],y1[(len(x1))-1]] 
    plt.plot(x2, y2, linestyle='-', color=((120/225),0,0,0.6), dashes=[3, 2], label="Trendline")
    plt.plot(x2, y2, linestyle='-', color=((0,0,0,0)), dashes=[1,6], label=table_1_trend)

    plt.legend()
    plt.xticks(np.arange(x1[0],(x1[len(x1)-1]+change_x), 1.0))
    plt.xlabel(x_title, fontsize=10)
    plt.ylabel(y_title, fontsize=10)
    plt.title(graph_title, fontsize=5)
    

    final_plot=plt.savefig("static/images/graph_1.png", transparent=False)
    return
#-----------------------------------------------
#Table 2 GOOD!!
def analysis_2(np,plt,category,Chart_title="Title"): #assuming the category is individual and in a list
    petDict={}
    petDict_percentages={}
    animal_list=[]
    percentage_list=[]
    for animal in category:
        if animal in petDict:
            petDict[animal]+=1
        else:
            petDict[animal]=1
    for Animal,value in petDict.items():
        percentage_list.append((value/(len(category)))*100)
        petDict_percentages[Animal]=((value/(len(category)))*100)
    for single_animal in petDict.keys():
        animal_list.append(single_animal)
        slices=percentage_list

    colors=plt.cm.Blues(np.linspace(0,1,10))

    plt.cla()
    plt.pie(slices, labels=animal_list, colors=colors, startangle=90, radius=1.2, autopct="%1.1f%%")
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc="upper left")
    final_plot=plt.savefig("static/images/graph_2.png",transparent=True)
    return    
#------------------------------------------------------------
#table 3:
def analysis_3(plt, x_list, y_list, chart_title, x_title, y_title):
    plt.figure(figsize=(20, 20))
    plt.cla()
    plt.clf()
    plt.plot(
        x_list, y_list,
        color=(0.98, 0.88, 0.20),  
        linestyle='dashed', 
        linewidth=1.5,  
        marker='o', 
        markerfacecolor=(102/255, 155/255, 188/255), 
        markersize=8  
    )
    plt.gca().invert_xaxis()
    plt.title(chart_title, fontsize=24)  
    plt.xlabel(x_title, fontsize=16)
    plt.ylabel(y_title, fontsize=16)
    output_path = "static/images/graph_3.png"
    plt.savefig(output_path, transparent=False)


def create_graphs():
    clear_old_graphs()
    import matplotlib.pyplot as plt #NECESSARY
    import numpy as np #NECESSARY
    from cycler import cycler #this doesnt work idk why
    
    temp = {}
    get_list = data()
    (date_val_dict, title_lst) = get_list.run()
    for i, keys in date_val_dict.items():
        temp[i] = int(keys)
    numDict=temp
    
    yearList=list(temp.keys())
    graph_title1="Title"
    x_title1="Date"
    y_title1="y-axis"
    analysis_1(np,plt,numDict,yearList,graph_title1,x_title1,y_title1)
    """np AND plt are NECESSARY and MUST STAY LIKE THAT | numDict compares two values that you want a value1 per value 2 for | rest are titles for graphs """
    
    category=title_lst
    graph_title2="Title"
    analysis_2(np,plt,category,graph_title2)
    """ plt is NECESSARY and MUST STAY LIKE THAT to make a graph | category is a list[] | title2 is just the title u want for graph2"""
    
    x_list=temp.keys()
    y_list=temp.values()
    graph_title3="Title"
    x_title3="Date"
    y_title3="Money"
    x_list = list(x_list)
    x_list.reverse()
    analysis_3(plt,x_list,y_list,graph_title3,x_title3,y_title3)
    """ plt is NECESSARY and MUST STAY LIKE THAT to make a graph | everything else is actually so free"""
    return ["./static/images/graph_1.png", "./static/images/graph_2.png", "./static/images/graph_3.png"]
