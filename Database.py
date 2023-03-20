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
            for key in data:
                record = data[key]
                first_name = record['first_name']
                print(first_name)
                last_name = record['last_name']
                email = record['email']
                contact = record['contact']
                Company = record['Company']
                Risk = record['Risk']
                Status = record['Status']
                query = ("INSERT INTO customers_id (first_name, last_name, email, contact, Company, Risk, Status) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                values = (first_name, last_name, email, contact, Company, Risk, Status)

                cursor.execute(query, values)
                # Get the ID of the last inserted record
                customer_id = cursor.lastrowid

                # Insert the remaining fields into their respective tables, using the customer_id as a foreign key
                cursor.execute("INSERT INTO first_name (customer_id, first_name) VALUES (%s, %s)", (customer_id, first_name))
                cursor.execute("INSERT INTO last_name (customer_id, last_name) VALUES (%s, %s)", (customer_id, last_name))
                cursor.execute("INSERT INTO email (customer_id, email) VALUES (%s, %s)", (customer_id, email))
                cursor.execute("INSERT INTO contact (customer_id, contact) VALUES (%s, %s)", (customer_id, contact))
                cursor.execute("INSERT INTO Company (customer_id, Company) VALUES (%s, %s)", (customer_id, Company))
                cursor.execute("INSERT INTO Status (customer_id, Status) VALUES (%s, %s)", (customer_id, Status))
                cursor.execute("INSERT INTO Risk (customer_id, Risk) VALUES (%s, %s)", (customer_id, Risk))

                self.connection.commit()
                print(cursor.rowcount, "record inserted.")

            cursor.close()
            self.connection.close()
    
    def queryDatabase(self, name):
        cursor = self.connection.cursor()
        query = f"SELECT customers_id.id, customers_id.first_name, customers_id.last_name, email.email, contact.contact, Company.Company, Status.Status, Risk.Risk FROM customers_id \
        JOIN first_name ON customers_id.id = first_name.customer_id \
        JOIN last_name ON customers_id.id = last_name.customer_id \
        JOIN email ON customers_id.id = email.customer_id \
        JOIN contact ON customers_id.id = contact.customer_id \
        JOIN Company ON customers_id.id = Company.customer_id \
        JOIN Status ON customers_id.id = Status.customer_id \
        JOIN Risk ON customers_id.id = Risk.customer_id \
        WHERE customers_id.first_name='{name}'"

        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            return row
        cursor.close()
        self.connection.close()






if __name__ == '__main__':
    db = DB()
    db.parseToDatabase()
    db.queryDatabase()
