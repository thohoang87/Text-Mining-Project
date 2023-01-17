# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

EXPOSE 8501
COPY . .
WORKDIR /Streamlit
ENV PYTHONPATH "${PYTHONPATH}:Application"
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "streamlit", "run", "main_page.py", "--server.port=8501","--server.address=0.0.0.0"]