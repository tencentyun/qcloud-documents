### 1. Usage scenario

Consider the following scenario: You want to grant each CAM user the permission to access the created resources. For example, the creator of COS resources has the permission to access the resources by default. If the resource owner (root account) authorizes the resources to the resource creator individually, the owner needs to write policies for each resource and authorize it to the creator, which has a high authorization cost. In this situation, you can implement the authorization using policy variables. The resource definition in the policy contains the creator information described using the placeholder. This placeholder is the policy variable. During authentication, the policy variable will be replaced with the context information from the request.
    
The following policy describes that the creator has the read permission of the resource:

```
{	 
        "version":"2.0", 
        "statement":        
         { 
            "effect":"allow", 
            "action":"name/cos:Read*", 
            "resource":"qcs::cos::uid/1238423:prefix/${uin}/*" 
         }
}
```

You need to add uin of the creator in each resource's path. If a user with uin "12356" has created a bucket named "test", the corresponding resource is described as "qcs::cos::uid/1238423:prefix/12356/test". When a user with uin "12356" accesses the resource, during the authentication process, the placeholder corresponding to the policy information will be replaced with the visitor's uin (i.e. 12356), so the resource would be "qcs::cos::uid/1238423:prefix/12356/*". The resource "qcs::cos::uid/1238423:prefix/12356/*" in the policy can access the resource "qcs::cos::uid/1238423:prefix/12356/test" through prefix match.


### 2. Locations where policy variables are used
    
**1) The resource element**
       
Policy variables can be used in the last piece of 6-piece format used to described the resource.
    
**2) The condition element**
    
Policy variables can be used in the condition value.
    
The following policy describes that the VPC creator has the access permission.
​
```
{  
        "version":"2.0", 
        "statement":        
         { 
            "effect":"allow", 
            "action":"name/vpc:*", 
            "resource":"qcs::vpc::uin/12357:vpc/*"
            "condition":{"string_equal":{"qcs:create_uin":"${uin}"}} 
         }
}
​
```
​

### 3. List of policy variables
    
The list of currently supported policy variables are as follows:

| Name | Description | 
|---------|---------|
| ${uin} | The uin of the current visitor's sub-account. In a scenario where the visitor is the root account, it's the uin of the root account. | 
| ${owner_uin} | The uin of the root account to which the current visitor belongs. | 
| ${app_id} | The appid of the root account to which the current visitor belongs. | 
