本篇文档介绍如何在 CentOS 系统下部署 nginx 项目，适用于刚开始使用腾讯云的个人用户。
## 软件版本
本篇文档在示例步骤中的软件版本如下，在实际操作时，请您以实际软件版本为准。
- 操作系统：CentOS 7.5
- Nginx 版本：nginx 1.12.2

## 安装 nginx
购买完成后，在云服务器的详情页面，单击【登录】，可以直接登录云服务器，输入自己的用户名密码后，开始搭建 nginx 环境。有关如何创建云服务器实例，请参考 [购买并启动云服务器实例](https://cloud.tencent.com/document/product/213/4855)。

```
# 安装 nginx：
yum -y install nginx  

# 查看 nginx 版本
nginx -v

# 查看 nginx 安装目录
rpm -ql nginx

# 启动 nginx
service nginx start
```
现在访问该云服务器的公网 IP 地址，出现如下页面表示 nginx 部署完成：
![](https://main.qcloudimg.com/raw/c3d248fcfdfa45ad40c96cdca6769551.png)
nginx 的默认根目录 root 是`/usr/share/nginx/html`，我们直接修改 html 下的 index.html 静态页面，用来标识这个页面的特殊性。
```
vim /usr/share/nginx/html/index.html
# 在页面中输入
Hello nginx , This is rs-1!
URL is index.html
```

应用型负载均衡可以根据后端服务器的路径来进行请求转发，现在在 /image 路径下部署静态页面，相关命令如下：
```
# 新建目录 image
mkdir /usr/share/nginx/html/image
cd /usr/share/nginx/html/image
vim index.html
# 在页面中输入
Hello nginx , This is rs-1!
URL is image/index.html
```

> 注：nginx 的默认端口是 `80`，如果想修改端口请修改配置文件并重启 nginx。

## 验证 nginx 服务
访问云服务器的公网 IP + 路径，如果可以显示出已部署好的静态页面，则证明 nginx 部署成功。
rs-1 的 index.html 页面：
![](https://main.qcloudimg.com/raw/02c7524bedbd68ae25a36577a2fcb148.png)
rs-1 的 /image/index.html 页面:
![](https://main.qcloudimg.com/raw/5663e2ee65aede1069a8ecf0d6003cc4.png)
