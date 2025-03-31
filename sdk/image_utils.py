import cv2
import numpy as np
from PIL import Image
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class ImageUtils:
    """图像处理工具类"""
    
    @staticmethod
    def cv2_to_qimage(cv_img):
        """将OpenCV图像转换为QImage
        
        Args:
            cv_img: OpenCV图像
            
        Returns:
            QImage对象
        """
        height, width, channel = cv_img.shape
        bytes_per_line = 3 * width
        return QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
    
    @staticmethod
    def cv2_to_qpixmap(cv_img):
        """将OpenCV图像转换为QPixmap
        
        Args:
            cv_img: OpenCV图像
            
        Returns:
            QPixmap对象
        """
        return QPixmap.fromImage(ImageUtils.cv2_to_qimage(cv_img))
    
    @staticmethod
    def pil_to_cv2(pil_img):
        """将PIL图像转换为OpenCV图像
        
        Args:
            pil_img: PIL图像
            
        Returns:
            OpenCV图像
        """
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    @staticmethod
    def cv2_to_pil(cv_img):
        """将OpenCV图像转换为PIL图像
        
        Args:
            cv_img: OpenCV图像
            
        Returns:
            PIL图像
        """
        return Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
    
    @staticmethod
    def resize_image(image, target_size, keep_ratio=True):
        """调整图像大小
        
        Args:
            image: 输入图像（OpenCV格式）
            target_size: 目标尺寸 (width, height)
            keep_ratio: 是否保持宽高比
            
        Returns:
            调整后的图像
        """
        if keep_ratio:
            h, w = image.shape[:2]
            ratio = min(target_size[0]/w, target_size[1]/h)
            new_size = (int(w*ratio), int(h*ratio))
        else:
            new_size = target_size
            
        return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    
    @staticmethod
    def draw_rectangle(image, x, y, w, h, color=(0, 255, 0), thickness=2):
        """在图像上绘制矩形
        
        Args:
            image: 输入图像
            x, y: 左上角坐标
            w, h: 宽度和高度
            color: 颜色
            thickness: 线条粗细
            
        Returns:
            绘制后的图像
        """
        result = image.copy()
        cv2.rectangle(result, (x, y), (x+w, y+h), color, thickness)
        return result
    
    @staticmethod
    def draw_text(image, text, x, y, color=(0, 255, 0), thickness=2, font_scale=0.8):
        """在图像上绘制文本
        
        Args:
            image: 输入图像
            text: 文本内容
            x, y: 文本位置
            color: 颜色
            thickness: 线条粗细
            font_scale: 字体大小
            
        Returns:
            绘制后的图像
        """
        result = image.copy()
        cv2.putText(result, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
        return result 