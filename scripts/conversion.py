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
                firstName = rows['first_name']
                data[firstName] = rows
        with open(jsonPath, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))
    
    def iterateJson(self):
        with open(self.Path, 'r') as toPrettify:
            jsonify = json.load(toPrettify)
            for key in range(len(jsonify)):
                firstName = key[firstName]['first_name']
                lastName = key[firstName]['last_name']
                company = key[firstName]['company']
                email = key[firstName]['email']
                contact = key[firstName]['contact']
                risk = key[firstName]['Risk']
                status = key[firstName]['Status']
            print(firstName, lastName, company, email, contact, risk, status)
                
            
        
if __name__ == '__main__':
    SSC = SpreadsheetConverter()
    SSC.converter()
    SSC.iterateJson()