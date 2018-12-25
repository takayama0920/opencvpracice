# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
fps = 30

# 録画する動画のフレームサイズ（webカメラと同じにする）
size = (640, 480)

dataDir = "./data"    #画像データを保存するディレクトリ
videoDir = "./video"  #動画データを保存するディレクトリ
VideoDate = datetime.now() #動画の日時　
VideoName = str(VideoDate)+".avi" #動画の名前
VideoPath = os.path.join(videoDir,VideoName) #動画の保存先のパス

# 出力する動画ファイルの設定
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(VideoPath, fourcc, fps, size)

print("StartTime :"+str(VideoDate)) #開始時刻

while(cap.isOpened()):
    # フレームをキャプチャする
    ret,frame = cap.read()
    if ret == True:
        data = datetime.now() #フレーム保存時の日時
        Filename = str(data)+".jpg" #画像の名前
        InputFilePath = os.path.join(dataDir, Filename) #画像の保存先のパス
        cv2.imwrite(InputFilePath,frame) #画像の保存
        print(Filename) #保存ログ

    else:
        break
    # 画面に表示する
    cv2.imshow('frame',frame)
    
    video.write(frame) #動画の保存
            
    # キー入力待機
    if cv2.waitKey(1) & 0xFF == ord('q'): # qが押された場合は終了する
        break

# キャプチャの後始末と，ウィンドウをすべて消す



FinishVideoDate = datetime.now()
print("FinishTime :"+str(FinishVideoDate)) #終了時刻
cap.release()
video.release()
cv2.destroyAllWindows()
