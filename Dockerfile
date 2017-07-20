FROM python:2.7.13
COPY app app
RUN cd app
RUN pip install -r requirements.txt
CMD python app.py