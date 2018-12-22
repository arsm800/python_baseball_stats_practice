# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = '/Users/AndrewSM/Downloads/python_test/Baseball-Reference Data Set - 2017 Pitchers.xlsx'

df = pd.read_excel(file) #dataframe
# I originally tried pd.ExcelFile(), but this did not work.  I was, however, able to call data.sheet_names successfully.  I think 

#You can also do it this way with ExcelFile (this is more efficient because you read the file only once):
data = pd.ExcelFile(file)

def excel_parse():
    df_pitching = data.parse()
    print(df_pitching.head())


#Print sheet names in excel workbook
def sheet_names():
    print(data.sheet_names)

sorted_by_IP = df.sort_values('IP', ascending=False)
topTenIP = sorted_by_IP.head(10)

#Sort by column 'IP' (Innings pitched) and print stats for pitchers with 10 most IP
def top_10_IP_sort():
    print(topTenIP)

#Create IP bar graph
def IP_bar():
    topTenIP.plot(kind='barh')
    plt.show()

#Create histogram of pitchers and the number of innings pitched
def IP_histogram():
    df['IP'].plot(kind='hist')
    plt.title('Innings Pitched')
    plt.ylabel('Pitchers')
    plt.xlabel('Innings')
    plt.show()

#Summary of data in each row
def data_row_summary():
    print(df.describe())

#Query maximum value
def query_max_wins():
    print(df['W'].max())

df_condensed = df[['Name', 'Tm', 'W', 'L', 'ERA', 'GS', 'IP', 'H', 'ER', 'BB', 'SO', 'ERA+', 'FIP', 'WHIP']]

#Create new data_frame using only some of existing columns
def new_df():
    print(df_condensed.head(10))

#Export data to existing black excel workbook
def export_data():
    exportFile = '/Users/AndrewSM/Downloads/python_test/Output.xlsx'
    df_condensed.to_excel(exportFile)

#Rename columns (This function still doesn't work properly)
rename = df_condensed.head(10)

def rename_columns():
    new_columns = rename.columns[0, 1]
    print(new_columns)

#Data for pitchers with ERA between 2 and 3
def ERA_under_3():
    ERA_under_3 = df_condensed[(df_condensed['ERA']<3) & (df_condensed['ERA']>2)]
    ERA_under_3_sorted = ERA_under_3.sort_values('ERA', ascending=False)
    print(ERA_under_3_sorted)
    
#Null Values
def null_values():
    null_values = pd.isnull(rename)
    print(null_values)

#Find all pitchers for the Braves with at least 10 wins
def ATL_Braves():
    braves = df_condensed[(df_condensed['Tm'] == 'ATL') & (df_condensed['W'] >= 10)]
    print(braves)

#Group by team and ERA - multiple variations (This code does not work)
def ERA_rank():
    team = df_condensed.groupby('Tm')['ERA']
    print(team)
    
#Find the number of Braves pitchers
def ATL():
    ATL = df_condensed[df_condensed['Tm'] == 'ATL']
    print(ATL['Name'].count())

#Calculate Atlanta's team WHIP (Hint: you can't just take the mean of each individual pitcher's WHIPs)
def team_WHIP():
    atlanta_braves = df_condensed[df_condensed['Tm'] == 'ATL']
    innings_pitched = atlanta_braves['IP'].sum()
    walks = atlanta_braves['BB'].sum()
    hits = atlanta_braves['H'].sum()
    team_WHIP = (walks+hits)/innings_pitched
    print(team_WHIP)    

#Test out melt function
#pd.melt(frame=df, id_vars='name', value_vars=['treatment a', 'treatment b’], var_name='treatment', value_name='result') 
                #keep this column              #collapse these columns         #new column name        #new column name for 
                                                                               #for value_vars         #fol value_vars
                                                                               #names                  #values
                                                                               
#Test out pivot function
df_pivot = df_condensed[['Name', 'Tm', 'W', 'L', 'SO']]    

def pivot():
    pivot_new = df_pivot.pivot_table(index='Tm', values=['W', 'L', 'SO'], aggfunc=np.sum)
    print(pivot_new.sort_values('W', ascending=False))  
    
    
#Separate first names and last names
def name_split():
    df_condensed['str_split'] = df_condensed.Name.str.split(' ')
    df_condensed['first_name'] = df_condensed.str_split.str.get(0)
    df_condensed['second_name'] = df_condensed.str_split.str.get(1)
    print(df_condensed.head())



#Sort Values
def Sort_SO():
    df_sort = df_condensed[df_condensed['SO']>=200]
    print(df_sort.sort_values('SO', ascending=False))    
    


#Frequency Counts
    
def team_frequency():
    freq = df_condensed.Tm.value_counts(dropna=False).head()
    print(freq)
    #Note: You can also use df_condensed['Tm'].value_counts...


#Summary Statistics
    
def summary():
    summary = df_condensed.describe()
    print(summary)
    
    
#Wins histogram

def wins_hist():
    df_condensed.W.plot('hist')
    plt.show()
    #You can use this histogram to discover outliers in your data.


#Box Plot - wins by team
    
def box_plot():
    df_condensed.boxplot(column='W', by='Tm')
    plt.show()


#Scatter Plot - Test for a correlation between strikeouts and wins

def scatter():
    x = df_condensed['SO']
    y = df_condensed['W']
    plt.scatter(x, y)
    plt.show()
    #You can also do df_condensed.plot(kind='scatter', x='SO', y='W')


#Split column via .str
    
def str_split():
    df_condensed['Letter'] = df_condensed.Tm.str[1:3]  #This takes out letters 1-2 in these (0,1,2,3) positions
    print(df_condensed.head())
    
    

#Split by space via .split() --- sort by last name z to a in own separate column
    
def split_space():
    df_condensed['name_split'] = df_condensed.Name.str.split()
    df_condensed['first_name'] = df_condensed.name_split.str.get(0)
    df_condensed['last_name'] = df_condensed.name_split.str.get(1)
    sorted = df_condensed.sort_values('last_name', ascending=False)
    print(sorted.head())
    
 #pd.concat(axis=0)   - concat rows 
 #pd.concat(axis=1)   - concat columns
 #pd.merge(left, right, left_on, right_on) - merge two tables (this is like a relational database, where "left_on" and "right_on"...
 #...columns are in different tables, but are identical data--like a primary key)  

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
