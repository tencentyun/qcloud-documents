## Label Overview
Label is essentially a key/value pair that is associated to an object (Kubernetes resources, such as Pod, Node, etc.). Label is designed to identify special properties of an object, and these properties are meaningful to users (for example, what does the label that identifies this Pod mean). Label can be used to classify objects in specific group (for example, all services of appA). You can add a label during the creation of an object, or make modifications at any later time. Each object can have multiple labels, but key value must be unique.
Tencent CCS allows you to add Labels to service pods. When searching services, you can also filer the services using label.

## How to Use Service Labels
### Display of Service Labels
You can view service labels in service list page and service details page. Since Tencent CCS may automatically add labels to services, the labels of services are classified into system label (cannot be modified) and user label (can be modified).
**Service labels displayed in service list page:**
![](//mc.qcloudimg.com/static/img/84129fe851591c95410ffef3720f424b/image.png)
**Service labels displayed in service details page:**
![](//mc.qcloudimg.com/static/img/599de3ec9efbfda563bbafeffbed9564/image.png)
Description of system label:

| Key Name of Label | Value of Label |
| ------| ------ |
| qcloud-app  | Service name  |

### Adding/Deleting Label
In service list page or service details page, click Label Display to edit labels, and then save new labels.
>**Note:**
>The modification of system label is not allowed.

![](//mc.qcloudimg.com/static/img/28d324c9146e75f9097844666e7aa548/image.png)

### Filtering Services by Label
In service list page, you can search services through filtering by label, and only services marked with the label are displayed.
![](//mc.qcloudimg.com/static/img/21205041928dd8c15779a32aa0a5cb78/image.png)

