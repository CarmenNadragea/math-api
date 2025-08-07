
FROM python:3.11-slim

#Seteaza directorul de lucru in container
WORKDIR /app

#Copiaza tot codul sursa in container
COPY . /app

#Instaleaza pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

#Expune portul pe care ruleaza Flask
EXPOSE 5000

#Seteaza variabilele de mediu pentru Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

#Porneste aplicatia flask
CMD ["flask", "run"]
