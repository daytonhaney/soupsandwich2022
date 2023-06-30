FROM python:latest
COPY . /intro-probsolving-andalgos-PythonSummer2022
RUN pip install -r /src/requirements.txt 
ADD main.py, list.py
CMD ["python3", "./main.py"]



