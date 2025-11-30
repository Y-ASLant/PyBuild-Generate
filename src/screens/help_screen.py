"""
帮助文档屏幕
"""

from pathlib import Path
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Static, Button, Markdown


class HelpScreen(Screen):
    """帮助文档屏幕"""

    CSS_PATH = Path(__file__).parent.parent / "style" / "help_screen.tcss"

    def compose(self) -> ComposeResult:
        """创建帮助文档界面组件"""
        with Container(id="help-container"):
            # 内容容器
            with VerticalScroll(id="help-content"):
                yield Static("加载中...", id="help-loading")

            # 返回按钮
            with Horizontal(id="help-buttons"):
                yield Button("返回", variant="primary", id="back-btn", flat=True)

    def on_mount(self) -> None:
        """挂载后加载文档"""
        self.load_help()

    def load_help(self) -> None:
        """加载 Tutorial.md"""
        project_root = Path(__file__).parent.parent.parent
        try:
            help_path = project_root / "docs" / "Tutorial.md"
            if help_path.exists():
                content = help_path.read_text(encoding="utf-8")
                # 移除加载提示
                loading = self.query_one("#help-loading", Static)
                loading.remove()
                # 添加 Markdown 内容
                scroll = self.query_one("#help-content", VerticalScroll)
                scroll.mount(Markdown(content, id="help-markdown"))
            else:
                self.query_one("#help-loading", Static).update("Tutorial.md 不存在")
        except Exception as e:
            self.query_one("#help-loading", Static).update(f"加载失败: {e}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """处理按钮点击事件"""
        if event.button.id == "back-btn":
            self.app.pop_screen()
