# ----------- Builder layer -----------

FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --prefix=/install -r /app/requirements.txt

# ----------- Worker layer -----------

FROM python:3.9-slim
WORKDIR /app

RUN apt update \
    && apt install --no-install-recommends -y \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

COPY apps/exporter/exporter.py /app/

ENTRYPOINT [ "python", "-u", "exporter.py" ]