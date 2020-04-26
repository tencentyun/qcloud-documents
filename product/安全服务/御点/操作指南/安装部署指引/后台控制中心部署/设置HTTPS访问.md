该操作步骤非必选步骤，用户可根据需求进行设置。
  
1. 准备证书。 需要企业用户提供相关 CA 证书，准备好后缀为 `*.crt` 和` *.key` 的证书。
![](https://main.qcloudimg.com/raw/b064ea77d6cf7165a48fc969740f0b6a.png)
2. 导入证书。登录御点后台控制中心所在服务器，将证书放置在`御点安装目录 \Data\ `路径下。
	- Windows 服务器：假设御点安装目录为`C:\Program Files (x86)\Tencent\PCMgrEnterprise`，则证书存放位置为` C:\Program Files (x86)\Tencent\PCMgrEnterprise\Data\ `。
	- Linux 服务器：证书存放位置为`/data/services/pcmgr_enterprise/data/`。
3. 修改配置，增加御点的 HTTPS 支持。在`御点安装目录 \Data\ `路径下创建`nginx_https.conf` 文件。
	- Windows服务器：假设御点安装目录为`C:\Program Files (x86)\Tencent\PCMgrEnterprise`，则文件位置为`C:\Program Files (x86)\Tencent\PCMgrEnterprise\Data\nginx_https.conf`。
	- Linux服务器：文件位置为`/data/services/pcmgr_enterprise/data/nginx_https.conf`。
	- 配置内容参考如下：
	>!配置中的名称需要和实际证书的名称保持一致。
![](https://main.qcloudimg.com/raw/8140bf2d150ddd0ceb3d18b5b1572349.png)
>
```
server {
listen 0.0.0.0:443 ssl;
keepalive_timeout 70;
server_tokens off;
server_name localhost;
ssl on;
ssl_certificate ../../../../Data/XXXXX.com.crt;
ssl_certificate_key ../../../../Data/ XXXXX.com.key;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
ssl_ciphers HIGH:!aNULL:!MD5;
add_header Strict-Transport-Security max-age=63072000;
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
client_header_buffer_size 4k;
client_header_timeout 200s;
#access_log logs/host.access.log main;
root ..\..\www_svr\public;
location / {
proxy_set_header Host $host:$server_port;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;proxy_set_header X-Forwarded-Proto $scheme;
#try files to node backend
try_files $uri $uri/ @node;
index index.html index.htm;
limit_conn one 5000; #连接数限制，超过限制返回503错误
#带宽限制,对单个连接限数，如果一个ip两个连接，就是500x2k
limit_rate 3072k;
}
error_page 500 502 503 504 /50x.html;
location = /50x.html {
root h
}
client_max_body_size 2048m;
location @node {
proxy_read_timeout 1200s;
proxy_set_header Host $host:$server_port;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_pass http://node_cgi_list;
}
}
```
4. 开启 HTTPS 支持开关，修改` user_config.dat` 配置
	- Windows 服务器：假设御点安装目录为`C:\Program Files (x86)\Tencent\PCMgrEnterprise`，则文件位置为`C:\Program Files (x86)\Tencent\PCMgrEnterprise\Data\user_config.dat`。
	- Linux 服务器：文件位置为`/data/services/pcmgr_enterprise/data/user_config.dat`。
	- 在文件中增加如下配置`"$(web_https)":"true"`。
<img src="https://main.qcloudimg.com/raw/4a6e2a44491c05260f5174bf4f7e5ed4.png"  />
5. 重启服务。
	- Windows 服务器，以**管理员权限启动 cmd.exe**，输入`sc stop DaemonSrv`，单击【回车】，待加载完毕后，输入`sc start DaemonSrv`，单击【回车】，如图所示即可重启。
	![](https://main.qcloudimg.com/raw/ac077f273751614aef24c5f2fec2f790.png)
	- Linux 服务器，运行`sh` ，文件位置为`/data/services/pcmgr_enterprise/public/supervisor_restart.sh`，脚本运行完毕即可重启，也可通过以下命令运行：
	```
	 [root@d2c2fce5c9e0 ~]# sh /data/services/pcmgr_enterprise/public/supervisor_restart.sh
	 ```
