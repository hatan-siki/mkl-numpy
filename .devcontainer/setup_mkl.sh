#!/bin/bash
# この設定しとかないとmklのインストール時に国選択しないといけなくなる
# (Dockerfileのenvにも指定したけど上手くいかなかったからスクリプト化した)
export DEBIAN_FRONTEND=noninteractive

apt update && apt install -y intel-mkl

cat <<_EOF_ > $HOME/.numpy-site.cfg
[mkl]
library_dirs = /usr/lib/x86_64-linux-gnu
include_dirs = /usr/include/mkl
mkl_libs = mkl_rt
lapack_libs =
_EOF_

# install numpy with mkl
python -m pip install -r requirements.txt
python -m pip uninstall numpy # numpyは一度削除する
python -m pip wheel --no-binary :all: numpy
python -m pip install --force-reinstall numpy*.whl

# scipyはまだエラー解消できていないのでコメント化
# python3 -m pip wheel --no-binary :all: scipy
# python3 -m pip install --force-reinstall scipy*.whl
