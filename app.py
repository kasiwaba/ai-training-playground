import logging
import sys
from pathlib import Path


logging.basicConfig(level=logging.INFO, format="%(message)s")

MIN_ARGUMENT_COUNT = 1
DEFAULT_TEMPLATE_NAME = "default"
TEMPLATE_DIRECTORY = Path("templates")


def load_template(template_name: str) -> str:
    """指定されたテンプレート名のファイル内容を読み込む。

    Args:
        template_name: 読み込むテンプレート名。

    Returns:
        テンプレートファイルの内容。

    Raises:
        ValueError: テンプレート名が空文字または空白のみの場合。
        FileNotFoundError: 指定されたテンプレートファイルが存在しない場合。
    """
    if not template_name.strip():
        raise ValueError("テンプレート名を入力してください")

    template_path = TEMPLATE_DIRECTORY / f"{template_name}.txt"
    return template_path.read_text(encoding="utf-8")


def create_greeting(name: str, template_name: str = DEFAULT_TEMPLATE_NAME) -> str:
    """名前とテンプレートからあいさつ文を生成する。

    Args:
        name: あいさつ対象の名前。
        template_name: 使用するテンプレート名。

    Returns:
        生成されたあいさつ文。

    Raises:
        ValueError: 名前が空文字または空白のみの場合。
        FileNotFoundError: 指定されたテンプレートファイルが存在しない場合。
    """
    if not name.strip():
        raise ValueError("名前を入力してください")

    template = load_template(template_name)
    return template.format(name=name)


def main(args: list[str]) -> int:
    """コマンドライン引数を受け取り、あいさつ文を出力する。

    Args:
        args: コマンドライン引数のリスト。

    Returns:
        終了コード。正常終了の場合は0、不正な入力の場合は1。

    Raises:
        なし。
    """
    if len(args) < MIN_ARGUMENT_COUNT:
        logging.error("使い方: python app.py <名前> [テンプレート名]")
        return 1