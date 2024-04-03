FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt  ./
RUN pip install --no-cache-dir -r requirements.txt 


COPY ./src ./src 

CMD ["uvicorn", "src.main:app", "--host","[hostmachine]s","--port","80","--reload"] 