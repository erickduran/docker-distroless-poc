FROM python:3.7-slim-stretch

WORKDIR /app
COPY . /app

RUN apt-get clean \
	&& apt-get -y update \
	&& apt-get -y install iputils-ping \
	&& pip install --upgrade pip \
	&& pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "app.py"]
