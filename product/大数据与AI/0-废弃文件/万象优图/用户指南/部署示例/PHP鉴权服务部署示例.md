本文档介绍了腾讯云万象优图服务端php的部署和集成，搭建一个php+nginx为基础，对web端或者移动端提供http签名接口服务的例子程序。
注意：本文档只是简单的示例，展示了服务端为终端提供签名的基本示例，开发者务必根据自身业务开发相应的鉴权服务逻辑，并集成到自身服务器中。
## 1 环境准备
下面以在腾讯云云服务器CentOS 6.2 64位上安装nginx为例，简单介绍如何将腾讯云万象优图集成，对web端或者移动端提供http签名接口服务所需要的基础环境搭建。开发者可以根据自己业务的需要，构建http或者非http服务，为自身业务的web端、移动端提供签名。
### 1.1 安装nginx

```
yum install nginx –y
service nginx restart
```
### 1.2 验证nginx
直接访问云服务器ip地址，验证nginx是否已经运行起来。
## 2 安装配置PHP环境
下面介绍安装php-fpm和配置web container的详细步骤。
1 安装php-fpm

```
yum install –y php php-fpm
service php-fpm restart
```
2 配置web container
修改/etc/nginx/conf.d/default.conf如下：

```
#
# The default server
#
server {
    listen       80 default_server;
    server_name  _;
    
    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    location ~ \.php$ {
        root           /data/www/tencentyun/;
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
}
```
3 重新加载nginx配置
修改配置完成后，需要执行以下命令重新加载配置。

```
nginx -s reload
```
## 3 部署集成PHP SDK及鉴权服务器逻辑开发
将sdk集成到开发者代码，开发鉴权服务逻辑，这里给一个简单的示例：
注意: 如果开发者想按照本示例做简单地测试，需要修改sdk中Tencentyun文件夹下Conf.php中APPID、SECRET_ID、SECRET_KEY为您在万象优图对应的鉴权信息；并将下列鉴权服务逻辑代码中的相应字段信息替换为自身的项目信息。
### 3.1 使用composer方式
1 安装composer到您的项目，这里是tencentyun目录下的php

```
cd /data/www/tencentyun/php
  curl -sS https://getcomposer.org/installer | php
```
2 为php项目指定依赖关系

```
{
	"require":{
		"tencentyun/php-sdk":"2.0.*"
	}
  }
```
3 安装依赖项

```
php composer.phar install
```
4 将sdk集成到开发者代码，开发鉴权服务逻辑，这里以php目录下getsign.php为例：
注意：如果开发者想按照本示例做简单地测试，需要将下面代码中的相应字段替换为自己的项目信息，具体见注释。

```
<?php

require 'vendor/autoload.php';

if (isset($_GET['type'])) {
    $type = $_GET['type'];
} else {
    $type = 'upload';
}

//以下bucket，projectId信息请到http://console.cloud.tencent.com/image/bucket获取,并替换为自己的项目信息
$bucket = 'test0706';     // 空间名称
$projectId = '10000037';  // 项目ID
$userid = 0;              // 用户ID 可以自定义 默认为0

switch ($type) {
    case 'upload':
        $fileid = '/u/can/use/slash/sample'.time();                              // 自定义文件名
        //生成新的上传签名
        $url = Tencentyun\ImageV2::generateResUrl($bucket, $userid, $fileid);
        $expired = time() + 999;
        $sign = Tencentyun\Auth::getAppSignV2($bucket, $fileid, $expired);
        $ret = array('url' => $url,'sign' => $sign);
        exit(json_encode($ret));
    case 'stat':
        $fileid = rawurldecode($_GET['fileid']);
        $url = Tencentyun\ImageV2::generateResUrl($bucket, $userid, $fileid);
        $ret = array('url' => $url);
        exit(json_encode($ret));
    case 'del':
    case 'copy':
        $fileid = rawurldecode($_GET['fileid']);
        $url = Tencentyun\ImageV2::generateResUrl($bucket, $userid, $fileid, $type);
        $sign = Tencentyun\Auth::getAppSignV2($bucket, $fileid, 0);
        $ret = array('url' => $url,'sign' => $sign);
        exit(json_encode($ret));
    case 'download':
        $fileid = rawurldecode($_GET['fileid']);
        $expired = time() + 999;
        $sign = Tencentyun\Auth::getAppSignV2($bucket, $fileid, $expired);
        $ret = array('sign' => $sign);
        exit(json_encode($ret));
    default:
        exit;
}

//end of script
```
### 3.2 直接源码集成
1 从github下载源码到php目录下的tencentyun目录

```
git clone https://github.com/tencentyun/php-sdk.git tencentyun
```
2 将sdk集成到开发者代码，开发鉴权服务逻辑，这里以php目录下getsigninclude.php为例：
注意：如果开发者想按照本示例做简单地测试，需要将下面代码中的相应字段替换为自己的项目信息，具体见注释。

```
<?php

require 'tencentyun/include.php';

//以下bucket，projectId信息请到http://console.cloud.tencent.com/image/bucket获取,并替换为自己的项目信息
$bucket = 'test0706';     // 空间名称
$projectId = '10000037';  // 项目ID
$userid = 0;              // 用户ID 可以自定义 默认为0

switch ($type) {
    case 'upload':
        $fileid = '/u/can/use/slash/sample'.time();                              // 自定义文件名
        //生成新的上传签名
        $url = Tencentyun\ImageV2::generateResUrl($bucket, $userid, $fileid);
        $expired = time() + 999;
        $sign = Tencentyun\Auth::getAppSignV2($bucket, $fileid, $expired);
        $ret = array('url' => $url,'sign' => $sign);
        exit(json_encode($ret));
    case 'stat':
        $fileid = rawurldecode($_GET['fileid']);
        $url = Tencentyun\ImageV2::generateResUrl($bucket, $userid, $fileid);
        $ret = array('url' => $url);
        exit(json_encode($ret));
    case 'del':
    case 'copy':
        $fileid = rawurldecode($_GET['fileid']);
        $url = Tencentyun\ImageV2::generateResUrl($bucket, $userid, $fileid, $type);
        $sign = Tencentyun\Auth::getAppSignV2($bucket, $fileid, 0);
        $ret = array('url' => $url,'sign' => $sign);
        exit(json_encode($ret));
    case 'download':
        $fileid = rawurldecode($_GET['fileid']);
        $expired = time() + 999;
        $sign = Tencentyun\Auth::getAppSignV2($bucket, $fileid, $expired);
        $ret = array('sign' => $sign);
        exit(json_encode($ret));
    default:
        exit;
}

//end of script
```
## 4 测试
1. 终端通过CGI：http://203.195.194.28/php/getsignv2.php?type=[opType]&fileid=[fileid]来获取相应的签名。
   opType：可取值：upload(上传), stat（查询）, copy（复制）, del（删除）和download（下载，如果开启token防盗链）；
   fileid：是图片资源的唯一标识；当opType为upload时，如果开发者没有指定fileid，fileid置空，否则指定为相应的fileid；下载签名，fileid可以空，也可以为开发者查看的图片fileid。
   注意： 下载签名只有开发者在控制台上面设置了token防盗链时才使用，如果没有token防盗链，不需要下载签名，直接使用下载url下载图片。
   示例：

```
http://203.195.194.28/php/getsignv2.php?type=upload&fileid=sample123
 http://203.195.194.28/php/getsignv2.php?type=copy&fileid=sample123
 http://203.195.194.28/php/getsignv2.php?type=stat&fileid=sample123
 http://203.195.194.28/php/getsignv2.php?type=del&fileid=sample123
 http://203.195.194.28/php/getsignv2.php?type=download&fileid=sample123
```
2 通过web端js或者移动端程序请求以上http接口获取签名，上传图片。Web端js示例请参考[web端部署与SDK集成](http://cloud.tencent.com/doc/product/275/web%E7%AB%AF%E9%83%A8%E7%BD%B2%E7%A4%BA%E4%BE%8B)；移动端程序示例请分别参考[移动端部署与SDK集成-Android](http://cloud.tencent.com/doc/product/275/Android%E9%83%A8%E7%BD%B2%E7%A4%BA%E4%BE%8B)和[移动端部署与SDK集成-iOS](http://cloud.tencent.com/doc/product/275/iOS%E9%83%A8%E7%BD%B2%E7%A4%BA%E4%BE%8B)。