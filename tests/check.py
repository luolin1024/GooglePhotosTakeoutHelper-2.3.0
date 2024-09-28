import os
import json

def check_json_titles(directory):
    # 遍历指定目录及其子目录
    for root, _, files in os.walk(directory):
        json_files = [file for file in files if file.endswith('.json')]
        other_files = [file for file in files if not file.endswith('.json')]

        for json_file in json_files:
            file_path = os.path.join(root, json_file)
            file_name_without_ext = os.path.splitext(json_file)[0]

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    title = data.get('title', '')

                    # 判断 title 和文件名是否一致
                    if title != file_name_without_ext:
                        match_flag = False
                        title_match_flag = False
                        picture_file_name = ''
                        # 检查同一目录下的非 JSON 文件
                        for other_file in other_files:
                            if title in other_file:
                                title_match_flag = True
                                picture_file_name = other_file
                                break
                            if file_name_without_ext in other_file:
                                match_flag = True
                                picture_file_name = other_file
                                break
                        if title_match_flag:
                            print(f'文件路径: {file_path}，title: {title} 与title匹配成功, 图片名: {picture_file_name}')
                        if match_flag:
                            print(f'文件路径: {file_path}，title: {title} 与文件名匹配成功, 图片名: {picture_file_name}')

            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f'无法处理文件 {file_path}: {e}')

# 调用函数，传入要检查的目录路径
check_json_titles('/Users/luolin/Downloads/Takeout')
