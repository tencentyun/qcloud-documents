自行部署适用于想将腾讯云 Wafer SDK 和 Demo 部署在自己的服务器上以获得更高的灵活性和操纵权限的用户。部署过程需要从 0 开始搭建线上环境，需要有一定的 Linux、Node.js 基础。如果您符合以上需求和条件，可以开始按本文自行部署。

本文基于以下环境：

- [腾讯云 CVM（云服务器）](https://cloud.tencent.com/product/cvm)：CentOS 7.3 64位

  ###### 如果系统不是 CentOS，以下操作只是包管理工具不同，例如 Ubuntu 则是 `apt-get` 等。

- [腾讯云 CDB（云数据库）](https://cloud.tencent.com/product/cdb)：MySQL 5.7

  ###### Wafer SDK 的数据库仅支持 5.7 及以上版本的 MySQL。为了生产环境的稳定，采用云数据库而非自行搭建。

  ###### 云服务器和云数据库必须在同一个腾讯云账号下，否则内网 IP 无法连通。

### 安装 Nginx

Node.js 是单进程的，我们可以通过多开 Node.js 并配合 Nginx 来实现多进程 Node.js 负载均衡，并且一些静态文件我们也可以直接通过 Nginx 代理，提高性能。其中第一步就是安装 Nginx。

通过 SSH 连接上云服务器，直接使用包管理工具 `yum` 安装 Nginx 即可：

```bash
yum -y install nginx
```

安装完成之后会显示 `Complete!`，可以通过如下命令检查 Nginx 是否安装成功：

```bash
nginx -v
```

这个命令会显示 Nginx 的版本号，如果显示如下信息，则安装成功：

<img width="253" alt="nginx" src="https://user-images.githubusercontent.com/3380894/29501809-e0dcde82-865d-11e7-9e94-16ca213439b8.png">

### 安装 Node.js

Wafer 的 Demo 需要 7.6 以上版本的 Node.js 才能运行，目前最新版本为 8.x，`yum` 本身不提供 Node.js 的源，所以首先我们得切换源：

```bash
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
```

接着就可以直接通过 `yum` 安装了：

```bash
yum -y install nodejs
```

同理，我们可以通过如下命令验证 Node.js 是否安装成功：

```bash
node -v
```

该命令会返回当前 Node.js 的版本号，如果你看到了版本号大于 7.6，则 Node.js 安装成功：

<img width="248" alt="node" src="https://user-images.githubusercontent.com/3380894/29501810-e110fa32-865d-11e7-8916-772986a7bacb.png">

### 开启 SFTP

SFTP 是一种安全的文件传输协议，我们可以通过 SFTP 把本地的文件上传到服务器上，通过以下命令检查 sftp 状态：

```bash
service sshd status
```

看到输出的信息中有 `active (running)` 则表示 `sshd` 进程已经开启，可以通过 sftp 连接：

<img width="570" alt="sshd" src="https://user-images.githubusercontent.com/3380894/29502647-196e5608-8664-11e7-9331-d172d6675d09.png">

接下来可以通过 FileZilla、Transmit 等 FTP 工具连接上服务器。

### 配置 Nginx 和 HTTPS

完成以上准备工作，就要开始配置 Nginx 和 HTTPS 了，首先需要申请一个 SSL 证书，可以到腾讯云[申请免费的 SSL 证书](https://console.cloud.tencent.com/ssl?apply=1)，申请成功之后下载证书，并把压缩包中 Nginx 目录下的证书文件通过 SFTP 上传到服务器的 `/data/release/nginx` 目录，如果没有这个目录则新建：

<img width="476" alt="ssl" src="https://user-images.githubusercontent.com/3380894/29503005-dc1cc412-8666-11e7-8dd3-29052d02554b.png">

上传完证书以后，可以开始配置 Nginx，进入服务器的 `/etc/nginx/conf.d` 目录，新建一个 `weapp.conf` 文件，将文件拷贝到本地，打开编辑，写入如下配置（请将配置里 `wx.ijason.cc` 修改为你自己的域名，包括证书文件）：

```nginx
upstream app_weapp {
    server localhost:5757;
    keepalive 8;
}

server {
    listen      80;
    server_name wx.ijason.cc;

    rewrite ^(.*)$ https://$server_name$1 permanent;
}

server {
    listen      443;
    server_name wx.ijason.cc;

    ssl on;

    ssl_certificate           /data/release/nginx/1_wx.ijason.cc_bundle.crt;
    ssl_certificate_key       /data/release/nginx/2_wx.ijason.cc.key;
    ssl_session_timeout       5m;
    ssl_protocols             TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers               ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA;
    ssl_session_cache         shared:SSL:50m;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://app_weapp;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

修改完将这个文件上传到服务器上，然后在 ssh 中输入：

```bash
nginx -t
```

如果显示如下信息，则配置成功：

<img width="474" alt="nginx-t" src="https://user-images.githubusercontent.com/3380894/29503573-46cfc9d6-866b-11e7-991f-35811dc431c7.png">

配置成功之后，输入 `nginx` 回车，即可启动 Nginx。

此时通过配置的域名访问服务器，会显示 Nginx 详情页：

<img width="1439" alt="chrome1" src="https://user-images.githubusercontent.com/3380894/29503634-02a94754-866c-11e7-9d03-336bae5a90b7.png">

如果访问 `http://你的域名/weapp/a` 会自动跳转到 HTTPS 上，并显示 `502 Bad Gateway`，则表示配置成功：

<img width="1439" alt="chrome2" src="https://user-images.githubusercontent.com/3380894/29503675-67beaaee-866c-11e7-8b29-6a2938329278.png">

### 上传 Demo 和启动

到 [wafer2-quickstart](https://github.com/tencentyun/wafer2-quickstart) 仓库下载最新的 Demo 代码，修改 `server/config.js`：

```javascript
const CONF = {
    port: '5757',
    rootPathname: '',

    // 微信小程序 App ID
    appId: '',

    // 微信小程序 App Secret
    appSecret: '',

    // 是否使用腾讯云代理登录小程序
    useQcloudLogin: true,

    /**
     * MySQL 配置，用来存储 session 和用户信息
     * 若使用了腾讯云微信小程序解决方案
     * 开发环境下，MySQL 的初始密码为您的微信小程序 appid
     */
    mysql: {
        host: '云数据库内网IP',
        port: 3306,
        user: 'root',
        db: 'cAuth',
        pass: '云数据库密码',
        char: 'utf8mb4'
    },

    cos: {
        /**
         * 区域
         * 华北：cn-north
         * 华东：cn-east
         * 华南：cn-south
         * 西南：cn-southwest
         * 新加坡：sg
         * @see https://cloud.tencent.com/document/product/436/6224
         */
        region: 'cn-south',
        // Bucket 名称
        fileBucket: 'qcloudtest',
        // 文件夹
        uploadFolder: ''
    },

    // 微信登录态有效期
    wxLoginExpires: 7200,
  
    // 其他配置 ...
    serverHost: '你的域名',
    tunnelServerUrl: 'http://tunnel.ws.qcloud.la',
    tunnelSignatureKey: '27fb7d1c161b7ca52d73cce0f1d833f9f5b5ec89',
  	// 腾讯云相关配置可以查看云 API 密钥控制台：https://console.cloud.tencent.com/capi
    qcloudAppId: '你的腾讯云 AppID',
    qcloudSecretId: '你的腾讯云 SecretId',
    qcloudSecretKey: '你的腾讯云 SecretKey',
    wxMessageToken: 'weixinmsgtoken',
    networkTimeout: 30000
}

module.exports = CONF
```

接着将 `server` 目录下的所有文件都上传到 `/data/release/weapp` 目录下：

<img width="378" alt="server" src="https://user-images.githubusercontent.com/3380894/29507314-1bc9cc52-8682-11e7-8820-c8bb9bead907.png">

使用 SSH 切换到代码目录：

<img width="422" alt="cd" src="https://user-images.githubusercontent.com/3380894/29507384-65b91426-8682-11e7-8efc-157fc6124b7e.png">

输入以下命令切换 `npm` 源到腾讯云镜像，防止官方镜像下载失败：

```bash
npm config set registry http://mirrors.tencentyun.com/npm/
```

接着安装全局依赖：

```bash
npm install -g pm2
```

然后安装本地依赖：

```bash
npm install
```

接着对数据库进行初始化，进入[云数据库](https://console.cloud.tencent.com/cdb)控制台，点击要使用的云数据库进去，再点击右上角“登录数据库”按钮。在弹出的页面中输入数据库账号密码进入数据库管理控制台，点击菜单栏的“返回 PMA”，在界面中点击左侧栏中的“新建”，输入数据库名为 `cAuth`，排序规则为 `utf8mb4_unicode_ci`，点击“创建”创建数据库：

<img width="1192" alt="pma" src="https://user-images.githubusercontent.com/3380894/29507971-27c68e8e-8685-11e7-91f3-bf384fc6b545.png">

接着返回 SSH，使用 Demo 代码里的 `tools/initdb.js` 工具初始化数据库：

```bash
node tools/initdb.js
```

初始化成功则会提示“数据库初始化成功！”

接着执行如下代码启动 Node.js

```bash
node app.js
```

### 完成

顺利完成以上操作，就完成了 Wafer Demo 在自己服务器上的部署。直接访问 `http://你的域名/weapp/login`，会提示：

```json
{"code":-1,"error":"ERR_HEADER_MISSED"}
```

则表示配置成功。你现在可以使用开发者工具来进行联调测试啦！
