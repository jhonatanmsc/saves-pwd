FROM python:3.8

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
#COPY . .

CMD ["uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "8000"]