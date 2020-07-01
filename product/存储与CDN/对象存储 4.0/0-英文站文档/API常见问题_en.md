## About the Usage of XML API and JSON API

### Permission Issues

**Q: Do XML API and JSON API share one key?**

A: Yes. For a 9-digit APPID starting with 125, please use the API key provided by Tencent Cloud. You can check your individual API key via COS console or at https://console.cloud.tencent.com/capi.

**Q: Do XML API and JSON API share one signature?**

A: No. They have separate signatures.

JSON API signature: https://cloud.tencent.com/document/product/436/6054

XML API signature: https://cloud.tencent.com/document/product/436/7778.

**Q: Do XML API and JSON API share the same ACL permissions?**

A: No. They have separate ACL permissions.

**Q: Do XML API and the console share the same ACL permissions?**

A: No. The console has the same ACL permissions with JSON API, but different ACL permissions from XML API.

**Q: Can XML API access the Bucket with the ACL permissions set by JSON API?**

A: By default, only the owner has the permission to access it, and others cannot. Bucket is Private. 

**Q: Can XML API access the Bucket with the ACL permissions set by the console?**

A: By default, only the owner has the permission to access it, and others cannot. Bucket is Private.

**Q: Can JSON API access the Bucket with the ACL permissions set by XML API?**

A: By default, only the owner has the permission to access it, and others cannot. Bucket is Private.

**Q: Can the console access the Bucket with the ACL permissions set by XML API?**

A: By default, only the owner has the permission to access it, and others cannot. Bucket is Private.

### Upload and Download Issues

**Q: What is the uploaded domain of XML API?**

A: The upload domain of V4 XML API varies depending on its region. For example, bucket-[a 9-digit number starting with 125].cn-south.myqcloud.com. The upload domains of V4 JSON API are gz.file.myqcloud.com and tj.file.myqcloud.com. The upload domain of V3 JSON API is web.file.myqcloud.com.

**Q: What is the upload path of XML API?**

A: For example, to upload a file Put, refer to API documentation at `http://BucketName-UID.Region.myqcloud.com/ObjectName` for details.

### Key Issues

**Q: How do I find the key position?**

A: You can view your key at https://console.cloud.tencent.com/cos4/secret. The available key is the APPID corresponding to the number string in the download address of the bucket you created.

**Q: How do I change the key? **

A: You cannot change the key currently. This function will be available in the future.

**Q: I accidently changed the key via "Cloud API Key". Does it affect anything?**

A: You can view the changes at https://console.cloud.tencent.com/capi. Note that such changes may lead to inconsistency between the keys at data side and CDN side. To solve CDN-related problems, you should rebind the CDN domain (including the default domain offered for free, which also needs to be closed and reopen); To solve the problems at data side, you should re-create the Bucket.

## Historical Versions and Data

### Historical Version Differences

**Q: What is the relationship between XML API and JSON API 4.0?**

JSON API 4.0 refers to the API used by users when connecting to COS after September 2016. The upload domain is [Region].file.myqcloud.com. JSON API 4.0 will be kept in a state of maintenance. They will be available for use but will not develop new features. The infrastructure of these APIs is the same as that of the APIs for standard XML, with data interoperability and can be cross-used. However, they're not compatible with each other and have different domains.

**Q: What is the relationship between XML API and JSON API 3.0?**

JSON API 3.0 refers to the API used by users when connecting to COS before October 2016. The upload domain is web.file.myqcloud.com. For users who use JSON API 3.0, COS will help them migrate data slowly and forward requests without changing the customers. The infrastructure of these APIs is different with that of the API for standard XML, without data interoperability, and both APIs are not compatible with each other.

**Q: How do I check my API version?**

A: You can use upload and download domains of the bucket to check your API version. They are structured as follows:

| Region   | Version       | Example download address                                   | Example upload address                                   |
| ---- | ---------- | ---------------------------------------- | ---------------------------------------- |
| Shanghai   | v3-JSON  | bucket-[an 8-digit number starting with 100].cos.myqcloud.com   | web.file.myqcloud.com                    |
| South China   | v4-JSON  | bucket-[a 9-digit number starting with 125].cosgz.myqcloud.com | gz.file.myqcloud.com                     |
| North China   | v4-JSON  | bucket-[a 9-digit number starting with 125].costj.myqcloud.com | tj.file.myqcloud.com                     |
| East China   | v4-JSON  | bucket-[a 9-digit number starting with 125].cossh.myqcloud.com | sh.file.myqcloud.com                     |
| South China   | v4-XML  | bucket-[a 9-digit number starting with 125].cn-south.myqcloud.com | bucket-[a 9-digit number starting with 125].cn-south.myqcloud.com |
| North China   | v4-XML  | bucket-[a 9-digit number starting with 125].cn-north.myqcloud.com | bucket-[a 9-digit number starting with 125].cn-north.myqcloud.com |
| East China   | v4-XML  | bucket-[a 9-digit number starting with 125].cn-east.myqcloud.com | bucket-[a 9-digit number starting with 125].cn-east.myqcloud.com |
| Singapore  | v4-XML  | bucket-[a 9-digit number starting with 125].sg.myqcloud.com    | bucket-[a 9-digit number starting with 125].sg.myqcloud.com    |

**Q: Where can I find XML API documentation?**

A: You can find the API documentation at https://cloud.tencent.com/document/product/436/7751.

## Historical Version Data 

**Q: I already have COS V3's Bucket and Object, can I use XML API?**

A: No, XML API is a COS V4 based architecture. It cannot connect with COS V3.

**Q: I created a Bucket and an Object using V3 JSON API. Can I use XML API to manage them?**

A: No, XML API is a COS V4 based architecture. It cannot connect with COS V3.

**Q: I created a Bucket and an Object using V3 console. Can I use XML API to manage them?**

A: No, XML API is a COS V4 based architecture. It cannot connect with COS V3.

**Q: I created a Bucket and an Object using XML API. Can I use V3 JSON API?**

A: No, XML API is a COS V4 based architecture. It cannot connect with COS V3.

**Q: I already have COS V4's Bucket and Object, can I use XML API?**

A: Yes, XML API is a COS V4-based architecture. It can be used to work with data generated by JSON API.

**Q: I created a Bucket and an Object using V4 JSON API. Can I use XML API to manage them?**

A: Yes, XML API is a COS V4-based architecture. It can be used to work with data generated by JSON API.

**Q: I created a Bucket and an Object using V4 console. Can I use XML API to manage them?**

A: Yes, XML API is a COS V4-based architecture. It can be used to work with data generated by JSON API.

**Q: I created a Bucket and an Object using XML API. Can I use V4 JSON API?**

A: Yes, you can use it to create data and do other things within its permission scope, but we recommend you don't do that.

**Q: Will the fee change?**

A: No, the standard storage fee will not change. You can refer to the product overview page for details. The new storage level is only available using V4 XML API.

## Function and Performance Differences

## Function Difference

**Q: What can XML API do?**

A: It can create, delete, query and list Bucket; create, delete, query, download and modify the attributes of Object; as well as perform multipart upload and appending upload.

**Q: Does XML API have all the functions of JSON API?**

A: Yes.

**Q: How XML API authentication is different from the previous authentication?**

A: XML API supports authentication across accounts, between root accounts, and between root accounts and sub-accounts.

**Q: Will you continue developing JSON API?**

A: No, we will maintain JSON API, but not develop it. We recommend you to replace it in the long run.

**Q: In addition to the current functions, what will XML API do in the future?**

A: It will support batch deletion, cross-domain operations, lifecycle management, manual replication, cross-zone automatic replication, static site, sheet uploads, version management, callback, and logging.

## Performance Difference

**Q: Do XML API and JSON API differ in performance?**

A: No. That is because they belong to the same architecture.

**Q: How does 4.0 excel over 3.0 in QPS?**

A: 4.0 breaks the speed limit of 20 qps for one directory in 3.0. Its average service capacity for one Bucket is 100 qps, and the maximum service capacity is 500 qps. With 4.0, you don't need to worry about the directory problem.

**Q: What if QPS exceeds 500?**

A: It is recommended that you keep the request rate below 500, otherwise it may cause a failure rate. If the QPS has to exceed 500, it is recommended to create multiple Buckets to share the traffic. If the QPS has to exceed 500 within one Bucket, please contact your key customer manager or h_cos_helper via rtx for assessment. You can also refer to Product Documentation - FAQs - Performance Optimization.

**Q: How does 4.0 excel over 3.0 in speed?**

A: 4.0 supports concurrent upload and multipart upload in parallel. In contrast to the relatively low upload speed of 3.0, 4.0 has a single-thread speed of 20 MB/s, a single file speed of dozens of hundreds of MB/s and a significantly high multi-thread speed.


