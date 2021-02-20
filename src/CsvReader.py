import csv

class CsvReader:
    data = []

    def __init__(self):
        pass

    def csv(self, data_path):
        with open(data_path) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

        return self.data