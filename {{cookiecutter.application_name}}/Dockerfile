FROM python:3.12-slim AS build

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON=3.12 \
    UV_PYTHON_DOWNLOADS=never

# Update the base image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

COPY --from=ghcr.io/astral-sh/uv:0.6 /uv /uvx /usr/local/bin/

ENV UV_PROJECT_ENVIRONMENT=/build/.venv
ENV PATH=/build/.venv/bin:$PATH

# Create user & cache
RUN mkdir /cache && \
    groupadd -g 1337 app && \
    useradd -u 1337 -g 1337 -b /home -c "Application User" -m -s /bin/sh app && \
    chown app:app /cache

# Install dependencies:
RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=cache,sharing=locked,target=/root/.cache \
    uv sync --extra debug --locked --no-default-groups --no-dev

# Install OpenTelemetry DistroS
RUN uv run opentelemetry-bootstrap -a requirements | uv pip install --requirement -

# Create the runtime image
FROM python:3.12-slim AS run

# Install app & uv to launch opentelemetry as entrypoint
ENV PYTHONPATH="/opt/{{cookiecutter.application_name}}:$PYTHONPATH"
ENV PATH=/build/.venv/bin:$PATH

COPY --from=ghcr.io/astral-sh/uv:0.6 /uv /uvx /usr/local/bin/
COPY --chown=app src/{{cookiecutter.application_name}} /app/
COPY --from=build --chown=app /build/.venv /build/.venv

USER 1337

ENTRYPOINT [ "uv" "run" "opentelemetry-instrument", "python3", "-m" , "flask", "--app", "/app/main:app", "run", "--host=0.0.0.0" ]
