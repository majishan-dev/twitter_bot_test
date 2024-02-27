import tweepy
import os
import pytz
from datetime import datetime
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーとアクセストークンの設定
api_key = os.getenv('API_KEY')
api_key_secret= os.getenv('API_KEY_SECRET')
access_token= os.getenv('ACCESS_TOKEN')
access_token_secret= os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

#現在の日時情報を取得
tz = pytz.timezone('Asia/Tokyo')
now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# 投稿
client.create_tweet(text=now)

