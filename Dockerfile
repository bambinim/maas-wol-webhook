FROM python:3

ENV HOST 0.0.0.0
ENV PORT 8080
ENV SSH_KEY_PATH /ssh/id_rsa

COPY ./* /srv

WORKDIR /srv
RUN pip install -r requirements.txt

ENTRYPOINT '/srv/app.py'