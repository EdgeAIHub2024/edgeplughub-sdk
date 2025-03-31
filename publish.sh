#!/bin/bash
# 清理旧的构建文件
rm -rf build/ dist/ *.egg-info/

# 构建包
python setup.py sdist bdist_wheel

# 上传到PyPI
# 取消下面注释并运行以发布到PyPI
# twine upload dist/*

echo "构建完成，检查dist目录中的包文件"
echo "要发布到PyPI，请运行: twine upload dist/*" 