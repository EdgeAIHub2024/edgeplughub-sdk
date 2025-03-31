# SDK 目录结构简化方案

## 当前结构
```
edgeplughub-sdk/
├── edgeplughub_sdk/    # Python包目录
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── plugin_base.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── base_ui.py
│   └── utils/
│       ├── __init__.py
│       └── image_utils.py
├── examples/           # 示例目录
│   └── face_detector/
├── setup.py            # 安装配置
├── MANIFEST.in         # 包含文件配置
└── README.md           # 文档
```

## 简化后的结构

以下是建议的简化结构，减少嵌套层级：

```
edgeplughub-sdk/
├── sdk/               # 核心SDK文件
│   ├── __init__.py    # 导出所有关键类
│   ├── plugin.py      # 插件基础类（原plugin_base.py）
│   ├── ui.py          # UI组件（原base_ui.py）
│   └── utils.py       # 工具函数（原image_utils.py）
├── examples/          # 示例目录保持不变
│   └── face_detector/
├── setup.py           # 安装配置
└── README.md          # 文档精简版
```

## 实施步骤

1. 将核心功能从嵌套的子模块合并到单个文件中
2. 在顶层`__init__.py`中直接导出所有需要的类和函数
3. 更新所有示例代码中的导入语句
4. 更新setup.py中的包配置

## 优势

1. 更直观的导入方式：`from edgeplughub_sdk import PluginBase, BasePluginUI`
2. 减少文件导航层级
3. 维护更加简单
4. 对于简单的SDK，平坦的结构更适合 