import csv

import mysql.connector


class PersistenceLayer:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = None

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        self.mydb.close()

    def populate_from_csv(self, file_path):
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            count = 0  # counter to keep track of number of rows read
            for row in reader:
                if count >= 100:  # exit loop if count reaches 100
                    break
                data = {
                    "REF_DATE": row["REF_DATE"],
                    "GEO": row["GEO"],
                    "DGUID": row["DGUID"],
                    "A_pfvp": row["A_pfvp"],
                    "UOM": row["UOM"][:50],
                    "UOM_ID": row["UOM_ID"],
                    "SCALAR_FACTOR": row["SCALAR_FACTOR"],
                    "SCALAR_ID": row["SCALAR_ID"],
                    "VECTOR": row["VECTOR"],
                    "COORDINATE": row["COORDINATE"],
                    "VALUE": row["VALUE"],
                    "STATUS": row["STATUS"],
                    "SYMBOL": row["SYMBOL"],
                    "TERMINATED": row["TERMINATED"],
                    "DECIMALS": row["DECIMALS"]
                }
                self.create(data)
                count += 1  # increment the counter after each row is read


    def create(self, data):
        self.connect()
        cursor = self.mydb.cursor()

        # prepare the SQL query
        sql = "INSERT INTO potato (REF_DATE, GEO, DGUID, A_pfvp, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, DECIMALS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
        values = (data["REF_DATE"], data["GEO"], data["DGUID"], data["A_pfvp"], data["UOM"], data["UOM_ID"],
                  data["SCALAR_FACTOR"], data["SCALAR_ID"], data["VECTOR"], data["COORDINATE"], data["VALUE"],
                  data["DECIMALS"])

        # execute the query and commit the changes
        cursor.execute(sql, values)
        self.mydb.commit()

        cursor.close()
        self.disconnect()

    def read(self, data):
        self.connect()
        cursor = self.mydb.cursor()

        # prepare the SQL query
        sql = "SELECT * FROM potato WHERE REF_DATE = %s AND GEO = %s AND DGUID = %s"
        values = (data["REF_DATE"], data["GEO"], data["DGUID"])

        # execute the query and fetch the result
        cursor.execute(sql, values)
        result = cursor.fetchall()

        cursor.close()
        self.disconnect()

        if result and len(result) >= 1:
            return result
        else:
            return None

    def update(self, data, updated_data):
        self.connect()
        cursor = self.mydb.cursor()

        # prepare the SQL query
        sql = "UPDATE potato SET REF_DATE = %s, GEO = %s, DGUID = %s, A_pfvp = %s, UOM = %s, UOM_ID = %s, SCALAR_FACTOR = %s, SCALAR_ID = %s, VECTOR = %s, COORDINATE = %s, VALUE = %s, DECIMALS = %s WHERE REF_DATE = %s AND GEO = %s AND DGUID = %s"
        values = (updated_data["REF_DATE"], updated_data["GEO"], updated_data["DGUID"], updated_data["A_pfvp"],
                  updated_data["UOM"], updated_data["UOM_ID"],
                  updated_data["SCALAR_FACTOR"], updated_data["SCALAR_ID"], updated_data["VECTOR"],
                  updated_data["COORDINATE"], updated_data["VALUE"], updated_data["DECIMALS"], data["REF_DATE"],
                  data["GEO"], data["DGUID"])

        # execute the query and commit the changes
        try:
            # execute the query and commit the changes
            cursor.execute(sql, values)
            self.mydb.commit()
            cursor.close()
            self.disconnect()
            return True
        except:
            cursor.close()
            self.disconnect()
            return False

    def delete(self, data):
        self.connect()
        cursor = self.mydb.cursor()

        # prepare the SQL query
        sql = "DELETE FROM potato WHERE REF_DATE = %s AND GEO = %s AND DGUID = %s"
        values = (data["REF_DATE"], data["GEO"], data["DGUID"])

        # execute the query and commit the changes
        try:
            # execute the query and commit the changes
            cursor.execute(sql, values)
            self.mydb.commit()
            cursor.close()
            self.disconnect()
            return True
        except:
            cursor.close()
            self.disconnect()
            return False

    def read_all(self):
        self.connect()
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM potato")
        return cursor.fetchall()
