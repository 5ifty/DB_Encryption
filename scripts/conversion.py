import pandas
import json
import os

# This script handles the conversion of the
# .xlxs(Spreadsheet), into a json file for encryption
# 

class SpreadsheetConverter():
    def __init__(self) -> None:
        pass
# This converter function allows for multiple processes
# in converting the xlsx file into a readable json format which will then be processed into the DB
    def converter():
        preconversion = pandas.read_excel(r"C:/Users/user/Documents/DB_Encryption/input/spreadsheetData.xlsx", sheet_name='ClientData')

        conversionList = preconversion.to_json(orient='records') # This outputs a string in json format

        conversionDict = json.loads(conversionList) # Converst list of raw data into a Json dict
    # This is dumping the data into a .json format
    # Due to error handling I've decided to check if the path is there or not
    # If it is there, we will continue, else we will make the file to dump, to stop any PathSpec Errors.
        Path = r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json'
        with open(r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json', 'w+') as convertedData:
            json.dump(conversionDict, convertedData)


if __name__ == '__main__':
    SpreadsheetConverter()
    SpreadsheetConverter.converter()