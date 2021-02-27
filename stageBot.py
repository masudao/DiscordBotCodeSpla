# インストールした discord.py を読み込む
import discord
# jsonData.pyの読み込み
import jsonDataKai
# commandMes.pyの読み込み
import commandMes
#時間関連処理の読み込み
from discord.ext import tasks
import asyncio
from datetime import datetime 

#ランダムを読み込む
import random
import json

# bot確認用チャンネル
CHANNEL_ID = 813987738395213825
# 一般チャンネルナワバリ
CHANNEL_ID_IPPAN = 802197583660449825
# 情報収集チャンネルガチマ
CHANNEL_ID_GACHI = 802228521455321088
# リグマチャンネル
CHANNEL_ID_LEAGUE = 802199203278356512

# 自分のBotのアクセストークン
json_file = open('Resourse/setting.json','r')
json_data = json.load(json_file)
TOKEN = json_data["DiscordToken"]

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動する時間のリスト
triger_time = ['01:00', '03:00', '05:00', '07:00', '09:00', '11:00', '13:00', '15:00', '17:00', '19:00', '21:00', '23:00']
test_triger = ['21:50', '21:55', '21:20', '21:25', '21:30', '11:00', '13:00', '15:00', '17:00', '19:00', '21:00', '23:00']

#のびたの絵文字の配列
nobita = ['<:0_nobita_cow:813608873473605642>', '<:0_nobita_frog:813265701728550934>'
, '<:0_nobita_mouse:813269966429356052>', '<:0_nobita_monkey:813263919061008425>']

# コマンド一覧
command = ['/oppai', '/aho', '/baka']

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# webapiを読み込んでjsonを読み込み、返す処理。関数呼び出しのときに引数指定できたらレギュラーとかガチマとか使い分けができそう
@client.event
async def on_message(message):
	
	# 別ファイルcommandMes.pyのメソッドを呼び出し、コメントを渡して向こうで発言内容を選択し、発言。
	if message.content in command:
		await message.channel.send(commandMes.mes(message.content))
		print('動作確認！')
	
	# 「/nobita」と発言したらナワバリ情報が帰ってくるコマンド処理。コマンド処理は上記の別ファイルのメソッド云々に以降しました。
	#if message.content == '/nobita':
		#await message.channel.send('ナワバリのルールは' + jsonDataKai.ruleDo())
		#await message.channel.send('ナワバリのステージは' + jsonDataKai.stageDo(10) + 'と' + jsonDataKai.stageDo(11) + random.choice(nobita))
		#await message.channel.send(jsonDataKai.stageDo(12))
		#await message.channel.send(jsonDataKai.stageDo(13))
		#print('動作確認！')
	#elif message.content == '/oppai':
		#await message.channel.send(random.choice(nobita) + '＜' + '<:47_otu:814169679991275562>' + '<:47_pai:814177301771714591>')
    	

#トリガータイムのリストをforで順番に見ていき、ifで現在の時間と一致するものがあれば実施
@tasks.loop(seconds=60)
async def loop():
	print('動いたよ')
	now = datetime.now().strftime('%H:%M')
#	for t in triger_time:
	for t in triger_time:
		if t == now:
			await client.wait_until_ready()
			channel_gachi = client.get_channel(CHANNEL_ID_GACHI)
			channel_league = client.get_channel(CHANNEL_ID_LEAGUE)
			#ガチマ処理
			await channel_gachi.send('ガチマのルールは' + jsonDataKai.ruleDo(1))
			await channel_gachi.send('ガチマのステージは' + jsonDataKai.stageDo(1) + 'と' + jsonDataKai.stageDo(2))
			await channel_gachi.send(jsonDataKai.stageDo(3))
			await channel_gachi.send(jsonDataKai.stageDo(4))   
			#リグマ処理
			await channel_league.send('リグマのルールは' + jsonDataKai.ruleDo(2))
			await channel_league.send('リグマのステージは' + jsonDataKai.stageDo(5) + 'と' + jsonDataKai.stageDo(6))
			await channel_league.send(jsonDataKai.stageDo(7))
			await channel_league.send(jsonDataKai.stageDo(8))   
		else:
			print('今の時間は' + now)


#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)	
