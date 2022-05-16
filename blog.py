from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Harsha',
        'title' : 'Post 1',
        'content' : 'Post 1 Content',
        'posted_on' : 'April 20, 2022'
    },
        {
        'author': 'Varma',
        'title' : 'Post 2',
        'content' : 'Post 2 Content',
        'posted_on' : 'May 20, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'Happy Blags - About')

if __name__ == '__main__':
    app.run(debug = True)