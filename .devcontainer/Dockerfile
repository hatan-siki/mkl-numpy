FROM ubuntu:22.04
# # 作業環境の設定
ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN mkdir -p /root/workspace
WORKDIR /root/workspace

# intel-mkl
RUN apt update && apt install -y \
    wget \
    git \
    curl \
    build-essential \
    gfortran \
    libopenblas-dev
RUN wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" |  tee /etc/apt/sources.list.d/oneAPI.list
RUN apt-get update && apt-get install -y intel-mkl
RUN { \
    echo '[mkl]'; \
    echo 'library_dirs = /usr/lib/x86_64-linux-gnu'; \
    echo 'include_dirs = /usr/include/mkl'; \
    echo 'mkl_libs = mkl_rt';\
    echo 'lapack_libs =';\
    } > $HOME/.numpy-site.cfg

# python
RUN apt update \
    && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install -y \
    python3.8 \
    python3-pip \
    python3.8-distutils \
    python3.8-dev
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 100
RUN update-alternatives --set python /usr/bin/python3.8
RUN python -m pip install --upgrade pip
RUN python -m pip wheel --no-binary :all: numpy
RUN python -m pip install --force-reinstall numpy*.whl
