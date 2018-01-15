Third-party mobile financial payment solution providers in close cooperation with WeChat, such as SwiftPass, have enabled off-line stores in all industries to improve efficiency and avoid inefficient cash settlement through WeChat Pay. The payment system is structured as follows:

1. The payment request submitted by a customer in a convenience store (such as 7-11) will be sent to WeChat Pay which will return ACK after acknowledgment.

2. After the returned ACK is confirmed, WeChat Pay system will send a message of "Successful Payment" displaying account information, time point, amount and terminal information. This message will then be sent to SwiftPass.

3. SwiftPass will write the details into CMQ for temporary storage. As the important settlement evidence between SwiftPass and the store (convenience store), the message of "Successful Payment" must be delivered in a reliable way to avoid losses.

4. The order payment message in CMQ will be returned to the servers of multiple stores (convenience store). This process can be addressed asynchronously without rapid feedback. The specific steps are: the message is written into the Queue, and an http proxy will pull the message from the Queue; then the message will be sent to the stores after pulled out.

5. Before CMQ is connected, if SwiftPass fails to inform the store, it will initiate a request to WeChat Pay again which will sent the same order payment message to SwiftPass for a second time. After CMQ is connected, the success rate of SwiftPass increases significantly from the perspective of WeChat, thus it will get a rating boost (in reliability and credit) from WeChat.

6. At last, each order payment message will be delivered to systems including Risk Control Management, Activity Management and Promotion by another topic. For instance, Risk Control Management will continuously analyze each order payment delivered by topic. If there is a surge in store A's transaction volume in a short time (It is suspected of scalping), the callback API will be used to stop subsequent transactions of store A.


Please refer to the following figure:
![](https://mc.qcloudimg.com/static/img/66c1ce82cd5b1a1112a5729550e19fd3/image.png)
