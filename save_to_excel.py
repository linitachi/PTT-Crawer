
import csv


class Savefile:
    def __init__(self, file_name):
        self._file_name = file_name
        with open(self._file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['標題', '價格', '發文日期', '作者'])

    def savetocsv(self, data):
        # 這裡要注意一下存的格()  []
        with open(self._file_name, 'a') as csv_file:
            for author, date, title, price in data:
                writer = csv.writer(csv_file)
                writer.writerow([title, price, date, author])
