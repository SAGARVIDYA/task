import os
import sys
import logging
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_SECRET_KEY')
client = Client(api_key, api_secret)

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_symbol(symbol):
    valid_symbols = ['BTCUSDT', 'ETHUSDT']
    return symbol.upper() in valid_symbols

def validate_quantity(quantity):
    try:
        return float(quantity) > 0
    except:
        return False

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        logging.info(f"Market Order Placed: {order}")
        print("Market Order Placed Successfully.")
    except Exception as e:
        logging.error(f"Market Order Failed: {e}")
        print(f"Error: {e}")

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )
        logging.info(f"Limit Order Placed: {order}")
        print("Limit Order Placed Successfully.")
    except Exception as e:
        logging.error(f"Limit Order Failed: {e}")
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 5:
        print("Usage:\npython binance_bot.py market BTCUSDT BUY 0.01\npython binance_bot.py limit BTCUSDT SELL 0.01 65000")
        sys.exit(1)

    order_type = sys.argv[1].lower()
    symbol = sys.argv[2].upper()
    side = sys.argv[3].upper()
    quantity = sys.argv[4]

    if not validate_symbol(symbol):
        print("Invalid symbol.")
        sys.exit(1)
    if not validate_quantity(quantity):
        print("Invalid quantity.")
        sys.exit(1)

    if order_type == 'market':
        place_market_order(symbol, side, quantity)
    elif order_type == 'limit':
        if len(sys.argv) < 6:
            print("Price required for limit order.")
            sys.exit(1)
        price = sys.argv[5]
        place_limit_order(symbol, side, quantity, price)
    else:
        print("Unknown order type. Use 'market' or 'limit'.")

if __name__ == '__main__':
    main()
