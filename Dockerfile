FROM python:3.12.3

WORKDIR "/questionnaire"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
RUN rm -rf /questionnaire/questionnaire_api/db.sqlite3
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD ["sh", "command.sh"]
