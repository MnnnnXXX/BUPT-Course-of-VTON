import subprocess
import os
import shutil

#densepose
def run_densepose():
    try:
        # 切换到 image-densepose 目录
        current_directory = os.path.dirname(os.path.abspath(__file__))
        densepose_directory = os.path.join(current_directory, "image-densepose")
        os.chdir(densepose_directory)
        print("-" * 60)
        print("Running apply_net.py...")
        command = [
            "python", "apply_net.py",
            "show", "configs/densepose_rcnn_R_50_FPN_s1x.yaml",
            "https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl",
            "image_path", "dp_segm", "-v", "--opts", "MODEL.DEVICE", "cpu"
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("命令执行失败:", e)
    finally:
        print("apply_net.py is down.")
        output_image_path = os.path.join(densepose_directory, "image-densepose", "0.jpg")
        parent_directory = os.path.dirname(os.getcwd())
        target_directory = os.path.join(parent_directory, "Output", "image-densepose")
        shutil.copy(output_image_path, target_directory)
        print("Output image copied to:", target_directory)

run_densepose()