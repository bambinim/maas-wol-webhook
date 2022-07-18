FROM python:3.8

ENV HOST 0.0.0.0
ENV PORT 8080
ENV SSH_KEY_PATH ~/.ssh/id_rsa

WORKDIR /srv
COPY ./ ./
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]