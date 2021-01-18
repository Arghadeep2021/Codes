import xlsxwriter
workbook = xlsxwriter.Workbook('Sheets.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
row=0
column=0

worksheet.write(0, 0, "Time Period",bold)
worksheet.write(0, 2, "Two_Wheeler", bold)
worksheet.write(0, 4, "Car/Jeep/Van/3W", bold)
worksheet.write(0, 6, "Lcv", bold)
worksheet.write(0, 8, "Bus", bold)
worksheet.write(0, 10, "Truck",bold)
worksheet.write(0, 12, "Truck_Multiaxle",bold)
worksheet.write(0, 14, "Tractor",bold)
worksheet.write(0, 16, "Non-Motorised vehicles",bold)
worksheet.write(0, 19, "Total hourly Vehicles",bold)
worksheet.write(1,0, "Direction",bold)
worksheet.write(1,2, "UP",bold)
worksheet.write(1,3, "Dn",bold)
worksheet.write(1,4, "UP",bold)
worksheet.write(1,5, "Dn",bold)
worksheet.write(1,6, "UP",bold)
worksheet.write(1,7, "Dn",bold)
worksheet.write(1,8, "UP",bold)
worksheet.write(1,9, "Dn",bold)
worksheet.write(1,10, "UP",bold)
worksheet.write(1,11, "Dn",bold)
worksheet.write(1,12, "UP",bold)
worksheet.write(1,13, "Dn",bold)
worksheet.write(1,14, "UP",bold)
worksheet.write(1,15, "Dn",bold)
worksheet.write(1,16, "UP",bold)
worksheet.write(1,18, "Dn",bold)
worksheet.write(1,19, "UP",bold)
worksheet.write(1,20, "Dn",bold)
worksheet.write(2,0, "From",bold)
worksheet.write(2,1, "To",bold)



workbook.close()



