import mysql.connector
import json
from scripts.decryption import Decryption

class DB():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='BD9vyfrx',
            database='collegedatabase'
        )
        if self.connection.is_connected():
            print('Connected!')
        else:
            print(':(')

    def parseToDatabase(self):
        cursor = self.connection.cursor()
        cursor.execute("DESCRIBE customers_id")
        column_names = [column[0] for column in cursor.fetchall()]

        if "first_name" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN first_name VARCHAR(255)")

        if "last_name" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN last_name VARCHAR(255)")
        
        if "email" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN email VARCHAR(255)")

        if "contact" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN contact VARCHAR(255)")

        if "Status" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN Status VARCHAR(255)")
        
        if "Company" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN Company VARCHAR(255)")

        if "Risk" not in column_names:
            cursor.execute("ALTER TABLE customers_id ADD COLUMN Risk VARCHAR(255)")




        with open(r'C:\Users\user\Documents\DB_Encryption\output\decryptedData.json') as f:
            data = json.load(f)
            for record_id, record in data.items():
                query = ("INSERT INTO customers_id (first_name, last_name, email, contact, Company, Risk, Status) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                values = (
                    record.get('first_name', ''),
                    record.get('last_name'),
                    record.get('email'),
                    record.get('contact'),
                    record.get('Company'),
                    record.get('Risk'),
                    record.get('Status')
                )

                cursor.execute(query, values)
                # Get the ID of the last inserted record
                customer_id = cursor.lastrowid

                # Insert the remaining fields into their respective tables, using the customer_id as a foreign key
                cursor.execute("INSERT INTO first_name (customer_id, new_first_name) VALUES (%s, %s)", (customer_id, record['first_name']))
                cursor.execute("INSERT INTO last_name (customer_id, last_name) VALUES (%s, %s)", (customer_id, record['last_name']))
                cursor.execute("INSERT INTO email (customer_id, email) VALUES (%s, %s)", (customer_id, record['email']))
                cursor.execute("INSERT INTO contact (customer_id, contact) VALUES (%s, %s)", (customer_id, record['contact']))
                cursor.execute("INSERT INTO Company (customer_id, Company) VALUES (%s, %s)", (customer_id, record['Company']))
                cursor.execute("INSERT INTO Status (customer_id, Status) VALUES (%s, %s)", (customer_id, record['Status']))
                cursor.execute("INSERT INTO Risk (customer_id, Risk) VALUES (%s, %s)", (customer_id, record['Risk']))

            self.connection.commit()





if __name__ == '__main__':
    db = DB()
    db.parseToDatabase()
