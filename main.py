from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:aaaaaa@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

    def __init__(self, title,body):
        self.title = title
        self.body = body

@app.route('/blog', methods=['POST','GET'])
def individual_post():

    post_id = request.args.get('post_id')
    indv_post = Post.query.get(id)
    return render_template('blog.html', indv_post=indv_post)



@app.route('/AddPost', methods=['POST','GET'])
def add_post():
    
    error = ""

    
     
    if request.method == 'POST':
        post_title = request.form['title']
        post_body = request.form['body']
        
        if len(post_title) < 1 or len(post_body) < 1:
            error = "feild is empty"
            return render_template('AddPost.html', title="Build-A-Blog", error = error) 

        new_post = Post(post_title,post_body)
        db.session.add(new_post)
        db.session.commit() 


        return redirect('/')

        
    return render_template('AddPost.html', title="Build-A-Blog")


@app.route('/', methods=['POST', 'GET'])
def index():
   
    post = Post.query.all()
    return render_template('BlogPost.html',title="Build-A-Blog", 
        post = post)


if __name__ == '__main__':
    app.run()