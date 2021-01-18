import xlsxwriter
workbook = xlsxwriter.Workbook("Name.xlsx")
worksheet = workbook.add_worksheet()
TIME_PERIOD = input()
TWO_WHELEERS = input()

worksheet.write("A1", "TIME_PERIOD")
worksheet.write("B1", "TWO_WHELEERS")


workbook.close()
