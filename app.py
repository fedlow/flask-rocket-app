from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Эта функция рендер HTML-шаблон из папки templates
    return render_template('index.html')

if __name__ == '__main__':
    # Запуск приложение в режиме отладки
    app.run(debug=True)