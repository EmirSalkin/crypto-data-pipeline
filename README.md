# 🚀 Crypto Data Pipeline API

Python, PostgreSQL ve FastAPI kullanarak geliştirdiğim basit bir backend & ETL projesi.

Bu projede:
- Harici bir crypto API’sinden veri çekiliyor
- PostgreSQL veritabanına kaydediliyor
- FastAPI ile API endpointleri üzerinden servis ediliyor

Projeyi geliştirirken öğrenme sürecimde AI/vibe coding desteği kullandım.

---

# ⚙️ Kullanılan Teknolojiler

- Python
- PostgreSQL
- FastAPI
- Requests
- Psycopg2
- Python-dotenv

---

# 🏗️ Proje Yapısı

```text
project/
│
├── etl.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

# ▶️ ETL Çalıştırma
```bash
python etl.py
```
---
# ▶️ API Çalıştırma
```bash
python -m uvicorn main:app --reload --port 8080
```

---

# 🌐 Endpointler

## Tüm Veriler
```http
GET /prices
```

## Tek Coin
```http
GET /prices/BTC
```
---
# 📖 Swagger Docs

FastAPI otomatik olarak API dokümantasyonu oluşturur.
Tarayıcıdan erişim:
```text
http://127.0.0.1:8080/docs
```
---
# ✅ Bu Projede Öğrendiklerim
- API’den veri çekme
- PostgreSQL kullanımı
- ETL mantığı
- FastAPI ile REST API geliştirme
- `.env` kullanımı
---

# 👨‍💻 Geliştirici

Emir Salkin