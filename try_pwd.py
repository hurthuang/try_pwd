password = 'a123456'
try_pwd = 3
while try_pwd > 0:
	pwd = input('請輸入密碼(最多三次)：')
	if pwd == password:
		print('登入成功！')
		break
	else:
		try_pwd = try_pwd - 1
		print('登入失敗！')
		if try_pwd == 0:
			print('帳號被鎖住！')
			break
		else:
			print('還剩', try_pwd, '次')