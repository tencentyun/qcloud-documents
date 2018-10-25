A new mobile phone will be launched at an e-commerce website, and users with reservation codes are given the priority to purchase the new product. The users can obtain the reservation codes just by registering an account. And it is expected that there will be more than 10 million users to request for a reservation code.

In business scenarios sensitive to IO latency such as "Seckilling" on Double 11 Day or flash sale for mobile phone reservation, when the volume of external requests exceeds the capacity of a system on which no protective measures are taken, every request processed by the system will be rendered invalid due to timeout caused by the overload of timeout requests accumulated over time, leading to the total failure of the service provided by the system. And the service cannot be recovered automatically.

![](//mccdn.qcloud.com/static/img/359a93649d78a12b1d0fd20aad46b920/image.png)

In this case, the middleware, Tencent Cloud CMQ, can be introduced to make the non-real-time business logics asynchronous, such as the three business logics for the service for receiving requests, for processing requests and for returning results.

After the CMQ is introduced, when the reservation campaign starts, there is a surge of massive concurrent visits:
- For every reservation request from customer, a message indicating success will be returned on the page. Then the customer can close the page and go on with other activities. The reservation code will then be sent to the customer's mailbox/mobile phone later:
- If the number of registration and reservation requests exceeds 10 million, these requests can be stored temporarily in the Tencent Cloud CMQ clusters
- and be processed by the backend service based on the actual "select", "insert" and "update" capacities of the database.
- After the requests are processed successfully, the results are returned to the users. Every user will receive the reservation code within 5-30 minutes after the reservation request is made.
