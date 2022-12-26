FROM python:3.9

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY apps/analyzer/ /app/
COPY configs/selector.json /app/

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0" ]

