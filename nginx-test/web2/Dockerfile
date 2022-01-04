FROM python:3.9

RUN pip install flask

COPY . /
WORKDIR /

EXPOSE 8082

ENTRYPOINT ["python"]

CMD ["web02.py"]