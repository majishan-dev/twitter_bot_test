import tweepy
import os
from datetime import datetime
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーとアクセストークンの設定
api_key = os.getenv('api_key')
api_key_secret= os.getenv('api_key_secret')
access_token= os.getenv('access_token')
access_token_secret= os.getenv('access_token_secret')

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

#現在の日時情報を取得
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 投稿
client.create_tweet(text=now)

