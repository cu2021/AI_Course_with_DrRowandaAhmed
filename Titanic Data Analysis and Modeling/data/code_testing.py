# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:33:26 2023

@author: Sally
"""

import pandas as pd
def main():
    df1 = pd.read_csv('train.csv')
    columns= df1[['Age', 'Survived']]
    print(df1)
    df1['Age_Group'] = pd.cut(df1['Age'], bins=[0, 16, 55, 100], labels=['kid', 'adult', 'elder'], include_lowest=True)
    # Save the modified DataFrame back to a new CSV file
    df1.to_csv('train.csv')
    # Exploration of relationship between Age_Group and Survived
    age_survived_count = df1.groupby('Age_Group')['Survived'].count()
    age_survived_mean = df1.groupby('Age_Group')['Survived'].mean()
    age_survived_propo = age_survived_mean *100
    
    print(age_survived_count)
    print(age_survived_propo)
    
    age_result = age_survived_count *100/891
    print(age_result)
if __name__ == "__main__":
	main()
   
