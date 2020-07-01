## 环境及依赖
环境：在腾讯云 CVM 上安装对应的 Python，[下载地址](https://www.python.org/downloads/)。
依赖：本例使用 Python-memcached 1.5.4 版本，在 CVM 上安装此客户端，[下载地址](https://pypi.python.org/pypi/python-memcached)。

## 使用步骤
在 CVM 上部署好 Python 环境及 Python-memcached 客户端。
编写测试代码并运行。

## 代码示例 python-memcached-demo.py
将代码中 *** 号替换为您的 IP:Port，在管理中心，单击【NoSQL高速存储】，在 NoSQL 高速存储【管理视图】，可以看到系统分配的 IP:Port。

```
#!/usr/bin/env python
import memcache
mc = memcache.Client(['***.***.***.***:****'],debug=0)
mc.set("python-key","qcloud NoSQL Server")
value = mc.get("python-key")
print value
```
