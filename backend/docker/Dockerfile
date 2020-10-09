FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY docker/requirements.txt /code/docker/
RUN pip install -r docker/requirements.txt

