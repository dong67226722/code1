import random
import time

while(1):
	player = int(input("你要出什么? (1代表石头, 2代表剪刀, 3代表布.)"))
	computer = random.randint(1, 3)
	if player >= 4:
		print("输入错误，退出游戏！")
		break
	print("玩家%d, 电脑%d"%(player, computer))
	if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
		print("玩家赢了！")
	elif player == computer :
		print("平局！")
	else:
		print("电脑赢了！")
	time.sleep(2)
