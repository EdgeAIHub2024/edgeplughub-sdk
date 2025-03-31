from edgeplughub_sdk.core.plugin_base import PluginBase, PluginInput, PluginOutput, DataType
import cv2
import numpy as np

class FaceDetectorPlugin(PluginBase):
    """人脸检测插件示例"""
    
    def __init__(self):
        super().__init__()
        self.plugin_id = "face_detector"
        self.name = "人脸检测器"
        self.version = "1.0.0"
        self.description = "一个简单的人脸检测插件示例"
        self.category = "计算机视觉"
        self.author = "EdgeAIHub团队"
        self.dependencies = ["opencv-python", "numpy"]
        self.supported_input_types = [DataType.IMAGE]
        self.supported_output_types = [DataType.IMAGE, DataType.JSON]
        
        # 模型相关
        self.face_cascade = None
        
    def initialize(self):
        """初始化模型"""
        # 使用OpenCV预训练的人脸检测模型
        try:
            self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            return True
        except Exception as e:
            print(f"初始化失败：{str(e)}")
            return False
    
    def process(self, input_data: PluginInput) -> PluginOutput:
        """处理输入图像，检测人脸"""
        # 验证输入
        if not self.validate_input(input_data):
            return PluginOutput(
                success=False,
                data=None,
                error_message="不支持的输入数据类型，请提供图像数据"
            )
        
        try:
            # 确保模型已初始化
            if self.face_cascade is None:
                if not self.initialize():
                    return PluginOutput(
                        success=False,
                        data=None,
                        error_message="无法初始化人脸检测模型"
                    )
            
            # 处理图像
            image = input_data.image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # 检测人脸
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            # 在图像上标记人脸
            result_image = image.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(result_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # 准备返回数据
            face_data = []
            for (x, y, w, h) in faces:
                face_data.append({
                    "x": int(x),
                    "y": int(y),
                    "width": int(w),
                    "height": int(h)
                })
            
            return PluginOutput(
                success=True,
                data={
                    "image": result_image,
                    "faces": face_data
                },
                metadata={
                    "face_count": len(faces),
                    "processing_time_ms": 0  # 实际应用中可测量处理时间
                }
            )
            
        except Exception as e:
            return PluginOutput(
                success=False,
                data=None,
                error_message=f"处理失败：{str(e)}"
            ) 