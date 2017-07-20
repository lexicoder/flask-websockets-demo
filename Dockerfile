FROM python:2.7.13
WORKDIR /opt/
COPY app app
RUN pip install -r app/requirements.txt
CMD python app/app.py