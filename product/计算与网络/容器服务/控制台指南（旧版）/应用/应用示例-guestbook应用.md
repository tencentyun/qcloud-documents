Guestbook留言板是一个比较典型的web应用服务，由一个frontend前端服务和redis-master和redis-slave两个后端存储服务组成。用户通过web前端提交数据，写入到redis-master上，然后通过读取同步到redis-slave上的数据展示给用户。

在[Guestbook应用模板][1]中已经介绍了如何将`Guestbook`的部署信息通过模板的方式保存起来。本示例将介绍如何使用创建好的模板来快速部署`Guestbook应用`。

## 步骤一： 创建Guestbook的应用的模板

创建Guestbook的应用模板的过程，可以参考[Guestbook应用模板][2]

## 步骤二： 新建应用

在[应用列表][3]中，单击新建按钮。

![应用guestbook示例-009.png](https://main.qcloudimg.com/raw/924dc0e0389bdfb0a77fb5c7d52d424d.png)

## 步骤三： 配置应用

在新建应用后，进入到应用配置页面，在该页面执行下面的操作

1. 填写应用名称和描述
2. 选择地域和应用需要部署到的集群

![应用guestbook示例-10.png](https://main.qcloudimg.com/raw/5a260c3f60ff8bcce9f33560950cef96.png)

单击下一步进入应用编辑页面，可以对应用中模板内容和配置项进行进一步的修改。

1. 选择应用模板，这里选择刚刚创建的`Guestbook`这个模板
2. 选择配置项，可以使用模板中默认的配置项也可以根据需要选择特定的配置项。这里我们选择使用模板中默认的配置项。
![应用guestbook示例-10.png][6]

>**注意：**
>创建应用时会从应用模板拷贝一份副本。在应用中更新模板内容，修改的内容并不会同步回原来的应用模板。

## 步骤四： 编辑应用

在应用编辑操作中，可以根据应用的需要对模板中的内容和配置文件的内容进行修改。因为我们在模板中已经将内容编辑好了，不再需要额外的修改，所以直接单击`完成`按钮，完成应用的编辑。更多关于应用编辑的操作，可以参考[应用模板内容操作指引][6]。

![应用guestbook示例-011.png][7]

在应用编辑完成后，这个应用已经创建。在应用列表页面可以看到对应的应用。只是这时候应用还处于未部署状态。单击应用的名称，进入应用详情页面，可以对应用中的服务进行部署操作。

## 步骤五： 部署应用中的服务

在应用详情页面，可以看到服务的状态为未部署，单击部署按钮，部署服务。

![应用guestbook示例-016.png][9]

查看应用中服务的状态已经变为了启动中。

![应用guestbook示例-013.png][10]

单击应用中服务的名称，跳转到服务页面查看服务详情。

![应用guestbook示例-014.png][11]

## 步骤六： 访问部署的应用

通过`frontend`服务的负载均衡器IP可以直接访问前端的服务。

![应用guestbook示例-015.png][13]


  [1]: https://cloud.tencent.com/document/product/457/11951
  [2]: https://cloud.tencent.com/document/product/457/11951
  [3]: https://console.cloud.tencent.com/ccs/application
  [4]: https://mc.qcloudimg.com/static/img/f94effc7b5ec3cdcd9821c27ea6b2871/image.png
  [5]: https://mc.qcloudimg.com/static/img/4e6d2c9483b595a773ef7bc9fe70d57b/image.png
  [6]: https://mc.qcloudimg.com/static/img/8e4e1a1d62d87803bb220cdb33fbeb07/image.png
  [7]: https://mc.qcloudimg.com/static/img/6529c013018af4adfb2dcdf2ae030085/image.png
  [9]: https://mc.qcloudimg.com/static/img/bc929d90e0ee89ef24d8c2bdf3bcff63/image.png
  [10]:https://mc.qcloudimg.com/static/img/0cb66aea86f1db958db13ebbee05f563/image.png
  [11]: https://mc.qcloudimg.com/static/img/c9c0ca79b3fe41d9a33bebfec53d7b74/image.png
  [12]: https://mc.qcloudimg.com/static/img/059891cc1b9177964366b4dcf97c2bcc/image.png
  [13]: https://mc.qcloudimg.com/static/img/d45bb96194851eed18b07acbf8c23121/image.png
