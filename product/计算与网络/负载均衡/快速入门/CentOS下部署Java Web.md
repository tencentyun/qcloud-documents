本文将为您详细介绍如何在 CentOS 系统下部署 Java Web 项目，适用于刚开始使用腾讯云的个人用户。
## 软件版本
本文在示例步骤中的软件版本如下，在实际操作时，请您以实际软件版本为准。
- 操作系统：CentOS 7.5
- Tomcat 版本：apache-tomcat-8.5.39
- JDK 版本：JDK 1.8.0_201

## 安装JDK
购买负载均衡服务后，在云服务器的详情页面，单击**登录**，可以直接登录云服务器，输入自己的用户名密码后，开始搭建 Java Web 环境。有关如何创建云服务器实例，请参见 [云服务器-创建实例](https://cloud.tencent.com/document/product/213/4855)。

### 下载 JDK
输入如下命令：
```
mkdir /usr/java  # 创建 java 文件夹
cd /usr/java     # 进入 java 文件夹
```
<pre>
<code># 上传 JDK 安装包（推荐）
推荐您使用 <a href="https://winscp.net/eng/docs/lang:chs" target="_blank">WinSCP</a> 或其他工具将 JDK 安装包上传到上述 java 文件夹下，然后解压安装包。
或者
# 直接使用命令（推荐您使用上传 JDK 安装包的方法）： wget 下载链接，下载得到的压缩包无法解压，这是因为直接下载的压缩包默认没有接受 Oracle BSD 许可；每个人的 cookie 不一样，请前往https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html页面同意许可协议并获取带有自己 cookie 的下载链接。
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz</code>
</pre>
```
# 解压
chmod +x jdk-8u201-linux-x64.tar.gz
tar -xzvf jdk-8u201-linux-x64.tar.gz
```

### 设置环境变量
1. 打开 `/etc/profile` 文件。
```
vi /etc/profile
```
2. 按下 i 键进入编辑模式，在该文件中添加如下信息。
```
# set java environment
export JAVA_HOME=/usr/java/jdk1.8.0_201
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH
```
3. 按下 Esc 键退出编辑模式，输入`:wq`保存并关闭文件。
4. 加载环境变量。
```
source /etc/profile
```

### 查看 JDK 是否安装成功
运行`java -version`命令，显示 JDK 版本信息时，表示 JDK 已经安装成功。
![](https://main.qcloudimg.com/raw/6d3531f4d466e5428885ec38a3542c2e.png)

## 安装 Tomcat

### 下载 Tomcat
输入如下命令：
```
# 镜像地址会改变，Tomcat 版本也会不断升级。如果下载链接失效，请您到 [Tomcat 官网](https://tomcat.apache.org/download-80.cgi)选择合适的安装包地址。
wget http://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-8/v8.5.39/bin/apache-tomcat-8.5.39.tar.gz
tar -xzvf apache-tomcat-8.5.39.tar.gz
mv apache-tomcat-8.5.39 /usr/local/tomcat/
```
在`/usr/local/tomcat/`目录中包含如下文件：
- bin：脚本文件，包含启动和关闭 Tomcat 服务脚本。
- conf：各种全局配置文件，其中最重要的是 server.xml 和 web.xml。
- webapps：Tomcat 的主要 Web 发布目录，默认情况下把 Web 应用文件放于此目录。
- logs：存放 Tomcat 执行时的日志文件。

>!如果下载链接失效，请替换为 [Tomcat 官网](https://tomcat.apache.org/download-80.cgi ) 的最新下载链接。
>

### 添加用户
```
# 创建一般用户 www来运行 Tomcat
useradd www
# 创建网站根目录
mkdir -p /data/wwwroot/default
# 将需要部署的 Java Web 项目文件 WAR 包上传到网站根目录下，然后将网站根目录下文件权限改为 www。本示例将直接在网站根目录下新建一个 Tomcat 测试页面：
echo Hello Tomcat! > /data/wwwroot/default/index.jsp
chown -R www.www /data/wwwroot
```

### 设置 JVM 内存参数
1. 创建一个`/usr/local/tomcat/bin/setenv.sh`脚本文件。
```
vi /usr/local/tomcat/bin/setenv.sh
```
2. 按下 i 键进入编辑模式，添加如下内容。
```
JAVA_OPTS='-Djava.security.egd=file:/dev/./urandom -server -Xms256m -Xmx496m -Dfile.encoding=UTF-8'
```
3. 按 Esc 键退出编辑模式，输入`:wq`保存并退出编辑。

### 配置 server.xml
1. 切换到 `/usr/local/tomcat/conf/` 目录。
```
cd /usr/local/tomcat/conf/
```
2. 备份 server.xml 文件。
```
mv server.xml server_default.xml
```
3. 创建一个新的 server.xml 文件。
```
vi server.xml
```
4. 按下 i 键进入编辑模式，添加如下内容。
```
<?xml version="1.0" encoding="UTF-8"?>
<Server port="8006" shutdown="SHUTDOWN">
<Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener"/>
<Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener"/>
<Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener"/>
<Listener className="org.apache.catalina.core.AprLifecycleListener"/>
<GlobalNamingResources>
<Resource name="UserDatabase" auth="Container"
 type="org.apache.catalina.UserDatabase"
 description="User database that can be updated and saved"
 factory="org.apache.catalina.users.MemoryUserDatabaseFactory"
 pathname="conf/tomcat-users.xml"/>
</GlobalNamingResources>
<Service name="Catalina">
<Connector port="8080"
 protocol="HTTP/1.1"
 connectionTimeout="20000"
 redirectPort="8443"
 maxThreads="1000"
 minSpareThreads="20"
 acceptCount="1000"
 maxHttpHeaderSize="65536"
 debug="0"
 disableUploadTimeout="true"
 useBodyEncodingForURI="true"
 enableLookups="false"
 URIEncoding="UTF-8"/>
<Engine name="Catalina" defaultHost="localhost">
<Realm className="org.apache.catalina.realm.LockOutRealm">
<Realm className="org.apache.catalina.realm.UserDatabaseRealm"
  resourceName="UserDatabase"/>
</Realm>
<Host name="localhost" appBase="/data/wwwroot/default" unpackWARs="true" autoDeploy="true">
<Context path="" docBase="/data/wwwroot/default" debug="0" reloadable="false" crossContext="true"/>
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
prefix="localhost_access_log." suffix=".txt" pattern="%h %l %u %t &quot;%r&quot; %s %b" />
</Host>
</Engine>
</Service>
</Server>
```
5. 按 Esc 键退出编辑模式，输入`:wq`保存并退出编辑。

## 启动 Tomcat
### 方法一
进入 Tomcat 服务器的 bin 目录，然后执行`./startup.sh`命令启动 Tomcat 服务器。
```
cd /usr/local/tomcat/bin
./startup.sh
```
运行结果如下：
![](https://main.qcloudimg.com/raw/c118899986968ecd5982eb8cdb2beff9.png)
### 方法二
1. 设置快捷启动，在任何地方都可以通过 service tomcat start 来启动 Tomcat。
```
wget https://github.com/lj2007331/oneinstack/raw/master/init.d/Tomcat-init
mv Tomcat-init /etc/init.d/tomcat
chmod +x /etc/init.d/tomcat
```
2. 运行以下命令，设置启动脚本 JAVA_HOME。
```
sed -i 's@^export JAVA_HOME=.*@export JAVA_HOME=/usr/java/jdk1.8.0_201@' /etc/init.d/tomcat
```
3. 设置自启动。
```
chkconfig --add tomcat
chkconfig tomcat on
```
4. 启动 Tomcat。
```
# 启动 Tomcat
service tomcat start
# 查看 Tomcat 运行状态
service tomcat status
# 关闭 Tomcat
service tomcat stop
```
运行结果如下：
![](https://main.qcloudimg.com/raw/78800e85c09820d98a0a15dc2792aaa8.png)
5. 若提示没有权限，请切换为 root 用户并修改权限。
```
cd /usr/local
chmod -R 777 tomcat
```
6. 在浏览器地址栏中输入 `http://公网IP:端口`（端口为 server.xml 中设置的 connector port）进行访问。出现下图所示页面时表示安装成功。
![](https://main.qcloudimg.com/raw/f80eefbdc90644d0a5e8a367fbe58dce.png)

### 配置安全组
如果访问不通，请检查安全组。如上示例中 server.xml 中的 connector port 是8080，因此需在对应的云服务器所绑定的安全组上放通 TCP:8080，详情请参见 [添加安全组规则](https://cloud.tencent.com/document/product/215/39790)。
![](https://main.qcloudimg.com/raw/966d10d1b63663af4d056854a7123c33.png)
