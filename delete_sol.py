import os
import glob

# 遍历spec文件夹下的所有子文件夹
for root, dirs, files in os.walk("spec_folder"):
    for dir_name in dirs:
        # 提取子文件夹名字的第一个单词
        first_word = dir_name.split("_")[0]
        
        # 构建当前子文件夹的路径
        subdir_path = os.path.join(root, dir_name)
        
        # 在子文件夹内找到所有.sol文件
        sol_files = glob.glob(f"{subdir_path}/*.sol")
        
        # 删除不包含第一个单词的.sol文件
        for file_path in sol_files:
            if first_word not in os.path.basename(file_path):
                os.remove(file_path)
                print(f"Deleted {file_path}")

# 注意：在执行删除操作前，请确保备份重要数据，以免意外删除。
