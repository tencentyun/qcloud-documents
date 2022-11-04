DolphinScheduler 是一个可视化 DAG 工作流任务调度平台，其暂不支持自定义 JDBC 作为数据源，因此集成 DLC 只能在任务中定义 jdbc 连接信息，从而创建 DLC 调度任务。以下指引以 Python 任务为例。

## 准备工作
1. 部署与使用 DolphinScheduler。
建议通过 Docker 部署 DolphinScheduler，可参考 [官方部署文档](https://dolphinscheduler.apache.org/zh-cn/docs/2.0.0/user_doc/guide/installation/docker.html) 和 [快速上手文档](https://dolphinscheduler.apache.org/zh-cn/docs/2.0.0/user_doc/guide/quick-start.html)。
2. 安装 Python 环境、Java 环境。
3. 准备 [dlc-jdbc jar 包](https://dlc-jdbc-1304028854.cos.ap-beijing.myqcloud.com/dlc-jdbc-2.2.3-jar-with-dependencies.jar)。

## 创建并运行任务
具体流程：
1. 创建工作流。
2. 创建任务。
3. 选择 Python 任务。
4. 填写脚本等信息。
5. 上线启动。

具体操作可以参考 DolphinScheduler 官方 [快速上手文档](https://dolphinscheduler.apache.org/zh-cn/docs/2.0.0/user_doc/guide/quick-start.html)，脚本内容可参考下述代码。
```python
import jaydebeapi

jdbc_url = "jdbc:dlc:dlc.tencentcloudapi.com?task_type=SQLTask&datasource_connection_name=DataLakeCatalog®ion=ap-guangzhou&data_engine_name=public-engine"
user = "xx"
pwd = "xx"
driver = "com.tencent.cloud.dlc.jdbc.DlcDriver"
jar_file = '/opt/dolphinscheduler/libs/dlc-jdbc-2.2.3-jar-with-dependencies.jar'
sql = "select 1"
conn = jaydebeapi.connect(driver, jdbc_url, [user, pwd], jar_file)
curs = conn.cursor()
curs.execute(sql)
array_size = curs.arraysize.real
rowcount = curs.rowcount.real
print(array_size)
print(rowcount)
rows = curs.rowcount.real
if rows != 0:
    result = curs.fetchall()
    print(result)

curs.close()
conn.close()

```
