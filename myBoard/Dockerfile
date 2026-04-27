FROM python:3.11.6
WORKDIR /usr/src/app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /usr/src/app/board_project
RUN chmod +x ../entrypoint.sh
CMD ["../entrypoint.sh"]
EXPOSE 8000
