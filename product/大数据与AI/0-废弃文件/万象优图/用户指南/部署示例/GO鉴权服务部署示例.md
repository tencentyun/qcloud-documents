本文档介绍腾讯云万象优图服务端go的部署和集成，搭建一个go+nginx为基础，对web端或者移动端提供http签名接口服务的例子程序。
注意：本文档只是简单的示例，展示了服务端为终端提供签名的基本示例，开发者务必根据自身业务开发相应的鉴权服务逻辑，并集成到自身服务器中。
## 1 环境准备
下面以在腾讯云云服务器CentOS 6.2 64位上安装nginx为例，简单介绍如何将腾讯云万象优图集成，对web端或者移动端提供http签名接口服务所需要的基础环境搭建。开发者可以根据自己业务的需要，构建http或者非http服务，为自身业务的web端、移动端提供签名。
### 1.1 安装nginx
yum install nginx –y
service nginx restart
### 1.2 验证nginx
直接访问云服务器ip地址，验证nginx是否已经运行起来。
## 2 安装配置Go环境
go的web开发框架可以自由选择，这里以beego为例，beego详见[Homepage-beego](http://beego.me/)。
### 2.1 beego安装
安装beego

```
go get github.com/astaxie/beego
```
安装bee

```
go get github.com/beego/bee
```
### 2.2 配置bee环境
bee安装完成后配置环境变量PATH。

```
export PATH=$PATH:$GOPATH/bin
```
### 2.3 配置web container
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

    location ^~ /go/ {
        proxy_pass http://localhost:9001;
    }
}
```
修改配置完成后，需要执行以下命令重新加载配置。

```
nginx -s reload
```
### 2.4 创建项目
在任意目录下创建新应用服务器项目，这里项目名采用signServer。

```
bee new signServer
```
## 3 集成Go SDK
在开发环境下直接执行如下命令来集成Go SDK。

```
go get github.com/tencentyun/go-sdk
```
## 4 开发鉴权服务逻辑
以下代码是一个简单的示例，开发者需要根据自己的业务需求来开发相应代码。
注意：如果开发者想根据此示例进行简单的测试，请将conf目录下的app.conf配置文件中相应的项目信息替换为自己项目的信息，具体见下面“配置的读取”注释。
1. 代码开发
在之前建立的signServer项目controllers目录下编写sign.go

```
package controllers

import (
        "encoding/json"
        "fmt"

        "github.com/astaxie/beego"
        "github.com/tencentyun/go-sdk"
)

type signData struct {
        Version string `json:"ver"`
        Sign    string `json:"sign"`
}

type SignController struct {
        beego.Controller
}

func (c *SignController) Get() {
        appid, _ := beego.AppConfig.Int("appid")
        sid := beego.AppConfig.String("sid")
        skey := beego.AppConfig.String("skey")
        bucket := beego.AppConfig.String("bucket")

        types := c.Input().Get("type")
        fileid := c.Input().Get("fileid")

        var data signData
        cloud := qcloud.PicCloud{uint(appid), sid, skey, bucket}
        data.Version = "V2"
        if types == "" || types == "upload" {
                data.Sign, _ = cloud.Sign(3600)
        } else if types == "copy" ||
                types == "del" ||
                types == "download" {
                data.Sign, _ = cloud.SignOnce(fileid)
        } else {
                data.Sign = ""
        }

        rsp, err := json.Marshal(data)
        if err != nil {
                fmt.Println("error: ", err.Error())
        }
        c.Ctx.WriteString(string(rsp))
}
```
2. 配置的读取
Beego的配置文件在conf目录下的app.conf。
开发者需要将文件中的appid(项目ID)，sid（项目SecretID），skey（项目SecretKey），bucket（空间名称）分别替换为开发者自己的项目信息。

```
appname = signServer
httpport = 9000
runmode = dev

appid = 10000001
sid = AKIDNZwDVhbRtdGkMZQfWgl2Gnn1dhXs95C0
skey = ZDdyyRLCLv1TkeYOl5OCMLbyH4sJ40wp
bucket = testa
```
3.route逻辑(routers/router.go)

```
package routers

import (
    "github.com/tencentyun/go-sdk/sample/signServer/controllers"
    "github.com/astaxie/beego"
)

func init() {
    beego.Router("/", &controllers.MainController{})
    beego.Router("/go/getsign", &controllers.SignController{})
}

```
## 5 编译运行beego
在signServer项目目录下执行如下命令即可。

```
bee run
```
go将编译应用服务器到一个binary文件，例如上述例子里为signServer。可以随便复制到任何地方执行（连带conf，statics和views，这里包含一些配置、静态资源和模板）。
以后只需要直接执行binary文件即可。不需要多次执行bee run。
## 6 测试
1. 终端通过CGI：http://203.195.194.28/go/getsign?type=[opType]&fileid=[fileid]来获取相应的签名。
opType：可取值：upload(上传), stat（查询）, copy（复制）, del（删除）和download（下载，如果开启token防盗链）；
fileid：是图片资源的唯一标识；当opType为upload时，如果开发者没有指定fileid，fileid置空，否则指定为相应的fileid；下载签名，fileid可以空，也可以为开发者查看的图片fileid。
注意： 下载签名只有开发者在控制台上面设置了token防盗链时才使用，如果没有token防盗链，不需要下载签名，直接使用下载url下载图片。
示例：

```
http://203.195.194.28/go/getsign?type=download&fileid=sample123
 http://203.195.194.28/go/getsign?type=upload&fileid=sample123
 http://203.195.194.28/go/getsign?type=copy&fileid=sample123
 http://203.195.194.28/go/getsign?type=del&fileid=sample123
 http://203.195.194.28/go/getsign?type=stat&fileid=sample123
```
2 通过web端js或者移动端程序请求以上http接口获取签名，上传图片。Web端js示例请参考[web端部署与SDK集成](/doc/product/275/web端部署示例)；移动端程序示例请分别参考[移动端部署与SDK集成-Android](/doc/product/275/Android部署示例)和[移动端部署与SDK集成-iOS](/doc/product/275/iOS部署示例)。