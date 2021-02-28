import discord
import jsonDataKai
from jsonDataKai import StageData
import commandMes
from stage_image import mergeImage

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


# コマンド一覧
command = ['/oppai', '/aho', '/baka', '/next_gachi', '/next_league']

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
	elif message.content.startswith('教えてボット'):
		stage_data = StageData().get_gachi_now()
		embed, image_path = set_embed(stage_data, "ガチマッチ")
		await message.channel.send(embed=embed, file=image_path)
		stage_data = StageData().get_league_now()
		embed, image_path = set_embed(stage_data, "リーグマッチ")
		await message.channel.send(embed=embed, file=image_path)
    	

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

def set_embed(stage_data, mode):
    mergeImage(stage_data.stage1_image, stage_data.stage2_image)
    image_path = discord.File("output.png", filename="output.png")

    embed = discord.Embed(
        title = mode,
        colour = discord.Colour.blue()
    )

    embed.add_field(name=stage_data.rule, value=chr(173), inline=False)
    embed.add_field(name=stage_data.stage1_name, value=chr(173), inline=True)
    embed.add_field(name=stage_data.stage2_name, value=chr(173), inline=True)
    embed.set_image(url="attachment://output.png")

    return embed, image_path

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)	
