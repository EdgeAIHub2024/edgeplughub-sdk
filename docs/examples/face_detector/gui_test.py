import sys
import cv2
import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

from edgeplughub_sdk.ui.base_ui import BasePluginUI
from edgeplughub_sdk.utils.image_utils import ImageUtils
from plugin import FaceDetectorPlugin
from edgeplughub_sdk.core.plugin_base import PluginInput, DataType

class FaceDetectorUI(BasePluginUI):
    def __init__(self):
        super().__init__("人脸检测器")
        
        # 创建插件实例
        self.plugin = FaceDetectorPlugin()
        self.plugin.initialize()
        
        # 当前处理的图像
        self.current_image = None
        self.processed_image = None
        
        # 初始化界面
        self.init_ui()
        
    def init_ui(self):
        # 调用父类的init_ui方法
        super().init_ui()
        
        # 添加图像显示区域
        self.image_display = self.add_image_display(min_size=(400, 300))
        
        # 添加结果显示区域
        self.result_display = self.add_result_display()
        
        # 添加按钮
        self.select_button = self.add_button("选择图片", self.select_image, style="primary")
        self.process_button = self.add_button("检测人脸", self.process_image)
        self.process_button.setEnabled(False)
        
        # 显示欢迎信息
        self.show_message("欢迎使用人脸检测插件，请选择一张图片", "info")
        
    def select_image(self):
        """选择图片按钮回调"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择图片", "", "图片文件 (*.jpg *.jpeg *.png *.bmp)"
        )
        
        if file_path:
            try:
                # 读取图像
                self.current_image = cv2.imread(file_path)
                if self.current_image is None:
                    self.show_message("无法读取图像文件", "error")
                    return
                
                # 显示图像
                self.display_image(self.current_image)
                
                # 显示文件信息
                file_name = os.path.basename(file_path)
                img_height, img_width = self.current_image.shape[:2]
                self.result_display.setText(f"已加载: {file_name}\n大小: {img_width}x{img_height}")
                
                # 启用处理按钮
                self.process_button.setEnabled(True)
                
                self.show_message("图片加载成功，点击'检测人脸'开始处理", "info")
                
            except Exception as e:
                self.show_message(f"加载图片时出错: {str(e)}", "error")
    
    def process_image(self):
        """处理图片按钮回调"""
        if self.current_image is None:
            self.show_message("请先选择一张图片", "warning")
            return
        
        try:
            # 创建输入数据
            input_data = PluginInput(
                data_type=DataType.IMAGE,
                data=self.current_image,
                metadata={"source": "file"}
            )
            
            # 处理图像
            self.show_message("正在处理...", "info")
            output = self.plugin.process(input_data)
            
            if output.success:
                # 显示处理后的图像
                self.processed_image = output.data["image"]
                self.display_image(self.processed_image)
                
                # 显示检测结果
                face_count = len(output.data["faces"])
                result_text = f"检测到 {face_count} 张人脸\n\n"
                
                for i, face in enumerate(output.data["faces"]):
                    result_text += f"人脸 {i+1}: "
                    result_text += f"位置=({face['x']},{face['y']}), "
                    result_text += f"大小={face['width']}x{face['height']}\n"
                
                self.result_display.setText(result_text)
                
                # 显示成功消息
                self.show_message(f"处理完成，检测到 {face_count} 张人脸", "info")
            else:
                self.show_message(f"处理失败: {output.error_message}", "error")
                
        except Exception as e:
            self.show_message(f"处理图片时出错: {str(e)}", "error")
    
    def display_image(self, image):
        """在界面上显示图像"""
        if image is not None:
            pixmap = ImageUtils.cv2_to_qpixmap(image)
            self.image_display.setPixmap(pixmap.scaled(
                self.image_display.width(), 
                self.image_display.height(),
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            ))

def main():
    app = QApplication(sys.argv)
    window = FaceDetectorUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 