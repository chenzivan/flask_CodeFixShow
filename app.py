from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


def process_model(text):
    # 在这里调用你的模型，将文本作为输入，获得模型的输出
    # 这里只是一个示例，你需要替换为你的实际代码
    return "模型输出：" + text


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_model = request.form.get('model')
        input_text = request.form.get('input_text')

        # 在这里调用处理模型的函数
        model_output = process_model(input_text)

        return render_template('index.html', input_text=input_text, model_output=model_output)
    else:
        # 渲染初始页面，显示模型选择表单
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
