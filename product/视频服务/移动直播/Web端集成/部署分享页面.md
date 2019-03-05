## 1.功能介绍

视频分享页面是用于直播APP分享的承载页，可以让用户能够在微信、QQ等移动端APP中以网页的形式打开，观看视频和进行IM通信，增强APP的传播度，提高曝光率。

本片文档主要介绍如何将该源码部署在一台自己搭建的 apache 服务器上，适合没有静态网页部署经验的工程师朋友进行网页代码调试。

## 2.分享操作流程

- APP构造分享URL，并带上需要的参数。例如：
<table class="t" style="text-align: center; width:750px">
<tbody>
<tr><td>
`http://imgcache.qq.com/open/qcloud/video/share/xiaozhibo.html?sdkappid=1400012345&acctype=8888&userid=test1234&type=0`
</td></tr>
</tbody></table>
- 当用户打开分享URL时，分享页将会根据URL的参数去小直播的livedemo server拉取数据，包括视频播放地址，主播的资料，IM的房间信息等，然后呈现视频播放和IM消息的收发功能

## 3.Demo目录结构
- sdk： IM sdk 代码
- js：  demo的js代码
- img： 图片文件
- css： 样式文件

## 3.部署分享页面
源码提供了一系列的静态文件，用于部署到静态文件服务器，例如Nginx、Apache、Nodejs等

### 3.1准备环境

- 操作系统：windows 7 64位
- web服务器软件：Apache 2.4 64位
- 运行demo也可以是其他web服务器软件，比如Nginx
- 服务器拥有公网IP以及域名，这里以域名 `www.xiaozhibo.com` 为例

<font color="red">欢迎使用腾讯云一站式解决方案，免去各种繁琐配置操作，包括云服务器、域名服务等解决方案，详情请点击</font>

[https://cloud.tencent.com/product/cvm](https://cloud.tencent.com/product/cvm)


### 3.2安装apache

下载 64位 apache，地址：
http://www.apachehaus.com/cgi-bin/download.plx?dli=StmURFWaNJzTEx2KWVkRwAlVOpkVFVFdSxGZPVWQ

查看其他版本，地址：
http://www.apachehaus.com/cgi-bin/download.plx

将下载的压缩包，解压到本地某个目录下，比如，放在D:\Program Files\目录下。

编辑apache配置文件：

```
D:\Program Files\Apache24\conf\httpd.conf
```

找到：Define SRVROOT 这一项，将其右方的值改为当前你Apache安装存放的目录地址，如下：

```
Define SRVROOT "D:/Program Files/Apache24"
```

继续找，找到：Listene 80，若你电脑的80端口被占用（可在cmd下用命令netstat -a查看），则将80端口改为别的端口，这里我们使用8080端口，如下：

```
Listen 8080
```

改完以上两个地方，记得保存httpd.conf文件。

接下来需要配置安装Apache的主服务，有了它，Apache才可启动：
打开CMD窗口，输入：

```
"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
```
该命令的意思是，安装apache服务，并将该服务名称命名为apache(你也可以改成别的)，回车。

正常安装完毕如下所示：

```
C:\Users\peakerdong>"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
[Fri May 20 13:39:16.474314 2016] [mpm_winnt:error] [pid 14884:tid 144] AH00433: apache: Service 
is already installed.
```

其中，Errors reported here must be corrected before the service can be started.意思是，若该句话后面有错误信息，则表示服务安装失败，需要先改正错误。若没有，则成功。

在安装目录中，找到D:\Program Files\Apache24\bin\ApacheMonitor.exe可执行文件，双击运行，桌面右下角会出现图标，双击打开窗口界面，会看到如图所示：
![](//mccdn.qcloud.com/static/img/02ef4d509e5579661953a9cc3dc4ee59/image.png)

点击左侧start，启动apache服务。

打开浏览器，输入访问 `http://localhost`
如果你设置的端口是8080，则访问地址是`http://localhost:8080/`
出现以下界面，表示apahce启动成功。
![](//mccdn.qcloud.com/static/img/1a051fa9cbedf08e55a979f732e824ef/image.png)

如果服务器拥有公网IP以及域名，可以使用域名访问，例如：
`http://www.xiaozhibo.com/`

### 3.3 运行demo

将demo中的share目录的文件拷贝到apache web运行目录下：

```
D:\Program Files\Apache24\htdocs
```

这时访问分享页的地址将会是

`http://www.xiaozhibo.com/share/xiaozhibo.html`

注意：这里的地址还未带上必要的参数。

完整的分享链接需要小直播APP追加参数进行构造，最终实际的分享地址应该是：

`http://www.xiaozhibo.com/share/xiaozhibo.html?sdkappid=1400012894&acctype=6672&userid=test1234&type=0&ts=1479299174`

当用户打开分享URL时，分享页将会根据URL的参数去小直播的livedemo server拉取数据，包括视频播放地址，主播的资料，IM的房间信息等，然后呈现视频播放和IM消息的收发功能

### 3.4 服务器配置参考

- [Apache服务器搭建及静态web站点常规配置](https://my.oschina.net/wdos/blog/71512)

- [Nginx静态服务器配置](http://www.cnblogs.com/h9527/p/5530298.html)




