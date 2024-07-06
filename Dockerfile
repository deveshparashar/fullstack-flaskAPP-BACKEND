FROM ubuntu:20.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev  

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# COPY ./templates /app/templates/
# COPY ./static /app/static/
COPY ./03-db.py /app
COPY ./books.sqlite /app
COPY ./03-dynamic-remote-sql.py /app
COPY ./Dockerfile   /app
CMD ["python3", "./03-dynamic-remote-sql.py"]

