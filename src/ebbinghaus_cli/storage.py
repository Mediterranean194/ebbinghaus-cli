import json
from pathlib import Path

DATA_DIR = Path.home() / ".ebbinghaus"
DATA_FILE = DATA_DIR / "cards.json"

def load() -> list[dict]:
    """加载存入json文件中的数据"""
    if not DATA_FILE.exists():
       return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        obj = json.load(f)

    if not isinstance(obj, list):
        raise ValueError("json文件数据异常")
    
    return obj

def save(cards: list[dict]) -> None:
    """保存卡片数据到json文件"""
    
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)

    return None




