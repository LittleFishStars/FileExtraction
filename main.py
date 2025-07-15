import os
import pathlib as pl
import shutil
import sys

from alive_progress import alive_bar

if __name__ == '__main__':
    path = pl.Path(input('path>>>') if len(sys.argv) < 2 else sys.argv[1])
    # 检查路径是否存在且为目录
    if not path.exists() or not path.is_dir():
        print("错误：提供的路径无效或不是一个目录。")
        sys.exit(1)
    target_folder = path / "合并"
    try:
        target_folder.mkdir(exist_ok=True)
    except Exception as e:
        print(f"创建目标文件夹时出错: {e}")
        sys.exit(1)

    # 遍历所有子文件夹
    with alive_bar(len(os.listdir(path))) as bar:
        for folder in path.iterdir():
            bar()
            if folder.is_dir() and folder.name != "合并":
                # 遍历子文件夹中的所有文件
                for file in folder.iterdir():
                    if file.is_file():
                        # 构建新的文件名
                        new_file_name = folder.name + file.name
                        new_file_path = target_folder / new_file_name
                        try:
                            # 复制文件
                            shutil.copy(file, new_file_path)
                        except Exception as e:
                            print(f"复制文件 {file} 时出错: {e}")
