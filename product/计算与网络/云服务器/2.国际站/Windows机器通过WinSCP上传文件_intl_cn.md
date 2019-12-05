WinSCP是一个Windows环境下使用SSH的开源图形化SFTP客户端，同时支持SCP协议。它的主要功能就是在本地与远程计算机间安全的复制文件。与使用FTP上传代码相比，通过WinSCP可以直接使用服务器账户密码访问服务器，无需在服务器端做任何配置。下载地址：[官方下载](http://winscp.net/eng/docs/lang:chs) [太平洋下载中心下载](http://dl.pconline.com.cn/html_2/1/86/id=7244&pn=0.html)

安装完成后启动WinSCP，界面如下。按图示填写信息并登录。

![](//mccdn.qcloud.com/img56b024e2768ad.png)

>字段填写说明：
- 协议：SFTP或者SCP均可
- 主机名：云服务器的公网IP（登录[云服务器控制台](https://console.cloud.tencent.com/cvm)可查看云服务器的公网IP）
- 用户名：云服务器的系统用户名（SUSE/CentOS/Debian：root，Windows：Administrator，Ubuntu：ubuntu）
- 密码：云服务器的用户名对应的密码
- 端口：默认22

信息填写完毕之后点击登录，界面如下:

![](//mccdn.qcloud.com/img56b0272d4ed3a.png)

登录成功之后，鼠标选中本地文件，拖拽到右侧的远程站点，即可将文件上传到Linux云服务器。

![](//mccdn.qcloud.com/img56b027728e1ec.png)
