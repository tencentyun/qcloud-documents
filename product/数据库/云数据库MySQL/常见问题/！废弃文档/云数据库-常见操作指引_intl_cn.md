## 1、如何备份数据

云数据库实例每天会进行全量备份，开发者可以在控制台外网或者内网下载备份数据，也可以在phpMyAdmin中手动备份数据库。

## 2、如何查看云数据库慢查询日志

可在云数据库控制台导出并查看并慢查询日志。

云数据库的慢查询时间(long_query_time)的默认值是10秒，用户可以自行修改，命令如下：

<pre> set global long_query_time = 1
</pre>

详细请参考[MySQL官方手册](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_long_query_time)。 


## 3、如何授权其他用户操作云数据库

root用户可以使用mysql的grant命令对其他用户进行授权，注意不能使用grant all进行授权。

目前shutdown和file权限没有开放给root用户，因此root不能新建拥有所有权限的用户。授权时，请参考以下命令：

<pre>grant SELECT,INSERT, UPDATE, DELETE, CREATE, DROP, ALTER on *.* to 'myuser'@'%' identified 
by 'mypasswd';</pre>
 
## 4、如何通过公网访问云数据库

国内地域的云数据库外网访问已正式发布，香港与北美地域暂不支持外网访问。

如果您需要通过公网访问，可以通过在有公网IP的云服务器上搭建MySQL Proxy的方式，利用MySQL Proxy进行访问。

详细请参考[MySQL Proxy官方手册](http://dev.mysql.com/downloads/mysql-proxy/)。

搭建方法参考如下：

1)下载mysql-proxy安装包到云服务器

wget [http://cdn.mysql.com/Downloads/MySQL-Proxy/mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz](http://cdn.mysql.com/Downloads/MySQL-Proxy/mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz)

2)解压上述安装包

tar -xzf mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit.tar.gz 

3)查看解压出来的目录

ls mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit 目录下包含有bin、lib、libexec等目录： bin、libexec目录包含mysql proxy等程序，lib目录带有程序依赖的库，如glibc、pcre等。 请保持bin、lib、libexec目录的相对路径关系，避免找不到依赖的库。

4)进入mysql proxy所在目录并运行

cd mysql-proxy-0.8.4-linux-glibc2.3-x86-64bit/bin 
./mysql-proxy --proxy-backend-addresses=10.**.**.17:3306 --proxy-address=:4040 

参数介绍：

--proxy-backend-addresses=10.**.**.17:3306， 云数据库的ip和端口,您需要把其中的10.**.**.17:3306换成您的云数据库的ip和端口。
--proxy-address=:4040，代理的监听地址和端口。默认是":4040"，表示本机所有4040端口的所有ip。 

还可以在命令后面添加一些参数：

--daemon，让代理处于后台运行
--keepalive，代理崩溃后尝试重启代理
运行命令后，会显示如下信息，提示代理搭建成功：
2014-09-01 11:56:38: (critical) plugin proxy 0.8.4 started 
如果没有成功启动，欢迎咨询我们。
该代理的监听端口是4040,我们接下来测试代理能否成功转发。

5)从外网访问云服务器上的mysql proxy。

在一台外网机子运行【假设外网ip为182.*.*.2】 mysql -h 182.*.*.2 -P 4040 -u root -p 按提示输入您的云数据库密码后，看是否成功登录云数据库。 如果登录失败，请检查：

a 第4)步中云数据库的ip和端口是否正确。

b.外网机子是否能ping通云服务器的外网ip

c.云服务器是否成功启动mysql proxy。


## 5、云数据库的默认字符集编码如何修改

云数据库与MySQL数据库一样，默认字符集编码格式是：latin1，即ISO-8859-1编码格式。

开发者可以在云数据库的管理控制台修改Server端的数据库字符集，目前支持latin1,gbk,utf8，utf8mb4四种字符集设置。

虽然云数据库支持默认字符集编码的设置，但我们还是建议您在创建表时，显式的指定表的编码，并在连接建立时指定连接的编码。

这样，您的应用将会有更好的移植性。

关于MySQL字符集的相关资源请参考[MySQL官方手册](https://dev.mysql.com/doc/refman/5.7/en/charset.html)。

可通过CDB管理控制台修改字符集。

## 6、云数据库如何统计访问次数

云数据库的访问次数根据MySQL状态变量Queries计算得来。

## 7、云数据库如何做读写分离

可通过购买只读实例做读写分离。

