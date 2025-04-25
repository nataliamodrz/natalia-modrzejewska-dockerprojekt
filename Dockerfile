# 1. Obraz bazowy
FROM python:3.10-slim

# 2. Katalog roboczy
WORKDIR /app

# 3. Skopiuj pliki do kontenera
COPY projekt.py .
COPY requirements.txt .

# 4. Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# 5. Uruchom aplikację
CMD ["python", "projekt.py"]
