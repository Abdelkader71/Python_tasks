import openpyxl

data = [["prototype" , "ID"]]

def read_file(filepath):
    global data
    counter = 0
    file = open(filepath , "r")
    for line in file:
        data.append([line ,f"IDX0{counter}"])
        counter+=1
    
def write_excelsheet(filepath):
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    global data
    for row in data:
        sheet.append(row)
    workbook.save(filepath)
    workbook.close()

    
read_file("header.h")
write_excelsheet("prototypes.xlsx")
