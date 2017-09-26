Tencent Cloud's database hosting data centers are distributed in different locations worldwide, which are divided into regions and availability zones.

Each region is an independent geographical location. Within each region, there are multiple mutually isolated locations referred to as availability zones. Each region is completely independent. Each availability zone is independent. However, availability zones in the same region can be connected via private network links with low latency.

Tencent Cloud supports distribution of cloud resources in different locations by users. Users are advised to consider placing resources in different availability zones when designing system to shield "service unavailable" status caused by single point of failure.


<table class="table-striped">
    <tbody>
        <tr>
            <th>&nbsp;</th>
            <th>Region</th>
            <th>Availability Zone</th>
        </tr>
        <tr>
            <td rowspan="7">Within Chinese territory</td>
            <td rowspan="3">South China (Guangzhou)</td>
            <td>Guangzhou Zone 1 (Sold out)</td>
        </tr>
        <tr>
            <td>Guangzhou Zone 2</td>
        </tr>
        <tr>
            <td>Guangzhou Zone 3</td>
        </tr>
        <tr>
            <td>South China (Shenzhen Finance)</td>
            <td>Shenzhen Finance Zone 1<span style="background-color: rgb(249, 249, 249);"> (only financial institutions and enterprises can initiate tickets for application)</span></td>
        </tr>
        <tr>
            <td>East China (Shanghai)</td>
            <td>Shanghai Zone 1</td>
        </tr>
        <tr>
            <td>East China (Shanghai Finance)</td>
            <td>Shanghai Finance Zone 1 (only financial institutions and enterprises can initiate tickets for application)</td>
        </tr>
        <tr>
            <td>North China (Beijing)</td>
            <td>Beijing Zone 1</td>
        </tr>
        <tr>
            <td rowspan="3">Outside China</td>
            <td>Southeast Asia (Hong Kong)</td>
            <td>Hong Kong Zone 1</td>
        </tr>
        <tr>
            <td>Southeast Asia (Singapore)</td>
            <td>Singapore Zone 1</td>
        </tr>
        <tr>
            <td>North America (Toronto)</td>
            <td>Toronto Zone 1</td>
        </tr>
    </tbody>
</table>



## Region
Different regions of Tencent Cloud are completely isolated to ensure maximal stability and fault tolerance among those regions. Currently, South China, East China, and North China are covered domestically, and Hong Kong and Singapore nodes for South East Asia and Toronto node for North America are also available. We will gradually increase region supply for coverage of more nodes. Users are advised to choose the region closest to their clients in order to reduce access latency and improve download speed.

Region attribute is differentiated for all behaviors such as enabling and viewing instances by users. If image of the instance that the users need to enable does not exist in the region, then the image needs to be copied to current region. For more information, refer to [Copy image][1].

- Even located in different availability zones, cloud resources in the same region are connected via private network, and can be accessed directly via [Private IP][2].
- Cloud products of different regions <font color="red">cannot communicate via private network by default</font>.
 - CVMs cannot access other CVMs, Cloud Database or Cloud Memcached across regions by default.
 - When binding Cloud Load Balance to the server, only CVM in the current region can be chosen;
- Cloud resources of different regions can perform Internet access via [Public IP][3]. Cloud Services in VPC can also communicate via [Peering connections][4] provided by Tencent Cloud using Tencent Cloud high-speed connected network, to realize connection that is more stable and faster than Internet access.
- [Cloud Load Balance][5] does not support cross-region traffic forwarding.
- The name of regional availability zone is the most straightforward representation of the coverage range of a data center. To make it easier for clients to understand the name of regional availability zone, the "coverage range + city where the data center is located" structure is used for region naming. The first half represents the coverage capability of the data center, and the second half indicates the city where the data center is located or near to. Availability zone name adopts the "city + number" structure.
- The above private network interconnection refers to the interconnection among resources under the same account. Private networks for resources under different accounts are completely isolated.

**Special instructions about Hong Kong region:**
- The following cloud services are temporarily unavailable: Cloud Memcached, elastic web engine, Cloud Object Storage, Cloud Block Storage, one-click opening of server and domain binding with separated regions and servers.
- When you need to log in to CVMs in Hong Kong region, login via jump server is recommended for better operation and maintenance experience.

**Special instructions about North America region:**
- The following cloud services are temporarily unavailable: Cloud Memcached, elastic web engine, Cloud Object Storage, mobile acceleration, Cloud Automated Testing, one-click opening of server and domain binding with separated regions and servers.
- Due to the considerable latency between North America and China, when you need to log in to CVMs in North America region, login via jump server is recommended for better operation and maintenance experience.

**Special instructions about Shanghai Finance Zone:**
Compliance zone customized according to regulatory requirements of finance industry features high level of security and isolation. Currently available services are CVM, finance database, Redis storage, face recognition, etc. Verified clients in finance industry can apply for using the zone by submitting tickets. For details, refer to [Introduction to finance zone][6].

## Availability zone
Availability zones (Zone) refer to Tencent Cloud's physical data centers whose power and network are independent from each other within the same region. They are designed to ensure that the failures within an availability zones can be isolated (except for large-scale disaster or major power failure) without spreading to and affecting other zones so that users' businesses can provide continuous online services. By starting an instance in an independent availability zone, users can protect their applications from being affected by the failures occurring in a single location.

When starting an instance, users can choose any availability zone within the specified region. If a user needs to ensure the high reliability of application systems so that the services are still available even when a failure occurs in an instance, the user can use cross-zone deployment scheme (e.g. [Cloud Load Balance][7], [Elastic IP][8], etc.) to allow the instance in another availability zone to handle the relevant requests in place of the failed instance.

## How to select region and availability zone
When purchasing Cloud Services, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve download speed.


[1]:	/doc/product/213/4943
[2]:	/doc/product/213/5225
[3]:	/doc/product/213/5224
[4]:	/doc/product/215/5000
[5]:	https://www.qcloud.com/doc/product/214
[6]:	http://www.qcloud.com/doc/product/304/%E9%87%91%E8%9E%8D%E4%BA%91%E7%AE%80%E4%BB%8B
[7]:	https://www.qcloud.com/doc/product/214
[8]:	/doc/product/213/5733
