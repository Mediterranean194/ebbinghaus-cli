import argparse

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ebbinghaus", description="This is a cli for ebbinghaus review.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("add", help="add a new flash card.")
    sub.add_parser("review", help="start reviewing the flash cards.")
    sub.add_parser("done", help="have done the review.")
    

    return parser

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    
    return 0

