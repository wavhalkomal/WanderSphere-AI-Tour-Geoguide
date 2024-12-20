#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:50:37 2024

@author: komalwavhal
"""


import pandas as pd
import os 
 
print(os.getcwd())

print( ' ------->>>>> read the excel file execution started '  )

    
print('read and perform data processing ') 
 
print( ' ------->>>>> read the excel file execution started '  )
     
print('read and perform data processing ') 
 


import os

try:
    ### for Windows users
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    print(desktop)
    Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
    print(Parent_Folder_Path)

except: 
    ### for Mac users
    desktop = os.path.expanduser("~/Desktop")
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    Parent_Folder_Path = desktop + "/AAI_551_Project_Repository"
    print(Parent_Folder_Path)
    
Parent_Folder_Path = Parent_Folder_Path
  
# Join various path components
output_filepath = os.path.join(Parent_Folder_Path, "flickr_photos_with_sentiment.xlsx") 
file_path = os.path.join(Parent_Folder_Path, "top_10_images.xlsx")
print(file_path)
  
print('============')

print(' ')
print(Parent_Folder_Path)
# 


file_path = os.path.join(Parent_Folder_Path, "top_10_images.xlsx")

print(' ')
print(Parent_Folder_Path)

print(' ')
print(file_path)

# /Users/komalwavhal/Desktop/AAI_551_Project_Repository/top_10_images.xlsx
# /Users/komalwavhal/Desktop/AAI_551_Project_Repository/top_10_images.xlsx



print(' ')
print(' ')

print(os.path.exists(file_path)) 

# if ()



print( ' ------->>>>> read the excel file execution started '  )
     
print('read and perform data processing ') 
 
df = pd.read_excel(file_path)

# Ensure the data is loaded correctly
# print(df.head())

# Sort the dataset based on the relevant columns:
# - Sentiment Score (higher is better)
# - Views (higher is better)
# - Comment Count (higher is better)

# We will assume that sentiment score, views, and comment count columns exist and are numeric.

# Convert the necessary columns to numeric (in case they are not already)
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce')
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce')
df['Views'] = pd.to_numeric(df['Views'], errors='coerce')
df['Comment Count'] = pd.to_numeric(df['Comment Count'], errors='coerce')
 
# Normalize the columns to combine the scores in a weighted manner.
# You can adjust the weights based on importance: here we just use equal weights for simplicity.

df['Ranking Score'] = df['Sentiment Score'] * 0.5 + df['Views'] * 0.3 + df['Comment Count'] * 0.2

# Sort by the 'Ranking Score' and get the top 5
top_10_images = df.sort_values(by='Ranking Score', ascending=False).head(10)

# Print the top 5 images and their URLs
top_10_image_info = top_10_images[['Place Name', 'Image URL', 'Sentiment Score', 'Views', 'Comment Count']]
    
top_10_images_filepath = os.path.join(Parent_Folder_Path, "top_10_images.xlsx") 
# Optionally, you can save this data into a new Excel file
top_10_image_info.to_excel(top_10_images_filepath, index=False)

print("Top 5 images data saved to 'top_10_images.xlsx'")

df = pd.read_excel('top_10_images.xlsx')

# for i in range(0,5):
#     print(df['Place Name'][i] , ' - ', df['Image URL'][i]) 
	 
    
# os.remove(file_path)  
# os.remove(top_5_images_filepath)
        
error_status = 'Error Not Occured'
print('error_status',error_status)