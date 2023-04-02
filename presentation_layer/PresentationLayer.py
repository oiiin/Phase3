import csv
import matplotlib.pyplot as plt

from business_layer.BusinessLayer import BusinessLayer

class PresentationLayer:
    def __init__(self):
        self.service = BusinessLayer()

    def insert(self, file_path):
        self.service.populate(file_path)
        print("Database populated successfully.")

    def add_record(self, data):
        self.service.create(data)
        print("Record added successfully.")

    def get_record(self, data):
        record = self.service.read(data)
        if record:
            print("Record found:")
            print(f"REF_DATE: {record[0][0]}")
            print(f"GEO: {record[0][1]}")
            print(f"DGUID: {record[0][2]}")
            print(f"A_pfvp: {record[0][3]}")
            print(f"UOM: {record[0][4]}")
            print(f"UOM_ID: {record[0][5]}")
            print(f"SCALAR_FACTOR: {record[0][6]}")
            print(f"SCALAR_ID: {record[0][7]}")
            print(f"VECTOR: {record[0][8]}")
            print(f"COORDINATE: {record[0][9]}")
            print(f"VALUE: {record[0][10]}")
            print(f"STATUS: {record[0][11]}")
            print(f"SYMBOL: {record[0][12]}")
            print(f"TERMINATED: {record[0][13]}")
            print(f"DECIMALS: {record[0][14]}")
        else:
            print("Record not found.")

    def update_record(self, data, updated_data):
        success = self.service.update(data, updated_data)
        if success:
            print("Record updated successfully.")
        else:
            print("Record not found.")

    def delete_record(self, data):
        success = self.service.delete(data)
        if success:
            print("Record deleted successfully.")
        else:
            print("Record not found.")

    def generate_horizontal_bar_chart(self):
        # Get user input for fields to use
        print("Select fields to use for bar chart:")
        print("1. A_pfvp")
        print("2. Value")
        field_1_choice = int(input("Enter choice for field 1: "))
        field_2_choice = int(input("Enter choice for field 2: "))

        # Determine field names based on user input
        field_1_name = ""
        field_2_name = ""
        if field_1_choice == 1:
            field_1_name = "A_pfvp"
        elif field_1_choice == 2:
            field_1_name = "Value"
        if field_2_choice == 1:
            field_2_name = "A_pfvp"
        elif field_2_choice == 2:
            field_2_name = "Value"

        # Retrieve data from service layer
        data = self.service.read_all()

        # Extract relevant data from each record
        field_1_values = [row[field_1_choice-1] for row in data]
        field_2_values = [row[field_2_choice-1] for row in data]

        # Create horizontal bar chart
        fig, ax = plt.subplots()
        ax.barh(field_1_values, field_2_values)
        ax.invert_yaxis()  # Invert y-axis to show items in descending order
        ax.set_xlabel(field_2_name)
        ax.set_ylabel(field_1_name)
        ax.set_title('Horizontal Bar Chart')

        plt.show()