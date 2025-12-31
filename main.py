"""
RAG Production App - Main Entry Point
A production-ready RAG Agent built with FastAPI and Inngest.
"""

import logging
import os
from fastapi import FastAPI
import inngest
import inngest.fast_api
from dotenv import load_dotenv
import uuid
import datetime
from inngest.experimental import ai  # type: ignore

# Load environment variables from .env file
load_dotenv()

# Initialize Inngest client for background job processing
inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer()
)

# Initialize FastAPI application
app = FastAPI()  # Setting up the FASTAPI

# Simple health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify the API is running."""
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}