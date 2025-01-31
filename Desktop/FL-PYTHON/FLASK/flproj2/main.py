from flask import Flask

app=Flask(__name__)


@app.route('/', methods=['GET'])
def home_func():
    return "Hello World, This is my first flask project. This is fun to learn. I am happy that i am learning this"

@app.route('/about', methods=['GET'])
def about_fun():
    return {"message":"This is about the programing framework"}

@app.route('/about', methods=['GET'])
def logout_fun():
    return {"message":"This is about the programing framework"}

if __name__=='__main__':
    app.run(debug=True)
