TsysAgent is a basic component of CPM OPS management feature. It is primarily used to support such features as password reset, distribution of EIP tunnel configuration. You cannot use related features if TsysAgent is not installed or exceptional. The following is a guide on the installation and repair of TsysAgent.

<br  />

## __Guide on Installation (Reinstallation/Repair) of TsysAgent__

### Windows Version
 __Download installation package__ 
Download installation package from http://mirrors.tencentyun.com/install/monitor_bm/TsysAgent_win64.zip

![](https://mc.qcloudimg.com/static/img/f09b2e84cfd437eda60a54e84128bc7f/001.png)
<br  />
 __Decompress zip file__ 

![](https://mc.qcloudimg.com/static/img/7691874f15cd0a44ad49ab4654a944f0/002.png)

<br  />
 __Install__ 
Double-click install.bat to install

 __Verify process and port__ 
Open "My Computer", enter "cmd" in address bar and press Enter.
![](https://mc.qcloudimg.com/static/img/a04a39f2b78d0d98e3df65c073e2ddf4/003.png)

Enter command tasklist, press Enter, and Tsys.exe TsysProxy.exe TsysAgent.exe is shown.
![](https://mc.qcloudimg.com/static/img/685ae2392c6c947738c2896e12271674/004.png)
![](https://mc.qcloudimg.com/static/img/419a0a66e59cc9b1b8e80416ff2d1b45/005.png)

Enter command netstat, press Enter, and the ports 48369, 42222 and 43333 are shown.

![](https://mc.qcloudimg.com/static/img/89d949fad505561ba994a6c1cbc081d7/006.png)
<br  /><br  />

### Linux Version
Execute related command under command line terminal
 __Download installation package__ 
Execute wget http://mirrors.tencentyun.com/install/monitor_bm/TsysAgent_64.tar.gz
``` 
[root@centos ~]# wget http://mirrors.tencentyun.com/install/monitor_bm/TsysAgent_64.tar.gz
--2017-06-09 16:17:52--  http://mirrors.tencentyun.com/install/monitor_bm/TsysAgent_64.tar.gz
Resolving mirrors.tencentyun.com (mirrors.tencentyun.com)... 10.112.65.62
Connecting to mirrors.tencentyun.com (mirrors.tencentyun.com)|10.112.65.62|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1969862 (1.9M) [application/octet-stream]
Saving to: 'TsysAgent_64.tar.gz'

100%[==========================================================================================================>] 1,969,862   7.87MB/s   in 0.2s   

2017-06-09 16:17:52 (7.87 MB/s) - 'TsysAgent_64.tar.gz' saved [1969862/1969862]
``` 

 __Decompress__ 
Execute tar xzpf TsysAgent_64.tar.gz
``` 
[root@centos ~]# tar xzpf TsysAgent_64.tar.gz
[root@centos ~]# ls
TsysAgent_64.tar.gz  TsysAgent_BS_64.tar.gz  install.sh
``` 

 __Install__ 
Execute ./install.sh
``` 
[root@centos ~]# ./install.sh
TsysAgent/
TsysAgent/upload/
TsysAgent/upload_bak/
TsysAgent/log/
TsysAgent/bin/
TsysAgent/bin/unstalltscagent.sh
TsysAgent/bin/start.sh
TsysAgent/bin/rtsvr.crt
TsysAgent/bin/tsysca.pub
TsysAgent/bin/.sessions/
TsysAgent/bin/.sessions/127.0.0.1:42222_0
TsysAgent/bin/.sessions/127.0.0.1:42222_1
TsysAgent/bin/pamcheck
TsysAgent/bin/sha512sum
TsysAgent/bin/.safe_TsysProxy_sh.pid
TsysAgent/bin/rsa_pri_key
TsysAgent/bin/agent_tsys_1.crt
TsysAgent/bin/rtsvrpri.key
TsysAgent/bin/netstat.sh
TsysAgent/bin/restart.sh
TsysAgent/bin/rtcli.crt
TsysAgent/bin/.safe_TsysAgent_sh.pid
TsysAgent/bin/prope_sock.sh
TsysAgent/bin/stop_proxy.sh
TsysAgent/bin/ps.sh
TsysAgent/bin/TsysAgent
TsysAgent/bin/TsysAgent.pid
TsysAgent/bin/tsysca.crt
TsysAgent/bin/rsa_rs
TsysAgent/bin/rtclipri.key
TsysAgent/bin/ping_client2
TsysAgent/bin/start_proxy.sh
TsysAgent/bin/promote
TsysAgent/bin/safe_TsysAgent.sh
TsysAgent/bin/agent_tsys_1.key
TsysAgent/bin/stop.sh
TsysAgent/bin/safe_TsysProxy.sh
TsysAgent/bin/ping_client
TsysAgent/bin/ping_client.conf
TsysAgent/bin/TsysProxy.pid
TsysAgent/bin/rsa_pub_key
TsysAgent/bin/netstat_proxy.sh
TsysAgent/bin/pri_key_100308
TsysAgent/bin/ps_proxy.sh
TsysAgent/bin/safe_prope.sh
TsysAgent/bin/rsa_rpk
TsysAgent/bin/TsysProxy
TsysAgent/etc/
TsysAgent/etc/sigex.list
TsysAgent/etc/allowBMregmode
TsysAgent/etc/key_shmcomm
TsysAgent/etc/ssl.conf
TsysAgent/etc/configtype
TsysAgent/etc/proxy_ctrl.conf
TsysAgent/etc/agent.ini_install
TsysAgent/etc/config.ini
TsysAgent/etc/ssl.ini
TsysAgent/etc/ssl_tfileserver.conf
TsysAgent/etc/autoreg
TsysAgent/etc/proxy_ctrl.conf_install
TsysAgent/etc/ctl_sigex
TsysAgent/etc/md5.list
TsysAgent/etc/key_df
TsysAgent/etc/key_md5
TsysAgent/etc/libgcc_s.so.1
TsysAgent/etc/server.ini
TsysAgent/etc/signature.list
TsysAgent/etc/agent.ini
TsysAgent/etc/cron_file1
TsysAgent/etc/allowlistenwanip
TsysAgent/etc/key_tm
TsysAgent/etc/key_ini
TsysAgent/update/
TsysAgent/agent_work/
TsysAgent/agent_work/backup/
TsysAgent/agent_work/agent_backup/
TsysAgent/agent_work/scan/
TsysAgent/agent_work/shell/
TsysAgent/agent_work/agent_upload/
TsysAgent/Readme
********************************************
Display TsysAgent Version
ver:Linux_64 S 3.2.22 May 17 2017 10:52:17
Dispaly TsysAgent listening port
tcp        0      0 127.0.0.1:42222         0.0.0.0:*               LISTEN      10345/TsysAgent  
``` 

 __Verify process and port__ 
Execute command ps aux | grep Tsys, and TsysProxy TsysAgent is shown.
``` 
[root@centos ~]# ps aux | grep Tsys
root     10311  0.0  0.1   9512  1420 pts/0    S    16:18   0:00 /bin/bash ./safe_TsysAgent.sh start
root     10345  0.0  0.1  15452  1712 pts/0    S    16:18   0:00 /usr/local/TsysAgent/bin/TsysAgent
root     10371  0.0  0.1   9512  1420 pts/0    S    16:18   0:00 /bin/bash ./safe_TsysProxy.sh start
root     10395  0.0  0.1  17008  1708 pts/0    S    16:18   0:00 /usr/local/TsysAgent/bin/TsysProxy
root     10580  0.0  0.0   9036   672 pts/0    R+   16:19   0:00 grep --color=auto Tsys
``` 
Execute command netstat -anp | grep Tsys, and the ports 48369 and 42222 are shown.

``` 
[root@centos ~]# netstat -anp | grep Tsys
tcp        0      0 127.0.0.1:42222         0.0.0.0:*               LISTEN      10345/TsysAgent     
tcp        0      0 0.0.0.0:48369           0.0.0.0:*               LISTEN      10395/TsysProxy
``` 

