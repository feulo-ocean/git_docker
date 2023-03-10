FROM debian:11-slim
RUN apt update && apt install -y python3
RUN pip3  install flask
WORKDIR /teste
COPY app.py .
ENTRYPOINT flask run --host=0.0.0.0