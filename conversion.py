import pandas
import json

# This script handles the conversion of the
# .xlxs(Spreadsheet), into a json file for encryption
# 

class SpreadsheetConverter():
    def __init__(self) -> None:
        pass
# This converter function allows for multiple processes
# in converting the xlsx file into a readable json format which will then be processed into the DB
    def converter():
        preconversion = pandas.read_excel('../input/spreadsheetData.xlsx', sheet_name='ClientData')

        conversionList = preconversion.to_json(orient='records') # This outputs a string in json format

        conversionDict = json.loads(conversionList) # Converst list of raw data into a Json dict
    # This is dumping the data into a .json format
        with open('../output/convertedData.json', 'r+') as convertedData:
            json.dump(conversionDict, convertedData)


if __name__ == '__main__':
    SpreadsheetConverter()
    SpreadsheetConverter.converter()