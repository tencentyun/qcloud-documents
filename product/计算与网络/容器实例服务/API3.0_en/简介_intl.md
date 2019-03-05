Thank you for using Container Instance Service (CIS)

CIS provides flexible computing resources. You can use the APIs and examples described in this document to perform related actions on container instances, such as creation, termination, checking timestamp, and viewing logs.

Before using these APIs, please make sure that you have a thorough understanding of [CIS Overview](https://cloud.tencent.com/document/product/858).

>**Notes:**
>
> All CIS APIs under this module are of API 3.0.

## Glossary

The common terms involved in this document are as follows:

| Term | Full Name | Description |
|---------|---------|---------|
| Region | [Region](https://cloud.tencent.com/document/product/213/6091) | Indicates the region where the resource is located. Each region contains one or more availability zones. |
| Zone | [Availability Zone](https://cloud.tencent.com/document/product/213/6091) | Refers to Tencent Cloud's physical IDCs whose power and network are independent from each other within the same [region](https://cloud.tencent.com/document/product/213/6091). They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones so that users' businesses can provide continuous online services. |
| InstanceName | Container Instance Name | It is composed of lowercase letters, numbers and "-", with a length not more than 63 characters. It begins with a lowercase letter and ends with a lowercase letter or a number. |
| VpcId | VPC ID | [VPC](https://cloud.tencent.com/document/product/215) is a custom network space isolated logically. |
| SubnetId | VPC Subnet ID | A [subnet](https://cloud.tencent.com/document/product/215/4927) is an IP address block within a VPC. All cloud resources in your VPC must be deployed within the subnet. |
| Image | Container Image | The Docker image required to start a container. It contains all the dependencies needed by the container's main process and runtime. |
| RestartPolicy | Restart Policy | never: the container instance will not restart automatically after it exits; on-failure: the container instance restarts when it exits with a non-zero status code; always: the container instance always restarts regardless of its exit code. |
| State | Instance Status | Pending: creating; Running: running; Successed: execution succeeded and terminated; Failed: execution failed and terminated; Unknown: exceptional status |
| State | Container Status | Waiting: creating; Running: running; Terminated: ended and the cause of which is subject to the ExitCode. |


## Getting Started with APIs

The following introduces how to use CIS APIs in some typical scenarios:

You can quickly create an postpaid instance by using the API for creating container instances and providing necessary information like availability zone ID, image ID, and required configurations.

If you do not want to use the instance any more, you can terminate it using the API for deleting container instances. No charge will arise once the instance is deleted.

## Use Limits

The machines created by API are subject to the number limit described in the [Restrictions on CIS Purchase](https://cloud.tencent.com/document/product/858/17315), and share the quota with container instances created via the official website.

For more information on specific limits, see the documents for appropriate APIs or products.

