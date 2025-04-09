FROM python:3.11-slim-bullseye
# FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
# ARG <name>[=<default value>]
# ENV <key>=<value> ...

EXPOSE 8000

COPY requirements.txt /tmp/requirements.txt

# RUN <command>, выполняется в консоли /bin/sh -c или cmd /S /C (shell form)
# RUN [“executable”, “param1”, “param2”] (exec form)

RUN pip install -r /tmp/requirements.txt
# RUN ["pip", "install", "-r", "/tmp/requirements.txt"]

COPY scripts /app

# ADD [--chown=<user>:<group>] [--chmod=<perms>] [--checksum=<checksum>] <src>... <dest>
# ADD [--chown=<user>:<group>] [--chmod=<perms>] ["<src>",... "<dest>"]

# VOLUME ["/data"]

WORKDIR /app

# USER usr

# HEALTHCHECK [OPTIONS] CMD command
# HEALTHCHECK NONE
# HEALTHCHECK --interval=5m --timeout=3s \
# CMD curl -f http://localhost/ || exit 1

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
# CMD ["executable", "param1", "param2"] - exec-форма, она предпочтительна
# CMD ["param1", "param2"] - по умолчанию для ENTRYPOINT
# CMD command param1 param2 - shell-форма

# ENTRYPOINT [“executable”, “param1”, “param2”] - exec-форма предпочитаемая
# ENTRYPOINT command param1 param2 - shell-форма 
