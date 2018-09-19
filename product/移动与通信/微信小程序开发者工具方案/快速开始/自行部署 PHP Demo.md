自行部署适用于想将腾讯云 Wafer SDK 和 Demo 部署在自己的服务器上以获得更高的灵活性和操纵权限的用户。部署过程需要从零开始搭建线上环境，需要有一定的 Linux、PHP 基础。如果您符合以上需求和条件，可以开始按本文自行部署。

本文基于以下环境：

- [腾讯云 CVM（云服务器）](https://cloud.tencent.com/product/cvm)：CentOS 7.3 64位

  **如果系统不是 CentOS，以下操作只是包管理工具不同，例如 Ubuntu 则是 `apt-get` 等。**

- [腾讯云 CDB（云数据库）](https://cloud.tencent.com/product/cdb)：MySQL 5.7

  **Wafer SDK 的数据库仅支持 5.7 及以上版本的 MySQL。为了生产环境的稳定，采用云数据库而非自行搭建。**

  **云服务器和云数据库必须在同一个腾讯云账号下，否则内网 IP 无法连通。**

## 安装 Nginx

PHP-FPM 依赖于 Nginx 进行请求的派发与响应，并且一些静态文件我们也可以直接通过 Nginx 代理，提高性能。其中第一步就是安装 Nginx。

通过 SSH 连接上云服务器，直接使用包管理工具 `yum` 安装 Nginx 即可：

```bash
yum -y install nginx
```

安装完成之后会显示 `Complete!`，可以通过如下命令检查 Nginx 是否安装成功：

```bash
nginx -v
```

这个命令会显示 Nginx 的版本号，如果显示如下信息，则安装成功：

<img width="253" alt="nginx" src="https://mc.qcloudimg.com/static/img/fd6021afc2d8599604e46273ca9c194f/nginx.png">

## 安装 PHP

Wafer 的 Demo 需要 5.6 以上版本的 PHP 才能运行，目前最新版本为 7.x，`yum` 本身不提供 PHP 的源，所以首先我们得添加 remi 源：

```bash
wget 'https://mirrors.tuna.tsinghua.edu.cn/remi/enterprise/remi.repo' -O /etc/yum.repos.d/remi.repo
```

接着就可以直接通过 `yum` 安装了：

```bash
yum install --enablerepo=remi --enablerepo=remi-php56 php php-mbstring php-mcrypt php-mysql php-curl php-fpm
```

同理，我们可以通过如下命令验证 PHP 是否安装成功：

```bash
php -v
```

该命令会返回当前 PHP 的版本号，如果你看到了版本号大于 5.6，则 PHP 安装成功：

<img width="437" alt="node" src="https://mc.qcloudimg.com/static/img/644dde0092226c2748d5cb1eecca9984/php-v.png">

## 开启 SFTP

SFTP 是一种安全的文件传输协议，我们可以通过 SFTP 把本地的文件上传到服务器上，通过以下命令检查 sftp 状态：

```bash
service sshd status
```

看到输出的信息中有 `active (running)` 则表示 `sshd` 进程已经开启，可以通过 sftp 连接：

<img width="570" alt="sshd" src="https://mc.qcloudimg.com/static/img/8b329ba974d6e7899fccdb606a8c6c88/sftp.png">

接下来可以通过 FileZilla、Transmit 等 FTP 工具连接上服务器。

## 配置 Nginx 和 HTTPS

完成以上准备工作，就要开始配置 Nginx 和 HTTPS 了，首先需要申请一个 SSL 证书，可以到腾讯云[申请免费的 SSL 证书](https://console.cloud.tencent.com/ssl?apply=1)，申请成功之后下载证书，并把压缩包中 Nginx 目录下的证书文件通过 SFTP 上传到服务器的 `/data/release/nginx` 目录，如果没有这个目录则新建：

<img width="409" alt="ssl" src="https://mc.qcloudimg.com/static/img/fa4cba0bc508457040ff0ccf5052ba21/WX20171128-121407%402x.png">

上传完证书以后，可以开始配置 Nginx，进入服务器的 `/etc/nginx/conf.d` 目录，新建一个 `weapp.conf` 文件，将文件拷贝到本地，打开编辑，写入如下配置（请将配置里 `wx.wafersolution.com` 修改为你自己的域名，包括证书文件名）：

> 请提前将域名解析到服务器的 IP 上

```nginx
# 重定向 http 到 https
server {
    listen      80;
    server_name wx.wafersolution.com;

    rewrite ^(.*)$ https://$server_name$1 permanent;
}

server {
    listen      443;
    server_name wx.wafersolution.com;

    ssl on;

    ssl_certificate           /data/release/nginx/1_wx.wafersolution.com_bundle.crt;
    ssl_certificate_key       /data/release/nginx/2_wx.wafersolution.com.key;
    ssl_session_timeout       5m;
    ssl_protocols             TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers               ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA;
    ssl_session_cache         shared:SSL:50m;
    ssl_prefer_server_ciphers on;
  
  	root  /data/release/php-demo;

    location ~ \.php$ {
        root           /data/release/php-demo;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }

    location /weapp/ {
        root   /data/release/php-demo;
        index  index.html index.htm index.php;
    	try_files $uri $uri/ /index.php;
    }
}
```

修改完将这个文件上传到服务器上，然后在 ssh 中输入：

```bash
nginx -t
```

如果显示如下信息，则配置成功：

<img width="474" alt="nginx-t" src="https://mc.qcloudimg.com/static/img/17703dd9b8e47a349ab77c0d29531d06/nginx-t.png">

配置成功之后，输入 `nginx` 回车，即可启动 Nginx。

此时通过配置的域名访问服务器，会显示 `404 Not Found`，则表示配置成功：

<img width="1439" alt="chrome2" src="https://mc.qcloudimg.com/static/img/5e4c1a05191ff1655d223831ed1dc0bc/visit.png">

## 上传 Demo 和启动

到 [wafer2-quickstart-php](https://github.com/tencentyun/wafer2-quickstart-php) 仓库下载最新的 Demo 代码，修改 `server/config.php`：

```javascript
<?php
/**
 * Wafer php demo 配置文件
 */

$config = [
    'rootPath' => '',

    // 微信小程序 AppID
    'appId' => '',

    // 微信小程序 AppSecret
    'appSecret' => '',

    // 使用腾讯云代理登录
    'useQcloudLogin' => true,

    /**
     * 这里请填写云数据库的
     */
    'mysql' => [
        'host' => '云数据库内网IP',
        'port' => 3306,
        'user' => 'root',
        'db'   => 'cAuth',
        'pass' => '云数据库密码',
        'char' => 'utf8mb4'
    ],

    'cos' => [
        /**
         * 区域
         * 上海：cn-east
         * 广州：cn-sorth
         * 北京：cn-north
         * 广州二区：cn-south-2
         * 成都：cn-southwest
         * 新加坡：sg
         * @see https://cloud.tencent.com/document/product/436/6224
         */
        'region' => 'cn-sorth',
        // Bucket 名称
        'fileBucket' => 'wafer',
        // 文件夹
        'uploadFolder' => ''
    ],

    // 微信登录态有效期
    'wxLoginExpires' => 7200,
    'wxMessageToken' => 'abcdefgh',

    // 其他配置
    'serverHost' => 'wx.wafersolution.com',
    'tunnelServerUrl' => 'http://tunnel.ws.qcloud.la',
    'tunnelSignatureKey' => '27fb7d1c161b7ca52d73cce0f1d833f9f5b5ec89',
  	// 腾讯云相关配置可以查看云 API 密钥控制台：https://console.cloud.tencent.com/capi
    'qcloudAppId' => 1200000000,// 必须是数字
    'qcloudSecretId' => '你的腾讯云 SecretId',
    'qcloudSecretKey' => '你的腾讯云 SecretKey',
    'networkTimeout' => 30000
];
```

接着将 `server` 目录下的所有文件都上传到 `/data/release/php-demo` 目录下：

<img width="378" alt="server" src="https://user-images.githubusercontent.com/3380894/29507314-1bc9cc52-8682-11e7-8820-c8bb9bead907.png">

接着对数据库进行初始化，进入[云数据库](https://console.cloud.tencent.com/cdb)控制台，点击要使用的云数据库进去，再点击右上角【登录数据库】按钮。在弹出的页面中输入数据库账号密码进入数据库管理控制台，点击菜单栏的【返回 PMA】，在界面中点击左侧栏中的【新建】，输入数据库名为 `cAuth`，排序规则为 `utf8mb4_unicode_ci`，点击【创建】创建数据库：

<img width="1192" alt="pma" src="https://user-images.githubusercontent.com/3380894/29507971-27c68e8e-8685-11e7-91f3-bf384fc6b545.png">

接着点击左侧栏的【cAuth】数据库，再点击顶栏的【导入】，选择下载的代码中的 cAuth.sql 文件，点击【执行】即可完成导入：

<img width="1192" alt="pma" src="https://mc.qcloudimg.com/static/img/3368fdf7ab27a91faaa460f085ac95f4/sql.png">

## 启动 PHP

回到 SSH 界面，输入：

```bash
service php-fpm start
```

## 完成

顺利完成以上操作，就完成了 Wafer Demo 在自己服务器上的部署。直接访问 `http://你的域名/weapp/login`，会提示：

```json
{"code":-1,"error":"\u8bf7\u6c42\u5934\u672a\u5305\u542b x-wx-code\uff0c\u8bf7\u914d\u5408\u5ba2\u6237\u7aef SDK \u767b\u5f55\u540e\u518d\u8fdb\u884c\u8bf7\u6c42"}
```

则表示配置成功。你现在可以使用开发者工具来进行联调测试啦！
