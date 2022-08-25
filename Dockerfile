FROM python:3.10
ARG PIP_ARGS=
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app
# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./setup/requirements.txt /opt/app
ADD ./src /opt/app/src

RUN pip install -U pip
RUN pip install -r requirements.txt

# Change www-data user to match the host system UID and GID and chown www directory
RUN usermod --non-unique --uid 1000 www-data \
  && groupmod --non-unique --gid 1000 www-data \
  && chown -R www-data:www-data /opt/app

USER www-data

WORKDIR /opt/app/src

EXPOSE 8000