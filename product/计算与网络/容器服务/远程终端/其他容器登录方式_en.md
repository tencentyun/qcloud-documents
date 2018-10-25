### Logging in to Container on Console (Recommended)
1. Log in to [CCS Console](https://console.cloud.tencent.com/ccs).
2. Select the service to which the container belongs and enter the details page to view the list of pods. Select container and connect to the remote console.
3. For the FAQs on the Remote Terminal, please see [Details](https://cloud.tencent.com/document/product/457/8638)

![Alt text](https://mc.qcloudimg.com/static/img/fd06e590a5e2d109d5489b1df55454e5/20170316160930.png)

### Logging in to Container via the Container's Node
1. Acquire the IP address of the node where the container resides and the container's ID.
![Alt text](https://mc.qcloudimg.com/static/img/50e98338f439b70cd74120ea9c8da26b/%7B398D6714-100A-424F-8D29-CAB5271D0A51%7D.png)

2. Log in to the node. For more information, please see [Logging in to CVM](https://cloud.tencent.com/doc/product/213/5436).

3. View the container you wish to log in to by using the ``docker ps`` command.
```shell
[root@VM_88_88_centos ~]# docker ps | grep 75b3b15af61a  
75b3b15af61a       nginx:latest                                 "nginx -g 'daemon off"   About a minute ago   Up About a minute                       k8s_worid.e8b44cc_worid-24bn2_default_81a59654-aa14-11e6-8a18-52540093c40b_42c0b746
```
4. Log in to the container by using the "docker exec" command.
```shell
[root@VM_0_60_centos ~]# docker ps | grep 75b3b15af61a
75b3b15af61a        nginx:latest                                 "nginx -g 'daemon off"   2 minutes ago       Up 2 minutes                            k8s_worid.e8b44cc_worid-24bn2_default_81a59654-aa14-11e6-8a18-52540093c40b_6b389dd2
[root@VM_0_60_centos ~]# docker exec -it 75b3b15af61a /bin/bash
root@worid-24bn2:/# ls
bin  boot  dev	etc  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var
```

### Logging in to Container via SSH Key (when SSH Service is Already Installed on the Container)
1. Check the IP address of the container.
![Alt text](https://mc.qcloudimg.com/static/img/dd26c4cd651ef1dcbc3073dd326f417e/%7BB64BB446-EAA1-4804-B86C-09BE10B6A1C2%7D.png)

2. Log in to any node within the cluster. For more information, please see [Log in to CVM](https://cloud.tencent.com/doc/product/213/5436).

3. Log in to the container via SSH Key.

### Logging in to Container via Management Node
Available soon.


