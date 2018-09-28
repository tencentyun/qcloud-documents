## 开发前准备

### 环境依赖

在执行安装脚本之前，需要确保机器上已经安装了 Maven 和设置了环境变量。

#### 1. 安装 Maven 

参考 [Maven 下载](https://maven.apache.org/download.cgi)。

验证 Maven 安 当 Maven 安装完成后， 通过执行如下命令验证 Maven 是否安装成功。

- Windows 系统下

```
   mvn --version
```

- Linux、macOS 系统下

```
   mvn -v
```

   若出现正常的版本号信息后，说明 Maven 安装成功。

#### 2. 设置环境变量

##### 设置 MAVEN_HOME 和 PATH 环境变量

- Windows 系统下

```
   新建系统变量   MAVEN_HOME  变量值：E:\Maven\apache-maven-3.3.9
   编辑系统变量  Path         添加变量值： ;%MAVEN_HOME%\bin
```

- Linux、macOS 系统下

```
   export MAVEN_HOME=/usr/local/maven/apache-maven-3.3.9
   export PATH=$MAVEN_HOME/bin:$PATH
```

##### 设置 JAVA_HOME 环境变量

- Windows 系统下

```
   JAVA_HOME=C:/Program Files/Java/jdk1.5.0_05
```

- Linux、macOS 系统下

```
   export JAVA_HOME=$(/usr/libexec/java_home)
```


#### 3. Maven 配置腾讯云 TSF 私服地址 

##### 3.1 添加私服配置

找到 Maven 所使用的配置文件，一般在 ~/.m2/settings.xml 中，在 settings.xml 中加入如下配置：

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
                <id>qcloud-central</id>
                <name>qcloud mirror central</name>
                <url>http://mirrors.cloud.tencent.com/nexus/repository/maven-public/</url>
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



[setting.xml 样例文件下载>> ](https://main.qcloudimg.com/raw/0e3c73b64c4ec64ae9b16d1a347db462/settings.xml) （鼠标右键另存为链接）

##### 3.2 验证配置是否成功

在命令行执行如下命令 `mvn help:effective-settings` 。
   - 查看执行结果，没有错误表明 setting.xml 格式正确。
   - Profiles 中包含 qcloud-repo ，则表明 qcloud-repo 私服已经加入到 profiles 中。
   - ActiveProfiles 中包含 qcloud-repo，则表明 qcloud-repo 私服已经激活成功。
   
其他说明
   - 执行正确的 Maven 命令，无法现在 qcloud 相关依赖包，请重启 IDE，或者检查 IDE Maven 相关配置。

#### 4. 获取 Demo

[Demo 源码下载 >>](https://main.qcloudimg.com/raw/8b6d89e53ec8d272606370daaa5fd507/tsf-demo-simple-0823.zip)

### 安装 SDK

通过 Maven 获取 TSF SDK。在 Demo 工程 `pom.xml` 所在目录执行 `mvn clean package` 即可下载 TSF SDK。

![](https://main.qcloudimg.com/raw/d6d4c2e76bd308671472682999eb78d3.png)

> **注意：**如果无法下载相关依赖，请检查网络是否有防火墙限制。
