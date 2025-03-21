FROM apache/superset:latest
ENV SUPERSET_CONFIG_PATH=/app/superset_home/superset_config.py
COPY requirements.txt /app/docker/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/docker/requirements.txt
COPY ./superset_config.py /app/superset_home/superset_config.py
COPY ./entrypoint.sh /app/superset_home/entrypoint.sh
CMD [ "/app/superset_home/entrypoint.sh" ]