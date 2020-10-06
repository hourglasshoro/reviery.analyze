FROM python:3.8 as build
ENV PYTHONPATH=/app

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv \
 && pipenv install --system

FROM python:3.8-slim as prod
ENV PYTHONUNBUFFERED=1

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

COPY ./src/analyze ./src/analyze

CMD ["python", "main.py"]