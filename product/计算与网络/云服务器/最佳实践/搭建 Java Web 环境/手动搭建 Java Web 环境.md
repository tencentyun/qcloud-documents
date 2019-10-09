## 操作场景
本文档介绍如何在 Linux 操作系统的腾讯云云服务器（CVM）上手动部署 Java Web 环境。文档包含软件安装内容，请确保您已经熟悉软件安装方法，请参见 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046)。

Java Web 环境组成及说明：
- Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
- Apache Tomcat：Web 应用服务器，本文以 Apache Tomcat 8.5.46 版本为例。
- JDK：Java 开发工具包，本文以 jdk 1.8.0_221 版本为例。


## 前提条件
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建并登录云服务器
1. 在实例的管理页面，单击【新建】。
具体操作请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 云服务器创建成功后，返回至 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，查看和获取实例的以下信息。如下图所示：
![](https://main.qcloudimg.com/raw/96a5f8e2eca54d4ea3ec56cb439b025a.png)
 - 云服务器实例用户名和密码。
 - 云服务器实例公网 IP。
3. 登录 Linux 云服务器，具体操作请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
登录云服务器后，默认已获取 root 权限，以下步骤需在 root 权限下操作。



### 安装 JDK
1. 下载 JDK 源码包，您可前往 [Java SE 下载](https://www.oracle.com/technetwork/java/javase/downloads/index.html) 页面选择需要的版本。
>?请先将 JDK 源码包下载到本地，再上传至云服务器，否则会出现解压错误。
> - 若您使用机器为 Windows 操作系统，可通过 [ WinSCP 上传文件](https://cloud.tencent.com/document/product/213/2131)。
> - 若您使用机器为 Mac 或 Linux 操作系统，可通过 [SCP 上传文件](https://cloud.tencent.com/document/product/213/2133)。
>
2. 执行以下命令，新建 JDK 安装目录。
```
mkdir /usr/java
```
3. 执行以下命令，将 JDK 源码包解压到指定位置。
```
tar xzf jdk-8u221-linux-x64.tar.gz -C /usr/java
```
4. 执行以下命令，打开 `profile` 文件。
```
vim /etc/profile
```
5. 按 “**i**” 或 “**Insert**” 切换至编辑模式，在 `export PATH USER ...` 后另起一行，根据您实际使用的 JDK 版本添加以下内容。
```
export JAVA_HOME=/usr/java/jdk1.8.0_221（您的 JDK 版本）
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH
```
添加完成后，如下图所示：
![](https://main.qcloudimg.com/raw/a4d0466eca6c4c0ef219f571b7d165de.png)
6. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
7. 执行以下命令，读取环境变量。
```
source /etc/profile
```
7. 执行以下命令，查看 JDK 是否已经安装成功。
```
java -version
```
返回如下信息，则表示安装成功。
![](https://main.qcloudimg.com/raw/f12cfeed5d8aa15cccb9836637e9555f.png)

### 安装 Tomcat
1. 执行以下命令，下载 Tomcat 源码包，您可根据实际需求下载不同版本 Tomcat。
>?腾讯云软件源站每天从各软件源的官网同步一次软件资源，请从 [Tomcat 软件源](http://mirrors.tencent.com/apache/tomcat/) 中获取最新下载地址。
>
```
wget http://mirrors.tencent.com/apache/tomcat/tomcat-8/v8.5.46/bin/apache-tomcat-8.5.46.tar.gz
```
2. 执行以下命令，解压 Tomcat 源码包。
```
tar xzf apache-tomcat-8.5.46.tar.gz
```
3. 执行以下命令，移动并重命名解压后的源码包。
```
mv apache-tomcat-8.5.46 /usr/local/tomcat/
```
4. 执行以下命令，打开 `server.xml` 文件。
```
vim /usr/local/tomcat/conf/server.xml
```
找到 &lt;Host ... appBase="webapps"&gt;，按 “**i**” 或 “**Insert**” 切换至编辑模式，将 `appBase="webapps"` 替换为以下内容：
```
appBase="/usr/local/tomcat/webapps"
```
5. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
6. 执行以下命令，新建 `setenv.sh` 文件。
```
vi /usr/local/tomcat/bin/setenv.sh
```
7. 按 “**i**” 或 “**Insert**” 切换至编辑模式，输入以下内容，设置 JVM 的内存参数。
```
JAVA_OPTS='-Djava.security.egd=file:/dev/./urandom -server -Xms256m -Xmx496m -Dfile.encoding=UTF-8' 
```
8. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
9. 执行以下命令，启动 Tomcat。
```
/usr/local/tomcat/bin/startup.sh
```
显示结果如下，则成功启动。
![](https://main.qcloudimg.com/raw/64bdd25e734db46464655f15acae4c2f.png)

### 环境配置验证
1. 执行以下命令，创建测试文件。
```
echo Hello World! > /usr/local/tomcat/webapps/ROOT/index.jsp
```
2. 在浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP：8080
```
显示结果如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/359b7119e9e7d81e2e2728dabd57456a.png)
