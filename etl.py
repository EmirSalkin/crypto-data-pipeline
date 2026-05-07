import requests
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

API_KEY = os.getenv("API_KEY")


url = "https://api.freecryptoapi.com/v1/getData"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def save_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    try:
        with conn.cursor() as cur:

            symbols = ["BTC", "ETH", "SOL", "BNB", "XRP", "TRX", "DOGE","ADA"]

            for symbol in symbols:

                params = {"symbol": symbol}

                response = requests.get(
                    url,
                    headers=headers,
                    params=params,
                    timeout=10
                )

                response.raise_for_status()

                data = response.json()

                coin = data["symbols"][0]

                cur.execute("""
                    INSERT INTO crypto_prices(
                        symbol,
                        last_price,
                        last_btc_value,
                        lowest,
                        highest,
                        date_,
                        daily_change_percentage,
                        source_exchange
                    )
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)

                    ON CONFLICT(symbol, date_)
                    DO NOTHING
                """, (
                    coin["symbol"],
                    float(coin["last"]),
                    float(coin["last_btc"]),
                    float(coin["lowest"]),
                    float(coin["highest"]),
                    coin["date"],
                    float(coin["daily_change_percentage"]),
                    coin["source_exchange"]
                ))

        conn.commit()

    finally:
        conn.close()


def run():
    save_data()


if __name__ == "__main__":
    run()