import subprocess
import os
import shutil


def image_parse_v3():
    try:
        # 复制图像到目标文件夹
        source_image_folder = os.path.join(os.getcwd(), "./Output/resized_image")
        target_image_folder = os.path.join(os.getcwd(), "./image-parse-v3/image_segmentation/human_part_segmentation/input")

        # 如果目标文件夹不存在，则创建它
        if not os.path.exists(target_image_folder):
            os.makedirs(target_image_folder)

        # 遍历源文件夹中的所有文件，直接复制到目标文件夹中
        for filename in os.listdir(source_image_folder):
            source_file_path = os.path.join(source_image_folder, filename)
            target_file_path = os.path.join(target_image_folder, filename)
            shutil.copy(source_file_path, target_file_path)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        scripts_directory = os.path.join(current_directory, "image-parse-v3", "image_segmentation",
                                         "human_part_segmentation")
        os.chdir(scripts_directory)

        subprocess.run(["python", "human_part_segmentation_atr.py"], check=True)
        subprocess.run(["python", "human_part_segmentation_lip.py"], check=True)
        subprocess.run(["python", "palette.py"], check=True)
        subprocess.run(["python", "clean_mask.py"], check=True)

        output_segmentation_result = os.path.join(scripts_directory, "output", "0.png")

        parent_directory = os.path.abspath(os.path.join(os.getcwd(), "..", "..", ".."))
        target_directory = os.path.join(parent_directory, "Output", "image-parse-v3")
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        print("-" * 60)
        print("目标目录路径:", target_directory)
        shutil.copy(output_segmentation_result, target_directory)
    except subprocess.CalledProcessError as e:
        print("命令执行失败:", e)


image_parse_v3()