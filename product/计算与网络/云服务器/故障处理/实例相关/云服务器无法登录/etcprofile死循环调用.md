## 现象描述
使用 SSH 登录 Linux 实例时，SSH 命令在输出 “Last login: ” 相关信息后卡住。


## 问题原因
可能由于 `/etc/profile` 文件被修改过，出现在 `/etc/profile` 中调用 `/etc/profile` 现象，导致陷入死循环调用，无法成功登录。



## 解决思路
参考 [处理步骤](#ProcessingSteps)，检查并修复 `/etc/profile` 文件。


## 处理步骤[](id:ProcessingSteps)
1. [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，查看 `/etc/profile` 文件。
```
vim  /etc/profile
```
3. 检查 `/etc/profile` 文件中是否包含 `/etc/profile` 相关命令。
 - 是，则执行下一步。
 - 否，则请通过 [在线支持](https://cloud.tencent.com/act/event/Online_service?from=doc_213) 联系我们寻求帮助。
4. 按 **i** 进入编辑模式，在 `/etc/profile` 相关命令前增加 `#` 以注释该命令。
5. 按 **Esc** 退出编辑模式，并输入 **:wq** 保存修改。
6. 重新 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 进行登录。
