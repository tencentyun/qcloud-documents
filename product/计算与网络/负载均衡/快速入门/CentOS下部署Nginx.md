本文将为您详细介绍如何在 CentOS 系统下部署 Nginx 项目，适用于刚开始使用腾讯云的个人用户。
## 软件版本
本文在示例步骤中的软件版本如下，在实际操作时，请您以实际软件版本为准。
- 操作系统：CentOS 7.5
- Nginx 版本：Nginx 1.16.1

## 安装 Nginx
1. 购买完成后，在云服务器的详情页面，单击**登录**，可以直接登录云服务器，输入自己的用户名密码后，开始搭建 Nginx 环境。有关如何创建云服务器实例，请参见 [创建云服务器实例](https://cloud.tencent.com/document/product/213/4855)。
```
# 安装 Nginx：
yum -y install nginx  
# 查看 Nginx 版本
nginx -v
# 查看 Nginx 安装目录
rpm -ql nginx
# 启动 Nginx
service nginx start
```
2. 访问该云服务器的公网 IP 地址，出现如下页面则表示 Nginx 部署完成：
![](https://main.qcloudimg.com/raw/18c20d96d9b4e4d50a60da6f0c55c3e3.png)
3. Nginx 的默认根目录 root 是`/usr/share/nginx/html`，直接修改 `html` 下的 `index.html`静态页面，用来标识这个页面的特殊性，相关操作如下：
   1. 执行如下命令，进入html 下的 index.html 静态页面：
```bash
vim /usr/share/nginx/html/index.html
```
   2. 按“i”进入编辑模式，请在`<body></body>`标签内输入：
```bash
# 建议直接在<body>下方输入
Hello nginx , This is rs-1!
URL is index.html
```
    ![](https://main.qcloudimg.com/raw/02e833dd08a6873d5d015f4531d24645.png)
   3. 按 “Esc”，输入`:wq` 保存编辑。
4. 负载均衡（原“应用型负载均衡”）可以根据后端服务器的路径来进行请求转发，在`/image`路径下部署静态页面，相关操作如下：
   1. 依次执行如下命令，新建目录 `image` 并进入该目录：
```bash
mkdir /usr/share/nginx/html/image
cd /usr/share/nginx/html/image
```
   2. 执行如下命令，在`image`目录下创建 `index.html`静态页面：
```
vim index.html
```
   3. 按“i”进入编辑模式，在页面中输入：
```bash
Hello nginx , This is rs-1!
URL is image/index.html
```
   4. 按 “Esc”，输入`:wq `保存编辑。
>!Nginx 的默认端口是`80`，如果想修改端口请修改配置文件并重启 Nginx。

## 验证 Nginx 服务
访问云服务器的公网 IP + 路径，如果可以显示出已部署好的静态页面，则证明 Nginx 部署成功。
- rs-1 的 index.html 页面：
![](https://main.qcloudimg.com/raw/58c504ca0c2e624f0ddb582d1f280760.png)
- rs-1 的 /image/index.html 页面：
![](https://main.qcloudimg.com/raw/98d56c43e02b8b7bd6b09e95e48625f9.png)

