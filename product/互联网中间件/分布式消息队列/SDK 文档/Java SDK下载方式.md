## 开发前准备

在执行安装脚本之前，请确保您的机器上已经安装了 Java（≥1.8版本）和 Maven。

### 1. 安装 Java

#### 1.1 检查 Java 安装

打开终端，执行如下命令：

```
java -version
```

如果输出 Java 版本号，说明 Java 安装成功；如果没有安装 Java，请 [下载安装 Java 软件开发套件（JDK）](http://www.oracle.com/technetwork/java/javase/downloads/index.html)。


#### 1.2 设置 Java 环境

设置`JAVA_HOME`环境变量，并指向您机器上的 Java 安装目录。 
以 Java jdk1.8.0_20 版本为例，操作系统的输出如下：

| 操作系统 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| Windows  | Set the environment variable JAVA_HOME to <br/>C:\Program Files\Java\jdkjdk1.8.0_20 |
| Linux    | export JAVA_HOME=/usr/local/java-current                     |
| Mac OSX  | export JAVA_HOME=/Library/Java/Home                          |

将 Java 编译器地址添加到系统路径中：

| 操作系统 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| Windows  | 将字符串“;C:\Program Files\Java\jdk1.8.0_20\bin”添加到系统变量“Path”的末尾 |
| Linux    | export PATH=$PATH:$JAVA_HOME/bin/                            |
| Mac OSX  | not required                                                 |

使用上面提到的 `java -version` 命令验证 Java 安装。

### 2. 安装 Maven 

#### 2.1 下载  安装 Maven 

参考 [Maven 下载](https://maven.apache.org/download.cgi)。

#### 2.2 设置 MAVEN_HOME 和 PATH 环境变量

- Windows 系统下：

```
 新建系统变量  MAVEN_HOME   变量值：E:\Maven\apache-maven-3.3.9
 编辑系统变量  Path         添加变量值： ;%MAVEN_HOME%\bin
```

- Linux / macOS 系统下：

```
 export MAVEN_HOME=/usr/local/maven/apache-maven-3.3.9
 export PATH=$MAVEN_HOME/bin:$PATH
```

#### 2.3 验证 Maven 安装

当 Maven 安装完成后， 通过执行如下命令验证 Maven 是否安装成功。

```
   mvn --version
```

若出现正常的版本号信息后，说明 Maven 安装成功。



### 3. Maven 配置 TDMQ Pulsar 版私服地址 

#### 3.1 添加私服配置

找到 Maven 所使用的配置文件，一般在 `~/.m2/settings.xml` 中，在 settings.xml 中加入如下配置：

```xml
<profiles>
     <profile>
       <id>nexus</id>
       <repositories>
           <repository>
               <id>central</id>
               <url>http://repo1.maven.org/maven2</url>
               <releases>
                   <enabled>true</enabled>
               </releases>
               <snapshots>
                   <enabled>true</enabled>
               </snapshots>
           </repository>
       </repositories>
       <pluginRepositories>
           <pluginRepository>
               <id>central</id>
               <url>http://repo1.maven.org/maven2</url>
               <releases>
                   <enabled>true</enabled>
               </releases>
               <snapshots>
                   <enabled>true</enabled>
               </snapshots>
           </pluginRepository>
       </pluginRepositories>
   </profile>
   <profile>
       <id>qcloud-repo</id>
       <repositories>
           <repository>
              <id>tdmq</id>
              <url>http://mirrors.tencent.com/repository/maven/tdmq/</url>
              <releases>
                  <enabled>true</enabled>
                  <updatePolicy>always</updatePolicy>
              </releases>
              <snapshots>
                  <enabled>true</enabled>
                  <updatePolicy>always</updatePolicy>
              </snapshots>
          </repository>
          </repositories>
       <pluginRepositories>
           <pluginRepository>
               <id>qcloud-plugin-central</id>
               <url>http://mirrors.cloud.tencent.com/nexus/repository/maven-public/</url>
               <snapshots>
                   <enabled>true</enabled>
               </snapshots>
               <releases>
                   <enabled>true</enabled>
               </releases>
           </pluginRepository>
       </pluginRepositories>
   </profile>
 </profiles>
      
 <activeProfiles>
   <activeProfile>nexus</activeProfile>
   <activeProfile>qcloud-repo</activeProfile>
</activeProfiles>
```

[setting.xml 样例文件下载 >>](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/tdmq-doc/settings.xml)（鼠标右键另存为链接）



#### 3.2 验证配置是否成功

在命令行执行如下命令：

```
mvn help:effective-settings
```

- 查看执行结果，没有错误表明 setting.xml 格式正确。
- profiles 中包含 qcloud-repo ，则表明 qcloud-repo 私服已经加入到 profiles 中；activeProfiles 中包含 qcloud-repo，则表明 qcloud-repo 私服已经激活成功。可以通过 mvn help:effective-settings | grep 'qcloud-repo'命令检查。

![](https://main.qcloudimg.com/raw/43645276539f8a85703f137ae2bb65fc.png)

执行正确的 Maven 命令后，如果无法下载 qcloud 相关依赖包，请重启 IDE，或者检查 IDE Maven 相关配置。

## 安装 SDK

1. 在您 Java 工程的 pom.xml 中添加以下依赖：

  ```xml
<dependency>
			<groupId>com.tencent.tdmq</groupId>
			<artifactId>tdmq-client</artifactId>
			<version>2.6.0</version>
</dependency>
  ```

2. 在 pom.xml 所在目录执行 `mvn clean package` 即可下载 TDMQ Pulsar 版 SDK。
