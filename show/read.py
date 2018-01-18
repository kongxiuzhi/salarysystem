from openpyxl import load_workbook
file="/home/king/Downloads/工资查询/管理员账户.xlsx"
wb = load_workbook(file)
ws = wb['Sheet1']

def row_values():
	dataDict = {}
	ctn = 0
	for row in ws.rows:
		dataDict[ctn]=[]
		for cel in row:
			dataDict[ctn].append(cel.value)
		ctn+=1
	return dataDict

datas = row_values()

for i in datas:
	print(tuple(datas[i]))
			




