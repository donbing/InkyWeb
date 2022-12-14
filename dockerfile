FROM navikey/raspbian-bullseye:latest

RUN apt update && \
    apt install -y \
    --no-install-recommends \
    python3-pip python3-rpi.gpio libatlas-base-dev libopenjp2-7 libtiff5 libxcb1 libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt .
RUN pip3 install --user --prefer-binary --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . .

CMD [ "python3", "server.py" ]