FROM python:3.12.4
WORKDIR /opt/
EXPOSE 8080
COPY app app
RUN pip install -r app/requirements.txt
CMD python app/app.py