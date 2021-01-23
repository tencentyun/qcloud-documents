本文将为您介绍如何 Play 安装 Java 探针。

##  在 Play 上安装 Java 探针

### Play 2.3.x

进入项目目录，安装探针：

```
./activator -J-javaagent:/${路径}/tapm/tapm-agent-java.jar run
```

### Play 2.2+ production mode

> **注意:**`play start` 2.2+版本不允许使用  -javaagent  参数。

1. 解压包含 `start` 脚本的 zip 文件：

```
play clean dist && unzip target/universal/*.zip
```

2. 在启动应用时增加 `-J-javaagent` 参数：

```
cd UNZIPPEDFOLDER
./bin/SCRIPTNAME -J-javaagent:/${路径}/tapm-agent-java.jar
```

### Play 2 production mode

> **注意:** 该版本的Play使用`play start` 命名启动服务时，不支持-javaagent参数。

1. 解压包含 `start` 脚本的zip文件：

```
play clean dist && unzip dist/*.zip
```

2. 在启动应用时增加 `-javaagent` 参数：

```
cd UNZIPPEDFOLDER
chmod a+x start
./start -javaagent:/${路径}/tapm-agent-java.jar
```

### Play 2 development mode

1. 在 play 的安装目录修改 `framework/build`  文件 (或者修改 windows 环境下的 build.bat 文件)：

```
nano `which play`/../framework/build
```

2. 在 java exec 调用之前配置 JAVA_OPTS ，增加 -javaagent 参数：

```
JAVA_OPTS="$JAVA_OPTS -javaagent:/${路径}/tapm/tapm-agent-java.jar"
```

如果在调用 java exec 显示不存在 `${JAVA_OPTS}` ，需要将 `${JAVA_OPTS}`加入路径。

3. dev模式启动(切勿使用 `play start` )：

```
play run
```

### Play 1 installation

在运行应用的时候增加 -javaagent 参数：

```
play run helloworld -javaagent:/${路径}/tapm-agent-java.jar
```


