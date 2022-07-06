## 基础环境
目前 DLC 的 Spark 基础运行环境如下：
```
OS = Debian 11(bullseye)
Python = 3.9.2
```

## 基础镜像
DLC 提供如下 pyspark 镜像的，您可以根据需求选择：
```
spark:3.2.1-python
spark:3.2.1-python-ml
spark:3.2.1-python-ai
```

### spark:3.2.1-python
该版本镜像提供基础运行环境，具体依赖如下：
```
Package            Version
------------------ ---------
certifi            2022.6.15
charset-normalizer 2.1.0
greenlet           1.1.2
idna               3.3
numpy              1.23.0
pandas             1.4.3
pip                22.1.2
psycopg2-binary    2.9.3
pyarrow            8.0.0
PyMySQL            1.0.2
python-dateutil    2.8.2
pytz               2022.1
requests           2.28.1
setuptools         63.1.0
six                1.16.0
SQLAlchemy         1.4.39
urllib3            1.26.9
wheel              0.34.2
```

### spark:3.2.1-python-ml
该版本镜像提供轻量机器学习场景运行环境，具体依赖如下：
```
Package            Version
------------------ ---------
certifi            2022.6.15
charset-normalizer 2.1.0
greenlet           1.1.2
idna               3.3
joblib             1.1.0
networkx           2.8.4
numpy              1.23.0
packaging          21.3
pandas             1.4.3
patsy              0.5.2
pip                22.1.2
psycopg2-binary    2.9.3
pyarrow            8.0.0
PyMySQL            1.0.2
pyparsing          3.0.9
python-dateutil    2.8.2
pytz               2022.1
requests           2.28.1
scikit-learn       1.1.1
scipy              1.8.1
setuptools         63.1.0
six                1.16.0
SQLAlchemy         1.4.39
statsmodels        0.13.2
threadpoolctl      3.1.0
urllib3            1.26.9
wheel              0.34.2

```

### spark:3.2.1-python-ai
该版本镜像提供人工智能场景运行环境，具体依赖如下：
```
Package                      Version
---------------------------- ---------
absl-py                      1.1.0
astunparse                   1.6.3
cachetools                   5.2.0
certifi                      2022.6.15
charset-normalizer           2.0.12
flatbuffers                  1.12
gast                         0.4.0
google-auth                  2.8.0
google-auth-oauthlib         0.4.6
google-pasta                 0.2.0
grpcio                       1.47.0
h5py                         3.7.0
idna                         3.3
importlib-metadata           4.11.4
joblib                       1.1.0
keras                        2.9.0
Keras-Preprocessing          1.1.2
libclang                     14.0.1
Markdown                     3.3.7
networkx                     2.8.4
numpy                        1.23.0
oauthlib                     3.2.0
opencv-python                4.6.0.66
opt-einsum                   3.3.0
packaging                    21.3
pandas                       1.4.3
Pillow                       9.1.1
pip                          22.1.2
protobuf                     3.19.4
pyarrow                      8.0.0
pyasn1                       0.4.8
pyasn1-modules               0.2.8
pyparsing                    3.0.9
python-dateutil              2.8.2
pytz                         2022.1
requests                     2.28.0
requests-oauthlib            1.3.1
rsa                          4.8
scikit-learn                 1.1.1
scipy                        1.8.1
setuptools                   62.6.0
six                          1.16.0
tensorboard                  2.9.1
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.9.1
tensorflow-estimator         2.9.0
tensorflow-io-gcs-filesystem 0.26.0
termcolor                    1.1.0
threadpoolctl                3.1.0
torch                        1.11.0
torchvision                  0.12.0
typing_extensions            4.2.0
urllib3                      1.26.9
Werkzeug                     2.1.2
wheel                        0.34.2
wrapt                        1.14.1
zipp                         3.8.0
```

## 虚拟环境
如果默认提供的镜像不满足您的应用需求，您可以通过虚拟环境方式打包依赖，建议您使用 debian 同源操作系统，python = 3.9.X 安装、打包依赖，具体操作如下：
```
#> docker run -it -v {YOUR-WORKING-DIR}:/data --rm python:3.9-slim /bin/bash
root@000000> cd /data
root@000000> python3 -m venv pyspark-venv
root@000000 (pysaprk-venv)> source pyspark-venv/bin/activate
root@000000 (pyspark-venv)> pip3 install -i https://mirrors.tencent.com/pypi/simple/  {YOUR-DEPENDENCIES}
root@000000> deactivate
root@000000> tar czvf pysarpk-venv.tar.gz pyspark-venv # 打包虚拟环境
root@000000> exit # 退出 docker
```

