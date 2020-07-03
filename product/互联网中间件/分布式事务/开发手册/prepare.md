# 准备工作

## 环境要求

- JDK，建议1.8.161或以上版本。
- Maven，建议3.5.2或以上版本。
- 网络，能够连接到公网即可。

## 配置Maven仓库

下载`示例工程`后，可以通过以下配置引入腾讯云Maven仓库，以便于自动获取DTF相关依赖。

``` xml
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
    <activeProfile>qcloud-repo</activeProfile>
  </activeProfiles>
</settings>
```

## 获取腾讯云API密钥

使用DTF时，需要用户自行获取腾讯云[访问密钥](http://www.tencent.com)信息（即SecretId和SecretKey）。

> 注：该步骤获取`SecretId`，`SecretKey`。

## 获取事务分组ID，TC集群IP与端口

使用DTF时，需要用户自行[创建事务分组](http://www.tencent.com)，并获取其`事务分组ID`，`TC集群IP与端口`信息。

> 注： 该步骤获取`GroupId`(`事务分组ID`)，`BorkerList`(`TC集群IP与端口`)。
