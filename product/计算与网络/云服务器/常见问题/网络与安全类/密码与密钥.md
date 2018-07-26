### SSH 密钥登录与密码登录有何区别？
SSH 密钥是一种远程登录 Linux 服务器的方式，其原理是利用密钥生成器制作一对密钥（公钥和私钥）。将公钥添加到服务器，然后在客户端利用私钥即可完成认证并登录，这种方式更加注重数据的安全性，同时区别于传统密码登录方式的手动输入，又具有更高的便捷性。
目前 Linux 实例有密码和 SSH 密钥两种登录方式，Windows 实例目前只有密码登录一种方式。相关文档参考：
- [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)
- [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)

### 使用 SSH 密钥登录还可以同时使用密码登录吗？
用户使用 SSH 密钥对登录 Linux 实例，默认禁用密码登录，以提高安全性，所以密钥登录后用户将不能再使用密码登录。

### 忘记密码怎么办？
您可以登录云服务器控制台，对相应的云服务器进行重置密码，然后使用新密码登录实例。重置密码的详细操作指南，参见 [登录密码操作指南](https://cloud.tencent.com/document/product/213/17008) 的重置密码部分。

### 如何创建 SSH 密钥以及密钥丢失怎么办？
关于密钥的创建，可以参考 [SSH 密钥](https://cloud.tencent.com/document/product/213/16691) 的创建密钥部分，针对密钥丢失问题，我们提供两种方法解决：

 - 通过云服务器的 SSH 密钥控制台创建新的密钥，并使用新的密钥绑定原有实例。详情可参考 [SSH 密钥](https://cloud.tencent.com/document/product/213/16691)。创建新的密钥后，您可以在云服务器控制台 > 云主机页面 > 加载密钥，即可使用新的密钥登录实例。
 - 通过云服务器控制台重置密码，然后使用新密码登录实例。详情参见 [登录密码操作指南](https://cloud.tencent.com/document/product/213/17008) 的重置密码部分。

### 如何将 SSH 密钥绑定/解绑服务器？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **密钥绑定/解绑服务器** 部分。

### 如何修改 SSH 密钥名称/描述？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **修改 SSH 密钥名称/描述** 部分。

### 如何删除 SSH 密钥？

请参考 [SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691) **删除 SSH 密钥** 部分。

### SSH 密钥有哪些使用限制？

请参考 [SSH 密钥简介](https://cloud.tencent.com/document/product/213/6092) **使用限制** 部分。

### 使用 SSH 密钥无法登录 Linux 实例，如何排查？

您可以参考以下解决方案：

1. 在 [云服务器控制台](https://console.cloud.tencent.com/cvm/sshkey) 检查密钥是否与云服务器绑定，具体操作是通过搜索密钥名称找到密钥 ID，单击 ID 查看绑定该密钥的云服务器。

2. 在 [控制台](https://console.cloud.tencent.com/cvm/securitygroup) 取消或者修改安全组策略。参考：[安全组操作指南](https://cloud.tencent.com/document/product/213/12450)

3. 在 [控制台](https://console.cloud.tencent.com/cvm/sshkey) 取消密钥登录方式，或根据指导正确设置密钥验证登录机器。参考：[SSH 密钥操作指南](https://cloud.tencent.com/document/product/213/16691)

4. 使用 VNC 登录实例，查看网卡状态及 IP 配置信息是否正确。参考：[登录 Linux 实例操作指南](https://cloud.tencent.com/document/product/213/5436)
![](https://main.qcloudimg.com/raw/17fa30409db52577fc8fed99a43264d2.png)

5. 确认机器的 sshd 服务运行 OK，且端口等配置文件没有问题。
   ![](https://main.qcloudimg.com/raw/32364a0beac01cc63c82d61ebadf89c2.png)

6. 确认机器的 iptables 防火墙是否拦截，检查其策略是否 OK。![](https://main.qcloudimg.com/raw/9dbc3baa79c24673e59fb228cc57afad.png)

7. 确认机器的 tcp_wrappers 是否有对 ssh 访问的拦截控制。
   ![](https://main.qcloudimg.com/raw/76ac9f09b606cbd7f2121f4306ff3bc8.png)

8. 确认是否 ssh 登录机器的用户被 PAM 模块拦截登录（不常见）：
   ![](https://main.qcloudimg.com/raw/c7af6184b32867d0eb77cdfe1c362d04.png)

9. 确认实例是否正确地运行在模式 3 或模式 5：
   ![](https://main.qcloudimg.com/raw/0371d6b8c5a0b89ac70cff6b56adf3be.png)
