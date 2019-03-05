本文档介绍腾讯云·万象优图服务端nodejs的部署和集成，搭建一个nodejs+nginx为基础，对web端或者移动端提供http签名接口服务的例子程序。
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
## 2 安装配置Nodejs环境
下面介绍安装Nodejs和配置web container的详细步骤。
1 安装Nodejs

```
yum install -y nodejs npm
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

    location ^~ /node/ {
        proxy_pass http://localhost:9002;
    }
}
```
3 重新加载nginx配置
修改配置完成后，需要执行以下命令重新加载配置。
```
nginx -s reload
```
## 3 安装Nodejs SDK
执行以下命令安装Nodejs SDK。
```
cd /data/www/tencentyun/node
npm install tencentyun
```
## 4 开发鉴权服务逻辑
将sdk集成到开发者代码，开发鉴权服务逻辑，这里以node目录下getsignv2.js为例（开发者务必根据自身业务开发相应的鉴权服务逻辑）：
注意：如果开发者想按照本示例做简单地测试，需要将下面代码中的相应字段替换为自己的项目信息，具体见代码注释。

```
var http=require('http');
var url = require('url');
var util = require('util');
var tencentyun = require('tencentyun');

var server=new http.Server();
server.on('request',function(req,res){

    var urlinfo = url.parse(req.url,true),
        type = 'upload';

    if (urlinfo.query && urlinfo.query.type) {
        type = urlinfo.query.type;
    }

    //请将下面的bucket, projectId, secretId和secretKey替换成开发者自己的项目信息
    var bucket = 'test0706',
        projectId = '10000037',
        userid = 0,
        secretId = 'AKIDpoKBfMK7aYcYNlqxnEtYA1ajAqji2P7T',
        secretKey = 'P4FewbltIpGeAbwgdrG6eghMUVlpmjIe';

    tencentyun.conf.setAppInfo(projectId, secretId, secretKey);

    var error = false;

    switch(type) {
        case 'upload':
            var fileid = '/u/can/use/slash/sample' + Math.round(+new Date()/1000),
                expired = Math.round(+new Date()/1000) + 999,
                uploadurl = tencentyun.imagev2.generateResUrlV2(bucket, userid, fileid),
                sign = tencentyun.auth.getAppSignV2(bucket, fileid, expired);
                ret = {'sign':sign,'url':uploadurl};
            break;
        case 'stat':
            if (!urlinfo.query || !urlinfo.query.fileid) {
                error = true;
            } else {
                var fileid = decodeURIComponent(urlinfo.query.fileid),
                    otherurl = tencentyun.imagev2.generateResUrlV2(bucket, userid, fileid),
                    ret = {'url':otherurl};
            }
            break;
        case 'del':
        case 'copy':
            if (!urlinfo.query || !urlinfo.query.fileid) {
                error = true;
            } else {
                var fileid = decodeURIComponent(urlinfo.query.fileid),
                    otherurl = tencentyun.imagev2.generateResUrlV2(bucket, userid, fileid, type),
                    sign = tencentyun.auth.getAppSignV2(bucket, fileid, 0);
                    ret = {'sign':sign,'url':otherurl};
            }
            break;
        case 'download':
            if (!urlinfo.query || !urlinfo.query.fileid) {
                error = true;
            } else {
                var fileid = decodeURIComponent(urlinfo.query.fileid),
                    expired = Math.round(+new Date()/1000) + 999,
                    sign = tencentyun.auth.getAppSignV2(bucket, fileid, expired);
                    ret = {'sign':sign};
            }
            break;
    }

    res.writeHead(200,{'Content-Type':'application/json'});
    if (error) {
        res.end({'error':'params error'});
    } else {
        res.end(JSON.stringify(ret)); 
    }
});

server.listen(9002);
console.log('HTTP SERVER is LISTENING AT PORT 9002.');
```
## 5 运行程序
```
cd /data/www/tencentyun/node
nohup node getsignv2.js &
```
## 6 测试
1. 终端通过CGI：http://203.195.194.28/node/?type=[opType]&fileid=[fileid]来获取相应的签名。
opType：可取值：upload(上传), stat（查询）, copy（复制）, del（删除）和download（下载，如果开启token防盗链）；
fileid：是图片资源的唯一标识；当opType为upload时，如果开发者没有指定fileid，fileid置空，否则指定为相应的fileid；下载签名，fileid可以空，也可以为开发者查看的图片fileid。
注意： 下载签名只有开发者在控制台上面设置了token防盗链时才使用，如果没有token防盗链，不需要下载签名，直接使用下载url下载图片。
示例：
 ```
 http://203.195.194.28/node/?type=del&fileid=sample123
 http://203.195.194.28/node/?type=copy&fileid=sample123
 http://203.195.194.28/node/?type=stat&fileid=sample123
 http://203.195.194.28/node/?type=download&fileid=sample123
 http://203.195.194.28/node/?type=upload&fileid=sample123
```
2 通过web端js或者移动端程序请求以上http接口获取签名，上传图片。Web端js示例请参考[web端部署与SDK集成](/doc/product/275/web端部署示例)；移动端程序示例请分别参考[移动端部署与SDK集成-Android](/doc/product/275/Android部署示例)和[移动端部署与SDK集成-iOS](/doc/product/275/iOS部署示例)。