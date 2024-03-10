FROM python:3-alpine
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apk update \
    && apk add gcc \
    && apk add musl-dev \
    && apk add build-base \
    && apk add bash \
    && apk cache clean  \
    && rm -rf /var/cache/apk/*
RUN pip install --prefer-binary -r requirements.txt --no-cache-dir 
ARG DEFAULT_MODE
ARG DEFAULT_GIT_TOKEN
ARG DEFAULT_TABLE_ID
ARG DEFAULT_SHEET_ID
ARG DEFAULT_GOOGLE_TOKEN
ARG DEFAULT_REPO_LIST=list_repos.txt
ARG DEFAULT_OUT_FILE=output.csv
ENV MODE $DEFAULT_MODE
ENV GIT_TOKEN $DEFAULT_GIT_TOKEN
ENV GOOGLE_TOKEN $DEFAULT_GOOGLE_TOKEN
ENV TABLE_ID $DEFAULT_TABLE_ID
ENV SHEET_ID $DEFAULT_SHEET_ID
ENV REPO_LIST $DEFAULT_REPO_LIST
ENV OUT_FILE $DEFAULT_OUT_FILE
COPY *.py start.sh $GOOGLE_TOKEN $REPO_LIST /app/
RUN chmod +x start.sh
ENTRYPOINT [ "/bin/sh", "/app/start.sh" ]