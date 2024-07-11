print({})  #  空字典
print({"星期一": "apple"})  # 一個key=1,value=apple的字典
print({"星期一": "apple", "星期二": "banana"})  # 一個key=1,value=apple,一個key=2的字典


# 讀取字典
d = {"書名:蘋果,作者:香蕉"}
# key不可重複，value可以重複
print(d["書名"])  # 蘋果


# 字典走訪
d = {"書名:蘋果,作者:香蕉"}
for key in d:  # 如果直接將字典當作迴圈範圍的，預設只會獲得key
    print(key, d[key])
for key in d.keys():  # 可以使用keys()取得key
    print(key)
# 以上兩種方法都是可以取得key，解果相同
for value in d.values():  # 取得所有的value
    print(value)  # 香蕉，蘋果
for key, value in d.items():  # 取得所有的key,value分別存在兩個變數裡面
    print(f"key={key},value={value}")
for item in d.items():  # 取得所有的key,value，但一起存到一個變數裡面
    print(f"key={item[0]},value={item[1]}")


# 元素新增/修改
d = {"書名:蘋果,作者:香蕉"}
d["書名"] = "蘋果樹"
d["作者"] = "香蕉樹"  # 新增元素，當key不存在時就會新增元素
print(d)


# 檢查字典是否存在key
d = {"書名:蘋果,作者:香蕉"}
# 字典是否存在key
print("書名" in d)  # True
print("書名2" in d)  # False
# 字典是否存在value
print("香蕉" in d.values())  # True
print("蘋果" in d.values())  # True
L = ["書名", "作者"]
print("書名" in L)  # True
print("書名2" in L)  # False


# 刪除元素
d = "書名:蘋果,作者:香蕉"
d.pop("書名")  # 刪除key=書名的元素
print(d)
d.pop("橘子", "找不到")  # 如果刪除元素可能不存在
print(d)
