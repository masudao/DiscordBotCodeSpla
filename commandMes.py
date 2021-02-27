import random
import jsonDataKai

#のびたの絵文字の配列
nobita = ['<:0_nobita_cow:813608873473605642>', '<:0_nobita_frog:813265701728550934>'
, '<:0_nobita_mouse:813269966429356052>', '<:0_nobita_monkey:813263919061008425>']

def mes(value):
	if value == '/baka':
		test = 'テストばか'
		return test
	elif value == '/aho':
		test = 'テストあほ'
		return test
	elif value == '/oppai':
		return random.choice(nobita) + '＜' + '<:47_otu:814169679991275562>' + '<:47_pai:814177301771714591>'
	elif value == '/next_gachi':
		return '次のガチマのルールは' + jsonDataKai.ruleDo(20) + '\nステージは'
	elif value == '/next_league':
		return '次のリグマのルールは' + jsonDataKai.ruleDo(21)
		