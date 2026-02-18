import os
import json

FILE_NAME = "todo.json"

def ensure_file():
    """确保文件存在"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([], f)

def read_tasks():
    """读取任务列表"""
    ensure_file()
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def write_tasks(tasks):
    """写入任务列表"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(args):
    """添加任务"""
    tasks = read_tasks()
    task_id = len(tasks) + 1

    tasks.append({
        "id": task_id,
        "task": args.task,
        "done": False
    })
    write_tasks(tasks)
    print(f"✅ 已添加任务：{args.task}")

def del_task(args):
    """删除任务"""
    tasks = read_tasks()

    if args.number < 1 or args.number > len(tasks):
        print("❌ 任务编号不存在")
        return

    # 删除任务
    del tasks[args.number - 1]

    # 重新编号
    for i, task in enumerate(tasks, 1):
        task["id"] = i

    write_tasks(tasks)
    print(f"✅ 已删除任务：{args.number}")


def list_task(args):
    """列出任务"""
    tasks = read_tasks()

    if not tasks:
        print("📭 暂无任务")
        return

    print("📋 任务列表：")
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        print(f"{task['id']}. [{status}] {task['task']}")

def done_task(args):
    """完成任务"""
    tasks = read_tasks()
    changed = False
    
    for number in args.numbers:
        if number < 1 or number > len(tasks):
            print(f"❌ 任务 {number} 不存在")
            continue

        # 如果已经完成
        if tasks[number - 1]["done"]:
            print(f"⚠️ 任务 {number} 已完成")
            continue

        tasks[number - 1]["done"] = True
        print(f"✅ 任务 {number} 已完成")
        changed = True
    
    if changed:
        write_tasks(tasks)

def clear_done(args):
    """清除已完成任务"""
    tasks = read_tasks()
    
    new_tasks = [task for task in tasks if not task["done"]]

    if len(new_tasks) == len(tasks):
        print("⚠️ 暂无已完成任务")
        return
    
    # 重新编号
    for i, task in enumerate(new_tasks, 1):
        task["id"] = i

    write_tasks(new_tasks)
    print("🧹 已清空所有已完成任务")