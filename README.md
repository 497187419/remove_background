# Python 图片背景移除工具

一个简单的 Python 工具，用于快速移除人像图片的背景。本工具使用百度 AI 的人像分割 API 实现背景移除功能。

## 功能特点

- 支持批量处理图片
- 自动保留人像，移除背景
- 支持常见图片格式（PNG、JPG、JPEG）
- 处理后自动保存为 PNG 格式

## 使用方法

### 方法一：直接运行 Python 脚本

1. 确保已安装 Python 3.x 和必要的依赖：
   ```bash
   pip install requests
   ```

2. 将需要处理的图片和 `rm_bg.py` 放在同一目录下
3. 运行脚本：
   ```bash
   python rm_bg.py
   ```

### 方法二：使用编译好的可执行文件

1. 创建一个新文件夹
2. 将需要处理的图片放入该文件夹
3. 将 `rm_bg.py` 编译为可执行文件：
   ```bash
   pip install pyinstaller
   pyinstaller -F rm_bg.py
   ```
4. 运行生成的可执行文件

## 注意事项

- 图片文件名请勿包含特殊字符
- 处理后的图片将保存在原图片所在目录
- 如遇到 API 调用失败，请检查网络连接

## 示例

处理后：
![处理后](images/1.jpt)

## License

MIT License