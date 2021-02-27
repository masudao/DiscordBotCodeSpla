# webapiからデータを取得する機能
# jsonデータを取得、利用するための読み込み
import requests
import json

url_gachi = 'https://spla2.yuu26.com/gachi/now'
url_league = 'https://spla2.yuu26.com/league/now'
url_nawabari = 'https://spla2.yuu26.com/regular/now'

#ルールの情報
def ruleDo(val):
	if val == 1:
		#ガチマ
		#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
		response = requests.get(url_gachi)
		#response.json()でJSONデータに変換して変数へ保存
		jsonData = response.json()
		
		return jsonData["result"][0]["rule"]
		
	elif val == 2: 
	#リグマ
		#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
		response = requests.get(url_league)
		#response.json()でJSONデータに変換して変数へ保存
		jsonData = response.json()
		
		return jsonData["result"][0]["rule"]
		

#ステージの情報
def stageDo(num):
	if 0 < num < 5:
		#ガチマ
		#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
		response = requests.get(url_gachi)
		#response.json()でJSONデータに変換して変数へ保存
		jsonData = response.json()
	elif 4 < num < 9:
		#リグマ
		#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保
		response = requests.get(url_league)
		#response.json()でJSONデータに変換して変数へ保存
		jsonData = response.json()
	elif 9 < num < 14:
		#ナワバリ
		#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保
		response = requests.get(url_nawabari)
		#response.json()でJSONデータに変換して変数へ保存
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