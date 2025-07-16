# 1. Folosește o imagine Python minimă
FROM python:3.11-slim

# 2. Setează directorul de lucru în container
WORKDIR /app

# 3. Copiază tot codul sursă în container
COPY . /app

# 4. Instalează pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expune portul pe care rulează Flask
EXPOSE 5000

# 6. Setează variabilele de mediu pentru Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# 7. Pornește aplicația Flask
CMD ["flask", "run"]
