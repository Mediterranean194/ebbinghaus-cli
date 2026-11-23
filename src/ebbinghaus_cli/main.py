import argparse

def add_card(args: argparse.Namespace) -> int:
    print("add_card")
    return 0

def review_due(args: argparse.Namespace) -> int:
    print("review_due")
    return 0

def mark_done(args: argparse.Namespace) -> int:
    print("mark_done")
    return 0

COMMANDS = {
    "add": add_card,
    "review": review_due,
    "done": mark_done,
}

def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(prog="ebbinghaus", description="This is a cli for ebbinghaus review.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("add", help="add a new flash card.")
    sub.add_parser("review", help="start reviewing the flash cards.")
    sub.add_parser("done", help="have done the review.")
    
    return parser

def main(argv: list[str] | None = None) -> int:

    args = build_parser().parse_args(argv)
    
    handler = COMMANDS[args.command]  # 查表，拿到函数

    return handler(args)

    


