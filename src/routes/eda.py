from fastapi import FastAPI, status, HTTPException, Depends, UploadFile,File, Request,Response
from io import BytesIO
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import logging
import os 
from datetime import datetime

class Eda():

    def __init__(self):

        """
        Initialize class
        """

    def read_file(self, file):

        try:
            contents = file.file.read()
            buffer = BytesIO(contents)
            self.df = pd.read_csv(buffer)
            buffer.close()
            file.file.close()
            shape_df=self.df.count().to_dict()
            #headers = {'Content-Disposition': 'attachment; filename="data.json"'}
            #return Response(df.to_json(orient="records"), headers=headers, media_type='application/json')
            return shape_df
        
        except Exception as e:
            logging.info('Error is: ', e)
    
    def add_new(self,new_col,new_val):

        print(new_col)
        print(new_val)
        self.df[new_col]=pd.Series(new_val)

        #self.df.insert(2,new_val,new_col,True)
        shape_df=self.df.count().to_dict()

        return shape_df


    def clean_file(self):
        
        
        self.df=self.df.replace(to_replace="?", value="NA")
        self.df=self.df.replace(to_replace=" ", value="NA")
        col_name=list(self.df.columns)

        #If we have any numerical attributes that have missing values , fetch the specific points and replace missing values with median of that column

        for i in col_name:
            if self.df[i].dtype=='float64' or self.df[i].dtype=='int64':
                self.df[i].fillna(value=int(self.df[i].median()), inplace=True)
            #self.df[i].fillna(method = 'ffill', inplace = True)
        cleaned_df= list(self.df.isnull().sum())
        return cleaned_df
       

    def stats(self,col):

        #dynamically takes a datapoint name and returns statistical values of that column 
    
        stat_df_data=self.df[col].describe().to_dict()
        return stat_df_data

                
    def plot_file(self):

        now = datetime.now()
        my_path="src/data/eda_images/"
        today_filename = "Histplot"+now.strftime("%d-%m-%Y")+".png"
        self.df.hist(linewidth=1, histtype='stepfilled', facecolor='#e88b84', figsize=(15, 15))
        plt.savefig(my_path+today_filename)
        plt.close()

        #Scatterplot that shows employees absent hours based on their age

        scatterfilename = "Scatterplot"+now.strftime("%d-%m-%Y")+".png"
        scat= plt.scatter('AbsentHours','Age', data=self.df)
        plt.savefig(my_path+scatterfilename)


        return f"Plots saved successfully in {my_path}"
    