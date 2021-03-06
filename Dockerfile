FROM rasa/rasa-sdk:1.10.0

WORKDIR /app

COPY actions/requirements-actions.txt ./

USER root

RUN pip install -r requirements-actions.txt

COPY ./actions /app/actions

USER 1001
