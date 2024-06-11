from prefect import task
from prefect.task_worker import serve

from models import User


@task
def send_welcome_email(user: User):
    print(f"Sending welcome email to {user.email}")


@task
def capture_analytics(user: User):
    print(f"Capturing analytics for {user.email}")


if __name__ == "__main__":
    serve(send_welcome_email, capture_analytics)
