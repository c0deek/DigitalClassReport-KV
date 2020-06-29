import openpyxl
import datetime
import json

from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font


def generate_xl(data, teachers):

	# parse data and teachers
	data = json.loads(data)
	teachers = json.loads(teachers)
	
	wb = Workbook()

	sheet = wb.active

	sheet.title = "Custom title"

	fontH = Font(name = 'Montserrat',
				 size = 15,
				 bold = True,
				)
				
	fontT = Font(name = 'Montserrat',
				 size = 10,
				 bold = True,
				)
				
	align = Alignment(horizontal = 'center',
					  vertical = 'center',
					 )
					 
	border = Border(right=Side(border_style='thin',
								  color='121212'),
								  
					bottom=Side(border_style='thin',
								    color='121212'),
					)

	columns = "A B C D E F G H I J K".split(" ")

	sheet.merge_cells('A1:K2')

	sheet['A1'] = "Kendriya Vidyalaya No.2, Armapur, Kanpur\n E-Learning Class Completion Report"
	
	sheet['A3'] = "Date"
	sheet['B3'] = "Name of the Teacher"
	sheet['C3'] = "Class"
	sheet['D3'] = "Subject"
	sheet['E3'] = "Total Students"
	sheet['F3'] = "Present"
	sheet['G3'] = "Absent"
	sheet['H3'] = "Topic"
	sheet['I3'] = "Platform Used"
	sheet['J3'] = "Homework"
	sheet['K3'] = "Remarks"

	i = 3
	for entry in data:
		i += 1
		sheet['A'+str(i)] = entry["fields"]['date'][5:] + "-" + entry["fields"]['date'][:4]
		sheet['B'+str(i)] = teachers[entry["fields"]['teacher']-1]["fields"]["name"]
		sheet['C'+str(i)] = str(entry["fields"]['Class']) + " " + entry["fields"]['section']
		sheet['D'+str(i)] = entry["fields"]['subject']
		sheet['E'+str(i)] = entry["fields"]['total_students']
		sheet['F'+str(i)] = entry["fields"]['present']
		sheet['G'+str(i)] = entry["fields"]['total_students'] - entry["fields"]['present']
		sheet['H'+str(i)] = entry["fields"]['topic']
		sheet['I'+str(i)] = entry["fields"]['platform']
		sheet['J'+str(i)] = entry["fields"]['homework']
		sheet['J'+str(i)] = entry["fields"]['homework']

	for col in range(1, len(columns)+1):
		sheet.column_dimensions[columns[col-1]].width = 11
		sheet.column_dimensions['B'].width = 22
		sheet.column_dimensions['F'].width = 7
		sheet.column_dimensions['C'].width = 6
		sheet.column_dimensions['G'].width = 6
		sheet.column_dimensions['H'].width = 14
		sheet.column_dimensions['I'].width = 16
		sheet.column_dimensions['J'].width = 20
				
		for row in range(1, 4 + len(data)):
			cell = sheet.cell(row = row, column = col)
			if(row == 1):
				cell.font = fontH
				sheet.row_dimensions[row].height = 25
			elif(row == 3):
				cell.font = fontT
				
			cell.alignment = align
			cell.border = border

			
	wb.save(filename = f'./media/report.xlsx')
