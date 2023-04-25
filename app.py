from flask import Flask, render_template, jsonify, request
import pandas as pd
import random
import sqlite3
from hangeul_jamo_splitter import *

def name_split(name):
    res = []
    for syl in list(name):
        res += split_syllable(syl)
    return ''.join(res)

# 가사 추출 함수
def extract_lyrics(song_name, lyrics_df):
    temp_df = lyrics_df[lyrics_df['곡명']==song_name]
    temp_df = temp_df[temp_df['제목점수'] != 1]
    temp_df = temp_df[temp_df['후렴점수'] == 1] # 랩이나 verse

    freq_max = temp_df.max()['최고빈도점수']
    random_lyrics = random.sample(list(temp_df[temp_df['최고빈도점수'] == freq_max]['라인'].values), 1)[0]

    return random_lyrics

app = Flask(__name__)

# df 가져오기
lyrics_df = pd.read_csv('bts_lyrics_data.csv', encoding = 'utf8')
song_ls = list(set(lyrics_df['곡명'].values))

# 첫 화면
@app.route('/')
def index():

    return render_template('index.html')

# 정답 얻기
@app.route('/answer', methods = ['GET'])
def answer():
    answer = random.sample(song_ls, 1)[0]
    hint = extract_lyrics(answer, lyrics_df)
    res = {'answer' : answer, 'hint' : hint}
    return res

# 검색어 추천
@app.route('/search', methods = ['GET'])
def search():

    # 검색창 입력값 받기
    word = request.args.get('keyword')


    if word != '':
        # DB 불러오기
        conn = sqlite3.connect('test_db.sqlite')
        lyrics_df.to_sql('songs', conn, if_exists='replace', index=False)

        # SQL 식 완성하기
        SQL = rf"""
        SELECT 곡명 FROM songs
        WHERE 곡명 LIKE '%{word}%'
        """

        # DB에 SQL 적용하기
        df_temp = pd.read_sql(SQL,conn)
        
        # 검색된 값 리스트로 가져오고 텍스트로 합하기
        temp_ls = list(set(df_temp['곡명'].to_list()))
        
    else:
        temp_ls = ['']
        
    return '\n'.join(temp_ls)


if __name__ == '__main__':
    app.run(debug=True)