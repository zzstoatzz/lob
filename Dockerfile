FROM prefecthq/prefect:3.0.0rc2-python3.12

WORKDIR /app

COPY . .

RUN pip install -U uv
RUN uv venv
RUN uv pip install git+https://github.com/prefecthq/prefect.git@main