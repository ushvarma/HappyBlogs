from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('http://127.0.0.1:5000/')
        else:
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect('http://127.0.0.1:5000/')
            else:
                file.save(file.filename)
                return 'file uploaded successfully'
    return redirect(request.url)
     

if __name__ == '__main__':
    app.run(debug = True)