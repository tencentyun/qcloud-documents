本文介绍如何使用 Python 语言连接和操作图数据库 KonisGraph。以 [Gremlin-console tutorials](https://tinkerpop.apache.org/docs/3.5.1/tutorials/getting-started/#_the_first_five_minutes) 中的人和软件的关系图为示例。
![enter image description here](https://main.qcloudimg.com/raw/51a52aabf2b24289aa61f713a8cd1eb4.png)
如图所示，整个图包含2类点 person 和 software，2类边 knows 和 created，和几类属性 id、name、age、lang、weight。

## 环境准备
1. 安装 Python 语言环境。
2. 安装 gremlinpython。
```sh
pip3 install gremlinpython
```
>!gremlinpython 依赖 python 3.5 及以上版本。
3. 获取图数据库的连接参数。在 [控制台](https://console.cloud.tencent.com/konisgraph) 实例详情页中可以查看实例的 VIP 和 PORT，即内网地址和 Gremlin 端口。

## 示例程序
```python
from gremlin_python.driver import client
from gremlin_python.driver.protocol import GremlinServerError
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

import json


class Tutorial:
    def __init__(self, host, port, username, password):
        self.url = "ws://{0}:{1}/gremlin".format(host, port)
        self.username = username
        self.password = password
        self._client = client.Client(self.url, 'g', username=username, password=password)
        self._traversal = None
        self._connection = None

    def create_property_meta(self, p_name, p_type, p_default):
        script = 's.addP("{0}", "{1}", "{2}")'.format(p_name, p_type, p_default)
        self.__execute_script(script)

    def create_vertex_meta(self, v_name, v_id, v_props):
        script = 's.addV("{0}", "{1}", {2})'.format(v_name, v_id, v_props)
        self.__execute_script(script)

    def create_edge_meta(self, e_name, e_from, e_to, e_props):
        script = 's.addE("{0}", "{1}", "{2}", {3})'.format(e_name, e_from, e_to, e_props)
        self.__execute_script(script)

    def traversal(self):
        if self._traversal is None:
            self._connection = DriverRemoteConnection(
                self.url, "g", username=self.username, password=self.password
            )
            self._traversal = traversal().withRemote(self._connection)
        return self._traversal

    def close(self):
        if self._connection is not None:
            self._connection.close()
        if self._client is not None:
            self._client.close()

    def __execute_script(self, script):
        try:
            result_set = self._client.submit(script)
            future_results = result_set.all()
            future_results.result()
        except GremlinServerError as e:
            print(e)


if __name__ == "__main__":
    t = Tutorial("KONISGRAPH_VIP", KONISGRAPH_PORT, "your username", "your password")

    t.create_property_meta("id", "T_LONG", "0")
    t.create_property_meta("name", "T_STRING", "")
    t.create_property_meta("age", "T_INT", "0")
    t.create_property_meta("weight", "T_DOUBLE", "0.0")
    t.create_property_meta("lang", "T_STRING", "")

    t.create_vertex_meta("person", "id", ["name", "age"])
    t.create_vertex_meta("software", "id", ["name", "lang"])
    t.create_edge_meta("knows", "person", "person", ["weight"])
    t.create_edge_meta("created", "person", "software", ["weight"])

    g = t.traversal()
    try:
        g.addV('person').property('id', 1).property('name', 'marko').property('age', 29). \
            addV('person').property('id', 2).property('name', 'vadas').property('age', 27). \
            addV('person').property('id', 4).property('name', 'josh').property('age', 32). \
            addV('person').property('id', 6).property('name', 'peter').property('age', 35).iterate()

        g.addV('software').property('id', 3).property('name', 'lop').property('lang', 'java'). \
            addV('software').property('id', 5).property('name', 'ripple').property('lang', 'java').iterate()

        g.V(1).addE('knows').to(__.V(2)).iterate()
        g.V(1).addE('knows').to(__.V(4)).iterate()
        g.V(1).addE('created').to(__.V(3)).property('weight', 0.4).iterate()
        g.V(6).addE('created').to(__.V(3)).property('weight', 0.2).iterate()
        g.V(4).addE('created').to(__.V(3)).property('weight', 0.4).iterate()
        g.V(4).addE('created').to(__.V(5)).property('weight', 1.0).iterate()

        print("marko: " + json.dumps(g.V().has('person', 'name', 'marko').valueMap().next()))

        print("who marko knows: " + json.dumps(g.V().has('person', 'name', 'marko').out('knows').valueMap().toList()))

        print("who creates software lop: " + json.dumps(g.V().has('software', 'name', 'lop').in_('created').valueMap().toList()))
    except GremlinServerError as e:
        print(e)
    finally:
        t.close()
```

## 运行程序
```sh
python3 tutorial.py
```

