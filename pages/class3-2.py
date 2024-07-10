import streamlit as st

st.title("欄位元件")
(
    col1,
    col2,
) = st.columns(
    2
)  # 2層
col1.button("按鈕1")  # 在col1中放一個按鈕
col2.button("按鈕2")  # 在col2中放一個按鈕
with col1:  # 在col1中任意增加元件
    st.markdown("這是欄位1")
    st.button("左邊按鈕")
with col2:  # 在col2中任意增加元件
    st.markdown("這是欄位2")
    st.button("右邊按鈕")

col3 = st.columns([1, 5, 1])  # 3攔,list中的數字代表每個欄位的寬度
col3[0].button("按鈕1", key="button1")  # 在col3中的第0個欄位建立一個按鈕
col3[1].button("按鈕2", key="button2")  # 在col3中的第1個欄位建立一個按鈕
col3[2].button("按鈕3", key="button3")  # 在col3中的第2個欄位建立一個按鈕

st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.markdown(f"你輸入的文字是：{text}")


st.title("session_state")
ans = 1
st.markdown(f"##### {ans}")
if st.button("按鈕", key="btn"):  # 如果該按鈕被按下頁面會重新執行
    ans += 1  # ans=ans+1
    st.markdown(f"##### {ans}")  # 這時ans會是2,不會變成3以上,因為會重新定義為1
    if "ans" not in st.session_state:  # 如果session_state中沒有ans這個變數
        st.session_state.ans = 1  # 就會建立一個名為ans的狀態變數,設定為1
if st.button("session_state按鈕", key="session_btn"):  # 如果該按鈕被按下頁面會重新執行
    st.session_state.ans += 1  # session_state中的ans+這時候ans可以持續增加
    st.markdown(f"##### {st.session_state.ans}")
