# webapiからデータを取得する機能
# jsonデータを取得、利用するための読み込み
import requests
import json

url_gachi = 'https://spla2.yuu26.com/gachi/now'
url_league = 'https://spla2.yuu26.com/league/now'
url_nawabari = 'https://spla2.yuu26.com/regular/now'
url_gachi_next = 'https://spla2.yuu26.com/gachi/next'
url_league_next = 'https://spla2.yuu26.com/league/next'

#ルールの情報
def ruleDo(val):
	if val == 1:
		#今のガチマ情報取得
		#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存イカ同様
		response = requests.get(url_gachi)
		#response.json()でJSONデータに変換して変数へ保存イカ同様
		jsonData = response.json()
		
		return jsonData["result"][0]["rule"]
		
	elif val == 2: 
		#今のリグマ情報取得
		response = requests.get(url_league)
		jsonData = response.json()
		
		return jsonData["result"][0]["rule"]
		
	elif val == 20:
		#次のガチマ情報取得
		response = requests.get(url_gachi_next)
		jsonData = response.json()
		
		return jsonData["result"][0]["rule"]

	elif val == 21:
		#次のリグマ情報取得
		response = requests.get(url_league_next)
		jsonData = response.json()
		
		return jsonData["result"][0]["rule"]


#ステージの情報
def stageDo(num):
	if 0 < num < 5:
		#今のガチマのステージ情報取得
		response = requests.get(url_gachi)
		jsonData = response.json()
	elif 4 < num < 9:
		#今のリグマのステージ情報取得
		response = requests.get(url_league)
		jsonData = response.json()
	elif 9 < num < 14:
		#今のナワバリのステージ情報取得
		response = requests.get(url_nawabari)
		jsonData = response.json()
		
	# 1~2はガチマステージ名、3~4はガチマステージ写真、5~6はリグマステージ名、7~8はリグマステージ写真
	if num == 1:
		return jsonData["result"][0]["maps_ex"][0]["name"]
	elif num == 2:
		return jsonData["result"][0]["maps_ex"][1]["name"]
	elif num == 3:
		return jsonData["result"][0]["maps_ex"][0]["image"]
	elif num == 4:		
		return jsonData["result"][0]["maps_ex"][1]["image"]	
	elif num == 5:
		return jsonData["result"][0]["maps_ex"][0]["name"]
	elif num == 6:
		return jsonData["result"][0]["maps_ex"][1]["name"]
	elif num == 7:
		return jsonData["result"][0]["maps_ex"][0]["image"]
	elif num == 8:		
		return jsonData["result"][0]["maps_ex"][1]["image"]	
	elif num == 10:
		return jsonData["result"][0]["maps_ex"][0]["name"]
	elif num == 11:
		return jsonData["result"][0]["maps_ex"][1]["name"]
	elif num == 12:
		return jsonData["result"][0]["maps_ex"][0]["image"]
	elif num == 13:		
		return jsonData["result"][0]["maps_ex"][1]["image"]	