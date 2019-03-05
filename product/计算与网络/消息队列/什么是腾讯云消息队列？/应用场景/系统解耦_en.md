Take the IT architecture in e-commerce as an example: In traditional tight-coupling ordering scenario, a customer places an order with an e-commerce website, for instance, to purchase a mobile phone. After receiving the request, the order system calls the API of inventory system immediately, with the stock quantity of the commodity decreasing by 1. However, such model carries huge risks:

- Due to the tight-coupling between the order system and inventory system, the failure to access the inventory system (caused by upgrade, business changes or faults) will makes inventory subtraction based on order impossible, thus leading to the failure of the order.
- Traditional solution to the problem is establishing a "socket" connection between the order system and inventory system. However, in case of the change of IP/port of inventory system or addition of receivers of inventory system, it is necessary to make changes to the order system.
- Massive requests in short time and frequent SQL queries on and modifications to inventory data place a heavy load on the inventory system.
- User experience: When the order processing fails, user makes a retry, then the retry still fails, and so on...resulting in the customer churn.

The scheme with CMQ is shown as below:
![](//mccdn.qcloud.com/static/img/faf759d10bd01b50b8ff19d40fe93f13/image.png)

Several systems work separately for decoupling:

- Order system: After an order is placed by a user, the system processes the data on a basis of persistency, and writes the message into message queue, then returns the order to the user. The order placement is completed successfully. At this point, the user can consider that the mobile phone has been purchased successfully. CMQ offers asynchronous communication protocol, which means that after sending a message to the message queue, the sender can go back immediately instead of waiting for a response from the receiver. The message will be retained in the queue until it is fetched by the receiver.

- Inventory system: The system handles inventory data based on the order information acquired from CMQ.

In this way, the order placement will not be affected even if the inventory system is down during the process (When recovered, the inventory system will acquire the order information from CMQ for processing). After writing the order information into CMQ, the order system is not responsible for any subsequent operations. Now, the decoupling between the order system and inventory system is achieved.

In businesses like e-commerce where reliable delivery of messages needs to be ensured, even if the receiver (inventory system) is unavailable for reasons such as power outage, crash or CPU overload when the sender (order system) sends a message, receiver can still receive the message once becoming available. The distributed message queue storage of Tencent Cloud CMQ ensures that the message is stored persistently until it is acquired by the receiver successfully without any data loss that may occur when some message queue schemes are stored in the memory of a single machine.
