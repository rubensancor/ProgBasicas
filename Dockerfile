# app/Dockerfile.prod

###########
# BUILDER #
###########

# pull official base image
FROM python:3 as builder

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
# RUN pip install --upgrade pip
# RUN pip install flake8==3.9.1
COPY . .
# RUN flake8 --ignore=E501,F401 .

# install python dependencies TODO: Install poetry
# COPY requirements.txt .
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
RUN pip install -r requirements.txt


#########
#  DEV  #
#########

FROM builder as dev

# install dependencies
# COPY --from=builder /usr/src/app/wheels /wheels
# COPY --from=builder /app/requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install --no-cache /wheels/*
# RUN pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install -r requirements.txt

COPY ./start-dev.sh ./start-dev.sh
RUN chmod +x ./start-dev.sh
CMD ["bash", "./start-dev.sh"]

#########
# PROD  #
#########
FROM builder as prod

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
# COPY --from=builder /usr/src/app/wheels /wheels
# COPY --from=builder /app/requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install --no-cache /wheels/*
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
# USER app

COPY ./start-prod.sh ./start-prod.sh
RUN chmod +x ./start-prod.sh
CMD ["bash", "./start-prod.sh"]