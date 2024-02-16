# mkl-numpy

numpyをintel-mklに紐づけてインストールします.  
これにより行列計算などが非常に高速化します.

ついでにscikit-learn-intelexもインストールします.  
これによりsklearnの機械学習が非常に高速になります.

## 使い方

### プログラム実行時に指定する場合

 `python {実行対象}.py`の間に `-m sklearnex` を追加するだけ

```sh
python -m sklearnex {実行対象}.py
```

### プログラムに直接記述する場合

```py
# 一行目に以下を追加
from sklearnex import patch_sklearn
patch_sklearn()
```
