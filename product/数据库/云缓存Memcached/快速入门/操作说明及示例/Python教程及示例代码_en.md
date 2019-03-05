## 1. Environment and dependency

Environment: Install python [[download address](https://www.python.org/downloads/)] on Tencent Cloud CVM

Dependency  python-memcached 1.5.4 is used in this example. Install this client [[download address](https://pypi.python.org/pypi/python-memcached)] on Tencent Cloud CVM

## 2. Steps

Deploy python environment and python-memcached client on Tencent Cloud CVM

Write the test code and run.

## 3. Sample code: python-memcached-demo.py
Replace *** in the code with your IP:Port. In the console, click "NoSQL Fast Storage", and you can see IP:Port assigned by the system in "Management View".

```
#!/usr/bin/env python
import memcache
mc = memcache.Client(['***.***.***.***:****'],debug=0)
mc.set("python-key","qcloud NoSQL Server")
value = mc.get("python-key")
print value
```
