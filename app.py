import datetime

from flask import (Flask, request, render_template,
                   redirect, url_for, flash)


app = Flask(__name__)
app.secret_key = b'simbirsoft73(*&13%*$&^#'

posts = [
    {
        'date': datetime.datetime(2018, 6, 13, 13, 00, 00),
        'author': 'andrey',
        'name': 'Задача организации',
        'content': 'Задача организации, в особенности же новая модель организационной деятельности позволяет выполнять важные задания по разработке модели развития. Равным образом постоянный количественный рост и сфера нашей активности играет важную роль в формировании позиций, занимаемых участниками в отношении поставленных задач. Не следует, однако забывать, что постоянный количественный рост и сфера нашей активности обеспечивает широкому кругу (специалистов) участие в формировании новых предложений. Идейные соображения высшего порядка, а также консультация с широким активом позволяет оценить значение позиций, занимаемых участниками в отношении поставленных задач. Значимость этих проблем настолько очевидна, что сложившаяся структура организации обеспечивает широкому кругу (специалистов) участие в формировании соответствующий условий активизации.'
    },
    {
        'date': datetime.datetime(2018, 6, 13, 19, 45, 43),
        'author': 'alexey',
        'name': 'Модернизация модели развития',
        'content': 'Разнообразный и богатый опыт постоянный количественный рост и сфера нашей активности влечет за собой процесс внедрения и модернизации модели развития. С другой стороны дальнейшее развитие различных форм деятельности способствует подготовки и реализации существенных финансовых и административных условий. С другой стороны реализация намеченных плановых заданий требуют от нас анализа дальнейших направлений развития.'
    },
    {
        'date': datetime.datetime(2018, 6, 14, 1, 48, 00),
        'author': 'andrey',
        'name': 'Дальнейшее развтие',
        'content': 'Равным образом дальнейшее развитие различных форм деятельности обеспечивает широкому кругу (специалистов) участие в формировании систем массового участия. Не следует, однако забывать, что дальнейшее развитие различных форм деятельности требуют от нас анализа существенных финансовых и административных условий.'
    },
]


@app.route('/')
def index():
    return render_template('posts.html', posts=reversed(posts))


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        post = {
            'date': datetime.datetime.now(),
            'author': request.form['author'],
            'name': request.form['name'],
            'content': request.form['content'],
        }
        posts.append(post)

        flash('Новый пост добавлен')

        return redirect(url_for('index'))

    return render_template('add_post.html')


@app.route('/author/<string:author>')
def author(author):
    author_posts = [post for post in posts if post['author'] == author]

    return render_template('author.html',
                           author=author,
                           posts=author_posts)


@app.route("/about")
def about():
    return render_template('about.html')
