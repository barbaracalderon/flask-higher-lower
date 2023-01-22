import random
from flask import Flask

app = Flask(__name__)


@app.route("/")
def guess_the_number():
    return '''
    <h1>Guess a number between 0 and 9</h1>
    <p><b>HINT</b>: Type your guessing number on this URL, by placing "/your_number"</p>
    <p><img src="https://media0.giphy.com/media/26gs861AqzP6w1DAQ/giphy.gif?cid
    =ecf05e4752c703t528yipme4byawashw95iwlloeb2jis2bd&rid=giphy.gif&ct=g" width="480"></p>
    '''


def get_random_number():
    random_number = random.randint(0, 9)
    return random_number


RANDOM = get_random_number()


@app.route("/<random_number>")
def show_user_result(random_number):
    random_number = int(random_number)
    if random_number < RANDOM:
        return too_low_result()
    elif random_number == RANDOM:
        return correct_result()
    else:
        return too_high_result()


def too_low_result():
    return '''
    <h1 style="color:red">Too low!</h1>
    <p><img src="https://i.giphy.com/media/tjluV258hamaY/giphy.webp"></p>
    '''


def too_high_result():
    return '''
    <h1 style="color:blue">Too high!</h1>
    <p><img src="https://i.giphy.com/media/gnJgBlPgHtcnS/giphy.webp"></p>
    '''


def correct_result():
    return '''
    <h1 style="color:green">You are correct, my friend!</h1>
    <p><img src="https://i.giphy.com/media/RrVzUOXldFe8M/giphy.webp"></p>
    '''


if __name__ == "__main__":
    app.run(debug=True)
