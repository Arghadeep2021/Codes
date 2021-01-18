import xlsxwriter
workbook = xlsxwriter.Workbook("Name.xlsx")
worksheet = workbook.add_worksheet()


worksheet.write("A1", "TIME PERIOD")
worksheet.write("B1", "2 WHELEERS")


workbook.close()
