# EdgePlugHub 插件开发SDK

EdgePlugHub SDK提供开发边缘AI插件的标准接口和工具。

![SDK概述](docs/images/sdk_overview.png)

## 安装

```bash
# 从PyPI安装
pip install edgeplughub-sdk

# 从源码安装
git clone https://github.com/EdgeAIHub2024/edgeplughub-sdk.git
cd edgeplughub-sdk
pip install -e .
```

## SDK核心功能

- **插件基类**: 提供标准化的插件接口
- **数据格式**: 统一的输入/输出数据格式
- **UI组件**: 可复用的界面组件
- **工具类**: 图像处理、数据转换等工具函数

## 快速开始

### 创建插件类

```python
from edgeplughub_sdk import PluginBase, PluginInput, PluginOutput, DataType

class MyPlugin(PluginBase):
    def __init__(self):
        super().__init__()
        self.plugin_id = "my_plugin"
        self.name = "我的插件"
        self.version = "1.0.0"
        self.supported_input_types = [DataType.IMAGE]
        self.supported_output_types = [DataType.JSON]
        
    def initialize(self):
        # 加载模型和资源
        return True
        
    def process(self, input_data: PluginInput) -> PluginOutput:
        # 处理输入数据
        image = input_data.data
        # ... 处理逻辑 ...
        return PluginOutput(
            success=True,
            data={"result": "处理结果"}
        )
```

### 创建UI界面

```python
from edgeplughub_sdk import BasePluginUI, ImageUtils

class MyPluginUI(BasePluginUI):
    def __init__(self):
        super().__init__("我的插件")
        self.init_ui()
        
    def init_ui(self):
        # 添加UI组件
        self.image_display = self.add_image_display()
        self.result_display = self.add_result_display()
        self.select_button = self.add_button("选择图片", self.select_image)
        self.process_button = self.add_button("处理", self.process_image)
```

## 示例插件

参考[examples目录](examples/)中的完整示例:
- [人脸检测插件](examples/face_detector/) - 展示基本工作流程

## 插件结构

一个基本的插件包含以下文件:

```
my_plugin/
├── plugin.py        # 插件核心实现
├── gui_test.py      # GUI测试入口
├── manifest.json    # 插件清单
├── requirements.txt # 依赖项
└── README.md        # 说明文档
```

## API文档

详细API文档请参考[API文档](docs/api.md)。 