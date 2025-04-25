FROM python:3.11
COPY requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt
RUN pip install mcpo
COPY . /src
CMD [ "mcpo", "--port", "8080", "--", "python", "mcp_server/app.py" ]
