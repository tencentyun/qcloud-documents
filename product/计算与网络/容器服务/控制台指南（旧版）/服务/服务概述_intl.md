## Service Overview
A service consists of multiple containers with the same configuration and rules used to access these containers.

### Service Type
Services are divided into private network services and public network services.

**Service within a cluster**: Neither public nor private network is used. The service is not associated with any public network load balancer. You can only access the service within a cluster.

**Public network services**: Public network is used. The service is automatically associated with public network load balancers. You can access the service via public network load balancers.

**Private network services**: Private network is used. The service is automatically associated with private network load balancers. You can access the service via private network load balancers.

### Service Configuration
You can configure your services during creation, or update the configuration by updating the service.

## Help Topics

- [Basic Operations of Service](https://cloud.tencent.com/document/product/457/9096)
- [Service Life Cycle](https://cloud.tencent.com/document/product/457/9097)
- [Configuring Service Access Type](https://cloud.tencent.com/document/product/457/9098)
- [Configuring Service Resource Limits](https://cloud.tencent.com/document/product/457/9099)
- [Configuring Service Commands and Parameters](https://cloud.tencent.com/document/product/457/9100)
- [Configuring Service Health Check](https://cloud.tencent.com/document/product/457/9094)
