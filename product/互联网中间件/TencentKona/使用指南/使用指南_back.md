## 安装指南
提供 rpm、tar 两种安装方式
1. rpm 安装

1）配置 yum repo， `sudo vi /etc/yum.repos.d/artifactory.repo`
```
[Artifactory]
name=Artifactory
baseurl=https://mirrors.tencent.com/repository/rpm/tencent_rpm/x86_64  
enabled=1
```

2) 安装 Kona
```
yum install KonaJDK -y --nogpgcheck
```

2. tar 安装指定版本的 Kona JDK

1) 下载 KonaJDK 安装包
```
cd 安装目录
wget https://linzang-jdk-1257356411.cos.ap-chengdu.myqcloud.com/Kona-RELEASE/KonaJDK/KonaJDK-8.0.0-8u232.ga.x86_64.tar.gz
```

2）解压并设置 JAVA_HOME
```
tar -xvf KonaJDK-8.0.0-8u232.ga.x86_64.tar.gz
export JAVA_HOME=目标安装目录/KonaJDK-8.0.0-8u232.ga
export PATH=${JAVA_HOME}/bin:$PATH
export CLASSPATH=.:${JAVA_HOME}/lib
```

3. docker

1) 登录镜像仓库
```
sudo docker login --username=[username] csighub.tencentyun.com
```

2）拉取镜像
```
sudo docker pull csighub.tencentyun.com/konajdk/konajdk:v1
``

## JFR 使用

Java Flight Recorder 用于收集 Java 应用在运行过程中的诊断及性能数据，back port 自 OpenJDK11。如果使用的是默认的配置，理论上 JFR 开销是小于2%的，因此必要情况下可用在现网收集数据。

### 简要用法

1. JFR的开启、记录与关闭
```
//默认关闭，需要使用时，在应用启动命令中带上 -XX:+EnableJFR 参数开启JFR
$JAVA_HOME/bin/java -XX:+EnableJFR YourApplication
//当需要开始记录时先获取YourApplication的pid，使用jcmd pid JFR.start开始记录，当java应用正常停止时会自动将运行数据记录在filename参数指定的文件中
$JAVA_HOME/bin/jcmd <your_pid> JFR.start name=anyname_for_dump filename=anyname_for_your_record.jfr
//如果JFR.start后，打算导出截止目前为止的记录就用jcmd JFR.dump 可以通过filename指定导出数据的位置，注意name要与JFR.start中指定的name一致：
$JAVA_HOME/bin/jcmd <your_pid> JFR.dump name=anyname_for_your_record filename=anyname_for_dump_record.jfr
//停止记录(注意这个停止如果没有带后面的name和filename参数，将不会执行dump直接停止记录)
$JAVA_HOME/bin/jcmd <your_pid> JFR.stop name=anyname_for_your_record filename=anyname_for_dump_record.jfr
```

2. 使用JMC(JAVA Mission Controll)分析.jfr文件
- 需使用7.0以上版本

3. 更多使用方法参照Oracle的相关说明文档