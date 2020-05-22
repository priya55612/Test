FROM pytorch/pytorch:latest

RUN apt-get update && apt-get install -y vim

WORKDIR /code/
COPY . .

RUN /opt/conda/bin/conda install --yes --file requirements.txt


CMD ["python","test_data.py"]
