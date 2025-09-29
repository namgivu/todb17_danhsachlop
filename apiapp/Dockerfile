FROM python:3.12-alpine

WORKDIR      /app
COPY Pipfile .

RUN python -m pip install --upgrade pip pipenv
RUN python -m pipenv install

COPY app.py                .
COPY data/danhsachlop.json ./data/danhsachlop.json

EXPOSE 5000

CMD PYTHONPATH=`pwd` python -m pipenv run  python app.py
