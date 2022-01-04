FROM python:3.9

RUN pip install flask

COPY . /
WORKDIR /

EXPOSE 8081

ENTRYPOINT ["python"]

CMD ["web01.py"]