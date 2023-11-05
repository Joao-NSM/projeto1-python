FROM python 

RUN pip install Flask 

WORKDIR /app
COPY . .

EXPOSE 5000

CMD python3 projeto1.py