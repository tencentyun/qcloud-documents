## Overview of Load Balancer
Load balancer of the container is the access entry to services created by the container. One load balancer is configured for one service frontend. The backend consists of multiple containers. Rather than the type of load balancer, you should focus on the features.

When the service is created:

- for public network, the TCP/UDP protocol-supported load balancer that can provide public network services is automatically created.
- for private network, the TCP/UDP protocol-supported load balancer that can provide private network services is automatically created.

If HTTP/HTTPS forwarding is required, you can create an HTTP/HTTPS load balancer on the load balancer page and configure the forwarding rules.

## Instructions

- [Basic Operations of Load Balancer](https://cloud.tencent.com/document/product/457/9109)
- [Forwarding Configuration of Load Balancer](https://cloud.tencent.com/document/product/457/9111)
