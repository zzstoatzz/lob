FROM prefecthq/prefect:3.0.0rc2-python3.12

WORKDIR /app

COPY . .

RUN pip install uv
RUN uv venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . .venv/bin/activate


RUN uv pip install git+https://github.com/prefecthq/prefect.git@improve-failed-action-logging --force-reinstall