FROM redcanary/invoke-atomicredteam:latest

RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update

RUN bash -c "DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata" && \
    apt-get install -y python3.9 python3.9-distutils python3.9-venv


RUN python3.9 -m ensurepip

RUN python3.9 -m pip install howler-client==1.6.0.dev16137

COPY detection.py /root/detection.py
COPY test.txt /root/test.txt
COPY test.txt /root/test_control.txt

WORKDIR /root