## 1. 本地Windows机器使用密钥登录Linux云服务器
### 1.1. 创建SSH密钥、下载私钥并绑定Linux云服务器
![](//mccdn.qcloud.com/img56a5d553bddcf.png)

登录[腾讯云控制台](https://console.qcloud.com)，点击【云服务器】-【SSH密钥】进入密钥窗口。点击【创建密钥】按钮，输入密钥名创建一个新密钥。创建完密钥后，点击【下载】按钮，下载私钥。

然后右键选择刚创建的密钥ID，选择绑定需要登录的Linux服务器进行绑定。

### 1.2. 使用Putty登录
#### 1.2.1. 客户端下载
进入http://www.putty.nl/download.html ，分别下载putty.exe及puttygen.exe两个文件。

#### 1.2.2. 密钥格式转换
打开puttygen.exe，点击“Load”按钮，在弹窗中首先进入您存放密钥的路径，然后选择“All File（\*.\*）”，选择某个私钥（例子中为文件david，david是密钥的名称），点击“打开”。

![](//mccdn.qcloud.com/img56a5c48fb810a.png)

在key comment栏中输入密钥名，输入加密私钥的密码（可选），点击“Save private key”，在弹窗中选择您存放密钥的目录，然后在文件名栏输入密钥名+".ppk"，点击“保存”按钮。
![](//mccdn.qcloud.com/img56a5c4ff657cc.png)

#### 1.2.3. 登录远程Linux云服务器
打开putty.exe，进入”Auth“配置。

![](//mccdn.qcloud.com/img56a5c61c61e42.png)

点击“Browse”按钮，打开弹窗后进入密钥存储的路径，并选择密钥，点击“打开”，返回配置界面，进入“Session”配置。
![](//mccdn.qcloud.com/img56a5c67ea3edb.png)

在Session配置页中，配置服务器的IP，端口，连接类型。
- IP：云服务器的公网IP。登录[腾讯云控制台云服务器页面](https://console.qcloud.com/cvm)，可在列表页及详情页中获取主机公网IP。
- 端口：云服务器的端口，必须填22。（请确保云主机22端口已开放，详见查看[安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)及网络ACL）
- 连接类型：选择SSH。

在“Saved Sessions”输入框中中输入会话名称（本例为test），再点击“Save”按钮，然后双击会话名称或者点击“Open”按钮发起登录请求。
![](//mccdn.qcloud.com/img56a5c6bca781f.png)


### 1.3. 使用SecureCRT登录
#### 1.3.1. 复制公钥
登录[腾讯云控制台](https://console.qcloud.com)，点击【云服务器】-【SSH密钥】进入密钥窗口。点击您绑定了Linux云服务器的SSH密钥ID，进入密钥详情页，复制公钥信息。

![](//mccdn.qcloud.com/img56a5c9c132dc8.png)

将公钥内容粘贴到空白文本中，并保存文本名为密钥名.pub（图中例子为test.pub），将公钥文件保存在私钥文件（本例中私钥名为test）所在的文件夹下。

>注：私钥和公钥要相同的文件名，本例中公钥名为test.pub，那么私钥名必须为test。 

#### 1.3.2. 配置并连接服务器
打开secureCRT，点击快速连接，配置登录主机名称/IP、端口、系统管理员用户名。

- Protocol：协议类型。选择SSH2。
- Hostname：云服务器的公网IP。登录[腾讯云控制台云服务器页面](https://console.qcloud.com/cvm)，可在列表页及详情页中获取主机公网IP。
- Port：云服务器的端口，必须填22。（请确保云主机22端口已开放，详见查看[安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)及网络ACL）
- Username： 管理员账号
服务器的操作系统不同，管理员帐号也会不一样，如下所示：
SUSE/CentOS/Debian：root
Windows：Administrator
ubuntu：ubuntu 

之后再将登录认证协议按照图中所示进行配置，最后点击“Properties”按钮，进入公钥配置页面。

![](//mccdn.qcloud.com/img56a5cbb542b7d.png)

在公钥配置页面点击图中按钮选择公钥文件（test.pub）并点击“open”按钮，然后点击“ok”按钮确认公钥配置完成。
![](//mccdn.qcloud.com/img56a5ccf6807c7.png)

配置完成后，点击”Connect“按钮连接服务器。

## 2. 本地Linux/Mac OS X系统机器使用密钥登录Linux云服务器
### 2.1. 创建SSH密钥、下载私钥并绑定Linux云服务器
![](//mccdn.qcloud.com/img56a5d553bddcf.png)

登录[腾讯云控制台](https://console.qcloud.com)，点击【云服务器】-【SSH密钥】进入密钥窗口。点击【创建密钥】按钮，输入密钥名创建一个新密钥。创建完密钥后，点击【下载】按钮，下载私钥。

然后右键选择刚创建的密钥ID，选择绑定需要登录的Linux服务器进行绑定。


### 2.2. 使用下载的密钥文件登录
1) 打开SSH客户端（Mac可使用系统自带的终端）。 
2) 查找您的私有密钥文件 ([云服务器关联的密钥文件])。 
3) 您的密钥必须不公开可见，SSH才能工作。请使用此命令：
```
chmod 400 [云服务器关联的密钥文件]的绝对路径。 
```
4) 输入命令：
```
ssh -i "[云服务器关联的密钥文件]的绝对路径" [云服务器登录账号]@[云服务器公网IP]。
```
例如：
```
ssh -i "Mac/Downloads/shawn_qcloud_stable" ubuntu@119.xxx.xxx.xxx
```
上边内容，其中`[]`内，需要根据cvm系统情况，实际判断：
`[云服务器登录账号]`：其他Linux为root，ubuntu账号为 ubuntu；
