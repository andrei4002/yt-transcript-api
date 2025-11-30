# YouTube Transcript API Wrapper

A FastAPI-based REST API wrapper for fetching YouTube video transcripts. This service provides a simple HTTP interface to retrieve transcripts from YouTube videos.

## Features

- 🎥 Fetch YouTube video transcripts via REST API
- 🌍 Support for multiple languages
- 📝 Get transcripts in detailed format or as full text
- 🐳 Docker support with multi-platform builds (AMD64 & ARM64)
- ⚡ Built with FastAPI for high performance
- 🔍 Automatic API documentation
- 🔐 Optional Bearer token authentication

## Authentication

The API supports optional Bearer token authentication. If the `API_TOKEN` environment variable is set, the following endpoints require a valid Bearer token in the `Authorization` header:
- `/` (root endpoint)
- `/transcript/{video_id}`

The `/health` endpoint remains public for monitoring purposes.

**To enable authentication:**
```bash
export API_TOKEN=your-secret-token-here
```

**To use authentication in requests:**
```bash
# Root endpoint
curl -H "Authorization: Bearer your-secret-token-here" \
  "http://localhost:8000/"

# Transcript endpoint
curl -H "Authorization: Bearer your-secret-token-here" \
  "http://localhost:8000/transcript/dQw4w9WgXcQ"
```

If `API_TOKEN` is not set, the API works without authentication (public access).

## Quick Start

### Using Docker

```bash
# Pull the image
docker pull andrei4002/yt-transcript-api:latest

# Run the container
docker run -p 8000:8000 andrei4002/yt-transcript-api:latest
```

The API will be available at `http://localhost:8000`

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

## API Endpoints

### Root

```bash
GET /
```

Returns API information and available endpoints.

**Authentication:** Required if `API_TOKEN` is set

**Example Request (without authentication):**
```bash
curl http://localhost:8000/
```

**Example Request (with authentication):**
```bash
curl -H "Authorization: Bearer your-api-token" http://localhost:8000/
```

**Response:**
```json
{
  "name": "YouTube Transcript API Wrapper",
  "version": "1.0.0",
  "endpoints": {
    "health": "/health",
    "transcript": "/transcript/{video_id}",
    "docs": "/docs",
    "redoc": "/redoc"
  }
}
```

### Health Check

```bash
GET /health
```

Returns the service status. This endpoint is always public (no authentication required).

**Response:**
```json
{
  "status": "ok"
}
```

### Get Transcript

```bash
GET /transcript/{video_id}?lang=en&full_text=false
```

Fetches the transcript for a YouTube video.

**Path Parameters:**
- `video_id` (required): YouTube video ID (e.g., `dQw4w9WgXcQ`)

**Query Parameters:**
- `lang` (optional): Language code (e.g., `en`, `es`, `fr`). If not provided, YouTube defaults are used.
- `full_text` (optional): If `true`, returns a single `text` field with the full transcript. Default: `false`

**Example Request (without authentication):**
```bash
curl "http://localhost:8000/transcript/dQw4w9WgXcQ?lang=en&full_text=false"
```

**Example Request (with authentication):**
```bash
curl -H "Authorization: Bearer your-api-token" \
  "http://localhost:8000/transcript/dQw4w9WgXcQ?lang=en&full_text=false"
```

**Response (detailed format):**
```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "transcript": [
    {
      "text": "Never gonna give you up",
      "start": 0.0,
      "duration": 3.5
    },
    ...
  ]
}
```

**Response (full_text format):**
```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "text": "Never gonna give you up Never gonna let you down..."
}
```

**Error Responses:**
- `401`: Missing authorization token (when API_TOKEN is set)
- `403`: Invalid authorization token (when API_TOKEN is set) or transcripts are disabled for this video
- `404`: No transcript found or video is unavailable
- `500`: Internal server error

## API Documentation

When running locally, interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Docker

### Build

```bash
docker build -t yt-transcript-api .
```

### Run

```bash
# Without authentication
docker run -p 8000:8000 yt-transcript-api

# With authentication
docker run -p 8000:8000 -e API_TOKEN=your-secret-token yt-transcript-api
```

## Requirements

- Python 3.11+
- FastAPI
- uvicorn
- youtube-transcript-api

## License

See [LICENSE](LICENSE) file for details.

