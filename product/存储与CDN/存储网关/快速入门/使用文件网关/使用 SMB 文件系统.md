

创建文件系统后，请在其他服务器或客户端上按照如下指引进行配置，挂载该文件系统并使用。SMB 网关支持 CIFS、 SMB2.0 及 SMB 3.0。

>!若在 CVM 上使用网关，建议将网关部署在各来访客户端的 VPC 下；如果在不同 VPC 时，请使用 [对等连接](https://cloud.tencent.com/document/product/215/5000) 方法实现网络互通。


## 创建 SMB 用户并分配权限
在存储网关控制台创建用来访问文件系统的用户，设置用户名及密码，并为该用户分配文件系统权限。
![](https://mc.qcloudimg.com/static/img/26b6ad3bfa669ad01dc0852cd810df26/image.png)

## 添加访问白名单
在文件系统处，添加来访客户端的 IP 到 "允许访问地址" 中以获得访问权限 。如果使用 CVM 来访，建议将外网地址和内网地址都添加到来访地址中（ 可以到 CVM 控制台获取内网和外网 IP ）。
![](https://mc.qcloudimg.com/static/img/ba1f23f1ceaec7a46e47a25594960b39/image.png)


## 打开 "映射网络驱动器"
登录到需要挂载文件系统的 Windows 上，在 "开始" 菜单中找到 "计算机"，单击鼠标右键出现菜单，单击菜单中的 "映射网络驱动器"。 
![](https://mc.qcloudimg.com/static/img/5696d66a83d4e9b35196274f89e07dfc/image.png)
![](https://mc.qcloudimg.com/static/img/6eeb1c0838e6aab185ed8b76dc736912/image.png)

## 输入访问路径
在弹出的设置窗口中设置 "驱动器" 盘符名称及文件夹（即在 SMB 文件系统中看到的挂载目录）。
![](https://mc.qcloudimg.com/static/img/004ef32b0b934ed6d666405a38fff999/image.png)

## 输入用户名密码
单击【完成】按钮后，在弹出的窗口中输入第一步创建的用户名密码，单击确认完成挂载。
![](https://mc.qcloudimg.com/static/img/27f2f6fdcb2f75ea974ef96bdb90ef28/image.png)

>!请勿从多台客户端主机上使用相同用户名密码访问同一文件系统，该操作会被系统自动识别为非法（文件系统会锁住）。

## 验证读写
确认后，页面直接进入到已经挂载的文件系统中。可以右键新建一个文件来验证读写的正确性。
![](https://mc.qcloudimg.com/static/img/60b9388885536ec7d81b1cf7f76c39d5/image.png)

## 断开文件系统
要断开已经挂载的文件系统，只需鼠标右键单击磁盘，再出现的菜单中单击【断开】选项，即可断开文件系统的连接。
![](https://mc.qcloudimg.com/static/img/376cd0547aa64f4d519e5444c5a58f93/image.png)
