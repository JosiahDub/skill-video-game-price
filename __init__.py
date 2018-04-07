from flask import Flask
from flask_assistant import Assistant, tell
# from PriceGuide import PriceGuide
# from config import PORT
#
# price_guide = PriceGuide()
app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('game-price-intent')
def game_price(game, console=None):
    print(game)
    print(console)
    if console is None:
        query = game
    else:
        query = game + " " + console
    result = price_guide.game_info(query)
    try:
        loose_price = loose_to_speech(result['loose-price'])
        print(result)
    except KeyError:
        loose_price = 'No result'
    return tell(loose_price)


def loose_to_speech(loose_price):
    dollars = int(str(loose_price)[:-2])
    if dollars == 0:
        dollars = ''
    elif dollars == 1:
        dollars = "One dollar"
    else:
        dollars = str(dollars) + " dollars"
    cents = int(str(loose_price)[-2:])
    if cents == 0:
        cents = ''
    elif cents == 1:
        cents = ' one cent.'
    else:
        cents = str(cents) + " cents."
    if dollars and cents:
        speech = dollars + " and " + cents
    elif dollars:
        speech = dollars
    else:
        speech = cents
    return speech


if __name__ == '__main__':
    app.run(debug=True, port=PORT, use_reloader=False)
