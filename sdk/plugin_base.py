from abc import ABC, abstractmethod
import json
import os
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum

class DataType(Enum):
    """数据类型枚举"""
    IMAGE = "image"
    TEXT = "text"
    JSON = "json"
    BINARY = "binary"

@dataclass
class PluginInput:
    """插件输入数据格式"""
    data_type: DataType
    data: Any
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class PluginOutput:
    """插件输出数据格式"""
    success: bool
    data: Any
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class PluginBase(ABC):
    """插件基类，所有插件都需要继承此类"""
    
    def __init__(self):
        self.plugin_id = None
        self.name = None
        self.version = None
        self.description = None
        self.category = None
        self.author = None
        self.dependencies = []
        self.supported_input_types = []
        self.supported_output_types = []
        
    @abstractmethod
    def initialize(self):
        """初始化插件，加载必要的资源"""
        pass
    
    @abstractmethod
    def process(self, input_data: PluginInput) -> PluginOutput:
        """处理输入数据
        
        Args:
            input_data: 插件输入数据
            
        Returns:
            插件输出数据
        """
        pass
    
    def validate_input(self, input_data: PluginInput) -> bool:
        """验证输入数据格式
        
        Args:
            input_data: 输入数据
            
        Returns:
            是否有效
        """
        if not isinstance(input_data, PluginInput):
            return False
        if input_data.data_type not in self.supported_input_types:
            return False
        return True
    
    def get_manifest(self):
        """获取插件清单信息"""
        return {
            "id": self.plugin_id,
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "category": self.category,
            "author": self.author,
            "dependencies": self.dependencies,
            "supported_input_types": [t.value for t in self.supported_input_types],
            "supported_output_types": [t.value for t in self.supported_output_types]
        }
    
    def save_manifest(self, plugin_dir):
        """保存插件清单到文件
        
        Args:
            plugin_dir: 插件目录
        """
        manifest_path = os.path.join(plugin_dir, "manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(self.get_manifest(), f, ensure_ascii=False, indent=2)
    
    @classmethod
    def load_manifest(cls, plugin_dir):
        """从文件加载插件清单
        
        Args:
            plugin_dir: 插件目录
            
        Returns:
            插件清单信息
        """
        manifest_path = os.path.join(plugin_dir, "manifest.json")
        if os.path.exists(manifest_path):
            with open(manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None 