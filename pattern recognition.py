#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import re
import urllib

def readCSV(filename):
	csvfile = file(filename, 'rb')
	reader = csv.reader(csvfile)
	count = 0
	answer = 0
	
	for line in reader:
		if count < 6:
			count += 1
			continue
		sentences = line[1].split('\n')
		for sentence in sentences:
			sentence_unicode = sentence.decode('gbk')
			temp_sentence = sentence_unicode.encode('utf-8')
			print sentence_unicode
			#纯数字形式
			start_position = 0
			m = re.search(r"(\d[\d|，]*(\.\d*)?[美]*元)", temp_sentence[start_position:])
			while m != None:
				(start, end) = m.span()
				start_position = end + start_position
				money = m.group(0).replace('，','')
				print unicode(money, 'utf-8')
				m = re.search(r"(\d[\d|，]*(\.\d*)?[美]*元)", temp_sentence[start_position:])
			#纯中文形式
			start_position = 0
			m = re.search(r"(([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖拾十]+[百佰千仟万萬亿]*元)?([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖]+角)?[零一壹二贰两三叁肆四五伍六陆七柒捌八九玖]+分)|(([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖拾]+[十百佰千仟万萬亿]*元)?[零一壹二贰两三叁肆四五伍六陆七柒捌八九玖]+角)|([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖拾十]+[百佰千仟万萬亿]*元)", temp_sentence[start_position:])
			while m != None:
				(start, end) = m.span()
				start_position = end + start_position
				money = m.group(0).replace('，','')
				print unicode(money, 'utf-8')
				m = re.search(r"(([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖拾十]+[百佰千仟万萬亿]*元)?([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖]+角)?[零一壹二贰两三叁肆四五伍六陆七柒捌八九玖]+分)|(([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖拾]+[十百佰千仟万萬亿]*元)?[零一壹二贰两三叁肆四五伍六陆七柒捌八九玖]+角)|([零一壹二贰两三叁肆四五伍六陆七柒捌八九玖拾十]+[百佰千仟万萬亿]*元)", temp_sentence[start_position:])
			#中英结合
			start_position = 0
			m = re.search(r"(\d[\d|，]*(\.\d*)?[百佰千仟万萬亿]+元)", temp_sentence[start_position:])
			while m != None:
				(start, end) = m.span()
				start_position = end + start_position
				money = m.group(0).replace('，','')
				print unicode(money, 'utf-8')
				m = re.search(r"(\d[\d|，]*(\.\d*)?[百佰千仟万萬亿]+元)", temp_sentence[start_position:])
		if count > 16:
			break
		count += 1	
if __name__ == '__main__':
	readCSV("train.csv")