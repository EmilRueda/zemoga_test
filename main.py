import uvicorn

from fastapi import FastAPI

from routes.user import router as user_router
from routes.twitter import router as twitter_router

from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Zemoga test",
    description=(
        "This is a Zemoga test of a simple portfolio web app"
        "developtment with Python usign the framework Fast API"
    )
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_router, prefix="")
app.include_router(twitter_router, prefix="/tweets")

if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )