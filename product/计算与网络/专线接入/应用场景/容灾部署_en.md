## Application Scenarios
The user already has large scale applications. His/Her focus has been shifted from the balance between infrastructure deployment and business growth to the stability and reliability of the infrastructure for multi-center development. He/She hopes to eliminate business risks caused by single data center failure by eliminating single points.

**User's core pain point**
- How to realize multi-location disaster recovery and improve infrastructure reliability.
- How to deploy quickly while reducing infrastructure construction period.
- How to re-use stock data center to reduce operating costs (use existing servers first).


## Solutions:
### Hybrid Cloud Disaster Recovery Deployment
- **Multi-location data center deployment**: Build master and slave clusters in local data center and public cloud data center.
- **Data synchronization**: Synchronize data via Direct Connect or VPN to avoid single center failure.
- **Traffic forwarding**: Provide lossy but uninterrupted services by forwarding the traffic to normal data centers.

### Deployment of Cloud Disaster Recovery at Two Locations and Three Centers
- **Cross-availability zone deployment**: You can create subnets and deploy services in different availability zones within one VPC. Data can be synchronized between subnets of different availability zones. The goal of using different availability zones is to ensure that the failures are isolated from each other.
- **Cross-region deployment**: You can deploy the same service in the VPC of another region to achieve multi-location disaster recovery and avoid failures in one region from spreading to other regions.
- **Cross-region high-speed interconnection**: VPCs of two different regions achieve interconnection via cross-region peering connection.
Traffic forwarding: it provides lossy but uninterrupted services by forwarding the traffic to other normal data centers when a data center breaks down.


## Steps

### Steps of Deployment of Hybrid Cloud Disaster Recovery
1) Create a VPC on Tencent Cloud and deploy data centers. [Click here to view VPC Instructions](https://cloud.tencent.com/document/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8).
2) Synchronize customer's local data center and the VPC data center on the cloud via Direct Connect, [Click here to view Direct Connect Instructions](https://cloud.tencent.com/document/product/215/4976#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97).
3) Forward the traffic to other normal data centers when a data center breaks down.

### Steps of Deployment of Cloud Disaster Recovery at Two Locations and Three Centers
1) Cross-availability zone deployment. You can create subnets and deploy master and slave synchronization service in different availability zones within one VPC. Data can be synchronized between subnets of different availability zones. The goal of using different availability zones is to ensure that the failures are isolated from each other. [Click here to view Subnet Instructions](https://cloud.tencent.com/document/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8).
2) Cross-region deployment. You can deploy the same service in the VPC of another region to achieve multi-location disaster recovery and avoid failures in one region from spreading to other regions. [Click here to view VPC Instructions](https://cloud.tencent.com/document/product/215/4927#.E5.88.9B.E5.BB.BA.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E3.80.81.E5.88.9D.E5.A7.8B.E5.8C.96.E5.AD.90.E7.BD.91.E5.92.8C.E8.B7.AF.E7.94.B1.E8.A1.A8).
3) Cross-region high-speed interconnection. 3) Create a cross-region peering connection to achieve high-speed data synchronization between two VPCs. [Click here to view Peering Connection Instructions](https://cloud.tencent.com/document/product/215/5000#.E5.BF.AB.E9.80.9F.E5.85.A5.E9.97.A8).


