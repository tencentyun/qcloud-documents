## 基于TencentHub 的持续集成和持续交付
### 整体流程
#### 图示

![Alt text][tencenthubcicd]
1. 通过容器服务镜像仓库设置镜像来源, 目前支持`源码构建`、`Dockerfile构建`、`手动上传` 三种方式。
2. 设置源码构建即可实现每次提交代码，自动生成容器镜像功能。
3. 若需要设置镜像生成后自动触发更新服务，则需要针对镜像设置触发器。
4. 设置源码构建和触发器完成后即可实现-提交代码后自动触发构建镜像，镜像生产自动触发更新服务。

#### 说明
1. 源码构建和触发器设置均是独立模块，可以只使用其中任意环节。
2. 源码构建&Dockerfile构建镜像可查看[源码构建概述](https://cloud.tencent.com/document/product/457/10151)。
3. 触发器可支持多种触发动作，详情查看[镜像触发器概述](https://cloud.tencent.com/document/product/457/10155)。

### 操作步骤
#### 第一步：设置源码持续构建镜像
1. 新建需要测试的镜像仓库`helloworld`, 进入helloworld详情页
![Alt text][step1]
2. 设置镜像构建设置需要关心以下几点：

 - 代码源：当前支持GitHub和Gitlab
 - 源码Repository：需要包含Dockerfile文件，Dockerfile文件是构建镜像的步骤描述；还需要包含所需代码, 同时在Dockerfile中添加代码。详情可见[如何编写Dockerfile](https://cloud.tencent.com/document/product/457/9115#dockerfile-.E8.87.AA.E5.8A.A8.E7.BC.96.E8.AF.91.E7.94.9F.E6.88.90.EF.BC.88.E6.8E.A8.E8.8D.90.E4.BD.BF.E7.94.A8.EF.BC.89)
 - 下述提供了本次测试Helloworld的Dockerfile和index文件, 将Dockerfile和index.html放在同一个根目录下。
 **Dockerfile文件**：
```shell
FROM nginx
#file author
MAINTAINER tencentcloudccs
ADD ./ /usr/share/nginx/html
```
**index.html文件**
```shell
hello world
```
- 触发方式：设置提交代码到分支触发
- Dockerfile路径：由于Dockerfile和index.html都根目录下，所以直接填写Dockerfile即可。更多见[源码构建Dockerfile路径设置](https://cloud.tencent.com/document/product/457/10618)
![Alt text][step2]

第一步设置完成后，即可实现每次提交代码，自动生成容器镜像功能。可提交代码进行测试，也可以手动执行立即构建。
![Alt text][step3]

#### 第二步：设置镜像仓库触发器持续部署服务
1. 首先需要一个目标服务，用户持续部署，如无，则需创建一个。这里我们创建一个[ginx服务](https://cloud.tencent.com/document/product/457/7851). 
2. 进入上述设置好源码构建的helloworld镜像仓库详情页，进入触发器设置
![Alt text][step4]
3. 添加完成一个触发器，需要关注以下几点：

- 触发条件： 根据生成的镜像的版本号(tag),判断是否执行触发动作， 若触发条件匹配则执行触发动作，这里选择全部触发,即只要有新的镜像tag生成就会执行触发动作。
- 触发动作：当前支持更新服务指定容器。 选择需要持续部署的服务和容器。

![Alt text][step5]

第二步设置完成后，即可手动上传镜像或手动构建镜像验证触发器。以下是手动构建验证测试。
#### 第三步：提交代码验证
通过上述第一步和第二步已经完成了持续集成镜像和持续交付服务，下述进行提交代码做整个流程的最终效果验证。
1. 通过公网访问该nignx服务，当前效果如下。
![Alt text][step6]
2. 更新index.html文件并提交到github。可查看部署过程
![Alt text][step7]
3. 再次访问该服务。
![Alt text][step8]

到此为止，已经完成基于TencentHub持续集成和持续交付的部署。


[tencenthubcicd]: https://mc.qcloudimg.com/static/img/34c83b4280eb33e35197083330dbad7d/%7BE5F1B207-719E-4F6D-B0AB-D390CED90D22%7D.png

[step1]: https://mc.qcloudimg.com/static/img/9b6de96e4af4dfa36e31e0f5608033e4/%7B8657D57E-E403-4E63-B5EC-894CF5BC864E%7D.png

[step2]: https://mc.qcloudimg.com/static/img/7ed37353251703dbf0f2b9e4ee39ed37/%7B611F6AE1-8E51-4CFF-95BB-DB6F7ECBBC70%7D.png

[step3]:https://mc.qcloudimg.com/static/img/1f9872b83b828d91bc2df9a7fb2fe08f/%7B8EA0E3A0-0A0A-451A-85BC-AEF63B74406E%7D.png

[step4]: https://mc.qcloudimg.com/static/img/2c8746f2d4d3c317a3a5afbfd1ed0469/%7BC573A8FF-341A-40DD-A6F3-28D2F0E3EC6B%7D.png

[step5]:https://mc.qcloudimg.com/static/img/46a872c20298deb9d8877e13bfc482a3/%7B29136692-0878-4F89-A14A-6BE54C200129%7D.png

[step6]: https://mc.qcloudimg.com/static/img/f79a067501bb84f32344413000a692c4/%7B90C6BA00-8B63-4194-9FBA-6B60336F584D%7D.png

[step7]:https://mc.qcloudimg.com/static/img/7336d8db7e93d20f2771b4ce31d62a8d/%7B43F6A977-2B44-498B-85A7-B7CA55510738%7D.png

[step8]:https://mc.qcloudimg.com/static/img/4b3e5492bcaa316aba457b1b141ce90b/%7BA5FB88F5-697E-468C-9732-E1893D932875%7D.png