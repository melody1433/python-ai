import streamlit as st
import os

folderpath = "markdown"  # 這是相對路徑
files = os.listdir(folderpath)  # 取得資料夾中的所有檔案
files_name = []  # 建立一個空的list準備存需要的檔案
for f in files:
    if f.endswith(".md"):  # 如果檔案名稱結尾是.md
        files_name.append(f)  # 就會加入到files_name中

for f in files_name:  # 逐一讀取files_name中的檔案
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as file:  # 打開檔案
        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 建立一個擴展元件,標題為檔案名稱
        st.markdown(content)  # 把檔案內容顯示在擴展元件中
import streamlit as st
import time
