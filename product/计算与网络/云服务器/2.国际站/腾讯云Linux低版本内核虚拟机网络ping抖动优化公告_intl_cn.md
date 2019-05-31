
尊敬的腾讯云用户：
您好，

在已知特定场景下，您的云服务器网络繁忙时，ping云服务器会有20ms到100ms不等的ping抖动。如图所示：
![](//mc.qcloudimg.com/static/img/e82e1c21f7658006ca2eb155d6fbf9d4/image.jpg)
【受影响虚拟机配置】
1. 单队列多云服务器
2. 装有如下所示受影响的版本内核
>2.6.18版本：所有
>2.6.32版本：centos 2.6.32-174.el6之前的内核版本
>
>注：3.0之后的内核版本不受影响


3. virtio0-input中断的smp_affinity配置成分发到所有核，例如4核云服务器配置成f，8核云服务器配置成ff
    1) `cat /proc/interrupts |grep virtio0-input |cut -d: -f 1` 查看virtio0-input的中断号
    2) `cat /proc/irq/<中断号>/smp_affinity` 查看中断亲和度
    

【原因】
在云服务器繁忙时配置网卡中断发送到所有核会引起网卡中断的重入，重入会导致额外的虚拟机退出，从而影响网络中断处理并造成ping抖动。
2011年内核增加了新的特性避免了上述问题,具体可点击[这里](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/commit/?id=a5c262c5fd83ece01bd649fb08416c501d4c59d7) 查看详情。


【修正方法】
将网卡中断亲和度设置到一个核上：
1.`cat /proc/interrupts |grep virtio0-input |cut -d: -f 1` 查看virtio0-input的中断号
2. `echo 1 > /proc/irq/<中断号>/smp_affinity`

腾讯云
2016-12-08







