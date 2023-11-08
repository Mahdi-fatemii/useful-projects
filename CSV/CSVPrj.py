import pandas as pd
import matplotlib.pyplot as plt
import csv 


def column_names(fileName):
    #reading the csv file 
    df = pd.read_csv(f'{fileName}.csv')
    #making a list of columns name from the csv file    
    list_of_column_names = list(df.columns)
    return list_of_column_names


def visualization_csv():
    x = []
    y = []
    
    fileName = input('enter your csv file name in the directory:')
    #opening the csv file
    csvFile = open(f'{fileName}.csv', 'r')
    #reading the file using csv.reader( ) function
    lines = csv.reader(csvFile, delimiter=',') 
    # Reading each line in the file using for loop
    for row in lines:      #Append required columns of the CSV file into a list
        x.append(row[0]) 
        y.append(row[1])
    #getting the csv file columns names to use for lable
    column = column_names(fileName)
    #After reading the whole CSV file, plot the required data as X and Y axis.
    plt.scatter(x, y, color = 'g',s = 100) 
    plt.xticks(rotation = 25) 
    plt.xlabel(f'{column[0]}') 
    plt.ylabel(f'{column[1]}') 
    plt.title('') #because the titles of files may be different i left this line empty  
    plt.show() 


def visualization_csv_merged(fileName):
    x = []
    y = []
    
    #opening the csv file
    csvFile = open(f'{fileName}.csv', 'r')
    #reading the file using csv.reader( ) function
    lines = csv.reader(csvFile, delimiter=',') 
     # Reading each line in the file using for loop
    for row in lines:        #Append required columns of the CSV file into a list
        x.append(row[0]) 
        y.append(row[1])
    #getting the csv file columns names to use for lable
    column = column_names(fileName)
    #After reading the whole CSV file, plot the required data as X and Y axis.
    plt.scatter(x, y, color = 'g',s = 100) 
    plt.xticks(rotation = 25) 
    plt.xlabel(f'{column[0]}') 
    plt.ylabel(f'{column[1]}') 
    plt.title('') #because the titles of files may be different i left this line empty  
    plt.show() 


def merge_two_csv():
    #getting the csv files names with input
    csvFileName = input('enter your first csv file name in the same directory as this python file:')
    csvFileName2 = input('enter your second csv file name in the same directory as this python file:')
    df1 = pd.read_csv(f'{csvFileName}.csv') #reading first csv files
    columns1 = column_names(csvFileName) #finding first csv file columns names
    df2 = pd.read_csv(f'{csvFileName2}.csv')#reading second csv files
    columns2 = column_names(csvFileName2) #finding first csv file columns names
    # finding the columns name that exists in both files using for loops and if
    columnEquals = []
    for i in columns1:
        for j in columns2:
            if i == j :
                columnEquals.append(i)
    # a while loop to get the specific name of column to avoid from syntax errors            
    while True:
        [print(i) for i in columnEquals]
        column = input('please enter the column name you want to do the merging on it from the displayed names above:')
        if column in columnEquals:
            break
        else:
            continue
    #merging the two csv files with outer method
    c_result_m = df1.merge(df2, how='outer', on=f'{column}')    #using "on=" to take column on which we want to merge or we can give a list of columns name to merge on multiple columns
    print(c_result_m)
    #creating a new merged file
    c_result_m.to_csv(f'merged file_{csvFileName}+{csvFileName2}.csv', index=False)
    print(f'check the "merged file_{csvFileName}+{csvFileName2}.csv" at directory for more information ')
    fileName =f'merged file_{csvFileName}+{csvFileName2}'
    return fileName


def main():
    while True:
        print('1: Visualization\n2: Merge\n3: Exit')
        chk = input('select a number:')
        if chk == '1':
            # function for visualising the choosen csv file
            visualization_csv()
            continue
        elif chk == '2':
            #merging cs files with below function 
            fileName = merge_two_csv()
            chk1 = input('do you want to visualise the merged file?(y or n):')
            while True:
                if chk1 == 'y':
                    #using the created files name for visualising
                    visualization_csv_merged(fileName)
                    break
                elif chk1 == 'n':
                    break
        elif chk == '3':
            print('Goodbye')
            break
        
        

main()