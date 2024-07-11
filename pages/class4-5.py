import streamlit as st
import os

st.title("購物平台")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾下所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input("欄數", min_value=50, max_value=500, step=50, value=100)
for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)

    st.title("新增商品庫存")
