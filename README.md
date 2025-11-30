# YouTube Transcript API Wrapper

A FastAPI-based REST API wrapper for fetching YouTube video transcripts. This service provides a simple HTTP interface to retrieve transcripts from YouTube videos.

## Features

- 🎥 Fetch YouTube video transcripts via REST API
- 🌍 Support for multiple languages
- 📝 Get transcripts in detailed format or as full text
- 🐳 Docker support with multi-platform builds (AMD64 & ARM64)
- ⚡ Built with FastAPI for high performance
- 🔍 Automatic API documentation

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

### Health Check

```bash
GET /health
```

Returns the service status.

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

**Example Request:**
```bash
curl "http://localhost:8000/transcript/dQw4w9WgXcQ?lang=en&full_text=false"
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
- `403`: Transcripts are disabled for this video
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
docker run -p 8000:8000 yt-transcript-api
```

## Requirements

- Python 3.11+
- FastAPI
- uvicorn
- youtube-transcript-api

## License

See [LICENSE](LICENSE) file for details.

