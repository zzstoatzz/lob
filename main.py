from fastapi import FastAPI, Request
from prefect.events import emit_event

from models import User
from tasks import capture_analytics, send_welcome_email

app = FastAPI()


@app.post("/signup")
async def signup(request: Request):
    user = User.model_validate(await request.json())
    send_welcome_email.delay(user)
    capture_analytics.delay(user)
    emit_event(
        event="user.signed-up",
        payload={"user_data": user.model_dump_json()},
        resource={
            "prefect.resource.id": "onboarding-app",
        },
    )

    return {"message": "User signup successful!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
