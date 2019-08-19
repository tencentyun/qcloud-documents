在应用模板中我们使用nginx单服务应用作为应用模板的基础示例。在应用中我们同样使用nginx单服务应用作为示例。

## 步骤一： 创建nginx单服务的应用的模板

如果不存在nginx单服务应用的应用模板，则需要创建对应的应用模板，具体的创建过程可以可以参考[应用模板示例-Nginx单服务应用][1]。

如果已经存在对应的应用模板，则跳过此步骤。

## 步骤二： 新建应用

在[应用列表][2]中，单击新建按钮，开始基于应用模板创建应用。

![应用nginx示例-010.png](https://main.qcloudimg.com/raw/c77c84541bbde88f61517ec408ca73d5.png)

## 步骤三： 配置应用

在新建应用后，进入到应用配置页面，在该页面执行下面可以进行相应的配置。具体的内容包括：

1. 填写应用名称和应用描述
2. 选择应用需要部署到的地域和集群集群

![应用nginx示例-009.png](https://main.qcloudimg.com/raw/401698a511ec1f62b5b81bf32fe99a95.png)

单击下一步进入应用编辑页面，可以对应用中模板内容和配置项进行进一步的修改。
1. 选择应用模板，这里选择刚刚创建的`nginx`这个模板
2. 选择配置项。可以使用模板中默认的配置项也可以根据需要选择特定的配置项。这里我们选择使用模板中默认的配置项。

>**注意：**
>创建应用时会从应用模板拷贝一份副本。在应用中更新模板内容，修改的内容并不会同步回原来的应用模板。

## 步骤四： 编辑应用

在应用编辑操作中，可以更加应用的需要对模板中的内容和配置文件的内容进行修改。因为我们在模板中已经将内容已经编辑好了，不再需要额外的修改，所以直接单击`完成`按钮，完成应用的编辑。更多关于应用编辑的操作，可以参考[应用模板内容操作指引][5]。

![应用nginx示例-011.png][6]

在应用编辑完成后，这个应用已经创建。在应用列表页面可以看到对应的应用。只是这时候应用还处于未部署状态。单击应用的名称，进入应用详情页面，可以对应用中的服务进行部署操作。
## 步骤五： 部署应用中的服务

1. 在应用详情页面，可以看到服务的状态为未部署，单击`部署`按钮，部署服务。

![应用nginx示例-013.png][8]

2. 这样应用中的服务在集群中进行部署，查看应用中服务的状态已经变为了启动中。

![应用nginx示例-014.png][9]

>**重要：**
>更多关于应用内服务的操作可以参考[管理应用内服务][11]。

3. 单击应用中对应的服务，跳转到服务页面查看服务详情。

![应用nginx示例-015.png][10]

## 步骤六： 访问部署的应用

在应用部署完成后，可以通过应用中服务暴露的外网访问地方进行访问。对`nginx`服务中，可以通过暴露的外网负载均衡器IP和端口访问服务。

![应用nginx示例-016.png][13]

  [1]: https://cloud.tencent.com/document/product/457/11952
  [2]: https://console.cloud.tencent.com/ccs/application
  [3]: https://mc.qcloudimg.com/static/img/b69a1f01ddfb2abc05512e324865b8b3/image.png
  [4]: https://mc.qcloudimg.com/static/img/27eda4339af5b2d86959287a4192e783/image.png
  [5]: https://cloud.tencent.com/document/product/457/12199
  [6]: https://mc.qcloudimg.com/static/img/68364f4d1cc623615e0ddc01b9f302ac/image.png

  [8]: https://mc.qcloudimg.com/static/img/0bb4b714e791dc5c8ade33e2b1dea3d7/image.png
  [9]: https://mc.qcloudimg.com/static/img/189cb4d6c49b3f9605c641045894b101/image.png
  [10]: https://mc.qcloudimg.com/static/img/ad600fc08984247d9201869767afa1d1/image.png
  [11]: https://cloud.tencent.com/document/product/457/11989
  [12]: https://mc.qcloudimg.com/static/img/3aea8dfee04dd0b8beb5a7aa48ce1bf1/image.png
  [13]: https://mc.qcloudimg.com/static/img/40eb6e610d8f57e2da3089ad29564fc9/image.png
  [create]: https://mc.qcloudimg.com/static/img/193ee99a7ccaff383b87ef2491a4468c/image.png
  [create2]: https://mc.qcloudimg.com/static/img/9bef862af44c4b1acc3a571589ebf71f/image.png
