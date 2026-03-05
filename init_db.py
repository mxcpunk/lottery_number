import sqlite3

def init():
    conn = sqlite3.connect('lottery.db')
    cursor = conn.cursor()
    # 根据 mydbmain.py 中的逻辑创建表结构 [cite: 4]
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()
    print("数据库初始化成功")

if __name__ == '__main__':
    init()