## 操作场景
RabbitMQ 是实现了高级消息队列协议（Advanced Message Queuing Protocol，AMQP）的开源消息代理软件。服务器端使用 Erlang 语言编写，支持 Python、Ruby、.NET、Java、JMS、C、PHP、ActionScript、XMPP、STOMP 及 AJAX 等多种客户端。具备易用性、扩展性及高可用性等优势，您可参考本文在腾讯云云服务器上部署 RabbitMQ。

## 示例版本
本文在示例步骤中的软件版本及组成如下：
- Linux：Linux 操作系统，本文以 CentOS 7.7 为例。
- RabbitMQ Server：开源消息代理软件，本文以 RabbitMQ Server 3.6.9 为例。
- Erlang：编程语言，本文以 Erlang 19.3 为例。


## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
- Linux 实例已配置安全组规则：放通80、5672及15672端口。具体步骤请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

## 操作步骤
### 安装 Erlang
1. [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。您也可以根据实际操作习惯，选择其他不同的登录方式：
	- [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699)
	- [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700)
2. 执行以下命令，安装依赖包。
```
yum -y install make gcc gcc-c++ m4 ncurses-devel openssl-devel unixODBC-devel
```
3. 执行以下命令，下载 Erlang 安装包。
```
wget http://erlang.org/download/otp_src_19.3.tar.gz
```
4. 执行以下命令，解压 Erlang 安装包。
```
tar xzf otp_src_19.3.tar.gz
```
5. 执行以下命令，创建 erlang 文件夹。
```
mkdir /usr/local/erlang
```
6. 依次执行以下命令，编译安装 Erlang。
```
cd otp_src_19.3
```
```
./configure --prefix=/usr/local/erlang --without-javac
```
```
make && make install
```
7. 执行以下命令，打开 profile 配置文件。
```
vi /etc/profile
```
8. 按 **i** 进入编辑模式，并在文件末尾输入以下内容。
```
export PATH=$PATH:/usr/local/erlang/bin
```
9. 按 **Esc** 并输入 **:wq** 保存文件并退出。
10. 执行以下命令，使环境变量立即生效。
```
source /etc/profile
```

### 安装 RabbitMQ Server
1. 执行以下命令，下载 RabbitMQ Server 安装包。
```
wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_9/rabbitmq-server-3.6.9-1.el7.noarch.rpm
```
本文以 RabbitMQ 3.6.9 版本为例，且使用 RabbitMQ 官网提供的下载地址，若出现下载链接失效等错误或需要其他 RabbitMQ 版本时，可前往 [rabbitmq-server](https://github.com/rabbitmq/rabbitmq-server/releases) 获取更多安装信息。
10. 执行以下命令，导入签名密钥。
```
rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
```
11. 依次执行以下命令，安装 RabbitMQ Server。
```
cd
```
```
yum install rabbitmq-server-3.6.9-1.el7.noarch.rpm
```
12. 依次执行以下命令，设置 RabbitMQ 开机自启动并启动 RabbitMQ。
```
systemctl enable rabbitmq-server
```
```
systemctl start rabbitmq-server
```
13. 执行以下命令，删除 RabbitMQ 默认帐户 guest。
```
rabbitmqctl delete_user guest
```
14. <span id="Step6"></span>执行以下命令，创建新用户。
```
rabbitmqctl add_user 用户名 密码
```
15. 执行以下命令，将新用户设置为管理员帐户。
```
rabbitmqctl set_user_tags 用户名 administrator
```
16. 执行以下命令，赋予管理员帐户所有权限。
```
rabbitmqctl set_permissions -p / 用户名 ".*" ".*" ".*"
```


### 验证安装
1. 执行以下命令，启动 RabbitMQ 的 Web 管理界面。
```
rabbitmq-plugins enable rabbitmq_management
```
2. 使用浏览器访问如下地址：
```
http://实例公网 IP:15672
```
如何获取实例公网 IP，请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
显示界面如下图所示，则说明 RabbitMQ Server 安装成功。
![](https://main.qcloudimg.com/raw/aacb15db11b5cf80dd6b7ba1dc80d331.png)
3. 使用 [步骤6](#Step6) 中创建的管理员用户进行登录，即可进入 RabbitMQ 管理界面。如下图所示：
![](https://main.qcloudimg.com/raw/7f8d24062541be6ba8b271483343b20a.png)

