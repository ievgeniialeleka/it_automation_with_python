FROM python:3.10
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 4000
CMD ["./app.py", "/home/ievgeniial/images/"]
