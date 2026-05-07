from fastapi import FastAPI
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

app = FastAPI()


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.get("/")
def home():
    return {"message": "API çalışıyor"}


# TÜM VERİLER
@app.get("/prices")
def get_prices():

    conn = get_connection()

    try:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT symbol,
                       last_price,
                       date_,
                       daily_change_percentage,
                       lowest,
                       highest
                FROM crypto_prices
                ORDER BY date_ DESC
                LIMIT 50
            """)

            rows = cur.fetchall()

            return [
                {
                    "Symbol": r[0],
                    "Price": float(r[1]),
                    "Date": str(r[2]),
                    "Daily Change Percentage": float(r[3]),
                    "Lowest": float(r[4]),
                    "Highest": float(r[5])
                }
                for r in rows
            ]

    finally:
        conn.close()


# TEK COIN
@app.get("/prices/{symbol}")
def get_price(symbol: str):

    conn = get_connection()

    try:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT symbol,
                       last_price,
                       date_,
                       daily_change_percentage,
                       lowest,
                       highest
                FROM crypto_prices
                WHERE symbol = %s
                ORDER BY date_ DESC
                LIMIT 1
            """, (symbol.upper(),))

            row = cur.fetchone()

            if not row:
                return {"error": "Symbol not found"}

            return {
                "Symbol": row[0],
                "Price": float(row[1]),
                "Date": str(row[2]),
                "Daily Change Percentage": float(row[3]),
                "Lowest": float(row[4]),
                "Highest": float(row[5])
            }

    finally:
        conn.close()