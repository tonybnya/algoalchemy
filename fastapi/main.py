"""
Entry point for the FastAPI application.
"""

import uvicorn
from fastapi import FastAPI
from app.routers import register_routers
from app.database import engine
import app.models

# Create tables in the database
app.models.Base.metadata.create_all(bind=engine)

# Create FastAPI application instance
app = FastAPI(
    title="AlgoAlchemy API",
    description="A clever mix of algorithms and the magic (alchemy) of Python & FastAPI.",
    version="0.1.0"
)

# Register all routers
register_routers(app)

if __name__ == "__main__":
    # Run the app with debug mode
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

