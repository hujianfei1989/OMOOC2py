# -*- coding:utf-8 -*-
from sys import *
from os.path import exists


def main():
	print u"欢迎来到History：1.打印历史记录 2.增加新内容  3.退出"
	choose = raw_input('>> ')
	if choose == '1':
		print_history()
	elif choose == '2':
		write_your_note()
	elif choose == '3':
		exit(0)
	else:
		print u"没懂！"
		mai()


def print_history():

	if exists("daily.txt") :
		print u"此前的记录："
		print 30 * '='
		filename = open("daily.txt",'r')
		for line in filename.readlines():
			print line
		print 30 * '='
		
	else:
		print u"没发现之前的，现在开始写吧！"
		filename = open("daily.txt",'w')
		filename.close()
		write_your_note()

def write_your_note():
	print u"请输入：",
	lines = raw_input(">> ")
	filename = open("daily.txt",'a+')
	filename.write(lines + "\n")
	filename.close()

if __name__ == '__main__':
	main()
	
