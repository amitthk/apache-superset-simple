FROM apache/superset:latest
ENV SUPERSET_CONFIG_PATH=/app/superset_home/superset_config.py \
    HOME_DIR="/app/superset_home" \
    INSTANT_CLIENT_ZIP="instantclient-basic-linux.x64-23.7.0.25.01.zip" \
    INSTANT_CLIENT_DIR="instantclient_23_7"
ENV LD_LIBRARY_PATH="$HOME_DIR/$INSTANT_CLIENT_DIR:$LD_LIBRARY_PATH"
ENV PATH="$HOME_DIR/$INSTANT_CLIENT_DIR:$PATH"
    
USER root
RUN apt-get update && apt-get install -y zip unzip libaio1
COPY install_oracle_client.sh /app/superset_home/install_oracle_client.sh
RUN cd /app/superset_home/ && chmod +x ./install_oracle_client.sh && ./install_oracle_client.sh
RUN chown -R superset:superset /app/superset_home

USER superset

COPY requirements.txt /app/docker/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/docker/requirements.txt
COPY ./superset_config.py /app/superset_home/superset_config.py
COPY ./entrypoint.sh /app/superset_home/entrypoint.sh
CMD [ "/app/superset_home/entrypoint.sh" ]
