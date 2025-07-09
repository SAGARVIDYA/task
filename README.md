# Binance Futures Order Bot

A CLI-based Python bot to place Binance USDT-M Futures market and limit orders securely using `python-binance`.

## ✅ Features
- Place **market** and **limit** orders via CLI.
- Uses **`.env`** for safe API key management.
- Logs transactions to `bot.log`.
- Easy to run inside **VS Code** or terminal.

## ✅ Requirements
- Python 3.8+
- Binance Futures account with API key & secret.

## ✅ Installation
```bash
pip install python-binance python-dotenv
```

## ✅ Environment Setup
Create a `.env` file in your project root:
```env
BINANCE_API_KEY=your_actual_api_key_here
BINANCE_SECRET_KEY=your_actual_secret_key_here
```
**⚠️ No quotes, no spaces around `=`**.

## ✅ Usage
Run inside your project folder:

### Market Order:
```bash
python binance_bot.py market BTCUSDT BUY 0.01
```

### Limit Order:
```bash
python binance_bot.py limit BTCUSDT SELL 0.01 65000
```

## ✅ Common Errors & Fixes
- **APIError -2015:** Invalid key, IP, or permissions.
  - Ensure API key and secret are correct.
  - Enable **Futures permission** on your API key.
  - Disable IP restrictions for initial testing.
  - Check you are using **LIVE keys on live** or **Testnet keys on testnet**.

- **API secret required for private endpoints:**
  - Confirm `.env` is correct.
  - Restart your terminal.
  - Print your keys using `print(api_key, api_secret)` to debug.

## ✅ Logging
All orders and errors are logged in `bot.log` for debugging and tracking.

## ✅ Notes
- Always test with **small quantities** or on **Binance Testnet** to avoid unintended losses.
- Keep your `.env` private and **never upload with keys to GitHub**.

## ✅ Author
Your Name Here  
For academic and practical learning on automated Binance Futures trading.

---

If you need **advanced orders (OCO, TWAP, Stop-Limit) for extension**, or a **report template for submission**, let me know!
