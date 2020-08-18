使用 Python，Node.js 等语言开发云函数 SCF 时，由于操作系统版本、系统库版本及语言版本不一致，在本地环境运行良好的程序部署到 SCF 后可能会出现错误。为解决依赖安装的问题，本文档介绍使用 `Docker` 为函数安装依赖。请参考以下示例：
- [为 `Node.js 8.9`安装 `nodejieba`](#node)。
- [为 `Python 3.6`安装 `pandas`](#python)。

## 安装 Docker

安装 `Docker`，详情请参阅 [Docker](https://docs.docker.com/install/)。

## Node 安装示例<span id="node"></span>
本节以下述代码为例：
```js
'use strict';

const jieba = require('nodejieba');

exports.main_handler = async (event, context, callback) => {
    return jieba.cut('你好世界');
};
```
此示例可在 Windows 和 macOS 上正确运行，但部署到 SCF 时会出现如下错误代码提示：
```js
{"errorCode":1,"errorMessage":"user code exception caught","stackTrace":"/var/user/node_modules/nodejieba/build/Release/nodejieba.node: invalid ELF header"}
```
为解决此问题，可使用 `Docker` 来安装依赖。请参考以下命令：
```js
$ docker run -it --network=host -v /path/to/your-project:/tmp/your-project node:8.9 /bin/bash -c 'cd /tmp/your-project && npm install nodejieba --save'
```

其中，`/path/to/your-project` 是项目路径, 对应于 `Docker` 容器里的 `/tmp/your-project` 目录。因此，在容器里的 `/tmp/your-project` 目录下安装 `nodejieba`，即在项目路径下安装了 `nodejieba`。依赖安装完成后，将代码重新部署到 SCF 上即可正常运行函数。

## Python 安装示例<span id="python"></span>
本节以下述代码为例：
```js
import pandas as pd

def main_handler(event, context):
    s = pd.Series([1, 3, 5, 6, 8])
    print(s)
    return len(s)
```
为 `Python 3.6`安装 `pandas`。请参考以下命令：
```js
$ docker run -it --network=host -v /path/to/your-project:/tmp/your-project python:3.6.1 /bin/bash -c 'cd /tmp/your-project && pip install pandas -t .'
```
依赖安装完成后，将代码重新部署到 SCF 上并运行，可收到如下日志：
```js
/var/user/pandas/compat/__init__.py:84: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.
  warnings.warn(msg)
0    1
1    3
2    5
3    6
4    8
dtype: int64
```
此时函数可以运行，但会产生警告提示无法加载 `lzma` 模块，若使用 `lzma` 压缩则会导致运行时错误。为解决此问题，需要进入容器内部，执行以下命令：
```js
$ docker run -it --network=host -v /tmp/foo:/tmp/bar python:3.6.1 /bin/bash
```
执行以下命令，安装 `pandas`。
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
可查看日志，如以下代码：
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

从上面的日志可以看到, 函数运行时确实会加载 `lzma`, 所以我们至少需要以下两个文件

- `/usr/local/lib/python3.6/lzma.py`
- `/usr/local/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so`

进一步地, 我们看看这个 `so` 文件有哪些依赖

```js
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

除去部分系统库, 看起来还需要这两个文件

- `/lib/x86_64-linux-gnu/liblzma.so.5`
- `/usr/local/lib/libpython3.6m.so.1.0`

把这四个文件拷贝至项目路径下, 并修改代码, 如下:

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

重新部署, 现在函数可以正常运行并且没有警告了 :)
