import streamlit as st

number = st.number_input("請輸入數字", step=1)
st.markdown(f"你輸入的數字是{number}")


st.title("練習")

number = st.number_input("請輸入分數", step=1, min_value=0, max_value=100)
st.markdown(f"你輸入的分數是{number}")
if number >= 90:
    st.markdown("你得到了A分")
elif number >= 80:
    st.markdown("你得到了B分")
elif number >= 70:
    st.markdown("你得到了C分")
elif number >= 60:
    st.markdown("你得到了D分")
else:
    st.markdown("你得到了F分")

st.title("按鈕練習")
st.button("點我", key="button")
if st.button("點我", key="button2"):
    st.balloons()
