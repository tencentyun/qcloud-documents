重置会话服务器自带的mysql root密码
1.修改my.cnf在[mysqld]中添加skip-grant-tables

 ![](//mc.qcloudimg.com/static/img/99f79ea91775063bf8a61397bbfc345d/image.png)

vim /opt/lampp/etc/my.cnf增加skip-grant-tables
[mysqld]
user = mysql
port=3306
socket          = /opt/lampp/var/mysql/mysql.sock
skip-grant-tables
2.重启mysql
/opt/lampp/ctlscript.sh restart mysql
3.用户无密码登录
/opt/lampp/bin/mysql -uroot -p回车两次
 ![](//mc.qcloudimg.com/static/img/5994adac6dbf3cd2a1d546337e91191c/image.png)
4.选择mysql库修改root密码
use mysql;
update user set authentication_string=password('YourPassword@123456') where user='root';不能用红色这句命令，这句适用于5.7不适用10.1.16-MariaDB，用绿色这句命令

update user set password=password("YourPassword@123456") where user="root";
flush privileges;
exit
5.修改my.cnf删除skip-grant-tables并重启mysql
vim /opt/lampp/etc/my.cnf
![](//mc.qcloudimg.com/static/img/dd6e23f6ef9016b28d0834cb0ad223e9/image.png) 
/opt/lampp/ctlscript.sh restart mysql
6.用新改的密码登录
/opt/lampp/bin/mysql -uroot -pYourPassword@123456
