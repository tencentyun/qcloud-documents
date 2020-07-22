## 实践-容器服务CI/CD工作流
本文主要叙述如何通过 Tencent Hub 实现容器服务 CI/CD 工作流，以部署开源 PHP 游戏网页游戏 2Moons 为例。

### 前期资源
- [游戏源码](https://github.com/jkroepke/2Moons)
- [Tencent Hub](https://cloud.tencent.com/product/thub)
- [TKE](https://cloud.tencent.com/product/ccs)
- 预先准备一个备案过的域名(eg:game.tdemo.net 或直接使用 IP)  

>?例子中为了方便测试，数据库也部署在 TKE 里面，生产环境一般会使用 TencentDB 实例。

### 准备工作
1. fork 游戏源码到自己的 github 方便后续修改和提交。这里 fork 到`https://github.com/Kevin-Qiu/2Moons`并新建`tencent_cloud`分支。   
2. 准备好 Dockerfile，可以参考`https://github.com/Kevin-Qiu/2Moons/blob/tencent_cloud/docker-compose.yml` 。 
![](https://main.qcloudimg.com/raw/bf260b3639ac37b5bbe7c1f588855c92)  
`https://github.com/Kevin-Qiu/2Moons/blob/tencent_cloud/Dockerfile`
![](https://main.qcloudimg.com/raw/3df9e45c7a7a8ce609a92d62d4eb6472)
3. 准备好 TKE 集群，对于这个例子来说，集群里面建议最好有4核 8G 的空闲资源，集群开启外网访问并记下账号/密码/证书/地址。
![](https://main.qcloudimg.com/raw/208b6f8337676af0b407660991806d56)  
![](https://main.qcloudimg.com/raw/82753f25ab10f27687b8764f95d6ee43)
4. 预先在 TKE 里面部署好 2Moon 需要的数据库，服务名 mariadb，1C2G，环境变量可以参考 `https://github.com/Kevin-Qiu/2Moons/blob/tencent_cloud/docker-compose.yml`，端口 3306，只允许集群内访问。
![](https://main.qcloudimg.com/raw/0394fe0fac5009bfb0b49f723e249ff9) 
![](https://main.qcloudimg.com/raw/3ed268c9d639e0f2e556012e9e4d7fbb) 
![](https://main.qcloudimg.com/raw/4c620032dea5c361913564613b310087) 
![](https://main.qcloudimg.com/raw/50d4f303764be4d9433a9752e6869a11)  
![](https://main.qcloudimg.com/raw/bbe07c0c0f16e9a5fb24a4df9ffd5e61)
    
### 持续集成 CI  
1. 先在 Tencent Hub 里面绑定 github。
![](https://main.qcloudimg.com/raw/9a94439aefae2a1f338ddb1dd5ad9399) 
2. 在 Tencent Hub 里面建立一个组织和仓库 demo/game，并记录下仓库地址/镜像地址。
![](https://main.qcloudimg.com/raw/a3847c5f03fa34b67896e9054e54ef21)
![](https://main.qcloudimg.com/raw/031a05168ea46f3e0e71ff4c1e250b5e)
![](https://main.qcloudimg.com/raw/0152f1cee6b2f58b9a117d540114e05e) 
3. 准备好需要部署到 TKE 的 yaml 文件。
`https://github.com/Kevin-Qiu/2Moons/blob/tencent_cloud/deploy.yaml`
![](https://main.qcloudimg.com/raw/0ef31b90963c272e391fdab62a7e1476) 
![](https://main.qcloudimg.com/raw/6c324d29fea5442e34b67b39bab1e022) 
4. 在仓库下面建立工作流，填入工作流名称，选择 github 项目，绑定自动和手动触发分支。
![](https://main.qcloudimg.com/raw/6662b50d549e9840ca45a525ebe589b6) 
![](https://main.qcloudimg.com/raw/dc07e1a482a4ce233acddafd50de8eb5) 
![](https://main.qcloudimg.com/raw/e834af4e497a548b169044c2aa0167a8) 
![](https://main.qcloudimg.com/raw/eca1f5bb92ae54d17efe00ae59062757) 
![](https://main.qcloudimg.com/raw/702a6b632f72a90e7f6fbf22261f8757)
![](https://main.qcloudimg.com/raw/57cc978a16d0d5ecf7fdcd085e2d99cf) 
5.推送代码到`https://github.com/Kevin-Qiu/2Moons` 的 `Tencent_Cloud`分支测试一下前面的 CI 结果，单击查看执行历史可以查看执行明细。 
![](https://main.qcloudimg.com/raw/9bd6d7622062836054cbd5d0ca6e3cc6)
![](https://main.qcloudimg.com/raw/b9c90e526d7e8fae6b3a34b63e9ad59e)
![](https://main.qcloudimg.com/raw/e4fca7b6494699139570b3dc0e373e0e) 
或者可以手动单击立即执行进行手动构建。
![](https://main.qcloudimg.com/raw/b2ebd9db790b999ad4c7b3b1e36390b0)
![](https://main.qcloudimg.com/raw/78327c840981a664e39463393afadff3)
![](https://main.qcloudimg.com/raw/90107ac71c7427fd4ec8cba1dacd1dcc) 
   
### 持续部署 CD
1. 单击查看与编辑继续完成 CD 部分，创建一个 CD 的 stage。
![](https://main.qcloudimg.com/raw/0bb55ea6ddcf90306159dcade08709ad)
2. 修改 Job 名为 deploy，选择工作流组件为 `kubectl_cmd` 组件。
![](https://main.qcloudimg.com/raw/17a5686fdca49e2ddfb0c5b4f2ad9459)
3. 把前面准备好的集群信息填入环境变量。
![](https://main.qcloudimg.com/raw/8c10be4527fb0e9d0ca44871596a16ec) 
4. 把前面准备好的 deploy 模板填入输入参数(这里支持多行文本)。
![](https://main.qcloudimg.com/raw/4be94e7cd9a44549983e00ded511ec0a) 
5. 从前面的 Job 里面选择输出注入到输入参数 `IMAGE_DIGEST` 中。
![](https://main.qcloudimg.com/raw/fad0e479f0ed0d42baefbe06e6a27c4b) 
![](https://main.qcloudimg.com/raw/9ae353382ea5cdad9e0f305529b546e4) 
![](https://main.qcloudimg.com/raw/975786b5d22c802c11f98d781a6a0cb5) 
![](https://main.qcloudimg.com/raw/5e7fb591759a36de7f3965902a906951) 
6. 最后构建 CD 的执行命令,参考命令如下：
`echo "$DEPLOY_TEMPLATE" | sed 's?$IMAGE_DIGEST?'"$IMAGE_DIGEST"'?g'  >> /tmp/deploy.yaml`
`cat /tmp/deploy.yaml`
`kubectl apply -f /tmp/deploy.yaml`
![](https://main.qcloudimg.com/raw/35696894bb14504f77aae09c8e97e693) 
填写完毕后保存。
7. 推送代码到 `https://github.com/Kevin-Qiu/2Moons` 的 `Tencent_Cloud` 分支测试一下前面的 CICD 结果，单击查看执行历史可以查看执行明细。
![](https://main.qcloudimg.com/raw/74c51e821a5bfa17e73cbedd6d36397c)
![](https://main.qcloudimg.com/raw/5e2751db6ece0961b59812eefdcf3e02)
![](https://main.qcloudimg.com/raw/3936f2edb3e8aa2ac787bbcd75dbc721)
![](https://main.qcloudimg.com/raw/234fcc7a179ce3928c7ba96d1e3956f7)
可以在执行参数这里查看参数传递是否有误。
![](https://main.qcloudimg.com/raw/dcbd971d4e37ec46c30bb956063a0a22)
执行结果为成功。
8.切换到 TKE 查看一下部署情况。
![](https://main.qcloudimg.com/raw/bf42f0cf3aef782531d558ea6d0c4954)
![](https://main.qcloudimg.com/raw/f42bfb74bd912c15ad17b936399a5445)
![](https://main.qcloudimg.com/raw/93a0475dde7abe848e3652e7358343f6)
Deploy 已经顺利执行。
配置一下 game.tdemo.net 域名指向为 ingress 的外网 IP。
![](https://main.qcloudimg.com/raw/15e1c6001c98edd3ccbd5538e34373a9)
![](https://main.qcloudimg.com/raw/2fc82a422a6f4db220943ae8e0d354c6)
![](https://main.qcloudimg.com/raw/73c9f1612c12b450b3c9f99df1b1f7c0)
![](https://main.qcloudimg.com/raw/9cb02e0ab8187bbbe68bcd09fe008087)
游戏到这里就部署好了。
  
