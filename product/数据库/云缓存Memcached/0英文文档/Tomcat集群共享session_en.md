To share session, multiple tomcat servers must be scheduled using load balance module. Here, we use nginx+tomcat+ckv in this example for illustration;

## 1. Deploy tomcat server

1. First, you need to deploy multiple tomcat servers, and make sure every server can be accessed;
2. Download memcached-session-manager-${version}.jar, which contains the core features of msm;

Download the corresponding supporting database based on different versions of tomcat servers:

Tomcat6:memcached-session-manager-tc6-${version}.jar
Tomcat7:memcached-session-manager-tc7-${version}.jar
Tomcat8:memcached-session-manager-tc8-${version}.jar

3. You need also to download spymemcached-2.11.1.jar to support memcached protocol
4. Determine a serialization scheme. Dependency between different schemes and JAR package is as follows:
- kryo-serializer
msm-kryo-serializer,kryo-serializers-0.11(0.11 is needed, as 0.20+ is for kryo2),kryo,minlog,reflectasm,asm-3.2
- javolution-serializer
msm-javolution-serializer,javolution-5.4.3.1
- xstream-serializer
msm-xstream-serializer,xstream,xmlpull,xpp3_min
- flexjson-serializer
msm-flexjson-serializer,flexjson
- JAVA's serialization scheme
Since spymemcached-2.11.1.jar comes with JAVA, the performance is relatively poor
5. Now, we need to put JAR package into the directory lib of tomcat, and modify the file context.xml under the directory conf. Here we take JAVA's serialization scheme as an example, you need to add the following content under the context tag:

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

Wherein, n1 is a cache server (ckv server) prepared to support memcached protocol. Multiple servers are allowed. Other options and descriptions of manager can be found [here].

## 2. Install nginx server

After all the tomcat servers are deployed, you need to install nginx server to achieve load balance. After the nginx initial page is opened, you can add the following content in the the file nginx.conf under the directory nginx:

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

Here, the listener port is changed to 13355. Both IPs in the tomcats are tomcat servers. "weight" is weight, which is set to the same value for better observation.

## 3. Write the test code

Lastly, we need to obtain test result from JSP page. The sample code on JSP page is as follows:

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

## 4 Test Result

Access to nginx server (http://119.29.82.140:13355/ShareSession/ShowSession), and refresh the page until you get the test result:

Session id is 5526F95AEB3#88C6F1C0B9C7A5B92E23-n1
Server IP is 127.0.0.1
Server name is tomcats

Session id is 5526F95AEB3E88C6F1C0B9C7A5B92E23-n1
Server iIP is 10.104.42.64
Server name is tomcats

One of the tomcat servers and nginx server reside in the same CVM. As shown in the above figure, IP address is changing, and session id remains unchanged, which means the session is successfully shared.

Based on the configuration in Manager, you can also configure multiple cache nodes, to implement disaster recovery of cache server. In addition, load balance can be achieved using methods such as apache.

