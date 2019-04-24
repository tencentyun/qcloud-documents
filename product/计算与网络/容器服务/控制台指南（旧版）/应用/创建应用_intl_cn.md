﻿登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。在应用管理->[应用页面][1]点击新建。

![创建应用-006.png][create]

## 应用配置

在新建应用后，进入到应用配置页面，在该页面执行下面可以进行相应的配置。具体的内容包括：

1. 填写应用名称和应用描述
2. 选择应用需要部署到的地域和集群

![创建应用-007.png][create2]

>**注意：**
>创建应用时会从应用模板拷贝一份副本。在应用中更新模板内容，修改的内容并不会同步回原来的应用模板。

## 应用编辑

配置应用后，进入应用编辑页面。在应用编辑页面。在应用编辑页面可以对模板和配置的内容进行进行修改。修改后点击保存，完成应用内容的编辑。更多关于模板内容的操作，可以参考[应用模板内容操作指引][6]。

![创建应用-008.png][7]

编辑完成后，点击`完成`按钮，完成应用创建。

## 部署应用中的服务

创建应用后，在[应用列表][9]可以看到新创建的应用。点击应用的名称，可以进入应用的详情页面，查看应用中各个服务的状态，以及对服务进行部署的操作。

![创建应用-009.png][10]

进入应用详情后，可以看到应用中具体的服务信息。此时服务的状态还是未部署。点击`部署`按钮，执行服务的部署操作。

这样应用的服务就部署完成了，在详情页面可以看到服务的状态从`未部署`变为了`已部署`。服务的运行状态变为了`启动中`。

![创建应用-013.png][12]

>**注意：**
>更多关于应用内服务的操作和状态说明可以参考[应用内服务管理][13]

## 访问部署的应用

在应用部署完成后，可以通过应用中服务暴露的外网访问地方进行访问。对`nginx`服务中，可以通过暴露的外网负载均衡器IP和端口访问服务。

![创建应用-014.png][14]

  [1]: https://console.cloud.tencent.com/ccs/application
  [create]: https://mc.qcloudimg.com/static/img/193ee99a7ccaff383b87ef2491a4468c/image.png
  [3]: https://cloud.tencent.com/document/product/457/11949
  [create2]: https://mc.qcloudimg.com/static/img/9bef862af44c4b1acc3a571589ebf71f/image.png
  [6]: https://cloud.tencent.com/document/product/457/12199
  [7]: https://mc.qcloudimg.com/static/img/68364f4d1cc623615e0ddc01b9f302ac/image.png
  [9]: https://console.cloud.tencent.com/ccs/application
  [10]: https://mc.qcloudimg.com/static/img/0bb4b714e791dc5c8ade33e2b1dea3d7/image.png
  [12]: https://mc.qcloudimg.com/static/img/189cb4d6c49b3f9605c641045894b101/image.png
  [13]: https://cloud.tencent.com/document/product/457/11989
  [14]: https://mc.qcloudimg.com/static/img/dbed8cb87251ea9d338e0dd3de2f8db5/image.png