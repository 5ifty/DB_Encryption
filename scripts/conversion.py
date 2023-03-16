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
    def converter(self):
        preconversion = pandas.read_excel(r"C:/Users/user/Documents/DB_Encryption/input/spreadsheetData.xlsx", sheet_name='ClientData')

        conversionList = preconversion.to_json(orient='records') # This outputs a string in json format

        conversionDict = json.loads(conversionList) # Converst list of raw data into a Json dict
    # This is dumping the data into a .json format
    # Due to error handling I've decided to check if the path is there or not
    # If it is there, we will continue, else we will make the file to dump, to stop any PathSpec Errors.
        self.Path = r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json'
        with open(self.Path, 'w+') as convertedData:
            json.dump(conversionDict, convertedData)
        
    def iterateJson(self):
        with open(self.Path, 'r') as toPrettify:
            jsonify = json.load(toPrettify)
            for first_name in range(len(jsonify)):
                jsonify[first_name]['first_name']
            for last_name in range(len(jsonify)):
                jsonify[last_name]['last_name']
            for company in range(len(jsonify)):
                jsonify[company]['Company']
            for email in range(len(jsonify)):
                jsonify[email]['email']
            


        


        
if __name__ == '__main__':
    SSC = SpreadsheetConverter()
    SSC.converter()
    SSC.iterateJson()