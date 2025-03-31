from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                           QLabel, QPushButton, QFileDialog, QMessageBox,
                           QStatusBar, QFrame)
from PyQt5.QtGui import QPixmap, QImage, QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class BasePluginUI(QMainWindow):
    """插件UI基类，提供通用的UI组件和样式"""
    
    def __init__(self, plugin_name):
        super().__init__()
        self.plugin_name = plugin_name
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle(self.plugin_name)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # 标题
        title = QLabel(self.plugin_name)
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setStyleSheet("color: #1A73E8;")
        title.setAlignment(Qt.AlignCenter)
        
        # 内容区域
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 10, 0, 0)
        
        # 按钮区域
        self.button_widget = QWidget()
        self.button_layout = QHBoxLayout(self.button_widget)
        self.button_layout.setSpacing(15)
        
        # 添加组件到布局
        layout.addWidget(title)
        layout.addWidget(self.content_widget, 1)
        layout.addWidget(self.button_widget)
        
        # 状态栏
        self.statusBar().showMessage("就绪")
        
    def add_button(self, text, callback, style=None):
        """添加按钮
        
        Args:
            text: 按钮文本
            callback: 点击回调函数
            style: 按钮样式
        """
        button = QPushButton(text)
        button.setFont(QFont("Arial", 14))
        if style:
            button.setStyleSheet(style)
        else:
            button.setStyleSheet("""
                background-color: #4285F4;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            """)
        button.clicked.connect(callback)
        self.button_layout.addWidget(button)
        return button
    
    def add_image_display(self, min_size=(400, 300)):
        """添加图片显示区域
        
        Args:
            min_size: 最小尺寸
            
        Returns:
            图片显示标签
        """
        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setMinimumSize(*min_size)
        image_label.setStyleSheet("""
            border: 2px solid #ddd;
            border-radius: 8px;
            background-color: #f8f8f8;
            padding: 5px;
        """)
        self.content_layout.addWidget(image_label)
        return image_label
    
    def add_result_display(self):
        """添加结果显示区域
        
        Returns:
            结果显示框架
        """
        result_frame = QFrame()
        result_frame.setFrameShape(QFrame.StyledPanel)
        result_frame.setStyleSheet("""
            background-color: #f8f8f8;
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 15px;
        """)
        result_layout = QVBoxLayout(result_frame)
        
        result_title = QLabel("分析结果")
        result_title.setFont(QFont("Arial", 16, QFont.Bold))
        result_title.setAlignment(Qt.AlignCenter)
        result_title.setStyleSheet("color: #1A73E8; margin-bottom: 10px;")
        
        result_label = QLabel("等待分析...")
        result_label.setAlignment(Qt.AlignLeft)
        result_label.setFont(QFont("Arial", 14))
        result_label.setStyleSheet("color: #424242; line-height: 150%;")
        result_label.setWordWrap(True)
        
        result_layout.addWidget(result_title)
        result_layout.addWidget(result_label)
        
        self.content_layout.addWidget(result_frame)
        return result_label
    
    def show_message(self, message, type="info"):
        """显示消息
        
        Args:
            message: 消息内容
            type: 消息类型 (info/warning/error)
        """
        if type == "info":
            self.statusBar().showMessage(message)
        elif type == "warning":
            QMessageBox.warning(self, "警告", message)
            self.statusBar().showMessage(f"警告：{message}")
        elif type == "error":
            QMessageBox.critical(self, "错误", message)
            self.statusBar().showMessage(f"错误：{message}")
    
    def select_file(self, title, file_filter):
        """选择文件
        
        Args:
            title: 对话框标题
            file_filter: 文件过滤器
            
        Returns:
            选中的文件路径
        """
        file_path, _ = QFileDialog.getOpenFileName(self, title, "", file_filter)
        return file_path if file_path else None 