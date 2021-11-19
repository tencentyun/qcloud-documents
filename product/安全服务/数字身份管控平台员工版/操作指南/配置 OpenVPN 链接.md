## 操作场景
OpenVPN 应用是使用 IAM 系统中的用户，来控制 OpenVPN 客户端的访问。底层是基于 radius 协议来实现的。具体流程如下:
![](https://main.qcloudimg.com/raw/92ccbd022737e390692021cda3bdc0db.png)

在 OpenVPN 客户端中输入 IAM 系统的用户名和密码，经过 OpenVPN 服务端，OpenVPN 服务端通过 radius 协议访问部署的 radius-server 服务，radis-server 携带用户名和密码去 IAM 进行认证并且返回认证结果。
>?OpenVPN 服务端需要安装 openvpn-radiusplugin 插件。

## 操作步骤
### 步骤1：IAM 侧配置
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam)，在左侧导航栏，单击【应用管理】。
2. 在应用管理页面，单击【应用市场新建】。
![](https://main.qcloudimg.com/raw/5df0ba019d711dbc3f0a47f71e9d4049.png)
3. 在应用市场新建页面，选择 OpenVPN 应用，单击【下一步：编辑应用信息】。
![](https://main.qcloudimg.com/raw/505fd604a5d368e03669ca5a936807d9.png)
4. 在应用市场新建页面，根据需求配置相关信息，单击【下一步：完成】。
![](https://main.qcloudimg.com/raw/8d0ae2eeb43eb04f3e6632a98d29801c.png)
5. 在应用管理页面，单击刚刚创建的“OpenVPN 应用名称” 。
![](https://main.qcloudimg.com/raw/4668235f0f5acf0196524df0d9af4c0c.png)
6. 在应用信息页面，单击【配置文件下载】，下载 radius-server 程序，并将该文件进行解压。
![](https://main.qcloudimg.com/raw/99fbb075e98aee046c592f4adf59b9e9.png)

### 步骤2：radius-server 安装与配置
#### 安装 Java 环境
1. 通过浏览器，下载 [jdk 11](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)。
2. 在命令提示符窗口中，输入如下指令，安装 jdk。
```
$ cd /user/local
$ tar -zxvf jdk-11.0.11_linux-x64_bin.tar.gz
```
3.  依次输入如下指令，配置 JAVA_HOME 环境变量。
```
$ vim /etc/profile
```
```
export JAVA_HOME=/usr/local/jdk-11.0.11
export PATH=$JAVA_HOME/bin:$PATH
```
```
$ source /etc/profile //配置文件立即生效
```
#### 修改启动脚本参数
默认的 exec.sh 脚本使用的是8080端口，shared 是随机参数的。如果需要改动，可以编辑 exec.sh 进行修改。
#### 启动脚本
执行 exe.sh 启动脚本。
 
