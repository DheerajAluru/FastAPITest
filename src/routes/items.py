from fastapi import FastAPI, status, HTTPException, Depends, UploadFile,File, Request, APIRouter,Query
from src.routes.eda import Eda
from fastapi.responses import JSONResponse
from typing import Annotated,List

Ed=Eda()
router=APIRouter()


@router.get("/")
async def root():
    return "Root"

#This method takes the csv file data, reads the file and returns the csv file info with column names and their value counts

@router.post("/upload")
async def get_file(file: UploadFile= File(...)):

    result= Ed.read_file(file)
    return JSONResponse(result)

#This method takes the csv file data, checks for missing values and fills them if required, return the count of missing values of columns after cleaning. (0 means no missing values)
@router.get("/clean")
async def clean():

    result= Ed.clean_file()
    return {"NA Values after cleaning":JSONResponse(result)}

#This method takes the column name dynamically and returns mean, median, min, max values for numerical variables

@router.get("/stats")
async def stats(col:str):

    result= Ed.stats(col)
    return {f"Stats for {col}":result}
 
#This method plots the histogram and scatter plots of the required variables and saves them in the local directory specified. 

@router.get("/plots")
async def plots():

    result= Ed.plot_file()
    return result


@router.get("/addnew")
async def add_col(new_col:str, new_val: List[str] = Query(None)):
    res= Ed.add_new(new_col,new_val)
    return res