import os
csv_files = list()
name_list = os.listdir("dataset")
for name in name_list:
    csv_files.append(f'dataset/{name}')
import pandas as pd


# 创建一个空的 DataFrame 用于存储合并后的数据
combined_data = pd.DataFrame()

# 遍历每个 CSV 文件并读取数据
for file in csv_files:
    # 读取 CSV 文件
    df = pd.read_csv(file)
    # 将读取的数据添加到 combined_data 中
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# 输出合并后的数据
print(combined_data)

# 可选：将合并后的数据保存到新的 CSV 文件
combined_data.to_csv('data.csv', index=False)
import pandas as pd

# 第一步：读取原始CSV文件
input_file = 'data.csv'
df = pd.read_csv(input_file)

# 第二步：选择需要的三个字段

selected_columns = ['url_absolute', 'page_html', 'page_text']
new_df = df[selected_columns]

# 第三步：将选定的字段保存到新的CSV文件中
output_file = 'new_data.csv'
new_df.to_csv(output_file, index=False)

print("提取完成，新的CSV文件已保存为:", output_file)

# 输入 CSV 文件路径
input_csv_path = 'new_data.csv'

# 读取 CSV 文件
data = pd.read_csv(input_csv_path)

# 删除空值行
cleaned_data = data.dropna()

# 输出 CSV 文件路径
output_csv_path = 'new_data_file.csv'

# 保存到新的 CSV 文件
cleaned_data.to_csv(output_csv_path, index=False)