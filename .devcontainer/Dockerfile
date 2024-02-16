FROM ubuntu:20.04
# # 作業環境の設定
ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN mkdir -p /root/workspace
COPY setup_mkl.sh /root/workspace
COPY requirements.txt /root/workspace
WORKDIR /root/workspace

# # 必要なモジュールのインストール
RUN apt update && apt install -y \
    wget git curl build-essential gfortran python-is-python3 python3-pip meson libopenblas-dev
# mklのパッケージを引っ張ってくる
RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" |  tee /etc/apt/sources.list.d/oneAPI.list
# mklのインストール関係
RUN bash setup_mkl.sh

