# 应用示例-guestbook应用

标签（空格分隔）： 未分类

---

Guestbook是一个比较典型的web应用服务，其有一个frontend前端服务和redis-master和redis-slave两个后端存储服务组成。本文将介绍如何使用模板来部署guestbook应用。

## 步骤一： 创建guestbook的应用的模板

创建nginx单服务的应用模板的过程，可以参考[补充应用示例-nginx单服务应用链接]

## 步骤二： 新建应用

在应用列表中，点击新建按钮。

补充： [新建页面截图]

## 步骤三： 配置应用

在新建应用后，进入到应用配置页面，在该页面执行下面的操作

3.1 填写应用名称和描述

3.2 选择应用需要部署到的集群(包括集群所在的地域和集群ID)

3.3 选择应用模板，这里选择刚刚创建的`guestbook`这个模板

3.4 配置项选择，默认情况下不选择配置项会使用模板中的配置项。这里我们使用模板中的配置项。

![应用guestbook示例-001.png-34.7kB][1]

3.5 点击下一步进入应用编辑操作

## 步骤四： 编辑应用

在应用编辑操作中，可以更加应用的需要对模板中的内容和配置文件的内容进行修改。因为我们在模板中已经将内容已经编辑好了，不再需要额外的修改，所以直接点击完成，完成应用的编辑。

![应用guestbook示例-002.png-47.2kB][2]

在应用编辑完成后，这个应用已经创建。再应用列表页面可以看到对应的应用。只是这时后应用还处于未部署状态。

![应用guestbook示例-003.png-29.6kB][3]

## 步骤五： 部署应用中的服务

5.1 点击应用的名称，进入应用详情页面

5.2 在应用详情页面，可以看到服务的状态为未部署，点击部署按钮，部署服务。

![应用guestbook示例-004.png-29.7kB][4]

5.3 这样应用中的服务在集群中进行部署，查看应用中服务的状态已经变为了已部署。

![应用guestbook示例-005.png-34.1kB][5]

5.4 点击应用中对应的服务，跳转到服务页面查看服务详情。

![应用guestbook示例-006.png-51.2kB][6]

这样就完成了应用的部署。

## 步骤六： 访问部署的应用

通过`frontend`服务的负载均衡器IP可以直接访问前端的服务。

![应用guestbook示例-007.png-10.9kB][7]

  [1]: http://static.zybuluo.com/yan234280533/zpaoi8v7n7nr0fmfkf0v33an/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-001.png
  [2]: http://static.zybuluo.com/yan234280533/nm7x9dtdmlpygt21c0aja9v4/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-002.png
  [3]: http://static.zybuluo.com/yan234280533/7kcevpu07qlzlkddyxc15kmr/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-003.png
  [4]: http://static.zybuluo.com/yan234280533/mdbe0nsjegm087eir7a6ssbj/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-004.png
  [5]: http://static.zybuluo.com/yan234280533/0b4y53777evzqp9y9xftj1em/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-005.png
  [6]: http://static.zybuluo.com/yan234280533/tbrtvxhxi1ysqix10ctilwfu/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-006.png
  [7]: http://static.zybuluo.com/yan234280533/unlkndoo6yvw0k3udwz5rf8z/%E5%BA%94%E7%94%A8guestbook%E7%A4%BA%E4%BE%8B-007.png