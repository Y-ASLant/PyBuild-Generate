# PyBuild-Generate 项目记录

## 技术栈
- **UI框架**: Textual (Python TUI框架)
- **语言**: Python
- **项目类型**: 交互式终端应用

## Textual CSS 注意事项

### 数值类型限制
- **padding、margin等属性只接受整数值**，不支持小数
  - ❌ 错误: `padding: 0.5 1;`
  - ✅ 正确: `padding: 0 1;` 或 `padding: 1 2;`
- 支持的格式:
  - 1个值: `padding: 1;` (四周相同)
  - 2个值: `padding: 1 2;` (垂直、水平)
  - 4个值: `padding: 1 2 3 4;` (上、右、下、左)

## 项目结构
```
PyBuild-Generate/
├── src/
│   ├── screens/          # 各个界面屏幕
│   │   ├── mode_selector_screen.py    # 模式选择界面
│   │   ├── compile_config_screen.py   # 编译配置界面
│   │   ├── project_selector_screen.py # 项目选择界面
│   │   └── ...
│   ├── utils/            # 工具类
│   └── app.py            # 主应用
├── main.py               # 启动入口
└── docs/                 # 文档
```

## UI调整经验
- 减少间距: 调整 `margin` 和 `padding` 值为0或更小的整数
- 向上移动内容: 减少容器的上padding值
- 紧凑布局: 设置组件的 `margin-top: 0` 和 `margin-bottom: 0`
