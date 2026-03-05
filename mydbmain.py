from mydbfunctions import mydb  # 确保这里的模块名与文件名一致

def main():
    # 调用 mydb 函数，获取数据库连接
    db_connection = mydb()
    
    # 你可以在这里执行数据库操作
    print("数据库连接成功！")
    
    # 记得在使用完后关闭连接
    db_connection.close()

if __name__ == "__main__":
    main()
