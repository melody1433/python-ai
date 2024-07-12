Here's the revised and well-structured code with comments for better understanding and maintenance:

```python
import streamlit as st
import time
import os
from openai import OpenAI  # pip install openai
from langchain_openai import ChatOpenAI  # pip install -U langchain-openai
from langchain_core.messages import HumanMessage, AIMessage  # pip install langchain

# Constants
IMAGE_FOLDER = "image"

# Initialize product data
def initialize_products():
    image_files = os.listdir(IMAGE_FOLDER)
    if "product" not in st.session_state:
        st.session_state.product = {}
    for image_file in image_files:
        product_name = image_file[:-4]  # Remove the file extension to get product name
        if product_name not in st.session_state.product:
            st.session_state.product[product_name] = {
                "price": 10,
                "stock": 10,
                "image": f"{IMAGE_FOLDER}/{image_file}",
            }

# Display products for purchase
def display_products():
    st.title("購物平台")
    col_num = st.number_input("欄數", min_value=1, step=1, value=2)
    cols = st.columns(col_num)
    i = 0
    for product_name, details in st.session_state.product.items():
        with cols[i % col_num]:
            st.image(details["image"], use_column_width=True)
            st.markdown(f"{product_name}")
            st.markdown(f"價格：${details['price']}")
            st.markdown(f"庫存：{details['stock']}")
            if st.button(f"購買{product_name}", key=f"{product_name}"):
                if details["stock"] > 0:
                    st.session_state.product[product_name]["stock"] -= 1
                    st.success(f"購買{product_name}成功！")
                    time.sleep(1)
                    st.experimental_rerun()
                else:
                    st.error(f"{product_name}庫存不足！")
        i += 1

# Add stock to products
def add_stock():
    st.title("新增商品庫存")
    product_names = list(st.session_state.product.keys())
    col1, col2 = st.columns(2)
    with col1:
        selected_product = st.selectbox("選擇商品", product_names)
    with col2:
        new_stock = st.number_input("新增庫存數量", min_value=1, step=1)
    if st.button("新增庫存"):
        st.session_state.product[selected_product]["stock"] += new_stock
        st.success(f"{selected_product}的庫存已新增{new_stock}個")
        time.sleep(1)
        st.experimental_rerun()

# Display current stock of products
def display_stock():
    st.markdown("目前商品庫存：")
    for product_name, details in st.session_state.product.items():
        st.markdown(f"{product_name}：{details['stock']}個")

# OpenAI Chat functionality
def openai_chat():
    col1, col2 = st.columns([4, 1])
    with col1:
        openai_key = st.text_input("Password", type="password", key="password")
        if not openai_key:
            st.warning("請輸入OpenAI API Key")
            st.stop()
    if "history" not in st.session_state:
        st.session_state.history = []
    with col2:
        if st.button("🗑️"):
            st.session_state.history = []
            st.experimental_rerun()
    msgs = [HumanMessage("請用繁體中文進行後續對話")]
    for actor, message in st.session_state.history:
        if actor == "user":
            st.chat_message("user", avatar="✨").write(message)
            msgs.append(HumanMessage(message))
        else:
            st.chat_message("assistant", avatar="🎇").write(message)
            msgs.append(AIMessage(message))
    chat = ChatOpenAI(model="gpt-4o", temperature=0.2, api_key=openai_key)
    prompt = st.chat_input("請輸入想要對話的訊息")
    if prompt:
        st.session_state.history.append(["user", prompt])
        msgs.append(HumanMessage(prompt))
        response = chat.invoke(msgs).content
        st.session_state.history.append(["assistant", response])
        st.experimental_rerun()

# OpenAI Image Generation functionality
def openai_image_generation():
    openai_key = st.text_input("Password", type="password", key="password")
    if not openai_key:
        st.warning("請輸入OpenAI API Key")
        st.stop()
    prompt_text = st.text_area("Prompt", "A cute baby sea otter")
    if st.button("開始生成圖片"):
        client = OpenAI(api_key=openai_key)
        generated_image = client.images.generate(
            model="dall-e-3",
            prompt=prompt_text,
            n=1,
            size="1024x1024",
        )
        image_url = generated_image.data[0].url
        st.image(image_url)

# Main function
def main():
    initialize_products()
    display_products()
    add_stock()
    display_stock()
    openai_chat()
    openai_image_generation()

if __name__ == "__main__":
    main()
```

This code is organized into separate functions for different tasks, making it clearer and easier to maintain. Each function has a specific responsibility, and the `main()` function ties them all together. This structure allows for easier debugging and future enhancements.
