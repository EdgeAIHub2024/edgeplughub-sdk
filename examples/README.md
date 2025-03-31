# 插件示例

本目录包含EdgeAIHub SDK的示例插件，演示如何使用SDK开发插件。

## 目录结构

```
examples/
├── face_detector/    # 人脸检测插件示例
│   ├── plugin.py      # 插件核心实现
│   ├── gui_test.py    # GUI测试界面
│   ├── manifest.json  # 插件清单
│   └── README.md      # 插件说明
└── README.md        # 本文件
```

## 运行示例

每个示例插件都可以独立运行，以下以人脸检测插件为例：

```bash
# 进入示例目录
cd face_detector

# 安装依赖
pip install -r requirements.txt

# 运行示例
python gui_test.py
```

## 示例说明

### 人脸检测插件

简单的人脸检测应用，使用OpenCV的Haar级联分类器检测图像中的人脸并标记位置。

**功能**：
- 加载图像文件
- 检测图像中的人脸
- 在图像上标记人脸位置
- 显示检测到的人脸数量和位置信息

**学习要点**：
- 插件基类的继承与实现
- 输入/输出数据格式处理
- UI界面开发
- 错误处理机制 