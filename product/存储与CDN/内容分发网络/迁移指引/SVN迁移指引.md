#### 迁移须知

迁移过程中请勿向 SVN 中更新资源，迁移完成后，请修改您业务中对应的 SVN 服务域名为 COS 的加速域名。

#### 1 安装 SVN 客户端

迁移 SVN 前，您需要将 SVN 服务器上的资源同步至本地。
推荐使用1.7版本的 SVN 客户端。请不要升级到1.8版本，1.8版本存在缺陷，可能会导致 SVN 同步异常。
- [SVN 客户端下载](http://subversion.apache.org/download/ )
- [SVN 中文简介](http://www.subversion.org.cn/?action-channel-name-product )
- [SVN 手册](http://svndoc.iusesvn.com/)

#### 2 迁出 SVN 数据

连接 SVN 库并迁出数据到本地服务器上：

1. 选择要存储 SVN 文件的目录，cd 进入该目录，执行 svn checkout 命令（CDN 服务的 SVN 路径获取，详见：[CDN 文件发布](http://cloud.tencent.com/doc/product/228/CDN%E6%96%87%E4%BB%B6%E5%8F%91%E5%B8%83)），拿云服务账号为1251991073的开发者举例，执行的命令如下所示：
```
svn checkout https://cdn.yun.qq.com/1251991073
```
2. 输入用户名和密码（即云服务账号和密码，详见：[CDN 文件发布](http://cloud.tencent.com/doc/product/228/CDN%E6%96%87%E4%BB%B6%E5%8F%91%E5%B8%83)）。
在您还没有上传任何文件到 SVN 库之前，这里 checkout 出来的只是目录，目录下没有文件（除了自动生成的 .svn 文件夹）。

#### 3 创建Bucket

登录 [COS 控制台](https://console.cloud.tencent.com/cos)，若未开通，请单击开通 COS 对象存储服务，在左侧单击【Bucket列表】：
![](https://mc.qcloudimg.com/static/img/b87d5d718cf5c7e8b6d93cd2acc78783/cos-1.png)

单击【创建Bucket】，填充如下项：
+ 选择【所属项目】: 您可以根据需要对该源站进行分项目管理
+ 填写 Bucket 名称：为 bucket 命名，示例中填写 APPID
+ 填写所属地域：根据需要选择 COS 所在园区
+ 访问权限：选择【公有读私有写】
+ CDN 加速：选择【开启】
  ![](https://mc.qcloudimg.com/static/img/30e118a44492ab71bc026ff503bf6ca7/cos-2.png)
此时可以看到该 bucket 对应的域名为：
![](https://mc.qcloudimg.com/static/img/e3cfe25fbc8f24caa5e7155c333a8b4c/cos-3.png)

#### 4 同步资源
利用 COS 本地同步工具，将本地资源同步至指定 bucket，使用方式可参考 [工具指南](https://cloud.tencent.com/document/product/436/15392)。


#### 5 资源 URL 变更
资源同步完毕后，可以看到原有路径：
```
http://1251991073.cdn.myqcloud.com/1251991073/image/1.png
```
通过 COS 的访问路径变为：
```
http://1251991073-1251991073.costj.myqcloud.com/image/1.png
```
您可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 查看该域名的流量带宽实时统计、分析数据：
![](https://mc.qcloudimg.com/static/img/97fab7ced01a83251798c55539d17991/cos-4.png)
COS 加速域名在 CDN 控制台上能够进行配置管理、查看统计分析数据、日志下载、刷新预热等功能。
更多 COS 使用指南可参考 [对象存储](https://cloud.tencent.com/document/product/436)。

