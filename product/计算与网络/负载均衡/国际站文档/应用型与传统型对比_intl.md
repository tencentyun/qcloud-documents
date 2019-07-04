## Prices and Product Positioning of Cloud Load Balancer Instances

## Cloud Load Balancer Product Positioning

When selecting products, you can refer to the following product positioning of application and conventional cloud load balancer products:

<table>
        <tbody>
                <tr>
            <th style="width: 10%;" rowspan="2">Product Type</th>
            <th style="width: 45%;" colspan="2" >Application Cloud Load Balancer</th>
            <th style="width: 45%;" colspan="2">Conventional Cloud Load Balancer</th>
        </tr>
        <tr>
            <th>Public Network</th>
            <th>Private Network</th>
            <th>Public Network</th>
            <th>Private Network</th>
        </tr>
        <tr>
            <td>Layer-7 forwarding (HTTP/HTTPS)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
        </tr>
        <tr>
            <td>Layer-4 forwarding (TCP/UDP)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
        </tr>    
                <tr>
            <td>HTTP/2 and websocket (secure) supported</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
        </tr>
        <tr>
            <td>Cloud Load Balance Policy</td>
                        <td>ip hash (Layer-7)<br>Weighted Round-Robin Scheduling<br>Weighted Least Connections Scheduling</td>
                        <td>ip hash (Layer-7)<br>Weighted Round-Robin Scheduling<br>Weighted Least Connections Scheduling</td>
                        <td>ip hash (Layer-7)<br>Weighted Round-Robin Scheduling<br>Weighted Least Connections Scheduling</td>
                        <td>Weighted Round-Robin Scheduling</td>
        </tr>   
         <tr>
            <td>Session Persistence</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
        </tr>   
        <tr>
            <td>Health Check</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✔</td>
        </tr>   
         <tr>
            <td>Custom Forwarding Rules (Domain Name/URL)</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
            <tr>
            <td>Forwarding to Different Backend Ports</td>
                        <td>✔</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
         <tr>
            <td>Redirection (rewrite)</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
             <tr>
            <td>Cross-region binding</td>
                        <td>✔</td>
                        <td>✖</td>
                        <td>✖</td>
                        <td>✖</td>
        </tr>   
        <tr>
            <td>Logs storage in COS</td>
                        <td>✔ (Layer-7)</td>
                        <td>Available soon</td>
                        <td>✔ (Layer-7)</td>
                        <td>✖</td>
        </tr>   
</tbody></table>

> Note: When a user cancels cloud load balance service in advance, the corresponding charges will be deducted from blocked balance in the user account according to the actual usage period. The remaining balance will be returned to the account.

## Cloud Load Balance Bandwidth Fee

### Bandwidth Fee Billing Scenario
1) CVM is paid by bandwidth: Consumed bandwidth is public network bandwidth already contained in the CVM. No additional bandwidth fee will be charged;
2) CVM is paid by traffic: Public network cloud load balancer used by the user will cause traffic, which will incur a corresponding cost. 

### Bandwidth Fee Billing Standard
In the above mentioned scenario 2), the actual bandwidth fee for using CLB refers to the network fee incurred by backend CVMs. For more information on the billing mode, please see [Network Billing](http://cloud.tencent.com/doc/product/213/%E8%B4%AD%E4%B9%B0%E7%BD%91%E7%BB%9C%E5%B8%A6%E5%AE%BD).

