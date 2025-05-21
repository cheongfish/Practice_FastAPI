FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim
RUN mkdir /venv
WORKDIR /venv
COPY dependencies/ .
CMD ["sleep", "infinity"]
