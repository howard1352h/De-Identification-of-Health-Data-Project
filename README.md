# :hospital: De-Identification of Health Data (ai cup 2020)
<br>醫病訊息決策與對話語料分析競賽 - 秋季賽：醫病資料去識別化 [連結](https://aidea-web.tw/topic/d84fabf5-9adf-4e1d-808e-91fbd4e03e6d)<br/>
<br>private 分數應為 **0.6733814391661656**，Private Leaderboard為 **第98名(總共有531組)**<br/>
<br>程式主要是參考 [https://github.com/huoliangyu/zh-NER-TF_Chinese-bi-LSTm-CRF](https://github.com/huoliangyu/zh-NER-TF_Chinese-bi-LSTm-CRF) 進行修改<br/>

# 專案講解
## 使用環境及工具
<br>使用**Ubuntu Server 16.04 LTS server**，顯卡為**Geforce GTX 1080 Ti**</br>
<br>使用python的版本為**3.6.5**</br>
<br>使用PIP安裝project需要的套件，打開terminal移至此project的資料夾並輸入以下命令</br>
```pip install -r requirements.txt```
## 訓練
<br>預設 train_data 為 ~\data_path\train_1_CRF.txt</br>
<br>預設 test_data 為 ~\data_path\test_1_CRF.txt</br>
```python main.py --mode=train```

## 生成預測的醫病資料
<br>會生成副檔名為.tsv的預測資料</br>
```python main.py --mode=demo --demo_model=YOUR_DEMO_MODEL ```



