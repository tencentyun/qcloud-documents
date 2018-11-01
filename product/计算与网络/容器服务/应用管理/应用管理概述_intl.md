With the rise of micro-service and Devops, the deployment and management for multiple services across multiple environments becomes a necessity. Besides, the complexity of deployment also greatly increases. Tencent TKE can help you achieve group management of services via applications, which significantly simplifies the service management. Meanwhile, Tencent TKE saves the service deployment information in application templates, and manages differentiated service information in different environments via configurations, thus achieving quick service deployment in different environments in the mode of "application template + configuration".

## Key Concepts in Application Management

Application management involves three key concepts:

**Application:** Tencent TKE performs unified management for multiple services via service groups. For more information on applications, please see [Application Overview][1].

**Application Template:** The service deployment information is saved in the form of YAML text. Users can deploy the same application in different environments with ease. For more information on application templates, please see [Application Template Overview][2].

**Configuration Management:** In the configuration management, the differentiated parts in different environments are reflected in configuration items, and values that frequently change are substituted by variables for easy modification and update. For more information on configuration management, please see [Configuration Items in the Application][3].

For more information on key concepts of application management, please see [Usage Guide][4].

## Application Management Scenarios
There are two major scenarios for application management: rapid application deployment in multiple environments, and service group-based Devops process management.

**Rapid application deployment in multiple environments**
As shown below, rapid application deployment in multiple environments can be achieved in the mode of application template + configurations of different environments. The application template describes the deployment information of multiple services, and the configuration item (such as the number of instance replicas, database address) reflects the differentiated settings in different environments . With "application template + configuration", application instances can be deployed in multiple environments quickly. For more information on application deployment in multiple environments, please see [Wordpress Deployment in Different Environments][5].

![多环境下应用的快速部署.png-20.6kB][6]

**Service group-based Devops process management**
In the Devops process, the application management groups services based on the concept of application. Services with high relevance are organized as a group for unified management to decrease the management complexity for multiple services.

In addition, synchronous management in different environments can be achieved using "application template + configuration". If the deployment information of the service is modified, the application template can be used for synchronous information management in multiple environments.

![多环境下应用的管理.png-13.8kB][7]

## Application Management Example

Let's take the application `nginxapp` as an example to illustrate how to use application management. This application has only one service `nginx`. The application can be quickly deployed to different namespaces by modifying the value of the variable `NAMESPACE` in the configuration item. For more information, please see [Nginx Application][8].

Guestbook is a typical web application service, and consists of a frontend service and two backend storage services, redis-master and redis-slave. These services can be defined in an application template, and the service deployment is described in a descriptive language. After the differentiated information of different environments is defined in the configuration file, the application can be deployed in different environments using "application template + configuration". And these services can be managed uniformly by using the application. For more information, please see [Guestbook Application][9].


  [1]: https://cloud.tencent.com/document/product/457/12204
  [2]: https://cloud.tencent.com/document/product/457/12200
  [3]: https://cloud.tencent.com/document/product/457/11987
  [4]: https://console.cloud.tencent.com/ccs/guide
  [5]: https://cloud.tencent.com/document/product/457/12197
  [6]: https://mc.qcloudimg.com/static/img/30ce4422ec69ff4d409c6bde714b2230/image.png
  [7]: https://mc.qcloudimg.com/static/img/a5ba801e8315e1a608b4bd7f8cad49f5/image.png
  [8]: https://cloud.tencent.com/document/product/457/11945
  [9]: https://cloud.tencent.com/document/product/457/11944
