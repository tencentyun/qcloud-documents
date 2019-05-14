JDK 是 Java 软件开发工具包，本文以 JDK 1.7 和 1.8 版本为例，分别介绍了 Windows 和 Linux 系统下 JDK 的安装与环境配置过程。

## Windows
### 1.下载 JDK
进入 [Oracle 官方网站](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) 下载合适的 JDK 版本，准备安装。
### 2. 安装
根据提示一步步安装，安装过程中可以自定义安装目录(默认安装到 C 盘)，例如我们选择的安装目录为：
`D:\Program Files\Java\jdk1.8.0_31`
`D:\Program Files\Java\jre1.8.0_31`
![本地同步工具1](//mc.qcloudimg.com/static/img/0652f9759c4f7fa7e61aa406ca1ad822/image.png)
### 3. 配置
安装完成后，右键单击【计算机】> 单击【属性】>【高级系统设置】>【环境变量】>【系统变量】>【新建】，分别配置软件。
变量名(N)：**JAVA_HOME**   
变量值(V)：D:\Program Files\Java\jdk1.8.0_31    *// 请根据自己的实际安装路径配置*
![本地同步工具2](//mc.qcloudimg.com/static/img/f02f0ec6b87576f32fbade9cd8d55c1e/image.png)
变量名(N)：**CLASSPATH**   
变量值(V)：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;        *//注意变量值开头有"."*
![本地同步工具3](//mc.qcloudimg.com/static/img/d2c87f5ce4c2927f5e9ca9d20e4478d6/image.png)
变量名(N)：**Path**
变量值(V)：%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;
![本地同步工具4](//mc.qcloudimg.com/static/img/5ee8cc105d52f9052cc49251ce88ed9a/image.png)
### 4. 测试
测试配置是否成功：【开始】（或快捷键：Win+R）>【运行】（输入 `cmd`）>【确定】（或按 Enter 键），输入命令 `javac` 并回车。出现如下图所示信息，则说明环境变量配置成功。
![本地同步工具5](//mc.qcloudimg.com/static/img/83f8417d6f540c20182267acba29f2ad/image.png)
## Linux
由于使用 yum 或者 apt-get 命令 安装 openjdk 可能存在类库不全，从而导致用户在安装后运行相关工具时可能报错的问题，所以此处我们推荐采用手动解压安装的方式来安装 JDK。具体步骤如下：
### 1. 创建目录 
在`/usr/`目录下创建`java`目录
```
mkdir /usr/java
cd /usr/java 
```
### 2. 下载并解压 JDK
```
curl -O http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz
tar -zxvf jdk-7u79-linux-x64.tar.gz 
```
### 3. 设置环境变量
```
vi /etc/profile 
```
在打开的 profile 文件中添加如下内容：
```
set java environment
JAVA_HOME=/usr/java/jdk1.7.0_79
JRE_HOME=/usr/java/jdk1.7.0_79/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH PATH 
```
让修改生效：
```
source /etc/profile 
```
### 4. 测试
```
java -version
```
显示如下信息，则说明配置成功：
```
java version "1.7.0_79" Java(TM) SE Runtime Environment (build 1.7.0_79-b15) Java HotSpot(TM) 64-Bit Server VM (build 24.79-b02, mixed mode) 
```
