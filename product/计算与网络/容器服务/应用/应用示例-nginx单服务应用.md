应用模板中我们使用nginx单服务的应用作为基础示例。在应用中我们同样使用nginx单服务应用作为示例。

## 步骤一： 创建nginx单服务的应用的模板

创建nginx单服务的应用模板的过程，可以参考[用示例-nginx单服务应用][1]

## 步骤二： 新建应用
在应用列表中，点击新建按钮。

![应用nginx示例-008.png-38kB][2]

## 步骤三： 配置应用

在新建应用后，进入到应用配置页面，在该页面执行下面的操作

3.1 填写应用名称和描述

3.2 选择应用需要部署到的集群(包括集群所在的地域和集群ID)

3.3 选择应用模板，这里选择刚刚创建的`nginxapp`这个模板

3.4 配置项选择，默认情况下不选择配置项会使用模板中的配置项。这里我们使用模板中的配置项。

![应用nginx示例-001.png-34.4kB][3]

3.5 点击下一步进入应用编辑操作

## 步骤四： 编辑应用

在应用编辑操作中，可以更加应用的需要对模板中的内容和配置文件的内容进行修改。因为我们在模板中已经将内容已经编辑好了，不再需要额外的修改，所以直接点击完成，完成应用的编辑。

![应用nginx示例-002.png-40.2kB][4]

在应用编辑完成后，这个应用已经创建。再应用列表页面可以看到对应的应用。只是这时后应用还处于未部署状态。

![应用nginx示例-004.png-23.4kB][5]

## 步骤五： 部署应用中的服务

5.1 点击应用的名称，进入应用详情页面

5.2 在应用详情页面，可以看到服务的状态为未部署，点击部署按钮，部署服务。

![应用nginx示例-005.png-22kB][6]

5.3 这样应用中的服务在集群中进行部署，查看应用中服务的状态已经变为了已部署。

![应用nginx示例-005.png-23.9kB][7]

5.4 点击应用中对应的服务，跳转到服务页面查看服务详情。

![应用nginx示例-006.png-46.7kB][8]

这样就完成了应用的部署。

## 步骤六： 访问部署的应用

通过`nginx`服务的负载均衡器IP可以直接访问前端的服务。

![应用nginx示例-007.png-17.6kB][9]


  [1]: https://cloud.tencent.com/document/product/457/11945
  [2]: https://mc.qcloudimg.com/static/img/d53130f06874376f75091affcaef4536/image.png
  [3]: https://mc.qcloudimg.com/static/img/8f4875ebcda51162829e72ddb0a2f44f/image.png
  [4]: https://mc.qcloudimg.com/static/img/70f5d4accc30c33ac0d46209a1e6c37d/image.png
  [5]: https://mc.qcloudimg.com/static/img/0f7b6fdf9b88a811fbc71365e3a00f63/image.png
  [6]: https://mc.qcloudimg.com/static/img/6c9ebb5ec4378e3989e336f32c2a1ff7/image.png
  [7]: https://mc.qcloudimg.com/static/img/7080e4548187a17192fa8d180442e252/image.png
  [8]: https://mc.qcloudimg.com/static/img/1b4a175ca1d258ec7ade435ca9ed79ad/image.png
  [9]: https://mc.qcloudimg.com/static/img/3aea8dfee04dd0b8beb5a7aa48ce1bf1/image.png
  
  
 

  
  
  
  
  