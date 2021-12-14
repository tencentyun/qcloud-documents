## 操作场景
本文档介绍如何在 Linux 操作系统的腾讯云云服务器（CVM）上手动搭建 Java Web 环境。

进行手动搭建 Java Web 环境，您需要熟悉 Linux 命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件使用、配置和兼容性比较了解。
>!腾讯云建议您可以通过云市场的镜像环境部署 Java Web 环境，手动搭建 Java Web 环境可能需要较长的时间。具体步骤可参考 [镜像部署 Java Web 环境](https://cloud.tencent.com/document/product/213/38096)。

## 示例软件版本
本文搭建的 Java Web 环境组成版本及说明如下：
- Linux：Linux 操作系统，本文以 CentOS 7.6 为例。
- Apache Tomcat：Web 应用服务器，本文以 Apache Tomcat 8.5.55 为例。
- JDK：Java 开发工具包，本文以 JDK 1.8.0_221 为例。


## 前提条件
已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。

## 操作步骤
### 步骤1：登录 Linux 实例
[使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)


### 步骤2：安装 JDK
1. 下载 JDK 源码包，您可前往 [Java SE 下载](https://www.oracle.com/technetwork/java/javase/downloads/index.html) 页面选择需要的版本。
>?请先将 JDK 源码包下载到本地，再上传至云服务器，否则会出现解压错误。
> - 若您使用机器为 Windows 操作系统，可通过 [WinSCP 上传文件](https://cloud.tencent.com/document/product/213/2131)。
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
5. 按 **i** 切换至编辑模式，在 `export PATH USER ...` 后另起一行，根据您实际使用的 JDK 版本添加以下内容。
```
export JAVA_HOME=/usr/java/jdk1.8.0_221（您的 JDK 版本）
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH
```
添加完成后，如下图所示：
![](https://main.qcloudimg.com/raw/a4d0466eca6c4c0ef219f571b7d165de.png)
6. 按 **Esc**，输入 **:wq**，保存文件并返回。
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

### 步骤3：安装 Tomcat
1. 执行以下命令，下载 Tomcat 源码包，您可根据实际需求下载不同版本 Tomcat。
>?本文使用 Apache 官网提供下载网址，若出现下载链接失效等错误或需要其他 Tomcat 版本时，可前往 [Apache 官网](https://tomcat.apache.org/) 获取更多安装信息。
>
```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-8/v8.5.55/bin/apache-tomcat-8.5.55.tar.gz
```
2. 执行以下命令，解压 Tomcat 源码包。
```
tar xzf apache-tomcat-8.5.55.tar.gz
```
3. 执行以下命令，将解压后的文件夹下的文件移动到 `/usr/local/tomcat/` 目录下。
```
mv apache-tomcat-8.5.55 /usr/local/tomcat/
```
4. 执行以下命令，打开 `server.xml` 文件。
```
vim /usr/local/tomcat/conf/server.xml
```
5. 找到 `<Host ... appBase="webapps">`，按 **i** 切换至编辑模式，将 `appBase="webapps"` 替换为以下内容：
```
appBase="/usr/local/tomcat/webapps"
```
6. 按 **Esc**，输入 **:wq**，保存文件并返回。
7. 执行以下命令，新建 `setenv.sh` 文件。
```
vi /usr/local/tomcat/bin/setenv.sh
```
8. 按 **i** 切换至编辑模式，输入以下内容，设置 JVM 的内存参数。
```
JAVA_OPTS='-Djava.security.egd=file:/dev/./urandom -server -Xms256m -Xmx496m -Dfile.encoding=UTF-8' 
```
9. 按 **Esc**，输入 **:wq**，保存文件并返回。
10. 执行以下命令，启动 Tomcat。
```
/usr/local/tomcat/bin/startup.sh
```
显示结果如下，则成功启动。
![](https://main.qcloudimg.com/raw/64bdd25e734db46464655f15acae4c2f.png)

## 验证环境配置
1. 执行以下命令，创建测试文件。
```
echo Hello World! > /usr/local/tomcat/webapps/ROOT/index.jsp
```
2. 在本地浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP：8080
```
显示结果如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/359b7119e9e7d81e2e2728dabd57456a.png)

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。
