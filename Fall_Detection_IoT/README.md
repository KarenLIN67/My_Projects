# 跌倒偵測物聯網系統 | Fall Detection IoT System


## 📌 Overview
本專案以 Python 開發，結合影像辨識、語音合成與樹莓派 GPIO 控制，
用於即時偵測老人或使用者跌倒行為，
當發生跌倒事件時可透過蜂鳴器警報及語音提示，未來可進一步推送訊息到 IoT 平台，
有效提升居家安全與照護便利性。


## 🧰 Technologies
- **Python**
- **OpenCV**：影像擷取與處理
- **NumPy**：矩陣與數學運算
- **RPi.GPIO**：樹莓派 GPIO 控制
- **gTTS & pygame**：語音合成與撥放提示音
- **Threading**：多執行緒確保系統穩定


## 🎯 Key Features
- 即時視訊監控與背景差分演算法
- 跌倒姿態判斷與角度閾值設定
- 當偵測到跌倒，自動觸發蜂鳴器、LED
- 自動生成語音提示並播放


## 📂 How to Run
```bash
# 建議先在樹莓派安裝必要套件
pip install opencv-python numpy RPi.GPIO gTTS pygame
```

# 執行程式
python `code/fall_detection.py`


## 📊 Demo
以下為本專案執行過程示範影片：
[👉 點此觀看 Demo 影片](https://drive.google.com/file/d/1lobTv1jgX47lWRnSClhSc8mQvUKVrcAr/view?usp=drive_link)

<img src="images/demo_cover.png" width="300"/>

## 📄 Related Report
[👉 點此下載 PDF 文字說明檔](./report_word.pdf)

[👉 點此下載 PPT 簡報檔](./report_ppt.pdf)
