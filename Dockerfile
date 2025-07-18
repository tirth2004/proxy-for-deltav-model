FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Copy your service account key into the image
COPY local-bliss-465905-r3-acb77d2aff76.json /app/

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/local-bliss-465905-r3-acb77d2aff76.json"

EXPOSE 8080
CMD ["uvicorn", "proxy:app", "--host", "0.0.0.0", "--port", "8080"]