FROM ubuntu:22.04
# # 作業環境の設定
ENV DEBIAN_FRONTEND=noninteractive
USER root
RUN mkdir -p /root/workspace
COPY requirements.txt /root/workspace
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
RUN python -m pip install -r requirements.txt

## ターミナルの表示を変更
RUN curl -o ~/.git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash \
    -o ~/.git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh

RUN echo 'PATH="$HOME/.local/bin:$PATH"' >> $HOME/.bashrc && \
    echo 'alias python="python3.8"' >> ~/.bashrc && \
    . $HOME/.bashrc

RUN echo 'source ~/.git-completion.bash' >> ~/.bashrc
RUN echo 'source ~/.git-prompt.sh\nGIT_PS1_SHOWDIRTYSTATE=true' >> ~/.bashrc
ENV PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(__git_ps1 " (%s)")\$ '
RUN echo "PS1='"${PS1}"'" >> ~/.bashrc
