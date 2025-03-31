from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="edgeplughub-sdk",
    version="0.1.0",
    author="EdgeAIHub Team",
    author_email="edgeaihubteam@gmail.com",
    description="EdgePlugHub插件开发SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EdgeAIHub2024/edgeplughub-sdk",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyQt5>=5.15.0",
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "pillow>=8.0.0",
        "requests>=2.25.0",
    ],
    keywords="edge computing, plugin development, ai, image processing",
) 