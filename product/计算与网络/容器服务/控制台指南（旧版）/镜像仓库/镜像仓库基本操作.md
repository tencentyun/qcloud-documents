## 镜像仓库概述
镜像仓库用于存放 Docker 镜像，Docker 镜像用于部署容器服务，每个镜像有特定的唯一标识（镜像的 Registry 地址+镜像名称+镜像 Tag）。

## 镜像类型
目前镜像支持 Docker Hub 官方镜像和用户私有镜像。

## 开通镜像仓库
![Alt text](https://mc.qcloudimg.com/static/img/b0ce4b921b60f4f79fec6be455e16f4f/Image+005.png)
首次使用镜像仓库的用户，需要先开通镜像仓库。

- **命名空间**：命名空间是您创建的私人镜像地址的前缀。
- **用户名**：默认是当前用户的账号，是您登录到腾讯云 docker 镜像仓库的身份。
- **密码**：是您登录到腾讯云 docker 镜像仓库的凭证。

## 创建镜像
1. 单击镜像列表页【新建】按钮。
![Alt text](https://mc.qcloudimg.com/static/img/73e7951509c8bef8f7eaf703af6cb8df/Image+001.png)
2. 输入镜像名称和描述，然后【提交】。
![Alt text](https://mc.qcloudimg.com/static/img/026b93deb76bfaeff5a27d24878529a2/Image+003.png)

## 推送镜像到镜像仓库
### 登录到腾讯云 registry
```
$ sudo docker login --username=[username] ccr.ccs.tencentyun.com
```
username：腾讯云账号，开通时已注册。输入密码后即登录完成。
### 上传镜像
```
$ sudo docker tag [ImageId] ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
$ sudo docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
```
- ImageId 和镜像版本号根据镜像信息补充
- namespace 是开通镜像仓库时填写的命名空间
- ImageName 是在控制台创建的镜像名称


## 下载镜像
登录到镜像仓库，需输入密码。
```
$ sudo docker login --username=[username] ccr.ccs.tencentyun.com
```
下载镜像。
```
$ sudo docker pull ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
```

## 删除镜像
选择镜像，单击【删除】并【确定】。删除镜像会删除该镜像的所有版本。
![Alt text](https://mc.qcloudimg.com/static/img/7bc3adadf35e8d452a380c613abb264e/Image+050.png)
