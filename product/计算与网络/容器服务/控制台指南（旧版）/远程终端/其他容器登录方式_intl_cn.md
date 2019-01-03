### 通过web终端登录到容器(推荐)
1.点击进入[容器服务控制台页面](https://console.cloud.tencent.com/ccs)。
2.选择容器所属服务，点击进入详情，查看实例列表，选择容器并连接远程终端。
3.更多远程终端常见问题点击[查看详情](https://cloud.tencent.com/document/product/457/8638?!preview&lang=zh)

![Alt text](https://mc.qcloudimg.com/static/img/fd06e590a5e2d109d5489b1df55454e5/20170316160930.png)

### 通过容器所在节点登录到容器
1.获取容器所在节点IP地址，容器ID。
![Alt text](https://mc.qcloudimg.com/static/img/50e98338f439b70cd74120ea9c8da26b/%7B398D6714-100A-424F-8D29-CAB5271D0A51%7D.png)

2.登录到节点，详情查看[登录到云主机](https://cloud.tencent.com/doc/product/213/5436)。

3.通过docker ps命令查看需登录的容器。
```shell
[root@VM_88_88_centos ~]# docker ps | grep 75b3b15af61a  
75b3b15af61a       nginx:latest                                 "nginx -g 'daemon off"   About a minute ago   Up About a minute                       k8s_worid.e8b44cc_worid-24bn2_default_81a59654-aa14-11e6-8a18-52540093c40b_42c0b746
```
4.通过docker exec命令登录到容器。
```shell
[root@VM_0_60_centos ~]# docker ps | grep 75b3b15af61a
75b3b15af61a        nginx:latest                                 "nginx -g 'daemon off"   2 minutes ago       Up 2 minutes                            k8s_worid.e8b44cc_worid-24bn2_default_81a59654-aa14-11e6-8a18-52540093c40b_6b389dd2
[root@VM_0_60_centos ~]# docker exec -it 75b3b15af61a /bin/bash
root@worid-24bn2:/# ls
bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
```

### 容器已安装SSH服务端，通过SSH登录到容器
1.获取容器IP地址。
![Alt text](https://mc.qcloudimg.com/static/img/dd26c4cd651ef1dcbc3073dd326f417e/%7BB64BB446-EAA1-4804-B86C-09BE10B6A1C2%7D.png)

2.登录集群内任意节点,详情查看[登录到云主机](https://cloud.tencent.com/doc/product/213/5436)。

3.通过SSH登录到容器。

### 通过管理节点登录到容器
敬请期待。

