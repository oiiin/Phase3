from presentation_layer.PresentationLayer import PresentationLayer


class Main:
    def __init__(self):
        self.presentation = PresentationLayer()


    def run(self):
        # Example usage of the presentation layer

        self.presentation.insert(r'C:\Users\ahmed\Desktop\Level4\Programming_Language_Research\32100358.csv')


        data = {
            "REF_DATE": "2022",
            "GEO": "Canada",
            "DGUID": "2016A000011124",
            "A_pfvp": "Potato",
            "UOM": "dollars",
            "UOM_ID": 225,
            "SCALAR_FACTOR": "units",
            "SCALAR_ID": 0,
            "VECTOR": "v234567",
            "COORDINATE": 1,
            "VALUE": 5000000,
            "STATUS": "F",
            "SYMBOL": "OK",
            "TERMINATED": "OK",
            "DECIMALS": 0
        }

        self.presentation.add_record(data)

        self.presentation.get_record(data)

        updated_data = {
            "REF_DATE": "2022",
            "GEO": "Canada",
            "DGUID": "2016A000011124",
            "A_pfvp": "Potat14",
            "UOM": "dollars",
            "UOM_ID": 225,
            "SCALAR_FACTOR": "units",
            "SCALAR_ID": 0,
            "VECTOR": "v234567",
            "COORDINATE": 1,
            "VALUE": 6000000,
            "STATUS": "F",
            "SYMBOL": "",
            "TERMINATED": "",
            "DECIMALS": 0
        }

        self.presentation.update_record(data, updated_data)

        self.presentation.delete_record(updated_data)

        self.presentation.generate_horizontal_bar_chart()

        print("Developer: Ahmed Ounissi")


if __name__ == "__main__":
    main = Main()
    main.run()
