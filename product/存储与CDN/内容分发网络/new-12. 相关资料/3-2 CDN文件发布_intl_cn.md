## 1. 文件发布步骤
Step1. 通过SVN上传/更新CDN文件
SVN的使用方式详见Windows环境下SVN使用指引或Linux环境下SVN使用指引。
使用SVN时，需要填写SVN库路径，以及用户名和密码，这些信息可在管理中心的CDN“文件发布”页面查看到，如下图所示：
![](https://mccdn.qcloud.com/static/img/56f91c137833a1667c82a1b9aecc6b0b/image.png)

Step2. 将文件生效到各CDN服务器上
在CDN“文件发布”页面，点击“CDN文件生效”按钮，则新上传文件会在5分钟内同步到各CDN服务器上。

简化的文件发布步骤：
![](https://mccdn.qcloud.com/static/img/625b3e88e1bac241fe7bcd619618c406/image.png)
Step1. 设置自动生效功能
如果开发者可以保证上传到CDN服务器的文件的正确性和有效性，则可以先在CDN“文件发布”页面，设置自动生效为“已启用”状态。


Step2. 通过SVN上传/更新CDN文件
SVN上的文件变更会自动同步到各CDN服务器节点，不需要每次更新后点击“CDN文件生效”按钮。
注意：自动生效开启前的SVN上的文件变更不会自动同步，如果需要同步，请点击“CDN文件生效”按钮。

## 2. 访问CDN发布的文件
通过CDN发布的文件，您可以通过CDN文件发布界面给出的url地址访问到。
![](https://mccdn.qcloud.com/static/img/7f4bda0577446fa6e2ce4eb5888df912/image.png)

例如：
您的云服务帐号为1251000013。通过SVN客户端，在 https://cdn.yun.qq.com/1251000013 下创建文件目录img，在img目录下上传文件CVM.png。生效后，就可以通过如下CDN公网访问地址，访问到CVM.png这个图片了。
`http://1251000013.cdn.myqcloud.com/1251000013/img/CVM.png`