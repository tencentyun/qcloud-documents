## 现象描述
执行命令或系统启动的过程中，出现命令找不到，或 lib 库找不到等报错信息。


## 可能原因
CentOS 7、CentOS 8、Ubuntu 20 等系统的 bin、sbin、lib 及 lib64 是软链接。如下所示：
```
lrwxrwxrwx   1 root root     7 Jun 19  2018 bin -> usr/bin
lrwxrwxrwx   1 root root     7 Jun 19  2018 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Jun 19  2018 lib64 -> usr/lib64
lrwxrwxrwx   1 root root     8 Jun 19  2018 sbin -> usr/sbin
```
若软链接被删除，则会导致在执行命令或系统启动的过程中出现报错。


## 解决思路
参考 [处理步骤](#ProcessingSteps)，检查并新建所需软链接。


## 处理步骤[](id:ProcessingSteps)
1. 参考 [使用救援模式](https://cloud.tencent.com/document/product/213/66678)，进入救援模式。
2. 执行其中的 `mount` 及 `chroot` 等命令。其中，执行 `chroot` 命令时：
 - 有报错，执行 `cd /mnt/vm1`。
 - 无报错，执行 `cd /`。
3. 执行以下命令， 查看对应的软链接是否存在。
```
ls -al / | grep -E "lib|bin"
```
 - 是，则请通过 [在线支持](https://cloud.tencent.com/act/event/Online_service?from=doc_213) 联系我们寻求帮助。
 - 否，则请按需执行以下命令，新建对应软链接。
```
ln -s usr/lib64 lib64
ln -s usr/sbin sbin
ln -s usr/bin bin
ln -s usr/lib lib
```
4. 执行以下命令，检查软链接。
```
chroot /mnt/vm1 /bin/bash
```
无报错信息，则说明软链接已成功修复。
5. 参考 [使用救援模式](https://cloud.tencent.com/document/product/213/66678)，退出救援模式，启动系统。
