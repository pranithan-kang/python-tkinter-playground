FROM python:3.9-slim-buster

RUN apt-get update -y

RUN apt-get install tk -y

CMD [ "/app/tkinter_app.py" ]
ENTRYPOINT [ "python3" ]