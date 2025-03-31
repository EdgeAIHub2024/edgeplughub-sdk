# 人脸检测插件示例

这是一个基于EdgePlugHub SDK开发的人脸检测插件示例，用于演示如何使用SDK创建一个完整的插件。

## 功能介绍

本插件可以：
- 加载图像文件
- 检测图像中的人脸
- 在图像上标记人脸位置
- 显示检测到的人脸数量和位置信息

## 技术实现

- 使用OpenCV的Haar级联分类器进行人脸检测
- 基于EdgePlugHub SDK的插件基类和UI基类
- 使用标准的数据输入输出格式

## 安装与运行

### 依赖安装

```bash
pip install -r requirements.txt
```

### 运行测试界面

```bash
python gui_test.py
```

## 插件结构

```
face_detector/
├── gui_test.py      # GUI测试入口
├── plugin.py        # 插件核心实现
├── manifest.json    # 插件清单
├── requirements.txt # 依赖列表
└── README.md        # 说明文档
```

## 开发说明

本示例演示了EdgePlugHub SDK的主要功能：

1. **插件基类继承**：通过继承`PluginBase`实现插件核心功能
2. **数据格式处理**：使用`PluginInput`和`PluginOutput`处理数据
3. **UI界面创建**：通过继承`BasePluginUI`快速创建用户界面
4. **图像处理**：使用`ImageUtils`处理图像格式转换

## 自定义开发

你可以基于本示例进行修改，创建自己的插件：

1. 修改`plugin.py`中的处理逻辑
2. 更新`manifest.json`中的插件信息
3. 调整`gui_test.py`中的界面设计
4. 根据需要添加新的依赖到`requirements.txt`

## 许可证

MIT 