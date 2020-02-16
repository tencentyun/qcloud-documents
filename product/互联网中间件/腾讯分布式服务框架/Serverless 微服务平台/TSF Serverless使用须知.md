>?TSF Serverless 目前处于内测阶段，欢迎填写 [使用申请](https://cloud.tencent.com/apply/p/om62iz2gqx)。

## 监听端口
- 如果您的业务是微服务（Spring、Mesh），则无需考虑端口监听问题。
- 如果您的业务是Web服务，您的服务需要**主动监听8080端口**。

## 上传程序包要求

目前 Serverless 应用支持的程序包格式包括 **jar、war、tar.gz 和 zip**。

- jar： FatJar 格式的程序包，用户可以参考 [如何打 FatJar 包](https://cloud.tencent.com/document/product/649/16934)。
- war： war 格式的程序包，在部署 war 包时，TSF 会自动安装 Tomcat 环境。示例 [demo 下载](https://alon-deployment-gz-1257356411.cos.ap-guangzhou.myqcloud.com/sample.war) ，示例 demo 部署成功后，使用 `http://<IP>:8080/sample` 访问，其中 IP 可以是实例的外网 IP。
- tar.gz 、zip ： 压缩包中**必须**包含三个文件，**确保文件名正确**：
  - start.sh：启动脚本
  - stop.sh：停止脚本
  - cmdline：用于检查应用进程是否存在，**没有**`.sh`后缀

| 文件类型 | 启动方式                                                     |
| -------- | ------------------------------------------------------------ |
| war      | 云服务器上的 agent 会使用`java -jar`命令启动程序。            |
| jar      | 云服务器上的 agent 会使用`java -jar`命令启动程序。            |
| tar.gz   | 云服务器上的 agent 会解压压缩包，使用解压目录下的`start.sh`脚本启动应用程序。 |
| zip      | 云服务器上的 agent 会解压压缩包，使用解压目录下的`start.sh`脚本启动应用程序。 |


## start.sh / stop.sh / cmdline 说明
以一个 Python 应用的压缩包为示例，解压后的文件目录如下：
- promotionService.py
- start.sh
- stop.sh 
- cmdline

start.sh 启动脚本内容如下：
```python
#! /bin/bash

already_run=`ps -ef|grep "python promotion"|grep -v grep|wc -l`
if [ ${already_run} -ne 0 ];then
	echo "promotionService already Running!!!! Stop it first"
	exit -1
fi

nohup python promotionService.py 8093 &
```

stop.sh 停止脚本内容如下：
```python
#!/bin/bash

pid=`ps -ef|grep "python promotion"|grep -v grep|awk '{print $2}'`
kill -SIGTERM $pid
echo "process ${pid} killed"
```

cmdline 检测进程脚本，agent 通过`ps -ef | grep 'cmdline 内容'`来检测进程是否存在，示例如下：
```
python promotion
```

cmdline 更多说明
如果启动应用是 Java 应用，启动脚本中通过`java -jar xxx.jar`来启动应用。在 cmdline 文件中使用完整的 Java 启动命令。例如启动脚本中包含如下启动命令：
```
java -Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m -jar consumer-demo-0.0.1-SNAPSHOT.jar
```
那么在 cmdline 中内容为：
```
java -Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m -jar consumer-demo-0.0.1-SNAPSHOT.jar
```
当应用启动后，agent 会在服务器上执行`ps -ef | grep 'cmdline 内容'`来检查进程是否存在。
![](https://main.qcloudimg.com/raw/d13fea5b8c7c59b091bfca894c9eadaa.png)
> !如果没有 cmdline 文件或者 cmdline 文件内容不正确，在控制台上部署组的状态会显示为 "已停止"，即使此时服务器上的应用已经运行起来（但是 TSF agent 无法获取应用进程状态）。


MacOS 系统压缩软件说明
对于 MacOS 系统的用户，使用系统自带压缩软件时，会在压缩包里面生成`__MACOSX`的临时目录，从而导致 agent 无法找到启停脚本。用户可以 [下载 Keka 压缩软件](https://www.keka.io/)，选择 zip 压缩格式，勾选【排除 Mac 资源文件】选项。将文件拖拽到 keka 界面上进行压缩，这种方式生成的压缩包没有`__MACOSX`的临时目录。
![](https://main.qcloudimg.com/raw/55dd0e931b437bf058fbdb83e55a32cf.png)


南北向调用 , tar.gz 和 zip 压缩包中也同样需要包含以下内容，**请确保文件名正确**：

- 业务代码**（必选）**：压缩包中需要包含程序运行所需的**全部依赖包（eg. node_modules）**。您的程序必须**监听8080端口**。
- start.sh**（必选）**：启动脚本。我们会通过运行启动脚本拉起您的程序。您可以把启动服务所需的参数填入启动脚本。需要注意的是，启动脚本需要放在**压缩包的根路径下**。以下是一个示例启动脚本：
```bash
#! /bin/bash
node index.js
```
- stop.sh**（必选）**：停止脚本。我们会通过运行停止脚本来终止程序运行。需要注意的是，停止脚本需要放在**压缩包的根路径下**。以下是一个示例停止脚本：
```bash
#! /bin/bash
pid=`ps -ef | grep "node index" | grep -v grep | awk '{print $2}'`
kill -SIGTERM $pid
```
- cmdline**（必选）**：用于检查应用进程是否存在。cmdline 检测进程脚本，agent 通过ps -ef | grep 'cmdline 内容'来检测进程是否存在，示例如下：：
```bash
node index.js
```
 更多 cmdline 介绍请参考 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359) 文档。
以 Node.js 为例，程序包结构如下：
```
.
├── node_modules  
├── index.js            
├── package.json
├── start.sh          //   启动脚本
└── stop.sh          //    停止脚本
```


## 本地临时存储
- 如果您需要在本地写临时文件，只能写到`/tmp`路径下，其他路径下写操作会失败。
- `/tmp`路径下空间有限，您需要定时清理。


## 旧版部署组/应用迁移说明
为提供更好的服务并全面支持微服务平台相关能力，我们在 [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本中对 Serverless 应用及部署组进行了升级。关于历史部署组，您需要关注以下几点：
- 历史部署组上的业务可照常运行。但为了保证您能享受新版本功能，我们强烈建议您重新创建部署组，并对旧版部署组做迁移。具体操作请参考 [部署组迁移指引](#migrate)。
- [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后默认历史集群不可新建部署组，请重新创建并选择新的集群进行操作。
- [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后的访问管理入口将从【应用】迁移到【部署组】。
- 如果需要查看历史部署组的域名，您可以通过登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，基于 TSF 应用名查找对应 API 网关。
例如：旧版应用名为 demo ，则对应 API 网关的默认域名为 `demo-<appid>.<region>.apigw.tencentcs.com`。
- [1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后 Serverless 应用的程序包需同时包含 start.sh、stop.sh、cmdline 三个文件，详见 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359) 。

<span id="migrate"></span>
#### 部署组迁移指引
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index?rid=1)，在左侧导航栏单击【集群】，新建一个集群。详细操作可参考 [集群](https://cloud.tencent.com/document/product/649/13684) 文档。
![](https://main.qcloudimg.com/raw/ff452959fb414689c1f615d87dba5bd8.png)
2. 单击【部署组】，创建 Serverless 应用部署组。
具体操作可参考 [Serverless 应用部署组](https://cloud.tencent.com/document/product/649/41099) 文档。**历史部署组不可直接创建 Serverless 集群**。
![](https://main.qcloudimg.com/raw/d5d8df48016e925646a9a2d137421bcb.png)
3. 部署 Serverless 应用。具体操作可参考 [Serverless 应用部署组](https://cloud.tencent.com/document/product/649/41099) 文档。
![](https://main.qcloudimg.com/raw/92c0af5aa842287b6152cb89c802b2ea.png)
4. 上传程序包。
本次程序包上传必须同时**包含 start.sh、stop.sh、cmdline**，详情请参考 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359)。
5. 开启外网访问。
单击部署组 ID，在部署组详情页开启外网访问，即可在外网访问已迁移至部署组的服务。
![](https://main.qcloudimg.com/raw/9ed6978228e87b5026a36225c9124f64.png)

