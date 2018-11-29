Namespace is an abstract collection of a group of resources and objects. For example, services in the development, integrated testing, and test environment can be placed in different namespaces.
## Category
Namespaces are divided into two categories by creation: the default namespaces created by clusters and the namespaces created by users.
### Default Namespaces Created by Clusters 
When it is enabled, Kubernetes cluster creates the namespaces of `default` and `kube-system` by default, which cannot be deleted.
 - `Default namespace` is used by default when no namespace is specified.
 - System services are generally recommended to be created in `kube-system namespace`.
 
### Namespaces created by users
Users can create namespaces as needed in the cluster. Namespace can be created either by environment types (such as development, integrated testing and test environment) or by application (such as App1 and App2).
>**Note:**
> Namespaces created by users can be deleted, which will result in the deletion of all the services under these namespaces.

## Operation Instructions
### Creating a Namespace
1. Log in to [CCS Console](https://console.cloud.tencent.com/ccs).
2. Click **Cluster** on the left navigation bar.
3. Click **ID/Name**of the cluster in the cluster list.
![](//mc.qcloudimg.com/static/img/61849c3dd8141879ca64e52a7348a065/image.png)
4. Click **Namespace List**, and then click **New Namespace**.
![](//mc.qcloudimg.com/static/img/605f218bba56eacb1f6d21ed507ea8eb/image.png)
5. Enter the information and click **Submit**.
 - **Name**: Name of the namespace.
 - **Description**: Details of the namespace. Such information are displayed in the **Namespace List** page.
![](//mc.qcloudimg.com/static/img/2eff6302e4e127f7d4c01f1fa552f52a/image.png)

### Viewing a Namespace List
1. Log in to [CCS Console](https://console.cloud.tencent.com/ccs).
2. Click **Cluster** on the left navigation bar.
3. Click **ID/Name**of the cluster in the cluster list.
![](//mc.qcloudimg.com/static/img/61849c3dd8141879ca64e52a7348a065/image.png)
4. Click **Namespace List** of the cluster to view the details.
![](//mc.qcloudimg.com/static/img/198a4f5c8bb8680093e89a9491d5b389/image.png)

### Using a Namespace
1. To create a service, select an appropriate namespace.
![](//mc.qcloudimg.com/static/img/0c7959a293de17fe5ceb3c34f3be8597/image.png)

2. To query a service, select an appropriate namespace to view all the services under the namespace.
![](//mc.qcloudimg.com/static/img/a2874127fc88b6deffe23710fe3b471b/image.png)

### Deleting a Namespace from a Cluster
1. Log in to [CCS Console](https://console.cloud.tencent.com/ccs).
2. Click **Cluster** on the left navigation bar.
3. Click **ID/Name**of the cluster in the cluster list.
![](//mc.qcloudimg.com/static/img/61849c3dd8141879ca64e52a7348a065/image.png)
4. Click **Namespace List**, select a namespace, and then click **Delete** on the left.
![](//mc.qcloudimg.com/static/img/8c3af52aa236daf6c9768a095d421623/image.png)
5. When a prompt page that displays details of the namespace appears, click **OK** to delete it.
![](//mc.qcloudimg.com/static/img/1d5fa45b089ce4c4120fe3050622f283/image.png)
>**Note:**
> Deleting a namespace will terminate all the resources under this namespace. All the data will be cleared and cannot be restored after termination. Please back up your data in advance.

## Application Practice
### Dividing Namespaces by Environment
In general, a service will go through development, integrated testing, test, and production environment before being published. Despite of deployment with same service, different logics are defined for these environments. Two approaches are available:
1. Create different clusters separately. In this way, the resources in different environments cannot be shared. Besides, services interconnection in different environments can only be achieved using the configured Load Balance.
2. Create appropriate namespaces for different environments. You can use service-name to directly access the service under the same namespace, and use service-name.namespace-name to access the service across namespaces.
As shown below, Namespace Dev, Namespace Intergrated and Namespace Test are created respectively for development environment, integrate testing environment, and test environment.
![Different namespaces are used for different environments](https://mc.qcloudimg.com/static/img/045ec0b79b88de1e4891c55904bc73bb/image.png)

### Dividing Namespaces by Application
If there are many services in the same environment, you are recommended to further divide namespaces by application. As shown below, different namespaces are divided according to App1 and App2, and the services for different applications are managed as a service group logically.
![Dividing namespaces for different applications](https://mc.qcloudimg.com/static/img/351a4eeeb0235692227093b6802aeaea/image.png)

Similarly, you can use service-name to directly access the service under the same application (namespace), and use service-name.namespace-name to access the service across applications (namespaces).

