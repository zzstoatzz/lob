from typing import TypeVar

from prefect import flow, task
from pydantic import BaseModel

from models import User

T = TypeVar("T", bound=BaseModel)


class TwitterAccount(BaseModel):
    username: str
    followers: int
    following: int


class LinkedinAccount(BaseModel):
    username: str
    n_connections: int


@task
def get_twitter_account(user: User):
    return TwitterAccount(username="johndoe", followers=100, following=200)


@task
def get_linkedin_account(user: User):
    return LinkedinAccount(username="johndoe", n_connections=300)


@task
def save_socials(*socials: T):
    for social in socials:
        print(f"Saving social: {social.model_dump_json()}")


@flow
def capture_user_socials(user: User):
    twitter_account = get_twitter_account(user)

    linkedin_account = get_linkedin_account(user)

    save_socials(twitter_account, linkedin_account)


if __name__ == "__main__":
    capture_user_socials.serve(name="capture-user-socials")
