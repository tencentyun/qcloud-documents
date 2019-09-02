We'll still use the example of an e-commerce website from the last document. Assume that a customer orders a new mobile phone, the associated subsystems will act as follows:
- Grant membership growth value after the payment is confirmed
- The gift system sends gifts to the customer 
- The coupon system sends coupons to the user three months after the order is completed 
- The customer ERP system records customer purchase behavior for analysis

It can be found that these tasks are independent from each other, that is, a task can be executed individually without waiting for the results of other modules. The introduction of Tencent Cloud CMQ can bring the following benefits:

- CMQ ensures reliable delivery of messages: Even if the recipient is not available due to power failure, downtime or CPU overload when the message is being sent, the CMQ system can ensure that the message is delivered when the recipient is available. CMQ's distributed message queue enables a message to be retained persistently until the recipient gets it successfully;
- The data produced can be consumed in different scenarios at the same time and be reused for many times. For example, the order data after produced can be retained in the CMQ persistently and be consumed by logic, business, billing, monitoring, statistics and other modules;
- The message life cycle can be defined according to different business characteristics, and deferred processing and multiple processing for messages can be achieved.

![](//mccdn.qcloud.com/static/img/550b2fd8b8c3fb6bc6e2d4a299b6401b/image.png)
