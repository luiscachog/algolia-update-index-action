FROM python:3.11.3-slim-bullseye

RUN pip install --upgrade 'algoliasearch>=3.0,<4.0'; mkdir -p /app
WORKDIR /app
COPY algolia-update-index.py /app

CMD ["python", "/app/algolia-update-index.py"]
