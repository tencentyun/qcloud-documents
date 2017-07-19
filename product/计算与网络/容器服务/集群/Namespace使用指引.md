## Namespace使用指引

### Namespace概述
命名空间(Namespace)是对一组资源和对象的抽象集合。例如可以将开发环境，联调环境，测试环境的服务分别放到不同的namespace中。

### 集群默认创建的Namespace
Kubernetes集群在启动时会默认创建`default`和`kube-system`这两个命名空间，这两个命令空间不可以删除。

 - 在不指定命名空间时，默认使用`default namespace`
 - 系统服务一般建议创建在`kube-system namespace`
 
#### 用户创建的Namespace
用户可以在集群中按照需要创建namespace。可以将按照不同的环境创建对应的namespace，例如开发环境，联调环境和测试环境分别创建对应的namespace。或者按照不同的应用创建对应的namespace，例如应用APP1和应用APP2分别创建对应的namespace。

用户创建的namespace可以进行删除，*但删除namespace操作会依次删除namespace下的所有服务*。

## Namespace 操作指引

### 创建Namespace

(1) 在控制台容器集群页面，点击进入集群信息查看页面。在集群信息查看页面中，选择集群namespace，在集群namespace页面中创建新的namespace。

![创建Namespace:2][4]

### 查看Namespace列表
(1) 在控制台容器集群页面，点击进入集群信息查看页面。在集群信息查看页面中，选择集群namespace，可以查看集群中所有的namespace。

![查看Namespace][5]

### 使用Namespace

(1) 创建服务时，选择对应的namespace

![创建服务选择Namepace][6]

(2) 查询服务时，选择对应的namespace，查看对应namespace下的所有服务。

![查看服务选择Namepace][7]

### 删除namespace
(1) 在控制台容器集群页面，点击进入集群信息查看页面。在集群信息查看页面中，选择集群namespace。选中需要删除的namespace后，点击删除。

![删除Namepace][8]

> **删除namespace默认会依次删除namespace下所有服务**

## Namespace使用实践
### Namespace实践(一)--按照不同环境划分Namespace

一般情况下，服务的发布过程中会经过开发环境，联调环境到测试环境再到生产环境的过程。这个过程中不同的环境上部署服务相同，只是在逻辑上进行了定义。

一种做法是对不同环境，分别创建不同的集群。但这样不同环境中资源不能进行共享。同时，不同环境中的服务互访也需要通过服务配置的LB才能够实现。

另外一种做法是，对于不同环境创建对应的namespace。同一namespace下通过可以通过服务名称(service-name)直接访问，跨namespace可以通过service-name.namespace-name访问。具体的方案入下图所示：

![不同环境使用不同的namespace][1]

如上图所示，对于开发环境，联调环境和测试环境分别创建Dev namespace，Intergrated namespace 和 Test namespace。

### Namespace实践(二)--按照应用划分Namespace

对于同一个环境中，服务数量比较多的情况。建议可以进一步按照应用划分namespace。例如下图中，按照APP1和APP2划分了不同的namespace，这样将不同应用的服务在逻辑上当做一个服务组进行管理。
![不同应用划分namespace][2]

同样的，在同一个应用(同一个namespace)内的服务通过服务名称(service-name)直接访问，不同的应用(不同的namespace)通过service-name.namespace-name访问。




  [1]: https://mc.qcloudimg.com/static/img/045ec0b79b88de1e4891c55904bc73bb/image.png
  [2]: https://mc.qcloudimg.com/static/img/351a4eeeb0235692227093b6802aeaea/image.png
  
  [4]: https://mc.qcloudimg.com/static/img/528c677110adb1ec07579ed8261470b1/%7B66A1271E-D2AA-419C-9CCD-FC01F8F34223%7D.png
  [5]: https://mc.qcloudimg.com/static/img/e3152d593a1ec26bbc4b1e9a1249c275/%7BB2B72727-D045-4AF9-BEE3-881710A3FAAD%7D.png
  [6]: https://mc.qcloudimg.com/static/img/36c079364ac866c5b8bea7cbb40cb24f/%7B36491261-01BC-439A-BE3C-427BCCC8F23D%7D.png
  [7]: https://mc.qcloudimg.com/static/img/39d4b0e70a36ad18105f6a48ecd915fd/%7BAA643B99-0399-475A-A828-5185861ACF53%7D.png
  [8]: https://mc.qcloudimg.com/static/img/39d4b0e70a36ad18105f6a48ecd915fd/%7B73600ECF-D15C-406C-8B8D-A63AFD80A3E1%7D.png