from fastapi import FastAPI, HTTPException, Query
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api._errors import NoTranscriptFound, VideoUnavailable

app = FastAPI(title="YouTube Transcript API Wrapper")

ytt_api = YouTubeTranscriptApi()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/transcript/{video_id}")
def get_transcript(
    video_id: str,
    lang: str | None = Query(
        None,
        description=(
            "Preferred language code (e.g. 'en'). "
            "If not provided, YouTube defaults are used."
        ),
    ),
    full_text: bool = Query(
        False,
        description=(
            "If true, return a single 'text' field with the full transcript "
            "instead of the detailed list."
        ),
    ),
):
    try:
        if lang:
            fetched = ytt_api.fetch(video_id, languages=[lang])
        else:
            fetched = ytt_api.fetch(video_id)

        transcript = fetched.to_raw_data()

        if full_text:
            # Join all text segments with spaces (or "\n" if you prefer lines)
            joined_text = " ".join(
                segment["text"].strip() for segment in transcript if segment["text"]
            )
            return {
                "video_id": video_id,
                "language": fetched.language_code,
                "text": joined_text,
            }

        # Default detailed format
        return {
            "video_id": video_id,
            "language": fetched.language_code,
            "transcript": transcript,
        }

    except TranscriptsDisabled:
        raise HTTPException(
            status_code=403,
            detail="Transcripts are disabled for this video.",
        )
    except NoTranscriptFound:
        raise HTTPException(
            status_code=404,
            detail="No transcript found for this video.",
        )
    except VideoUnavailable:
        raise HTTPException(
            status_code=404,
            detail="Video is unavailable.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))