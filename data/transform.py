import csv  # import to use the csv module
import os


def isExist(path):
    return os.path.exists(path)


column_name = ["trade_date", "pre_close", "open", "high", "low", "close", "volume", "amount", "change", "pctchange",
               "vwap", "turnover", "A_current_mv", "B_current_mv", "total_mv", "A_shrout", "B_shrout", "totshrout", "pe", "pb", "ps", "pc", "test"]


def writeOrAppendRow(row):
    fileName = "../csv/"+row[1]+".csv"
    row.pop(1)
    row.pop(1)
    if (isExist(fileName)):
        with open(fileName, 'a') as f:
            writer = csv.writer(f)  # this is the writer object
            writer.writerow(row)  # this is the data
            # writer.close()
    else:
        with open(fileName, 'a') as f:
            writer = csv.writer(f)  # this is the writer object
            writer.writerow(column_name)
            writer.writerow(row)  # this is the data
            # writer.close()


with open('./hfq_after17.csv', mode="r") as csv_file:  # "r" represents the read mode
    reader = csv.reader(csv_file)  # this is the reader object

    for item in reader:
        writeOrAppendRow(item)
