from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/courses')
def show_all_courses():
    courses = [
        'MISY350',
        'MISY330',
        'MISY160'
    ]
    return render_template('courses.html',courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
