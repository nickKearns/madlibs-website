from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)

    
