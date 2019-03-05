Resource element describes one or more operation objects, such as CVM resources, COS buckets, etc. 

### 1. Six-Piece format

All resources can be described using the following six-piece format. Each product has its own resources and the detailed resource definition. For more information on how to specify resource information, please see the corresponding product documentation.
    
The six-piece format is defined as follows:


```
qcs:project_id:service_type:region:account:resource
```

Where:

1) qcs is the abbreviation of Tencent Cloud service, which refers to the cloud resources of Tencent Cloud. This field is required.
    
2) project_id describes the project information, which is only used to be compatible with the earlier CAM logics. This field is left empty.
    
3) service_type describes the abbreviations of product names, such as cvm, cdn, etc. For more information, please see the corresponding product documentations. The abbreviation for CAM products is cam. "*" indicates all products. This field is required.
    
4) region describes the region information. A null value indicates all regions. The list of regions supported currently is as follows:

| Abbreviation for Region | Description | 
|---------|---------|
| gz | Guangzhou IDC | 
| sh | Shanghai IDC |
|shjr| Shenzhen Finance IDC |
| bj | Beijing IDC |
| ca | Canada IDC |
| sg | Singapore IDC |

5) account describes the root account information of the resource owner. Currently, the resource owner is described using uin and uid. The former is QQ number of the root account. Format is uin/${uin}, e.g. uin/164256472. The latter is appid of the root account. Format is uid/${appid}, e.g. uid/1000382392. A null value indicates the root account of the CAM user who creates the policy. Currently, the resource owners of COS businesses can only be described using uid, and the resource owners of other businesses can only be described using uin.
    
6) resource describes the specific resource of each product in details.
      
This field is required. The resource can be described as follows:

```
a.<resource_type>/<resource_id>

It indicates the ID of a resource under a sub-resource type. For example, vpc/vpc_id1 of a VPC product.

b. <resource_type>/<resource_path>
 
It indicates the ID of a resource with a path under a sub-resource type. For example, prefix/1228934/bucketName1/object2 of a COS product. Prefix match at the directory level is supported for this type of description. For example, prefix/1228934/bucketName1/* indicates all the objects under bucketName1.
c. <resource_type>/*
It indicates all the resources under a sub-resource type, such as vpc/*.
d.*
It indicates all the resources under a product.

```

In certain scenarios, resource elements can be described with "*", and the definitions are as follows. For more information, please see the corresponding product documentations.

a. If the action requires association with resources, "resource" is defined as "*", which means to associate all the resources.

b. If the action does not require association with resources, "resource" is defined as "*" in all cases.

c. If actions include those that require association with resources and those that don't, "resource" is defined as "*". There are two meanings: on one hand, it describes that the actions that require association with resources will associate all the resources; on the other hand, it describes the actions that do not require association with resources.


### 2. Definition of CAM resource
   
As a product of Tencent Cloud, CAM includes resources such as users, groups, policies, etc. Here lists the CAM resource descriptions.

**Root account:**
    
qcs::cam::uin/164256472:uin/164256472
    
or qcs::cam::uin/164256472:root

**Sub-account:**
    
qcs::cam::uin/164256472:uin/73829520

**Group:**
    
qcs::cam::uin/164256472:groupid/2340

**Anonymous user:**
     
qcs::cam::anonymous:anonymous
     
or*

**Policy:**
    
qcs::cam:: uin/164256472:policyid/*
    
qcs::cam:: uin/164256472:policyid/12423


### 3. Notes on resources
    
 
The resource owner must be a root account. The sub-account that creates the resource will not automatically have the permission to access that resource. It should be authorized by the resource owner.
