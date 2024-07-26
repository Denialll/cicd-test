FROM python:3

ADD Calculator.py .

CMD [ "python", "./Calculator.py" ]