from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# 数据库连接函数
def mydb():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mxcitas0919",
            database="loto7_db"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# 第一个部分：显示组合总数和status的组合总数
@app.route('/get_totals', methods=['GET'])
def get_totals():
    db = mydb()
    if db is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = db.cursor()

    # 查询总数
    cursor.execute("SELECT COUNT(*) FROM number7test3")
    total = cursor.fetchone()[0]

    # 查询status=0的组合总数
    cursor.execute("SELECT COUNT(*) FROM number7test3 WHERE status = 0")
    total_0 = cursor.fetchone()[0]

    # 查询status=1的组合总数
    cursor.execute("SELECT COUNT(*) FROM number7test3 WHERE status = 1")
    total_1 = cursor.fetchone()[0]

    db.close()

    # 返回JSON数据
    return jsonify({
        'total': total,
        'total_0': total_0,
        'total_1': total_1
    })

# 第二个部分：通过输入 7 个数字查询对应的 status 值
@app.route('/check_status', methods=['POST'])
def check_status():
    data = request.json
    numbers = data.get('numbers')

    if not numbers or len(numbers) != 7:
        return jsonify({'error': 'Please provide exactly 7 numbers'}), 400

    try:
        # 确保输入的数字是整数并排序
        sorted_numbers = sorted([int(num) for num in numbers])

        db = mydb()
        if db is None:
            return jsonify({'error': 'Database connection failed'}), 500

        cursor = db.cursor()

        # 执行查询，根据输入的 7 个数字查找 status 值
        query = """
        SELECT status FROM number7test3
        WHERE num1 = %s AND num2 = %s AND num3 = %s AND num4 = %s AND num5 = %s AND num6 = %s AND num7 = %s
        """
        cursor.execute(query, sorted_numbers)
        result = cursor.fetchone()

        db.close()

        # 如果找到了对应的组合，返回 status 值
        if result:
            status = result[0]
            return jsonify({'status': status})
        else:
            return jsonify({'status': 'No matching combination found'}), 404

    except ValueError:
        return jsonify({'error': 'Invalid input. All numbers must be integers.'}), 400

# 主页面显示两个部分内容
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
