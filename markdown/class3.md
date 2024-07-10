### 操作 List 的基本方法

```python
i = [1, 2, 3]
i.append(4)
print(i)  # [1, 2, 3, 4]
```

- 使用 `append` 方法將元素 4 添加到列表 `i` 中。

```python
j = [1, 2, 3, 4, 5]
j.remove(3)
print(j)  # [1, 2, 4, 5]
```

- 使用 `remove` 方法移除列表 `j` 中的元素 3。

```python
o = [9, 1, -4, 3, 7, 11, 3]
print(o.count(3))  # 2
```

- 使用 `count` 方法計算列表 `o` 中元素 3 出現的次數。

```python
for i in range(len(o)):
    if 3 in o:
        o.remove(3)
print(o)  # [9, 1, -4, 7, 11]
```

- 使用 `for` 迴圈和 `remove` 方法移除列表 `o` 中所有的元素 3。

```python
p = [1, 2, 3]
p.pop(0)
print(p)  # [2, 3]
```

- 使用 `pop` 方法刪除列表 `p` 中的第一個元素。

```python
l = [3, 1, 5, 4, 2]
l.sort()
print(l)  # [1, 2, 3, 4, 5]
l.reverse()
print(l)  # [5, 4, 3, 2, 1]
```

- 使用 `sort` 方法對列表 `l` 進行排序，然後使用 `reverse` 方法將列表 `l` 逆序排列。

```python
m = [3, 1, 5, 4, 2]
print(m.index(3))  # 0
```

- 使用 `index` 方法找出列表 `m` 中元素 3 的索引。

### Streamlit 符件

#### 欄位元件

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
with col1:
    st.markdown("這是欄位1")
    st.button("左邊按鈕")
with col2:
    st.markdown("這是欄位2")
    st.button("右邊按鈕")

col3 = st.columns([1, 5, 1])
col3[0].button("按鈕1", key="button1")
col3[1].button("按鈕2", key="button2")
col3[2].button("按鈕3", key="button3")
```

#### 文字輸入元件

```python
st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.markdown(f"你輸入的文字是：{text}")
```

#### Session State

```python
st.title("session_state")
ans = 1
st.markdown(f"##### {ans}")
if st.button("按鈕", key="btn"):
    ans += 1
    st.markdown(f"##### {ans}")
    if "ans" not in st.session_state:
        st.session_state.ans = 1
if st.button("session_state按鈕", key="session_btn"):
    st.session_state.ans += 1
    st.markdown(f"##### {st.session_state.ans}")
```

#### 點餐機

```python
import time

st.title("點餐機")
if "order" not in st.session_state:
    st.session_state.order = []
col1, col2 = st.columns(2)
with col1:
    foodInput = st.text_input("請輸入餐點")
with col2:
    if st.button("加入", key="add"):
        st.session_state.order.append(foodInput)
st.write(f"### 購物籃")
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])
    with col2:
        if st.button("移除", key=i):
            st.session_state.order.pop(i)
            st.rerun()

if st.button("重新整理"):
    st.success("準備重新整理")
    time.sleep(3)
    st.rerun()
```
