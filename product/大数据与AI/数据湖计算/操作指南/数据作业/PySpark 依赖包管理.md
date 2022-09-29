Spark 作业使用 PySpark 依赖包有两种方法：
1. 直接打包并使用依赖包。
2. 使用虚拟环境。

目前 DLC 的 PySpark 基础运行环境依赖于 Python3.9.2版本。
```
Python = 3.9.2
```

## 使用依赖包
1. 在本地环境中，使用 pip 指令安装并打包常用依赖，要求依赖包使用纯 Python 实现，不依赖 C 相关库。
```
pip install -i https://mirrors.tencent.com/pypi/simple/ <packages...>  -t dep

cd dep

zip -r ../dep.zip .
```

2. 在 [数据湖 DLC 控制台](https://console.cloud.tencent.com/dlc) 的数据作业模块中新建作业。在`--py-files`参数中引入打包好的 dep.zip 文件，该可以通过上传到 cos 或者本地上传的方式引入。
![](https://qcloudimg.tencent-cloud.cn/raw/30880e73e33a3e189afe479bac6b8431.png)

## 使用虚拟环境  
虚拟环境可解决部分 Python 依赖包对 C 的依赖问题。用户可根据需要，将依赖包编译安装进虚拟环境，然后将整个虚拟环境上传。
因为 C 相关的依赖涉及到编译安装，所以建议使用 x86架构的机器、CentOS(x86)系统、Python = 3.9.2 环境进行打包。

### 步骤一：打包虚拟环境
```
# python3 -m venv --copies pyvenv

# source pyvenv/bin/activate

# (pyvenv)> pip3 install -i [https://mirrors.tencent.com/pypi/simple/](https://mirrors.tencent.com/pypi/simple/) packages

# (pyvenv)> deactivate

# tar czvf pyvenv.tar.gz pyvenv/
```
打包完毕后，将打包好的虚拟环境包`pyvenv.tar.gz` 上传到 cos 中。
>! 请使用 tar 命令打包。

### 步骤二：编辑作业
在 [数据湖 DLC 控制台](https://console.cloud.tencent.com/dlc) 的数据作业模块中新建作业，参考如下截图操作。
- 在 --config 参数里加入如下参数。
```
spark.pyspark.python=venv/pyvenv/bin/python3
```
- 在 --archives  参数填入虚拟环境的完整路径， `#`号后面为解压文件夹名称。

![](https://qcloudimg.tencent-cloud.cn/raw/f1078e28d3c33048ef7f229666a67f99.png)
>! “#”号用于指定解压目录。
