
This document is intended to help you quickly get started with Tencent Cloud Container Service (CCS) by introducing basics and answering questions you may encounter while using it.


## Preparation for Use
1. Can I use CCS in basic network?
No, CCS only supports VPC network for now.

2. I know nothing about Kubernetes. Will it affect use of CCS?
No. We provide an easy-to-use console to help you use CCS, so you do not need to know its underlying implementation.

## Simple Trial
1. How to use CCS?
You can use it by creating a cluster and a service. For more information, please see [Examples on How to Get Started](/doc/product/457/11138).

2. Can I add an existing CVM to the cluster?
Yes. After a cluster is created, you can add existing CVMs to it.

3. Why does my service keep starting?
If no process is running in the container, the service may keep starting. For more questions about starting service, please see [Event FAQs](/doc/product/457/8187).

4. How to access the created service?
Different access entries are provided for different access methods. For more information, please see [Service Access Method](/doc/product/457/9098).

5. How does the container access public network?
If the host where the container resides has public network IP and bandwidth, the container can directly access public network. Otherwise, an NAT gateway is required for accessing public network.

## Deploying Business
1. My business needs to configure a lot of texts or environment variables. How do I manage them?
You can manage these configuration files via [Configuration Item](/doc/product/457/10173).

2. How do services access each other?
In a cluster, services with the same namespace can directly access each other. Services with different namespaces need to use <service-name\>.<namespace-name\>.svc.cluster.local to access each other.

3. What are the differences between ingress and service access method of "Via Internet"?
ingress is a collection of rules used to route external HTTP(S) traffic to service, which is not directly related to the service access method of "Via Internet".

4. My business is stateful and replies on disk.
You can mount data disk to container in the form of CBS data volume.

5. Will my business be interrupted when service is updating?
Two methods are provided to update service: rolling update and quick update. If you choose rolling update, your business will not be interrupted.









