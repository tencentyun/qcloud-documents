## Application Scenarios
Many companies, especially those specializing in games, deploy IT systems across different regions of the globe based on user distribution.

**User's pain points:**
- **Centralized deployment of core data**: Avoid cross-regional data communication as much as possible;
- **Access to the nearest system by region**: Reduce latency;
- **High-speed data interconnection between regions**: cross-server battle, etc.

## Solutions:
Tencent provides a "One Server Covering the Globe" solution for game companies:
1) **Database centralized deployment**. With 16 data centers covering 5 continents around the globe, Tencent Cloud allows game companies to deploy their game database center servers to any of these core data centers based on their business needs. The following two aspects shall be considered when selecting a data center for deployment of center servers: first, confirm with the game company the key region that it expects to cover, such as Europe, America or Southeast Asia; second, make a comparison on the network quality and coverage of overseas IDCs to select the optimal node for deployment.

2) **Player access to the nearest system by region**. To address the inconsistency of network latency among game center servers in over 200 countries/regions, Tencent Cloud deploys a set of access services for all IDCs across the world, to help players to access to the nearest system via DNSPod cloud resolution intelligent scheduling function. In addition, as players often play games with ones who live in the same region, the data of players can be cached by region and written back to the central database regularly to avoid poor gaming experience due to real-time data reading across regions. Domestically, Tencent Cloud has established three major data centers respectively in Beijing, Shanghai and Guangzhou. Internationally, it has set up multiple access points in North America, Europe, Asia Pacific and South for business distribution, deployment and connection. Companies equipped with cache servers can directly use Redis, MongoDB or other storage products provided by Tencent Cloud for easier implementation of business deployment and maintenance.


3) **High-speed data interconnection between regions**. The biggest challenge of using one server among multiple regions is high network latency in cross-server PVP gameplay. To reduce the network latency from game access server to the global center server, Tencent Cloud synchronizes high-speed data among VPCs by implementing peering connection across regions, which significantly minimize the cross-region network latency. 

## Steps
1) Centrally deploy databases, and create a VPC near the user's region. Click to view [Deploy Databases and CVMs Within a VPC](https://cloud.tencent.com/document/product/215/4927#.E5.90.91.E5 . AD.90.E7.BD.91.E4.B8.AD.E6.B7.BB.E5.8A.A.E.E4.BA.91.E4.B8.BB.E6.9C.BA).
2) Use DNSPod cloud resolution intelligent scheduling to enable players to access to the nearest system. Click to view [DNSPod Cloud Resolution Instructions](https://cloud.tencent.com/document/product/302/3446).
3) Use Tencent Cloud cross-region peering connection to achieve VPC high-speed data interconnection between regions. Click to view [Peering Connection Instructions](https://cloud.tencent.com/document/product/215/5000#.E5. BF.AB.E9.80.9F.E5.85.A5.E9.97.A8).
