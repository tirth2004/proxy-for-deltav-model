# Vertex AI FastAPI Proxy

This project provides a simple FastAPI-based proxy server that exposes a public HTTP endpoint for interacting with a private Google Vertex AI model. It allows anyone to send text prompts to your deployed Vertex AI model without exposing your Google credentials or requiring users to authenticate with Google.

## Features

- **POST /generate** endpoint: Accepts a JSON payload with a `text` field and returns the model's response.
- Securely calls your Vertex AI model using a service account.
- Designed for easy deployment on Google Cloud Run.

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vertexai-fastapi-proxy.git
cd vertexai-fastapi-proxy
```

### 2. Add Your Service Account Key

- **Do NOT commit this file to version control!**
- Download your Google Cloud service account key (JSON) and place it in the project directory (e.g., `local-bliss-465905-r3-acb77d2aff76.json`).
- Add the key filename to your `.gitignore`:
  ```
  *.json
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variable

```bash
export GOOGLE_APPLICATION_CREDENTIALS="./local-bliss-465905-r3-acb77d2aff76.json"
```

### 5. Run Locally

```bash
uvicorn proxy:app --host 0.0.0.0 --port 8080
```

---

## Usage

Send a POST request to `/generate` with a JSON body:

```bash
curl -X POST http://localhost:8080/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Give me advice for my startup iit.fun"}'
```

Response:

```json
{
  "result": "...model output..."
}
```

---

## Deploying to Google Cloud Run

1. **Build and push the Docker image:**
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/proxy
   ```
2. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy proxy \
     --image gcr.io/YOUR_PROJECT_ID/proxy \
     --platform managed \
     --region YOUR_REGION \
     --allow-unauthenticated \
     --port 8080
   ```
3. **After deployment, Cloud Run will provide a public HTTPS URL for your service.**

---

## Security Best Practices

- **Never commit your service account key to version control.**
- Restrict the service account's permissions to only what is necessary.
- Monitor usage and set up billing alerts in Google Cloud Console.
- Consider adding authentication, rate limiting, or API keys if exposing the endpoint publicly.

---

## License

MIT

---

## Disclaimer

This project is provided as-is. Use at your own risk. You are responsible for securing your Google Cloud resources and managing API usage and billing.
