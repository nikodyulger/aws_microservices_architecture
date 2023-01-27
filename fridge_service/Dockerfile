FROM python:3.9-slim

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./fridge /src/fridge

CMD ["uvicorn", "fridge.main:fridge", "--host", "0.0.0.0", "--port", "80"]