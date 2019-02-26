#### 迁移须知

迁移过程中请勿向SVN中更新资源，迁移完成后，请修改您业务中对应的SVN服务域名为COS的加速域名。

#### 1 安装SVN客户端

迁移SVN前，您需要将SVN服务器上的资源同步至本地。
推荐使用1.7版本的SVN客户端。请不要升级到1.8版本，1.8版本存在缺陷，可能会导致SVN同步异常。

SVN客户端下载：http://subversion.apache.org/download/ 
SVN中文简介：http://www.subversion.org.cn/?action-channel-name-product 
SVN手册：http://svndoc.iusesvn.com/

#### 2 迁出SVN数据

连接SVN库并迁出数据到本地服务器上：

1.选择要存储SVN文件的目录，cd进入该目录，执行svn checkout命令（CDN服务的SVN路径获取，详见：[CDN文件发布](http://cloud.tencent.com/doc/product/228/CDN%E6%96%87%E4%BB%B6%E5%8F%91%E5%B8%83)），拿云服务账号为1251991073的开发者举例，执行的命令如下所示：

```
svn checkout https://cdn.yun.qq.com/1251991073
```

2.输入用户名和密码（即云服务账号和密码，详见：[CDN文件发布](http://cloud.tencent.com/doc/product/228/CDN%E6%96%87%E4%BB%B6%E5%8F%91%E5%B8%83)）。

在您还没有上传任何文件到SVN库之前，这里checkout出来的只是目录，目录下没有文件（除了自动生成的.svn文件夹）。

#### 3 创建Bucket

登陆 [COS控制台](https://console.cloud.tencent.com/cos)，若未开通，请点击开通COS对象存储服务，在左侧点击【Bucket列表】：
![](https://mc.qcloudimg.com/static/img/b87d5d718cf5c7e8b6d93cd2acc78783/cos-1.png)

点击页面上【创建Bucket】按钮，填充如下项：
+ 选择【所属项目】: 您可以根据需要对该源站进行分项目管理
+ 填写 Bucket 名称：为bucket命名，示例中填写APPID
+ 填写所属地域：根据需要选择COS所在园区
+ 访问权限：选择【公有读私有写】
+ CDN加速：选择【开启】
  ![](https://mc.qcloudimg.com/static/img/30e118a44492ab71bc026ff503bf6ca7/cos-2.png)

此时可以看到该 bucket 对应的域名为：

![](https://mc.qcloudimg.com/static/img/e3cfe25fbc8f24caa5e7155c333a8b4c/cos-3.png)

#### 4 同步资源

利用COS本地同步工具，将本地资源同步至指定 bucket，使用方式可参考：
https://cloud.tencent.com/document/product/436/7133

#### 5 资源URL变更

资源同步完毕后，可以看到原有路径：

```
http://1251991073.cdn.myqcloud.com/1251991073/image/1.png
```

通过COS的访问路径变为：

```
http://1251991073-1251991073.costj.myqcloud.com/image/1.png
```

您可以在[CDN控制台](https://console.cloud.tencent.com/cdn) 查看该域名的流量带宽实时统计、分析数据：
![](https://mc.qcloudimg.com/static/img/97fab7ced01a83251798c55539d17991/cos-4.png)

COS加速域名在CDN控制台上能够进行配置管理、查看统计分析数据、日志下载、刷新预热等功能。

更多COS使用指南可参考：https://cloud.tencent.com/document/product/436

