import subprocess
import os
import shutil
# openpose
def openpose():
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        openpose_bin_directory = os.path.join(current_directory, "openpose",
                                              "openpose-1.7.0-binaries-win64-gpu-python3.7-flir-3d_recommended",
                                              "openpose")

        # 切换到 openpose/bin 目录
        os.chdir(openpose_bin_directory)

        parent_directory = os.path.abspath(os.path.join(os.getcwd(), "..", "..", ".."))
        target_directory = os.path.join(parent_directory, "Output")
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # 构建输出图片和JSON文件的路径
        image_output_path = os.path.join(target_directory, "openpose_img")
        json_output_path = os.path.join(target_directory, "openpose_json")

        # 打印输出文件夹的位置
        print("-" * 60)
        print("Image Output Directory:", image_output_path)
        print("JSON Output Directory:", json_output_path)

        # 构建命令
        command = [
            "bin\\OpenPoseDemo.exe",
            "--image_dir", "examples\\media",
            "--hand",
            "--write_images", image_output_path,
            "--write_json", json_output_path,
            "--disable_blending",
        ]

        # 运行命令
        subprocess.run(command)

    except FileNotFoundError as file_not_found_error:
        print("Error: FileNotFoundError -", file_not_found_error)
    except Exception as e:
        print("Error:", e)

openpose()