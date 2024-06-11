from fastapi import FastAPI, Request
from prefect.deployments import run_deployment

from models import User
from tasks import capture_analytics, send_welcome_email

app = FastAPI()


@app.post("/signup")
async def signup(request: Request):
    user = User.model_validate(await request.json())
    send_welcome_email.delay(user)
    capture_analytics.delay(user)
    await run_deployment(
        "capture-user-socials/capture-user-socials",
        parameters={"user": user.model_dump()},
        timeout=0,
    )

    return {"message": "User signup successful!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
