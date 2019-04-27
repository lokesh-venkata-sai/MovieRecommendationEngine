# our base image
FROM alpine:latest

# Install python and pip
RUN apk add python3
RUN apk add py3-cryptography
RUN apk add curl 
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

EXPOSE 5000

CMD ["python3", "/usr/src/app/main.py"]
