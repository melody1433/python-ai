import streamlit as st
import time

st.title("點餐機")
if "order" not in st.session_state:
    st.session_state.order = []  # 新增一個購物車的list
col1, col2 = st.columns(2)  # 2層
with col1:
    foodIput = st.text_input("請輸入餐點")  # 建立一個文字輸入檔
with col2:
    if st.button("加入", key="add"):  # 如果按鈕被按下
        st.session_state.order.append(foodIput)  # 將輸入的餐點加入購物車
st.write(f"### 購物籃")
for i in range(len(st.session_state.order)):  # 用index來取得購物車中的餐點
    col1, col2 = st.columns(2)  # 2層
    with col1:
        st.write(st.session_state.order[i])  # 顯示餐點
    with col2:
        if st.button("移除", key=i):  # 如果按鈕被按下,key是index
            st.session_state.order.pop(i)  # 刪除購物車中的餐點
            # 刪除購物車中的餐點,這時候不能用remove,因為remove是用元素來刪除,因為可能會刪除錯誤的餐點
            st.rerun()  # 重新整理頁面


if st.button("重新整理"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色的消息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理頁面
