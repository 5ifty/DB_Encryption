import mysql, mysql.connector
import json
from scripts.decryption import Decryption

class DB():
    def __init__(self) -> None:
        pass

    def databaseConnection(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'BD9vyfrx',
            database = 'collegedatabase'
        )
        if self.connection.is_connected():
            print('Connected!')
        else:
            print(':(')
    
    # For the sake of time consumption in this project- I have manually added in the tables to the database- all this loop is doing is getting the decrypted data
    # Then parsing it into the predefined Tables in the DB. This should do this simultaniously.
    def parseToDatabase(self):
        cursor = self.connection.cursor()
        # Making the tables just in case
        #cursor.execute("CREATE TABLE customers_id (id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (id))")
        # Create the first_names table
        #cursor.execute("CREATE TABLE first_name (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, first_name VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")
        #cursor.execute("CREATE TABLE last_name (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, last_name VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")
        #cursor.execute("CREATE TABLE email (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, email VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")
        #cursor.execute("CREATE TABLE contact (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, contact VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")
        #cursor.execute("CREATE TABLE Company (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, Company VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")
        #cursor.execute("CREATE TABLE Status (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, Status VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")
        #cursor.execute("CREATE TABLE Risk (id INT NOT NULL AUTO_INCREMENT, customer_id INT NOT NULL, Risk VARCHAR(50) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (customer_id) REFERENCES customers_id(id))")

        with open(r'C:\Users\oem\Documents\DB_Encryption\output\encryptionKey.json') as f:
            data = json.load(f)
            for record in data.values():
                query = ("INSERT INTO your_table (first_name, last_name, email, contact, Company, Risk, Status) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                values = (record['first_name'], record['last_name'], record['email'], record['contact'], record['Company'],
                record['Risk'], record['Status'])
                cursor.execute(query, values)
                # Get the ID of the last inserted record
                customer_id = cursor.lastrowid

                # Insert the remaining fields into their respective tables, using the customer_id as a foreign key
                cursor.execute("INSERT INTO customers_id (id) VALUES (%s)", (customer_id,))
                cursor.execute("INSERT INTO first_name (customer_id, first_name) VALUES (%s, %s)", (customer_id, record['first_name']))
                cursor.execute("INSERT INTO last_name (customer_id, last_name) VALUES (%s, %s)", (customer_id, record['last_name']))
                cursor.execute("INSERT INTO email (customer_id, email) VALUES (%s, %s)", (customer_id, record['email']))
                cursor.execute("INSERT INTO contact (customer_id, contact) VALUES (%s, %s)",(customer_id, record['contact']))
                cursor.execute("INSERT INTO Company (customer_id, contact) VALUES (%s, %s)",(customer_id, record['Company']))
                cursor.execute("INSERT INTO Status (customer_id, contact) VALUES (%s, %s)",(customer_id, record['Status']))
                cursor.execute("INSERT INTO Risk (customer_id, contact) VALUES (%s, %s)",(customer_id, record['Risk']))


        

if __name__ == '__main__':
    db = DB()
    db.databaseConnection()
    db.parseToDatabase()

# This should be useful for tomorrow - https://stackoverflow.com/questions/40450591/converting-json-to-sql-table