#等差級數 與 等比級數
series_type = input('請輸入級數類別(等差/等比):')

if series_type == '等差':
##從a1開始，公差為d，有n項，累加總和
	sum = 0
	a1 = float(input('請輸入首項: '))
	d = float(input('公差: '))
	n = int(input('總項數: '))
	for x in range (0, n):
		sum = sum + x*d + a1
	print('等差級數和為 ', sum)

elif series_type == '等比':
##從a1開始，公比為r，有n項，累加總和
	sum = 0
	a1 = float(input('請輸入首項:'))
	r = float(input('公比: '))
	n = int(input('總項數: '))
	for x in range (0, n):
		sum = sum + a1*r**x
	print('等比級數和為 ', sum)
	
else:
	print('錯誤級數類別') 

