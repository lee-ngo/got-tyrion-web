FROM python:2-slim

MAINTAINER John Harris <john@johnharris.io>

COPY . /usr/src/

WORKDIR /usr/src

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]
