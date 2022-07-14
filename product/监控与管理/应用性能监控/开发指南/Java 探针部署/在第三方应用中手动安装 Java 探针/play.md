本文将为您介绍如何 Play 安装 Java 探针。




## 前提条件

- 应用性能监控目前处于内测阶段，如需体验需通过 [应用性能监控内测申请](https://cloud.tencent.com/apply/p/f5yvbf09mka)。
- 在安装探针前，请先安装 Agent Collector。
- 在安装探针前，需要先确保本地浏览器时间与服务器时区、时间一致。若有多个服务器，则要保证本地浏览器、多个服务器的时区、时间都一致。否则，可能会影响数据的准确性，例如拓扑不正确等。
- 前往 TAPM 控制台 [探针下载](https://console.cloud.tencent.com/tapm/addagent) 页面下载 tapm-java-Agent。


##  操作步骤




### Play 2.3.x

进入项目目录，安装探针：

```plaintext
./activator -J-javaagent:/${路径}/tapm/tapm-agent-java.jar run
```

### Play 2.2+ production mode

>!play start 2.2及以上版本不允许使用  -javaagent  参数。

1. 解压包含 `start` 脚本的 zip 文件：
```plaintext
play clean dist && unzip target/universal/*.zip
```
2. 在启动应用时增加 `-J-javaagent` 参数：
```plaintext
cd UNZIPPEDFOLDER
./bin/SCRIPTNAME -J-javaagent:/${路径}/tapm-agent-java.jar
```

### Play 2 production mode

>! 该版本的 Play 使用 `play start` 命名启动服务时，不支持 -javaagent 参数。

1. 解压包含 start 脚本的zip文件：
```plaintext
play clean dist && unzip dist/*.zip
```
2. 在启动应用时增加 `-javaagent` 参数：
```plaintext
cd UNZIPPEDFOLDER
chmod a+x start
./start -javaagent:/${路径}/tapm-agent-java.jar
```


### Play 2 development mode

1. 执行以下命令，在 Play 的安装目录修改 `framework/build`  文件（或者修改 Windows 环境下的 build.bat 文件）：
```plaintext
nano `which play`/../framework/build
```
2. 在 java exec 调用之前配置 JAVA_OPTS ，增加 -javaagent 参数。
```plaintext
JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm/tapm-agent-java.jar"
```
 如果在调用 java exec 显示不存在 `${JAVA_OPTS}` ，需要将 `${JAVA_OPTS}` 加入路径。
3. 执行以下命令，以 dev 模式启动 Play（切勿使用 `play start`）：
```plaintext
play run
```


### Play 1 installation

在运行应用的时候增加 -javaagent 参数：

```plaintext
play run helloworld -javaagent:/${路径}/tapm-agent-java.jar
```


