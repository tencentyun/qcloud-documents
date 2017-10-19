## Setting Service Access Type
### Public Network Access

- A Layer-4 load balancer (LB) (1 CNY/day) that supports public network is created automatically.
- You can access the service via public network using LB VIP and access port. Meanwhile, the CVM port opens automatically.
- Access flow: Client > VIP:VPort (public IP) > Load balancer > NodeIP:NodePort > Kube-proxy (iptables) > Backend pod

### Private Network Access

- A Layer-4 LB that supports private network is created automatically.
- You can access the service via private network using LB VIP and access port. Meanwhile, the CVM port opens automatically.
- Acess flow: Client > VIP:VPort (private IP) > Public load balancer > NodeIP:NodePort > Kube-proxy (iptables) > Backend pod

### Access Within a Cluster

- This service access type only supports service access within a cluster.
- You can access the service within a cluster using service name or service IP +access port.
- Access flow: Front pod > DNS > Front pod > ServiceIP:Port > Kube-proxy (iptables) > Backend pod

The above three types can also be configured with Layer-7 LB (HTTP/HTTPS) to forward to the service. For more information, please see [How to Use Layer-7 LB for Container Services](https://cloud.tencent.com/document/product/457/9111).


