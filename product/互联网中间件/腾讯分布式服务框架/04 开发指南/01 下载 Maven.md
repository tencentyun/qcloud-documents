在正式开发应用前，请确保您的机器上已经安装了 Java 和 Maven。

## 安装 Java

### 步骤1：检查 Java 安装

打开终端，执行如下命令：
<dx-codeblock>
:::  bash
java -version
:::
</dx-codeblock>


如果输出 Java 版本号，说明 Java 安装成功；如果没有安装 Java，请 [下载安装 Java 软件开发套件（JDK）](http://www.oracle.com/technetwork/java/javase/downloads/index.html)。


### 步骤2：设置 Java 环境

设置`JAVA_HOME`环境变量，并指向您机器上的 Java 安装目录。 
以 Java 1.6.0_21 版本为例，操作系统的输出如下：

| 操作系统 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| Windows  | Set the environment variable JAVA_HOME to <br/>C:\Program Files\Java\jdk1.6.0_21 |
| Linux    | export JAVA_HOME=/usr/local/java-current                     |
| Mac OSX  | export JAVA_HOME=/Library/Java/Home                          |

将 Java 编译器地址添加到系统路径中。

| 操作系统 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| Windows  | 将字符串“;C:\Program Files\Java\jdk1.6.0_21\bin”添加到系统变量“Path”的末尾 |
| Linux    | export PATH=$PATH:$JAVA_HOME/bin/                            |
| Mac OSX  | not required                                                 |

使用上面提到的 **java -version** 命令验证 Java 安装。

## 安装 Maven 

### 步骤1：下载  安装 Maven 

参见 [Maven 下载](https://maven.apache.org/download.cgi)。

### 步骤2：设置 MAVEN_HOME 和 PATH 环境变量

- Windows 系统下
```
新建系统变量   MAVEN_HOME  变量值：E:\Maven\apache-maven-3.3.9
编辑系统变量   Path         添加变量值： ;%MAVEN_HOME%\bin
```

- Linux、macOS 系统下
```
export MAVEN_HOME=/usr/local/maven/apache-maven-3.3.9
export PATH=$MAVEN_HOME/bin:$PATH
```

### 步骤3：验证 Maven 安装

当 Maven 安装完成后， 通过执行如下命令验证 Maven 是否安装成功。
<dx-codeblock>
:::  mvn
mvn --version
:::
</dx-codeblock>


若出现正常的版本号信息后，说明 Maven 安装成功。


## Maven 配置 TSF 私服地址 

### 步骤1：添加私服配置

找到 Maven 所使用的配置文件，一般在`~/.m2/settings.xml`中，在 settings.xml 中加入如下配置 ：

您也可以下载 [setting.xml 样例文件](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/setting/settings.xml)（鼠标右键另存为链接）。
<dx-codeblock>
:::  xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
  <!-- localRepository
   | The path to the local repository maven will use to store artifacts.
   |
   | Default: ${user.home}/.m2/repository
  <localRepository>/path/to/local/repo</localRepository>
  -->
  
  <pluginGroups></pluginGroups>
  <proxies></proxies>
  <servers></servers>
  <mirrors></mirrors>
 
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
                <id>qcloud-central</id>
                <name>qcloud mirror central</name>
                <url>https://mirrors.cloud.tencent.com/nexus/repository/maven-public/</url>
                <snapshots>
                    <enabled>true</enabled>
                </snapshots>
                <releases>
                    <enabled>true</enabled>
                </releases>
            </repository>
            </repositories>
        <pluginRepositories>
            <pluginRepository>
                <id>qcloud-plugin-central</id>
                <url>https://mirrors.cloud.tencent.com/nexus/repository/maven-public/</url>
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

</settings>
:::
</dx-codeblock>

### 步骤2：验证配置是否成功

在命令行执行如下命令：
<dx-codeblock>
:::  mvn
mvn help:effective-settings
:::
</dx-codeblock>


- 查看执行结果，没有错误表明 setting.xml 格式正确。
- profiles 中包含 qcloud-repo ，则表明 qcloud-repo 私服已经加入到 profiles 中；activeProfiles 中包含 qcloud-repo，则表明 qcloud-repo 私服已经激活成功。可以通过`mvn help:effective-settings | grep 'qcloud-repo'`命令检查。
  ![](https://main.qcloudimg.com/raw/43645276539f8a85703f137ae2bb65fc.png)

>?执行正确的 Maven 命令后，如果无法下载 qcloud 相关依赖包，请重启 IDE，或者检查 IDE Maven 相关配置。



### 后续步骤

1. 完成以上步骤后，您可以参见 [应用开发](https://cloud.tencent.com/document/product/649/55489) 来开发您的应用。
2. 完成应用开发后，您可以参见 [应用打包](https://cloud.tencent.com/document/product/649/73793) 下载 TSF SDK 并将您的应用工程打包，部署到 TSF 平台。


