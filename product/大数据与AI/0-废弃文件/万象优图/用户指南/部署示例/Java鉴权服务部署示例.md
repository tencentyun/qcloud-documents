本文档介绍了腾讯云万象优图服务端java的部署和集成，搭建一个java+tomcat为基础，对web端或者移动端提供http签名接口服务的例子程序。
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
## 2 环境安装配置
### 2.1 java安装
有网络的情况下，可通过以下命令行安装。
```
yum install [java包名]
//java包可通过以下命令查看
yum –y search java
```
无网络的条件下可以去官网下载安装。
http://www.oracle.com/technetwork/java/javase/downloads/index.html 
### 2.2 配置java环境变量
编辑/etc/profile（或者其他可配置环境变量的文件)
```
export JAVA_HOME=/usr/java/jdk1.7.0_51
export JAVA_BIN=/usr/java/jdk1.7.0_51/bin
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export TOMCAT_HOME=/usr/local/tomcat
export CATALINA_HOME=$TOMCAT_HOME
export PATH=$PATH:$TOMCAT_HOME/bin
export JAVA_HOME JAVA_BIN PATH CLASSPATH TOMCAT_HOME CATALINA_HOME
```
配置完成后，需要source文件来载入配置。
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

    location ^~ /java/ {
		proxy_pass http://localhost:8080;
    }
}
```
修改配置完成后，需要执行以下命令重新加载配置。

```
nginx -s reload
```
### 2.4 tomcat安装
tomcat可以直接下载安装，下载地址：http://tomcat.apache.org/ 。
### 2.5 启动tomcat
执行tomcat安装目录下bin内的startup.sh
## 3 下载java sdk
在网络可用的情况下可以直接用git命令行下载。
git clone https://github.com/tencentyun/java-sdk.git
也可以直接在git网站下载，网址如下:
https://github.com/tencentyun/java-sdk/archive/master.zip
## 4 开发鉴权服务器逻辑
本节介绍一个简单的鉴权服务器代码示例，开发者需要根据自身业务逻辑开发相应的代码。
注意：如果开发者想根据此示例进行简单的测试，请将代码中相应的项目信息替换为自己项目的信息，具体见注释。
鉴权服务器代码的示例如下：(getsign.jsp)

```
<%@ page language="java" import="com.qcloud.*,org.json.*" pageEncoding="UTF-8"%>

<%
        //请将下面的APP_ID_V2，SECRET_ID_V2，SECRET_KEY_V2，BUCKET替换为开发者自己的项目信息
        int APP_ID_V2 = 10000001;  //项目ID
        String SECRET_ID_V2 = "AKIDNZwDVhbRtdGkMZQfWgl2Gnn1dhXs95C0"; //项目SecretID
        String SECRET_KEY_V2 = "ZDdyyRLCLv1TkeYOl5OCMLbyH4sJ40wp";  //项目SecretKey
        String BUCKET = "testa"; //空间名称bucket

        String type = request.getParameter("type");
        String fileid = request.getParameter("fileid");

        PicCloud pc = new PicCloud(APP_ID_V2, SECRET_ID_V2, SECRET_KEY_V2, BUCKET);
        String sign = "";
        long expired = System.currentTimeMillis() / 1000 + 3600;
        if(null == type || "".equals(type)){
                sign = pc.GetSign(expired);
        }else if("upload".equals(type)){
                sign = pc.GetSign(expired);
        }else if("copy".equals(type) ||
                        "del".equals(type) ||
                        "download".equals(type) ){
                sign = pc.GetSignOnce(fileid);
        }else{
                sign = "";
        }

        JSONObject jsonObject = new JSONObject();
        jsonObject.put("ver", "V2");
        jsonObject.put("sign", sign.toString());
        out.print(jsonObject.toString());

%>
```
开发完成后编译，注意，需要将依赖库也打包。
## 5 开发部署到tomcat
Tomcat的部署目录在安装目录/webapps下面。
部署包的目录结构例如：

```
drwxr-xr-x 2 root root 4096 Jul 24 13:40 META-INF
drwxr-xr-x 4 root root 4096 Jul 24 13:40 WEB-INF
-rw-r--r-- 1 root root  836 Jul 24 13:40 getsign.jsp
-rw-r--r-- 1 root root  462 Jul 24 13:40 index.html
```
## 6 测试
1. 终端通过CGI：http://203.195.194.28/java/getsign.jsp?type=[opType]&fileid=[fileid]来获取相应的签名。
opType：可取值：upload(上传), stat（查询）, copy（复制）, del（删除）和download（下载，如果开启token防盗链）；
fileid：是图片资源的唯一标识；当opType为upload时，如果开发者没有指定fileid，fileid置空，否则指定为相应的fileid；下载签名，fileid可以空，也可以为开发者查看的图片fileid。
注意： 下载签名只有开发者在控制台上面设置了token防盗链时才使用，如果没有token防盗链，不需要下载签名，直接使用下载url下载图片。
示例：

```
 http://203.195.194.28/java/getsign.jsp?type=download&fileid=sample123
 http://203.195.194.28/java/getsign.jsp?type=upload&fileid=sample123
 http://203.195.194.28/java/getsign.jsp?type=copy&fileid=sample123
 http://203.195.194.28/java/getsign.jsp?type=del&fileid=sample123
 http://203.195.194.28/java/getsign.jsp?type=stat&fileid=sample123
```
2 通过web端js或者移动端程序请求以上http接口获取签名，上传图片。Web端js示例请参考[web端部署与SDK集成](http://cloud.tencent.com/doc/product/275/web%E7%AB%AF%E9%83%A8%E7%BD%B2%E7%A4%BA%E4%BE%8B)；移动端程序示例请分别参考[移动端部署与SDK集成-Android](http://cloud.tencent.com/doc/product/275/Android%E9%83%A8%E7%BD%B2%E7%A4%BA%E4%BE%8B)和[移动端部署与SDK集成-iOS](http://cloud.tencent.com/doc/product/275/iOS%E9%83%A8%E7%BD%B2%E7%A4%BA%E4%BE%8B)。