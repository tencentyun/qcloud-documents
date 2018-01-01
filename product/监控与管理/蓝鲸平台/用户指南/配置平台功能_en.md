## 1 Foreword 
In ITIL system, Configuration Management Database (CMDB) is the basis for building other processes. In BlueKing, "[Configuration Console (CC)](http://o.qcloud.com/console?app=cc-new)" plays the role of CMDB, providing configuration data services of various OPS scenarios for other BlueKing platforms.
### 2. Term Definition  
We summarize some terms involved in the BlueKing Configuration Console.
### 2.1 Business 
There may be more than one product in your company. Each product has a corresponding requirement for CVM management. For the Configuration Console, each of these products is called business.
### 2.2 Key Advantages 
Each business has its own online environment. For game business, there are test server, trial server and formal server. If a game uses multi-zone/multi-server backend structure, it is composed of multiple major zones which are called clusters in the Configuration Console. A business consists of multiple clusters.
### 2.3 Module
Module is under the cluster. A collection that can independently implement a feature is known as a module, such as Nginx under a web business. A module can be mounted with multiple CVM resources, and a CVM resource can also be mounted to different modules. Multiple modules form a business cluster.
### 2.4. Resource Pool
Resource pool is introduced to meet the company's requirement for resource management. A resource pool is shared across a company. You can import your CVM resources into a resource pool in batches using Excel, and the resource admin allocates CVM resources for each business. 

## 3. Product Features
### 3.1. Feature Overview
BlueKing Configuration Console has the following features:
1. Web-based visual business topology
2. Diversified API services
3. System snapshot data display
4. Cross-cloud management 

### 3.2 Feature List
![Feature List](https://mc.qcloudimg.com/static/img/97a88cf8f7c02f007f462d9961215210/1.jpg)

### 3.3 CVM Management
CVM management is the core feature of the Configuration Console, which combines topology to implement cross-cloud management while maintaining the traditional list management. CVM management provides the following features:
![Configuration Console](https://mc.qcloudimg.com/static/img/3af3e7bf58f35183c7724b0b7c912454/2.jpg) 
1. CVM information is displayed at topology dimension. The topology tree on the left of the page shows the distribution of CVMs in each cluster and module.
2. Cross-cloud CVM management. You can easily manage CVMs in different clouds on the Configuration Console, without being affected by the conflict between private IPs.
3. Convenient CVM filtering. You can filter the CVMs by setting conditions on configure platform.
![Configuration Console](https://mc.qcloudimg.com/static/img/2e9cf42be6b7136ef02e34d2f322c4b3/3.jpg)  
4. Various value-added features. Configuration Console allows you to export tables, view data in real time and change CVM modules to help you better manage CVMs.
5. Custom display of CVM attributes. In CVM management page, you can display the CVM fields as needed, and import CVM fields that are not provided by the Configuration Console.
![Configuration Console](https://mc.qcloudimg.com/static/img/cf972e08779380f0a012412180f9431d/4.jpg) 
 

### 3.4 Business Topology
Business topology is the basis of CVM management on the Configuration Console. As business architectures and types become complicated, only when a proper business model is established can CVMs be managed in a structured way. Configuration Console supports custom structure and custom topology attributes.
![Configuration Console](https://mc.qcloudimg.com/static/img/c05c7bbcc55490021762e77757583669/5.jpg)  
1. Custom topology structure: Configuration Console supports a custom data structure with three levels — business, cluster, and module and a data structure with two levels — business and module. Users can build business structures suitable for different scenarios as needed.
2. Custom cluster and module attributes: In addition to standard attributes such as name and admin of cluster and module, custom attribute management is also provided in the Configuration Console. With a variety of custom attributes, users can perform CVM category management in diverse dimensions.

### 3.5 Cluster and Module
In the previous sections, we have introduced a rich variety of topology management features of Configuration Console. Based on topology management, we have further refined the topology to support the management of CVMs in a single cluster and module dimension, and provided features such as batch modification and cluster clone.
![Configuration Console](https://mc.qcloudimg.com/static/img/ece06283816610a16476e32eb771c7a0/6.jpg) 
1. Batch modification: For a multi-zone game, batch modification is a must.
2. Cluster clone: Cluster clone is widely used in the opening of batch zones and other scenarios of game businesses, which can save a lot of operation time and allow users to adjust topology structure conveniently.
![Configuration Console](https://mc.qcloudimg.com/static/img/300ea8d7e698e18d6f9aff615a65fd03/7.jpg)  

### 3.6 Business Management
Users can manage the developer's businesses on which they have permissions. They can view business list, add businesses, make modifications, implement batch modification and delete businesses.
![Business Management](https://mc.qcloudimg.com/static/img/dfff84cec57ae936f4d0e9e2d42f744b/61.jpg) 
Create a new business under the current developer by following the two steps below:
1. Select your business topology type, including three-level topology and two-level topology. Example:
![Business Management](https://mc.qcloudimg.com/static/img/b8dc69f34e1343d1581d013a81c6beb8/62.jpg)  
2. Enter the basic information of your business to be created, including business name, product personnel, business OPS and other fields.
![Business Management](https://mc.qcloudimg.com/static/img/e7649d7e9661d6ee0957c5d3bd73d89a/63.jpg) 
For a single business, the fields that can be modified include business name, OPS personnel and custom attributes.
![Business Management](https://mc.qcloudimg.com/static/img/2ff86893a0d77294d94c23068ee1e057/64.jpg) 
You can modify the attributes of specified fields for one or more businesses at the same time. The fields to be modified can be specified in the column of attribute name.
![Business Management](https://mc.qcloudimg.com/static/img/3e302c52fe319c7c771ee7d66c8a28ff/65.jpg) 
You can delete unnecessary businesses.
![Business Management](https://mc.qcloudimg.com/static/img/fba9e11f41f10f5b79df97d4eabf2906/66.jpg) 
### 3.7. Resource Pool Management
To manage CVMs across cloud platforms of the developer, you can sync or import CVMs, update CVMs, allocate CVMs in the resource pool to the idle server pool under the developer's specific business, or delete unnecessary private CVMs.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/a73c2050f029c4cf38ca25680ef1527b/71.jpg)
![Resource Pool Management](https://mc.qcloudimg.com/static/img/3a91cfa6dc71a46e691323b16748f3c6/72.jpg)  

Configuration Console has been connected with Tencent Cloud. If you have a CVM on Tencent Cloud, you can automatically sync the CVM on Tencent Cloud to the Configuration Console by clicking the "Sync CVM" button and put it to the current developer's resource pool.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/a9f8e5f7ddc11a8478b5dd5990dae6bc/73.jpg) 
Two import modes are provided to import private CVMs other than Tencent Cloud CVMs: quick import and custom batch file import.
1. For quick import, you only need to enter the private IP. Public IP and maintenance personnel are optional.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/5d2b64d084fe5d6ec6cc6db6924f31c7/74.jpg)
2 For custom import, custom fields of header can be imported, which is easy and convenient.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/7ad68473a21c3aa68293182b62263ca6/75.jpg)
![Resource Pool Management](https://mc.qcloudimg.com/static/img/847745d602a64ca210d9738e9650140e/76.jpg)
 
Arbitrarily assign the CVMs under the resource pool to any business of the current developer. By default, they are placed under the idle server pool of the business.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/b0ac972765156783ebe51712691d68bb/77.jpg) 
You can delete unnecessary CVMs in a private cloud conveniently.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/f539d23fb00c5df25d3e50199f327c59/78.jpg) 

### 3.8 Custom Attribute Management
Configuration Console provides basic topology models and their basic attributes to meet the users' requirements for basic business scenarios. It also supports model expansion and custom model attributes to apply to all business scenarios. Users can add custom attributes to their businesses, clusters, modules and CVMs, and these attributes are all at the developer dimension.
![Resource Pool Management](https://mc.qcloudimg.com/static/img/cb0d32f6f4781415b8a5a4962ff11664/79.jpg)
![Resource Pool Management](https://mc.qcloudimg.com/static/img/fb643919ce6008a1cb9e62e429adfba3/710.jpg) 

### 3.9 Operation Audit
All operations performed by users on the Configuration Console can be traced by checking the corresponding record. We can view the information under the Operation Audit menu item: 
![Resource Pool Management](https://mc.qcloudimg.com/static/img/1c11de1791a1642dac74269af47309a4/711.jpg)  






