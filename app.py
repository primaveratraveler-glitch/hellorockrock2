from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# クイズのデータ
quizzes = [
    {"question": "あなたはどこ生まれですか？", "answer": "冬の星", "correct": "あなたはシャロンです", "incorrect": "あなたはシャロン以外です"},
    {"question": "あなたの髪の色は何色ですか？", "answer": "茶色", "correct": "あなたは多分ベンジーです", "incorrect": "ベンジーじゃないと思います、おそらく。"},
    {"question": "冬の星ってどこだと思いますか？", "answer": "アイスランド", "correct": "あなたはチバユウスケです", "incorrect": "あなたはチバユウスケ以外です"}
]

@app.route('/')
def index():
    return render_template('index.html', quizzes=quizzes)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    quiz_index = data.get('quiz_index')
    user_answer = data.get('answer')
    
    if 0 <= quiz_index < len(quizzes):
        quiz = quizzes[quiz_index]
        if user_answer == quiz['answer']:
            return jsonify({'result': quiz['correct']})
        else:
            return jsonify({'result': quiz['incorrect']})
    
    return jsonify({'result': 'エラーが発生しました'})

if __name__ == '__main__':

    app.run(debug=True, port=5001)
