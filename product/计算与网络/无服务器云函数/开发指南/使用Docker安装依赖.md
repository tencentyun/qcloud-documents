## 操作场景
使用 Python，Node.js 等语言开发云函数 SCF 时，由于操作系统版本、系统库版本及语言版本不一致，在本地环境运行良好的程序部署到 SCF 后可能会出现错误。为解决依赖安装问题，本文档介绍使用 Docker 为函数安装依赖。详情请参考以下示例：
- [Node.js 8.9 安装 nodejieba](#node)
- [Python 3.6 安装 pandas](#python)


## 操作步骤

### 安装 Docker
在本地安装 Docker，详情请参见 [Docker](https://docs.docker.com/install/)。

<span id="node"></span>
### Node.js 8.9 安装 nodejieba

本节以下述代码为例：
```js
'use strict';

const jieba = require('nodejieba');

exports.main_handler = async (event, context, callback) => {
    return jieba.cut('你好世界');
};
```
此示例代码可在 Windows 和 macOS 上正确运行，但部署到 SCF 时会出现如下错误代码提示：
```plaintext
{"errorCode":1,"errorMessage":"user code exception caught","stackTrace":"/var/user/node_modules/nodejieba/build/Release/nodejieba.node: invalid ELF header"}
```
为解决此问题，可使用 Docker 来安装依赖。请参考以下命令：
```plaintext
$ docker run -it --network=host -v /path/to/your-project:/tmp/your-project node:8.9 /bin/bash -c 'cd /tmp/your-project && npm install nodejieba --save'
```

其中，`/path/to/your-project`是项目路径，对应于 Docker 容器里的`/tmp/your-project`目录。因此需要在容器里的`/tmp/your-project`目录下安装 nodejieba，即在项目路径下安装 nodejieba。   
依赖安装完成后，将代码重新部署到 SCF 上即可正常运行函数。


<span id="python"></span>
### Python 3.6 安装 pandas
本节以下述代码为例：
```plaintext
import pandas as pd

def main_handler(event, context):
    s = pd.Series([1, 3, 5, 6, 8])
    print(s)
    return len(s)
```

1. 参考以下命令，为 Python 3.6 安装 pandas。
```plaintext
$ docker run -it --network=host -v /path/to/your-project:/tmp/your-project python:3.6.1 /bin/bash -c 'cd /tmp/your-project && pip install pandas -t .'
```
2. 依赖安装完成后，将代码重新部署到 SCF 上并运行。函数可运行，但将产生警告提示“无法加载 lzma 模块，若使用 lzma 压缩则会导致运行时错误”。得到日志信息如下：
```plaintext
/var/user/pandas/compat/__init__.py:84: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)
0    1
1    3
2    5
3    6
4    8
dtype: int64
```
3. 为解决此问题，需要进入容器内部执行以下命令：
```plaintext
$ docker run -it --network=host -v /tmp/foo:/tmp/bar python:3.6.1 /bin/bash
```
4. 执行以下命令，安装 pandas。
```js
$ cd /tmp/bar
$ pip install pandas -t .
echo <<EOF >> index.py
> import pandas as pd
>
> def main_handler(event, context):
>     s = pd.Series([1, 3, 5, 6, 8])
>     print(s)
>     return len(s)
>
> main_handler({}, {})
> EOF
$ python -v index.py > run.log 2>&1
```
5. 执行以下命令，查看日志。示例如下：<span id="step5"></span>
```js
$ grep lzma run.log
# /usr/local/lib/python3.6/__pycache__/lzma.cpython-36.pyc matches /usr/local/lib/python3.6/lzma.py
# code object from '/usr/local/lib/python3.6/__pycache__/lzma.cpython-36.pyc'
# extension module '_lzma' loaded from '/usr/local/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so'
# extension module '_lzma' executed from '/usr/local/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so'
import '_lzma' # <_frozen_importlib_external.ExtensionFileLoader object at 0x7f446c40db70>
import 'lzma' # <_frozen_importlib_external.SourceFileLoader object at 0x7f446c40d160>
# cleanup[2] removing lzma
# cleanup[2] removing _lzma
# cleanup[3] wiping lzma
# cleanup[3] wiping _lzma
# destroy _lzma
# destroy lzma
```
分析日志信息可知函数运行时需要加载 lzma，需具备以下文件：
	- `/usr/local/lib/python3.6/lzma.py`
	- `/usr/local/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so`
6. 执行以下命令，查看 so 文件已具备的依赖：<span id="step6"></span>
```plaintext
$ ldd /usr/local/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so
	linux-vdso.so.1 (0x00007fff75bb1000)
	liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007fc743370000)
	libpython3.6m.so.1.0 => /usr/local/lib/libpython3.6m.so.1.0 (0x00007fc742e36000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fc742c19000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fc74286e000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fc74266a000)
	libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fc742467000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fc742166000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fc74379c000)
```
分析命令执行结果可知除部分系统库外，还需以下文件：
	- `/lib/x86_64-linux-gnu/liblzma.so.5`
	- `/usr/local/lib/libpython3.6m.so.1.0`
7. 将上述 [步骤5](#step5)、[步骤6](#step6) 得到的4个文件，拷贝至项目路径下，并参考以下示例修改代码：
	```js
	import os

	os.environ['LD_LIBRARY_PATH'] = os.path.dirname(
			os.path.realpath(__file__)) + ':' + os.environ['LD_LIBRARY_PATH']

	import pandas as pd

	def main_handler(event, context):
			s = pd.Series([1, 3, 5, 6, 8])
			print(s)
			return len(s)
	```
	
8. 将代码重新部署至 SCF，函数即可正常运行并且无告警提示。
