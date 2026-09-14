import pandas as pd
df = pd.DataFrame({"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [20, 30, 40]})

print(df)
df = pd.DataFrame(
data={"age": [20, 30, 40], "name": ["张三", "李四", "王五"]}, columns=["name", "age"], index=[101, 102, 103]
)
print(df)
print(df.columns)
print(df.index)
print(df.values)
print(df.head(2))
df.set_index("name", inplace=True)
print(df)
print(df.index)