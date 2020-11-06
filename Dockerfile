FROM tensorflow/tensorflow:2.3.1

RUN python -m pip install matplotlib flask

RUN mkdir /app

WORKDIR /app

COPY src ./

RUN export FLASK_APP=index.py

CMD [ "python", "index.py" ]