FROM python:2.7.18
WORKDIR /opt/
EXPOSE 8080
COPY app app
RUN pip install -r app/requirements.txt
CMD python app/app.py