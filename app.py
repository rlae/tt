from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

shapes = ['circle', 'square', 'triangle', 'rectangle']
round_num = 1  # 라운드 시작
pattern_length = 3  # 기본 패턴 길이

# 도형 패턴 생성 함수
def generate_pattern():
    return random.choices(shapes, k=pattern_length)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pattern')
def generate_pattern_route():
    pattern = generate_pattern()
    return jsonify(pattern)

@app.route('/check_pattern', methods=['POST'])
def check_pattern():
    data = request.json
    user_pattern = data['userPattern']
    correct_pattern = data['correctPattern']
    is_correct = user_pattern == correct_pattern
    return jsonify({'is_correct': is_correct})

@app.route('/update_difficulty', methods=['POST'])
def update_difficulty():
    global round_num, pattern_length
    round_num += 1
    pattern_length += 1  # 매 라운드마다 패턴 길이 1씩 증가
    return jsonify({'round': round_num, 'pattern_length': pattern_length})

if __name__ == '__main__':
    app.run(debug=True)
