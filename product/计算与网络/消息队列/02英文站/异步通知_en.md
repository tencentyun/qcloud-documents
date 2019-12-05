CMQ supports using Queue model with Topic model. A typical scenario is: the client initiates an asynchronous call request, and the backend has multiple logics and cannot return results in real time. Traditionally, the client performs polling repeatedly. You can use CMQ to add a subscription, which is configured to deliver a notification to the user at client upon the completion of multiple logics at back-end are completed.

- Please see the following figure:

![](//mc.qcloudimg.com/static/img/3e3b93780bfe9c9b7965e27fb54e341a/image.png)

