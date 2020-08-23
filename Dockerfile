FROM python:3.8-slim-buster

RUN pip install --upgrade 'algoliasearch>=2.0,<3.0'; mkdir -p /app
WORKDIR /app
COPY algolia-update-index.py /app

CMD ["python", "/app/algolia-update-index.py"]
