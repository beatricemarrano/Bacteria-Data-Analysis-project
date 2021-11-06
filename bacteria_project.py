#                                 BACTERIA PROJECT

#library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''---------------------------------------------------------------------------'''
'''------------------------------     DATA LOAD    ---------------------------'''
'''---------------------------------------------------------------------------'''
def dataLoad(filename):
    # Parameters
    # ----------
    # filename : TYPE string
    #     DESCRIPTION contains the filename of a data file

    # Returns
    # -------
    # data : TYPE An Nx3 matrix
    #     DESCRIPTION.
   
    #open the file for reading
    filein= open(filename, "r")
    #read all lines into an array
    lines= filein.readlines()
    #building the data matrix Nx3 
    data= np.loadtxt(lines)
    #check the errors and skip that row
    print("\n-> Data loading... deleting raws with Temperature not between 10 and 60,\nwith negative rate growth or with a type of bateria that is not 1,2,3 or 4\n")
    count=0 #index row current data
    count1 = 0 #index row original data
    
    for rows in data:
        flag=0 #flag variable that becomes 1 if at least one of the if conditions is true
        if rows[0]<10 or rows[0]>60:
            #error message 
            print("Error: in line", str(count1), "the Temperature isn't between 10 and 60")
            flag=1
            
        if rows[1]<0:
            print("Error:in line", str(count1), "the Growth rate is negative")
            flag=1
            
        if rows[2]!= float(1) and rows[2]!=float(2) and rows[2]!=float(3) and rows[2]!=float(4):
            print("Error:in line", str(count1), "the Bacteria isn't one of the four type of Bacteria")
            flag=1
        #skip this row    
        if flag==1:
            data= np.delete(data, count, 0)
            count=count-1 
            
        count=count+1  
        count1 = count1 + 1

    return data

'''---------------------------------------------------------------------------'''
'''--------------------------      DATA FILTER     ----------------------------'''
'''---------------------------------------------------------------------------'''
def dataFilter(filteredconditions, data):
    # Parameters
    # ----------
    # filteredconditions: TYPE string
    #                   DESCRIPTION it contains BacteriaListeria or RangeofGrowthRate 
    #                               or BacteriaListeria_RangeofGrowthRate
    
    #     DESCRIPTION contains the condition that must be satisfied in order 
    #                 for the data raws to be include in the calculation of 
    #                 statistics and generation of plots.
    # data: TYPE & DESCRIPTION the original Nx3 matrix on which the filteredconditions 
    #                 will be applied
    
    # Returns
    # ---------
    # filtereddata : TYPE & DESCRIPTION the new Nx3 matrix which respects the condition(s) 
    #               choosed by the user
    #         
    
    if filteredconditions=="BacteriaListeria":
        print("\nThe data has been filtered for Bacteria type Listeria\n")
        count=0
        filtereddata=data
        
        for rows in data:          
            #if the type of bacteria isn't the 3rd one(Listeria) we have to delete that raw
            if rows[2]==float(1) or rows[2]==float(2) or rows[2]==float(4):
                #skip this row
                filtereddata= np.delete(filtereddata, count, 0) 
                count=count-1
            count=count+1
              
    elif filteredconditions=="RangeofGrowthRate":
        print("\nThe data has been filtered for growth rate between 0.5 and 1\n")
        count=0
        filtereddata=data
        
        for rows in data:
            #if the growth rate is less than 0.5 or more than 1 we have to delete that raw
            if rows[1]<0.5 or rows[1]>1:
                #skip this row
                filtereddata= np.delete(filtereddata, count, 0) 
                count=count-1
            count=count+1
       
    print(filtereddata)
    return filtereddata

'''---------------------------------------------------------------------------'''
'''------------------------     DATA STATISTICS    ---------------------------'''
'''---------------------------------------------------------------------------'''
def dataStatistics(data, statistic):
    # Parameters
    # ----------
    # data: TYPE matrix Nx3
    #     DESCRIPTION 3 columns, temperature growthrate, bacteria
    #statistic:TYPE string
    #     DESCRIPTION specifying the statistic that should be calculated

    # Returns
    # -------
    # result : TYPE a scalar
    #     DESCRIPTION.it contains the calculated statistic
    
    if statistic=="Mean Temperature":
        v=data[:,0]
        result=np.mean(v)
        print("\nThe Mean Temperature is:", str(result))
        print("\nDESCRIPTION: the mean temperature is the sum of all the temperatures considered in the data, divided by the total number of temperatures considered")
 
    elif statistic=="Mean Growth rate":
        v=data[:,1]
        result=np.mean(v)    
        print("\nThe Mean Growth rate is:", str(result))
        print("\nDESCRIPTION: the mean growth rate is the sum of all the growth rates considered in the data, divided by the total number of growth rates considered")
        
    elif statistic=="Std Temperature":
        v=data[:,0]
        result=np.std(v)
        print("\nThe Std Temperature is:", str(result))
        print("\nDESCRIPTION: the standard deviation of temperature is the square root of the average of the squared deviations from the mean, i.e., std = sqrt(mean(x)), where x = abs(data - data.mean())**2.")
        
    elif statistic=="Std Growth rate":
        v=data[:,1]
        result=np.std(v)
        print("\nThe Std Growth rate is:", str(result))
        print("\nDESCRIPTION: The standard deviation of growth rate is the square root of the average of the squared deviations from the mean, i.e., std = sqrt(mean(x)), where x = abs(data - data.mean())**2.")
        
    elif statistic=="Rows":
        result= np.shape(data)[0]
        print("\nThe number of rows is:", str(result))
        print("\nDESCRIPTION: this is the number of rows in the data")
        
    elif statistic=="Mean Cold Growth rate": #when Temperature<20
        count=0
        for rows in data:
            if rows[0]>20:
                data=np.delete(data, count,0)
                count= count-1
            count=count+1
        
        v=data[:,1]
        result=np.mean(v)
        print("\nThe Mean Cold Growth rate is:", str(result))
        print("\nDESCRIPTION: the mean cold growth rate is the sum of all the growth rates considered in the data when tempearure is less than 20 degrees, divided by the total number of growth rates considered")
        
    elif statistic=="Mean Hot Growth rate": #when temperature>50
        count=0
        for rows in data:
            if rows[0]<50:
                data=np.delete(data, count,0)
                count= count-1
            count=count+1
        
        v=data[:,1]
        result=np.mean(v)
        print("\nThe Mean Hot Growth rate is:", str(result))
        print("\nDESCRIPTION: the mean hot growth rate is the sum of all the growth rates considered in the data when tempearure is grater than 50 degrees, divided by the total number of growth rates considered")    
    
    return result

'''---------------------------------------------------------------------------'''
'''---------------------------     DATAPLOT    -----------------------------'''
'''---------------------------------------------------------------------------'''
def dataPlot(data):
    # Parameters
    # ----------
    # data: TYPE matrix Nx3
    #     DESCRIPTION 3 columns, temperature, growthrate, bacteria

#1) PLOT OF THE NUMBER OF BACTERIA
    bacteria=['Salmonella', 'Bacillus', 'Listeria', 'Brochothrix'] #Bacteria type
    #variables used to count the numbers of each type of bacteria
    sal=0
    bac=0
    lis=0
    brocho=0
    #the last column of the data
    v=data[:,2]
    #counting the numbers of bacteria of the 4 different types
    for i in range(len(v)):
        if v[i]==float(1):
            sal=sal+1
        elif v[i]==float(2):
            bac=bac+1        
        elif v[i]==float(3):
            lis=lis+1    
        elif v[i]==float(4):
            brocho=brocho+1
            
    number_of_bacteria=[sal, bac, lis, brocho]        
    x_pos = np.arange(len(bacteria))
    plt.bar(x_pos, number_of_bacteria, align='center')
    plt.xticks(x_pos, bacteria)
    plt.ylabel('Number of bacteria')
    plt.xlabel('Bacteria type')
    plt.title('Number of different bacteria')
    plt.show()
    
#2) PLOT OF THE GROWTH RATE BY TEMPERATURE
    count1=0
    count2=0
    count3=0
    count4=0
    temp1=np.zeros(1000)
    temp2=np.zeros(1000)
    temp3=np.zeros(1000)
    temp4=np.zeros(1000)
    growth1=np.zeros(1000)
    growth2=np.zeros(1000)
    growth3=np.zeros(1000)
    growth4=np.zeros(1000)
    
    #creating 2 vectors that contains the temperature and the growth rate(for each type of bacteria) 
    for rows in data:
        if rows[2]==float(1):
            temp1[count1]=rows[0]
            growth1[count1]= rows[1]
            count1=count1+1
            
        elif rows[2]==float(2):
            temp2[count2]=rows[0]
            growth2[count2]= rows[1]
            count2=count2+1
            
        elif rows[2]==float(3):
            temp3[count3]=rows[0]
            growth3[count3]= rows[1]
            count3=count3+1
            
        elif rows[2]==float(4):
            temp4[count4]=rows[0]
            growth4[count4]= rows[1]
            count4=count4+1
    
    #we need to order the tempearture arrays in order to make the lines between the
    #dots in the plot ordered.
    #we have also to order the growth array as we are ordering the tempemperature array!                  
    zipped_lists = zip(temp1, growth1)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    temp1, growth1 = [ list(tuple) for tuple in  tuples]    

    zipped_lists = zip(temp2, growth2)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    temp2, growth2 = [ list(tuple) for tuple in  tuples] 
    
    zipped_lists = zip(temp3, growth3)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    temp3, growth3 = [ list(tuple) for tuple in  tuples] 
    
    zipped_lists = zip(temp4, growth4)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    temp4, growth4 = [ list(tuple) for tuple in  tuples] 
    
    #plot of the points and lines with legend, axis, title, ecc
    plt.plot(temp1, growth1, 'rD', label="Salmonella")
    plt.plot(temp1, growth1, '-r')    
    plt.plot(temp2, growth2, 'bs', label= "Bacillus")
    plt.plot(temp2, growth2, '-b')
    plt.plot(temp3, growth3, 'g^', label= "Listeria")
    plt.plot(temp3, growth3, '-g')
    plt.plot(temp4, growth4, 'co', label= "Brochothrix")
    plt.plot(temp4, growth4, '-c')
    
    plt.axis([10,60,0, 1])
    plt.ylabel('Growth rate')
    plt.xlabel('Temperature')
    plt.legend(loc="upper right") 
    plt.title('Growth rate by Temperature')
    plt.show()  

'''---------------------------------------------------------------------------'''      
'''-------------------------      INPUT NUMBER     ---------------------------'''
'''---------------------------------------------------------------------------'''
def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number
    #
    # Usage: num= inputNumber(prompt) Displays prompt and asks user to input a 
    # number. Repeats until user inputs a valid number
    #
    
    while True:
        try:
            num= float(input(prompt))
            break
        except ValueError:
            pass
        
    return num

'''---------------------------------------------------------------------------'''
'''--------------------------    DISPLAY MENU    -----------------------------'''
'''---------------------------------------------------------------------------'''
def displayMenu(options):
# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen. #
# Usage: choice = displayMenu(options)
#
# Input options Menu options (array of strings) 
# Output choice Chosen option (integer)

# Display menu options
    for i in range(len(options)):
        print("\n{:d}. {:s}\n".format(i+1, options[i]))

# Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ") 
    return choice

'''---------------------------------------------------------------------------'''
'''-------------------------------    MAIN    --------------------------------'''
'''---------------------------------------------------------------------------'''
# Define menu items
menuItems = np.array(["Load Data.", "Filter data", "Display statistics", "Generate plots", "Quit"]) 

# Define empty name variable
filename = ""
filteredconditions= ""
f=None 

# Start
while True:
    # Display menu options and ask user to choose a menu item 
    choice = displayMenu(menuItems)
    
    # Menu item chosen
    # ------------------------------------------------------------------ 
    # 1. Load Data
    if choice == 1:
        # Ask user to input the filename and save it in a variable
        #check if the file name is valid
        #if there arn't problems, load data 
        while True:
            try:
                filename=input("Please enter the filename of a data file: ")
                data= dataLoad(filename)
                break
            except FileNotFoundError:
                print("\nNon a valid file name. Please try again.\n")
            
    # ------------------------------------------------------------------ 
    # 2. Filter data
    elif choice == 2:
        # Is choice 1 already choosen?
        if filename == "":
            # Display error message 
            print("\nError: You have to choose 1. Load data before any other options\n")

        else:
            # Filter data
            print("\nThere are 3 different choices for filtring data:\n")
            filtered_condition_options=np.array(["Filter for Bacteria type Listeria", "Filter for growth rate between 0.5 and 1", "Disable all filters"])
            
            while True:
                # Display menu options and ask user to choose a menu item
                subchoice= displayMenu(filtered_condition_options)
                
                #filtered_condition_options chosen
                # ------------------------------------------------------------------ 
                # 1. Bacteria Listeria
                if subchoice == 1: 
                    # filter the data only for bacteria= Listeria type
                    filteredconditions="BacteriaListeria"
                    # filtereddata= dataFilter(filteredconditions, data)
                    if f==2: 
                        f=3
                        #filter from the already filtereddata because it is NOT the first time the user asks to filter
                        filtereddata= dataFilter(filteredconditions, filtereddata)
                    else:
                        f=1
                        #filter from the "original" data because it is the first time the user asks to filter
                        filtereddata= dataFilter(filteredconditions, data)
                    break
                # ------------------------------------------------------------------ 
                # 2. Growth rate between 0.5 and 1
                elif subchoice == 2:
                    # filter the data only for growth rate between 0.5 and 1
                    filteredconditions="RangeofGrowthRate"
                    # filtereddata= dataFilter(filteredconditions, data)   
                    if f==1: 
                        f=3
                        #filter from the already filtereddata because it is NOT the first time the user asks to filter
                        filtereddata= dataFilter(filteredconditions, filtereddata) 
                    else:
                        f=2
                        #filter from the "original" data because it is the first time the user asks to filter
                        filtereddata= dataFilter(filteredconditions, data) 
                    break
                # ------------------------------------------------------------------                
                # 3. Disable all filters
                elif subchoice == 3:
                    #old filters off using again the "original" data
                    filtereddata=data   
                    f=0
                    print("\nAll the old filters have been disabled\n")
                    print(filtereddata)
                    break

    # ------------------------------------------------------------------ 
    # 3. Display statistics
    elif choice == 3:
        # Is choice 1 already choosen?
        if filename == "":
            # Display error message 
            print("\nError: You have to choose 1. Load data before any other options\n")
            # Is choice 2 already choosen?
        if filteredconditions== "":
            print("\nError: You have to choose 2. Filter data before choosing 3. Display statistics\n")

        else:
            #the current filter is:
            print("\nThe current filter is:\n" )
            if f==0:
                print("for the original data\n") 
            if f==1:
                print("for Bacteria type Listeria\n")
            if f==2:
                print("for growth rate between 0.5 and 1\n") 
            if f==3:
                print("for Bacteria type Listeria and for growth rate between 0.5 and 1\n")
            print(filtereddata)

            #display statistics
            print("\n There are 7 different choices for a statistic to be displayed:\n")
            statistics_options=np.array(["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"])
            
            while True:
                subchoice1= displayMenu(statistics_options)
                statistic= ""
                
                #statistics_options chosen
                # ------------------------------------------------------------------ 
                # 1. Mean Temperature
                if subchoice1 == 1: 
                    statistic="Mean Temperature"
                    result= dataStatistics(filtereddata, statistic)
                    break
                # ------------------------------------------------------------------ 
                # 2. Mean Growth rate
                elif subchoice1 == 2:
                    statistic="Mean Growth rate"
                    result= dataStatistics(filtereddata, statistic)           
                    break
                # ------------------------------------------------------------------             
                # 3. Std Temperature
                elif subchoice1 == 3:
                    statistic="Std Temperature"
                    result= dataStatistics(filtereddata, statistic)           
                    break
                # ------------------------------------------------------------------ 
                # 4. Std Growth rate
                elif subchoice1 == 4:
                    statistic="Std Growth rate"
                    result= dataStatistics(filtereddata, statistic)           
                    break
                # ------------------------------------------------------------------ 
                # 5. Rows
                elif subchoice1 == 5:
                    statistic="Rows"
                    result= dataStatistics(filtereddata, statistic)           
                    break
                # ------------------------------------------------------------------ 
                # 6. Mean Cold Growth rate
                elif subchoice1 == 6:
                    statistic="Mean Cold Growth rate"
                    result= dataStatistics(filtereddata, statistic)           
                    break
                # ------------------------------------------------------------------ 
                # 7. Mean Hot Growth rate
                elif subchoice1 == 7:
                    statistic="Mean Hot Growth rate"
                    result= dataStatistics(filtereddata, statistic)           
                    break                
      
    # ------------------------------------------------------------------ 
    # 4. Generate plots
    elif choice == 4:
        # Is choice 1 already choosen?
        if filename == "":
            # Display error message 
            print("\nError: You have to choose 1. Load data before any other options\n")
        elif filteredconditions== "":
            print("\nError: You have to choose 2.Filter data before choosing 4. Generate plot\n")
        else: 
            #the current filter is:
            print("The current filter is:\n" )
            if f==0:
                print("for the original data\n")             
            if f==1:
                print("for Bacteria type Listeria\n")
            if f==2:
                print("for growth rate between 0.5 and 1\n") 
            if f==3:
                print("for Bacteria type Listeria and for growth rate between 0.5 and 1\n")
            print(filtereddata)
            
            #generate plots
            dataPlot(filtereddata)
    #------------------------------------------------------------------ 
    # 5. Quit
    elif choice == 5:
        print("\nThanks and goodbye!\n")
        # End
        break 




