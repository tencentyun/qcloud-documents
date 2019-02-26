### 使用 SSH 密钥登录有哪些限制？

请参考 [SSH 密钥简介](https://cloud.tencent.com/document/product/213/6092) **使用限制** 部分。

### 如何创建 SSH 密钥？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **创建 SSH 密钥** 部分。

### 如何将 SSH 密钥绑定/解绑服务器？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **密钥绑定/解绑服务器** 部分。

### 如何修改 SSH 密钥名称/描述？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **修改 SSH 密钥名称/描述** 部分。

### 如何删除 SSH 密钥？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **删除 SSH 密钥** 部分。

### 使用 SSH 密钥无法登录 Linux 实例，如何排查？

您可以参考以下解决方案：

1. 在 [控制台](https://console.cloud.tencent.com/cvm/securitygroup) 取消或者修改安全组策略。参考：[安全组操作指南](https://cloud.tencent.com/document/product/213/12450)

2. 在 [控制台](https://console.cloud.tencent.com/cvm/sshkey) 取消密钥登录方式，或根据指导正确设置密钥验证登录机器。参考：[SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691)

3. 使用 VNC 登录实例，查看网卡状态及 IP 配置信息是否正确。参考：[登录 Linux 实例操作指南](https://cloud.tencent.com/document/product/213/5436)

   ![](https://main.qcloudimg.com/raw/17fa30409db52577fc8fed99a43264d2.png)

4. 确认实例是否正确地运行在模式 3 或模式 5：
   ![](https://main.qcloudimg.com/raw/0371d6b8c5a0b89ac70cff6b56adf3be.png)

5. 确认机器的 sshd 服务运行 OK，且端口等配置文件没有问题。
   ![](https://main.qcloudimg.com/raw/32364a0beac01cc63c82d61ebadf89c2.png)

6. 确认机器的 iptables 防火墙是否拦截，检查其策略是否 OK。![](https://main.qcloudimg.com/raw/9dbc3baa79c24673e59fb228cc57afad.png)

7. 确认机器的 tcp_wrappers 是否有对 ssh 访问的拦截控制。
   ![](https://main.qcloudimg.com/raw/76ac9f09b606cbd7f2121f4306ff3bc8.png)

8. 确认是否 ssh 登录机器的用户被 PAM 模块拦截登录（不常见）：
   ![](https://main.qcloudimg.com/raw/c7af6184b32867d0eb77cdfe1c362d04.png)