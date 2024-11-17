#Table 1 good!
#------------------------------------------------

def trends(pList): # assumes that you have a list of percentages (like apples/farm) and tells you if the trend is positive, negative or "Stable" (not sure if thats the right word)
    n=(len(pList))-1
    if pList[n] > pList[0]:
        trend_word="Positive"
    elif pList[n] < pList[0]:
        trend_word="Negative"
    else:
        trend_word="Stable"
    return trend_word
    

def analysis_1(np,plt,appleFarmDict,yearList,graph_title="Title",x_title="x-axis",y_title="y-axis"): #assumes that you have a dictionary with the two things you want to compare [i.e apples(value) per farm (key)] LISTS MUST BE PROPORTIONAL!!
    pDict=dict()
    pList=[]
    yearCounter=0
    for farm,apple in appleFarmDict.items():
        percent=int((apple/farm)*100)
        pList.append(percent)
        pDict[yearList[yearCounter]]=percent
        yearCounter+=1
    table_1_trend=(f"$Trend:$ ${trends(pList)}$")

    x1=[]
    y1=[]
    for key in pDict.keys():
        x1.append(int(key))
    for value in pDict.values():
        y1.append(value)
    change_x=(x1[1]-x1[0])
    plt.plot(x1,y1)
    x2=[x1[0],x1[(len(x1))-1]] 
    y2=[y1[0],y1[(len(x1))-1]] 
    plt.plot(x2, y2, linestyle='-', color=((120/225),0,0,0.6), dashes=[3, 2], label="Trendline")
    plt.plot(x2, y2, linestyle='-', color=((0,0,0,0)), dashes=[1,6], label=table_1_trend)

    plt.legend()
    plt.xticks(np.arange(x1[0],(x1[len(x1)-1]+change_x), 1.0))
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(graph_title)

    final_plot=plt.savefig("analysis_1.png", transparent=False)
    return final_plot
#-----------------------------------------------
#Table 2 GOOD!!
def analysis_2(plt,pets,Chart_title="Title"): #assuming the category is individual and in a list
    petDict={}
    petDict_percentages={}
    animal_list=[]
    percentage_list=[]
    for animal in pets:
        if animal in petDict:
            petDict[animal]+=1
        else:
            petDict[animal]=1
    for Animal,value in petDict.items():
        percentage_list.append((value/(len(pets)))*100)
        petDict_percentages[Animal]=((value/(len(pets)))*100)
    for single_animal in petDict.keys():
        animal_list.append(single_animal)
        slices=percentage_list
#the actual chart:
    colors=[((120/225),0,0), ((193/225),(18/225),(31/225)), (0.98, 0.88, 0.20), (0,(48/225),(73/225)), ((102/225),(155/225),(188/225))]
    plt.pie(slices, labels=animal_list, colors=colors, startangle=90, radius=1.2, autopct="%1.1f%%")
    plt.legend(bbox_to_anchor=(1.05, 1.0),loc="upper left")
    plt.title(Chart_title)
    final_plot=plt.savefig("analysis_2.png",transparent=True)
    return final_plot      #!!!!!is this a good export??!!!!!!!!!!!
#---------------------------------------------------------------------------------

#Table 3:
#-------------------------------DO NOT TOUCH!---------------------------------------------
def n_categories(categoryDict_list):
        n_categories={}
        for items in categoryDict_list:
            for category in items:
                if category in n_categories:
                    n_categories[category]+=1
                else:
                    n_categories[category]=1
        return n_categories
    
def master_sword(repeat_num, cat_names_list):
    master_list_name=cat_names_list[repeat_num]
    return master_list_name

def funny_repeat(repeat_num, categoryDict_list, cat_names_list ): 
    simple_names=master_sword(repeat_num, cat_names_list)
    silly_string=[]
    for items in categoryDict_list:
        for keyName,nameValue in items.items():
            if keyName == cat_names_list[repeat_num]:
                silly_string.append(nameValue)
                
    print(silly_string)
    return silly_string
#-------------------------------DO NOT TOUCH!---------------------------------------------
def averages(mega_list):
    average_list=[]
    sum=0
    for list in mega_list:
        for num in list:
            sum+=num
        avg=sum/(len(list))
        average_list.append(avg)
    return average_list

def single_game_analysis(np,plt,nest_of_nests):
    #person_list = [key for key in nest_of_nests.keys()] 
    #print(person_list) #person list is a list of p1,p2, etc
    categoryDict_list =  [value for value in nest_of_nests.values()]
    cat_names_dict=n_categories(categoryDict_list)
    magic_num=len(n_categories(categoryDict_list)) #the number of categories 
    cat_names_list=[]
    mega_list=[]
    counter=0
    for key in cat_names_dict:
        cat_names_list.append(key)
    while counter!= magic_num:
        oh_my_god=(funny_repeat(counter,categoryDict_list, cat_names_list))
        mega_list.append(oh_my_god)
        counter+=1
    print("b",cat_names_list)
    #print(mega_list) #megalist is a list of each category's rating
    average_list=averages(mega_list)
    #print("a",average_list) #pretty self explanatory, an avg of each category's rating, in a list
    return average_list
    
def analysis_3(np,plt,nest_of_nests):
    n_nestNests="FUCK IF I KNOW"# num of video games
    single_game_analysis(np,plt,nest_of_nests)
    
    categoryDict_list =  [value for value in nest_of_nests.values()]
    print(categoryDict_list)
    cat_names_dict=n_categories(categoryDict_list)
    magic_num=len(cat_names_dict)
"""    #actual graph
    x=np.aranage(magic_num)
    width = 0.25
    multiplier=0
    fig, ax= plt.subplots(layout="constrained")
    #for attribute, measurement
"""

"""
def empty_table():
    from PIL import Image, ImgaeDraw, ImageFont
    img=Image.open("empty.png")
    img.save("new_image.png")
    return img.save()
"""
def main():
    import matplotlib.pyplot as plt
    import numpy as np
    
    nested_dict= {"P1":{"Story": 1, "Visuals": 2, "Gameplay": 3}, "P2":{"Story": 4, "Visuals":5, "Gameplay": 6}, "P3": {"Story": 7, "Visuals": 8, "Gameplay":9} }
    analysis_3(np,plt,nested_dict)
    print()

main()