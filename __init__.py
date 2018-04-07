from flask import Flask
from flask_assistant import Assistant, tell

app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('game-price-intent')
def game_price(game, console=None):
    if console is None:
        speech = "You said " + game
    else:
        speech = "You said " + game + " for the " + console + "."
    return tell(speech)

if __name__ == '__main__':
    app.run(debug=True)
