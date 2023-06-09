import pandas
import json
import os
import csv
# This script handles the conversion of the
# .xlxs(Spreadsheet), into a json file for encryption
# 

class SpreadsheetConverter():
    def __init__(self) -> None:
        self.Path = r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json'
        pass
# This converter function allows for multiple processes
# in converting the xlsx file into a readable json format which will then be processed into the DB
    def converter(self):
        xlsx2Csv = pandas.read_excel(r'C:/Users/user/Documents/DB_Encryption/input/spreadsheetData.xlsx')
 
        xlsx2Csv.to_csv(r'C:/Users/user/Documents/DB_Encryption/output/CSVData.csv', index=None, header=True)
        csvPath = r'C:/Users/user/Documents/DB_Encryption/output/CSVData.csv'
        jsonPath = r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json'

        if os.path.exists(r'C:/Users/user/Documents/DB_Encryption/output/CSVData.csv') == True:
            pass
        try:
            readCSV = pandas.DataFrame(pandas.read_csv(r'C:/Users/user/Documents/DB_Encryption/output/CSVData.csv)'))
        except OSError as e:
            pass

        # cvs2Json = xlsx2Csv.to_json(r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json')
        data = {}
        with open(csvPath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                person = rows['first_name']
                data[person] = rows
        with open(jsonPath, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))

        with open(self.Path, 'r') as jsonFile:
            iterateJson = json.load(jsonFile)
            for first_name in iterateJson:
                openDict = iterateJson[first_name]
                firstName = openDict['first_name']
                lastName = openDict['last_name']
                company = openDict['Company']
                email = openDict['email']
                risk = openDict['Risk']
                contact = openDict['contact']
                status = openDict['Status']
                print(f'{firstName, lastName, company, email, risk, contact, status}')
                


if __name__ == '__main__':
    S = SpreadsheetConverter()
