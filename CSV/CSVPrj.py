import pandas as pd
import matplotlib.pyplot as plt
import csv 


def column_names(fileName):
    df = pd.read_csv(f'{fileName}.csv')
    list_of_column_names = list(df.columns)
    return list_of_column_names


def visualization_csv():
    x = []
    y = []
    
    fileName = input('enter your csv file name in the directory:')
    csvFile = open(f'{fileName}.csv', 'r')
    lines = csv.reader(csvFile, delimiter=',') 
    for row in lines: 
        x.append(row[0]) 
        y.append(row[1])
  
    column = column_names(fileName)
    plt.scatter(x, y, color = 'g',s = 100) 
    plt.xticks(rotation = 25) 
    plt.xlabel(f'{column[0]}') 
    plt.ylabel(f'{column[1]}') 
    plt.title('') 
    plt.show() 


def visualization_csv_merged(fileName):
    x = []
    y = []
    
    csvFile = open(f'{fileName}.csv', 'r')
    lines = csv.reader(csvFile, delimiter=',') 
    for row in lines: 
        x.append(row[0]) 
        y.append(row[1])
  
    column = column_names(fileName)
    plt.scatter(x, y, color = 'g',s = 100) 
    plt.xticks(rotation = 25) 
    plt.xlabel(f'{column[0]}') 
    plt.ylabel(f'{column[1]}') 
    plt.title('') 
    plt.show() 


def merge_two_csv():
    csvFileName = input('enter your first csv file name in the directory:')
    csvFileName2 = input('enter your second csv file name in the directory:')
    df1 = pd.read_csv(f'{csvFileName}.csv')
    df2 = pd.read_csv(f'{csvFileName2}.csv')
    c_result_m = df1.merge(df2, how='outer')
    print(c_result_m)
    #creating merged file
    c_result_m.to_csv(f'merged file_{csvFileName}+{csvFileName2}.csv', index=False)
    print(f'check the "merged file_{csvFileName}+{csvFileName2}.csv" at directory for more information ')
    fileName =f'merged file_{csvFileName}+{csvFileName2}'
    return fileName


def main():
    while True:
        print('1: Visualization\n2: Merge\n3: Exit')
        chk = input('select a number:')
        if chk == '1':
            visualization_csv()
            continue
        elif chk == '2':
            fileName = merge_two_csv()
            chk1 = input('do you want to visualise the merged file?(y or n):')
            while True:
                if chk1 == 'y':
                    visualization_csv_merged(fileName)
                    break
                elif chk1 == 'n':
                    break
        elif chk == '3':
            print('Goodbye')
            break
        
        

main()