# ebbinghaus-cli

基于艾宾浩斯遗忘曲线的命令行复习工具。               

## 安装

```bash
pip install -e ".[dev]"                          
```

## 用法

```bash
ebbinghaus add      添加一张新卡片
ebbinghaus review   开始复习到期的卡片
ebbinghaus done     标记本次复习完成
```

## 开发

```bash
pytest
mypy src
```            
