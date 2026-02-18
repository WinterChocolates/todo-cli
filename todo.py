import argparse
from todo.todo import *

def main():
    parser = argparse.ArgumentParser(description="📌 Todo 命令行工具")
    subparsers = parser.add_subparsers(title="可用指令", dest="command")

    # 添加任务
    add_parser = subparsers.add_parser("add", help="添加任务")
    add_parser.add_argument("task", help="任务内容")
    add_parser.set_defaults(func=add_task)

    # 删除任务
    del_parser = subparsers.add_parser("del", help="删除任务")
    del_parser.add_argument("number", type=int, help="任务编号")
    del_parser.set_defaults(func=del_task)

    # 列出任务
    list_parser = subparsers.add_parser("list", help="列出任务")
    list_parser.set_defaults(func=list_task)

    # 完成任务
    # 批量完成任务
    done_parser = subparsers.add_parser("done", help="完成任务(支持多个)")
    done_parser.add_argument("numbers", type=int, nargs="+", help="任务编号(可多个)")
    done_parser.set_defaults(func=done_task)

    # 清空已完成
    clear_parser = subparsers.add_parser("clear", help="清空已完成任务")
    clear_parser.set_defaults(func=clear_done)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()