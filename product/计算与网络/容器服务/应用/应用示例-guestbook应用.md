Guestbook留言板是一个比较典型的web应用服务，由一个frontend前端服务和redis-master和redis-slave两个后端存储服务组成。用户通过web前端提交数据，写入到redis-master上，然后通过读取同步到redis-slave上的数据展示给用户。

为了实现快速的将在集群中部署`Guestbook应用`，在[Guestbook应用模板][1]中已经介绍了如何将`Guestbook`的部署信息通过模板的方式保存起来。本示例将介绍如何使用创建好的模板来快速部署`Guestbook应用`。

## 步骤一： 创建Guestbook的应用的模板

创建Guestbook的应用模板的过程，可以参考[Guestbook应用模板][1]

## 步骤二： 新建应用

在[应用列表][2]中，点击新建按钮。

![新建应用][11]

## 步骤三： 配置应用

在新建应用后，进入到应用配置页面，在该页面执行下面的操作

3.1 填写应用名称和描述

3.2 选择应用需要部署到的集群(包括集群所在的地域和集群ID)

3.3 选择应用模板，这里选择刚刚创建的`Guestbook`这个模板

3.4 配置项选择，默认情况下不选择配置项会使用模板中的配置项。这里我们使用模板中的配置项。

![应用guestbook示例-001.png-34.7kB][3]

3.5 点击下一步进入应用编辑操作

## 步骤四： 编辑应用

在应用编辑操作中，可以更加应用的需要对模板中的内容和配置文件的内容进行修改。因为我们在模板中已经将内容已经编辑好了，不再需要额外的修改，所以直接点击完成，完成应用的编辑。

![应用guestbook示例-002.png-47.2kB][5]

在应用编辑完成后，这个应用已经创建。再应用列表页面可以看到对应的应用。只是这时后应用还处于未部署状态。

![应用guestbook示例-003.png-29.6kB][4]

## 步骤五： 部署应用中的服务

5.1 点击应用的名称，进入应用详情页面

5.2 在应用详情页面，可以看到服务的状态为未部署，点击部署按钮，部署服务。

![应用guestbook示例-004.png-29.7kB][8]

5.3 这样应用中的服务在集群中进行部署，查看应用中服务的状态已经变为了已部署。

![应用guestbook示例-005.png-34.1kB][7]

5.4 点击应用中对应的服务，跳转到服务页面查看服务详情。

![应用guestbook示例-006.png-51.2kB][9]

这样就完成了应用的部署。

## 步骤六： 访问部署的应用

通过`frontend`服务的负载均衡器IP可以直接访问前端的服务。

![应用guestbook示例-007.png-10.9kB][10]

  [1]: https://cloud.tencent.com/document/product/457/11951
  [2]: https://console.cloud.tencent.com/ccs/application
  [3]: https://mc.qcloudimg.com/static/img/5929bfea74ad6e099c58c7b28cd690cd/image.png
  [4]: https://mc.qcloudimg.com/static/img/713bb12340507dc134ef46d2802e9efe/image.png
  [5]: https://mc.qcloudimg.com/static/img/36b6b557c0f66c8879e6ecf61688948f/image.png
  [6]: https://mc.qcloudimg.com/static/img/059891cc1b9177964366b4dcf97c2bcc/image.png
  [7]: https://mc.qcloudimg.com/static/img/91d91500a7a8b03c5317f6eb865f3730/image.png
  [8]: https://mc.qcloudimg.com/static/img/5040ad346837ccc0cc64b97c9ab4832d/image.png
  [9]: https://mc.qcloudimg.com/static/img/c874efeaa8f5080c69d007c36c6fda6f/image.png
  [10]: https://mc.qcloudimg.com/static/img/059891cc1b9177964366b4dcf97c2bcc/image.png
  [11]: https://mc.qcloudimg.com/static/img/836f6f0182d302059a4f49cf4b14c626/image.png
  
  
  







