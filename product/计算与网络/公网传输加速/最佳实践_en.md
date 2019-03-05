## Background
Company A, whose BACKEND service cluster located in Beijing, expects to connect customers nationwide. However, to save costs, the company does not want to deploy multiple sets of logic and data layers. In this case, a global floating IP is required to serve as the only access entry for global nearby distribution, dynamic traffic distribution, and failure elimination.

## Pain Points
Company A's IDC built by customers and the small- and medium-sized public cloud vendors cannot schedule the network across regions and do not have the Anycast capability, so it cannot meet the customer requirements. Customers may be bothered by the following problems:
1. Poor consistency and real-timeness because multiple public IPs need to be distinguished, each region is deployed with a cluster, multiple logical layers need to be maintained, and data read/write need to be performed across regions.
2. Too much subject to operator link quality. For example, service providers A and U suffered BGP network exceptions due to backbone network failures of an ISP in Beijing. As a result, the game could not be accessed in some regions and lost a large number of users.
3. All DDoS attacks target a single IP, which is very dangerous.

## Solutions
Based on customer's requirements, Tencent Cloud provides a solution to help solve the problems, as shown in the following figure:

![方案图](https://mc.qcloudimg.com/static/img/b98c06a9d399545c9760b5ba6dac161d/image.png)

The key points of the solution are as follows:
1. Use Anycast EIP. The IP can Anycast in multiple regions at the same time to share one server across the globe.
The user backend maintains one set of clusters and binds the Anycast EIP. The EIP uses Tencent Cloud's backbone network and POP point to route in multiple regions.
The customer does not need to select a network or manually specify the IP publishing location. Traffics complete global load balance nearby and enter/exit from the optimal region, which simplifies the backend. In addition, the customer's IP is converged, and one IP and DNS rule is not required for each region, which simplifies the filing and management processes.
2. The transmission quality is improved.
Multiple IP publishing sites provides multiple paths, enhancing fault tolerance of the network. In addition, the Direct Connect transmission is used after the nearby access, providing higher reliability, lower latency and improved player experience. For example, if the network linkage of China Telecom fails between Beijing and Hebei, but the IPs in Guangzhou and Shanghai can still distribute routes, the traffic of game users from Hebei to access Beijing will bypass to Tencent Cloud through the BGP traffic portal of Shanghai or Guangzhou. Therefore, this game company can continue to serve the players in case a disruption occurs in the services of its competitors.

