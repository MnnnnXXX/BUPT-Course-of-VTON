import tensorflow as tf

tf.compat.v1.disable_eager_execution()
import numpy as np
from PIL import Image
import cv2


class ImageMatting():
    def __init__(self, file_model, str_device):
        self.file_model = file_model
        self.device = str_device
        with tf.device(self.device):
            self.config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
            self.session = tf.compat.v1.Session(config=self.config)
        with self.session.as_default():
            with tf.compat.v1.gfile.FastGFile(self.file_model, 'rb') as f:
                graph_def = tf.compat.v1.GraphDef()
                graph_def.ParseFromString(f.read())
                tf.import_graph_def(graph_def, name='')
                self.output = self.session.graph.get_tensor_by_name(
                    'output_png:0')
                self.input_name = 'input_image:0'

    def preprocessing(self, file_img):
        img = Image.open(file_img)
        img = img.convert('RGB')
        # 调整图像大小为768x1024
        new_size = (768, 1024)
        img = self.resize_with_padding(img, new_size)
        img = np.array(img)
        img = img.astype(float)
        result = {'img': img}
        return result

    def forward(self, input):
        with self.session.as_default():
            feed_dict = {self.input_name: input['img']}
            output_img = self.session.run(self.output, feed_dict=feed_dict)
            return output_img

    def resize_with_padding(self, img, new_size):
        # 计算调整后的图像和原始图像的大小差距
        width_diff = new_size[0] - img.size[0]
        height_diff = new_size[1] - img.size[1]

        # 计算左右和上下填充的像素数
        left_padding = width_diff // 2
        right_padding = width_diff - left_padding
        top_padding = height_diff // 2
        bottom_padding = height_diff - top_padding

        # 使用白色填充图像边缘
        img_with_padding = Image.new(img.mode, new_size, color='white')
        img_with_padding.paste(img, (left_padding, top_padding))

        return img_with_padding


if __name__ == "__main__":
    file_model = "tf_graph.pb"
    device = '/CPU:0'
    # 实例构建
    m_ImageMatting = ImageMatting(file_model, device)

    # 图像预处理
    img_processed = m_ImageMatting.preprocessing(".\\Output\\resized_cloth\\0.jpg")

    # 图像抠图
    output_img = m_ImageMatting.forward(img_processed)

    # 读取蒙版,保存
    mask = output_img[:, :, -1]
    mask = mask.astype(np.uint8)
    cv2.imwrite(".\\Output\\cloth_mask\\0.jpg", mask)

    # 图像保存 png格式 增加Alpha
    output_img = cv2.cvtColor(output_img, cv2.COLOR_RGBA2BGRA)
    cv2.imwrite(".\\Output\\cloth_mask\\out.jpg", output_img)
