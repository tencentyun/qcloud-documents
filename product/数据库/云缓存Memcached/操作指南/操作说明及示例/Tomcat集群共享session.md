要实现session共享，多个tomcat服务器之间须使用负载均衡模块进行调度，这里用nginx+tomcat+ckv为例进行说明;

## 1 部署tomcat服务器

1.首先部署多个tomcat服务器，并确保每一个服务器均能正常访问;
2.下载memcached-session-manager-${version}.jar，此jar包包含了msm的核心功能;

根据不同的tomcat版本下载对应的支持库：

Tomcat6:memcached-session-manager-tc6-${version}.jar
Tomcat7:memcached-session-manager-tc7-${version}.jar
Tomcat8:memcached-session-manager-tc8-${version}.jar

3.为了支持memcached协议还必须下载spymemcached-2.11.1.jar
4.确定序列化方案，不同方案对jar包的依赖关系如下：
- kryo-serializer
msm-kryo-serializer,kryo-serializers-0.11(0.11 is needed, as 0.20+ is for kryo2),kryo,minlog,reflectasm,asm-3.2
- javolution-serializer
msm-javolution-serializer,javolution-5.4.3.1
- xstream-serializer
msm-xstream-serializer,xstream,xmlpull,xpp3_min
- flexjson-serializer
msm-flexjson-serializer,flexjson
- java自带序列化方案
spymemcached-2.11.1.jar已自带，性能相对较差
5. 现在我们需要把已经准备好的jar包全部放在tomcat的lib目录下，然后修改conf目录下的context.xml文件，此处以java自带序列化方案为例，在context标签下添加如下内容：

```
<Manager className="de.javakaffee.web.msm.MemcachedBackupSessionManager"   
         memcachedNodes="n1:10.66.121.134:9101"   
         requestUriIgnorePattern=".*\.(png|gif|jpg|css|js)$"   
         sessionBackupAsync="false"   
         sessionBackupTimeout="100"   
    sticky="false"
         transcoderFactoryClass="de.javakaffee.web.msm.JavaSerializationTranscoderFactory"   
         copyCollectionsForSerialization="false" />
```

其中n1为已备好的支持memcached协议的缓存服务器，可以设置多个，此处为ckv服务器，manager其他选项和说明可[参照这里].

## 2 安装nginx服务器

配置好所有tomcat服务器之后，需要安装nginx服务器，以实现负载均衡的功能，确保nginx起始页可以正常打开之后，打开nginx目录下的nginx.conf文件，添加如下内容：

```
upstream tomcats {
    server 10.104.37.25:8080 weight=1;
    server 10.104.42.64:8080 weight=1;
}
server {
    listen    13355;
    server_name    tomcats;
    charset utf-8;
    location / {
        proxy_pass    http://tomcats;
        proxy_redirect    off;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

这里我把监听端口改为了13355，tomcats里面的两个ip为两个tomcat服务器，weight为权重，为了便于观察效果，将权重设为相同。

## 3 编写测试代码

最后，我们需要实现jsp页面，测试结果，jsp页面示例代码如下：

```
<%@ page language="java" import="java.util.*,java.net.InetAddress" pageEncoding="ISO-8859-1"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'ShowSessionJsp.jsp' starting page</title>
    
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache">
    <meta http-equiv="expires" content="0">    
    <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
    <meta http-equiv="description" content="This is my page">
    <!--
    <link rel="stylesheet" type="text/css" href="styles.css">
    -->

  </head>
  
  <body>
    <%
        
        out.println("Session id is " + session.getId());%>
        <br/>
        <% 
        out.println("Server IP is "+InetAddress.getLocalHost().getHostAddress());%>
        <br/>
        <% 
        out.println("Server name is "+request.getServerName());
    %>
  </body>
</html>
```

## 4 测试结果

访问nginx服务器http://119.29.82.140:13355/ShareSession/ShowSession， 反复刷新页面，测试结果：

Session id is 5526F95AEB3#88C6F1C0B9C7A5B92E23-n1
Server IP is 127.0.0.1
Server name is tomcats

Session id is 5526F95AEB3E88C6F1C0B9C7A5B92E23-n1
Server iIP is 10.104.42.64
Server name is tomcats

其中一个tomcat服务器与nginx在同一台机器上，可以看到ip地址在变化，session id保持不变，说明共享session成功.

通过Manager中的设置还可以设置多个缓存节点，实现缓存服务器的容灾，此处不做赘述。另：负载均衡还可以通过apache等方式实现.
