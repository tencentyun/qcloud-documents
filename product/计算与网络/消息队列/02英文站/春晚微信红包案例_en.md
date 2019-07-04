The red packet activity on the Spring Festival Gala relates to the linkage of four large systems, including WeChat, WeChat Pay, Red Packet and Tenpay. Here is a brief introduction to the systems:

- Red Packet system: It is responsible for the sending, scrambling and opening of personal red packets, and list viewing;
- Tenpay system: It is responsible for order payment, high-performance storage for asynchronous incoming payment journal, and real time display of users' balance and bill;
- WeChat Access: It ensures the quality of users' access to the public network;
- WeChat Pay: It is the entry to online transaction.
    
![](//mc.qcloudimg.com/static/img/4e497929b188b4ddc76fe43934d9c126/image.png)

The distributed transaction similar to the Red Packet system is a focus of attention. For instance, "User A sends a red packet containing 10 CNY to user B", the following steps are needed:
1) Read the balance in account A
2) Execute subtraction on account A (subtract 10 CNY)
3) Write the result back to account A (verify the result once)
4) Read the balance in account B
5) Open the red packet sent by account A and read the value
6) Execute addition on account B (add 10 CNY)
7) Write the result into account B
    
To ensure data consistency, there are only two results for the steps above: the steps are all executed successfully, or the steps all fail and rollback will be performed. Meanwhile, the distributed lock mechanism should be introduced for accounts A and B during the operation of the steps to avoid dirty data. Operation will become very complicated in such a large distributed cluster as WeChat Red Packet system.

WeChat Red Packet system introduces Tencent Cloud CMQ to reduce system costs from the increasing distributed transactions. The new policy for the same scenario after CMQ is introduced will be described below.

- In the step 7 above, user B opens the red packet which contains 10 CNY. The posting in the last step always fails due to the concurrent pressure.
- All of the failed posting requests will be sent to CMQ by the team of Red Packet. If user B fails to update the balance, the mobile client will be in waiting. Then the account system will pull the request from CMQ repeatedly to retry the update operation. CMQ ensures that the posting request for the 10 CNY will never be lost until it is pulled out.
- On the lunar New Year's Eve, requests such as sending, opening and posting of red packets are performed in about a billion times. If we use the traditional transactional method, the concurrent pressure will be intensified to crash the system.
- CMQ message queue ensures reliable storage and transmission of red packet data by writing data for three copies in real time to prevent data loss. Multiple attempts can be made in case of posting failure to prevent disadvantages of traditional methods such as rollback after failure and frequent polling of database.

