The Qidian.com under China Reading Limited meets its 3 core demands through CMQ:

 1. In the "Zhangyishucai" operation system, the scrambled monthly pass for red packets will not be posted synchronously. The posting information will be written into the MQ first, and then the consumer pulls the information from MQ. After the consumer confirms the consumption, the callback API will delete the message in MQ.

 2. The journal logs of systems of Qidian.com, including the O&M, alarm, and operation systems, will be gathered in the CMQ first, and the big data analysis cluster in the backend will continuously pull messages from CMQ and analyze them based on the processing capacity. There is no upper limit for the number of retained messages in CMQ theoretically, exempting users from future worries.

 3. A message rewind feature similar to kafka is provided. You can re-consume the message that has been deleted after a business is successfully consumed using the message rewind feature, and also specify the offset position. This facilitates the reconciliation and business system retry by Qidian.com.

With a QPS for API requests of over 100,000 and a request volume per day of over 1 billion, the pressure imposed on CMQ by the overall business of Qidian can be huge. Customers may wonder if CMQ can provide stable support for such a huge business volume?

Users are unknown about the cluster in CMQ backend. CMQ controller server can relocate a queue according to the load of the cluster. If the request volume of a queue exceeds the service threshold of the current cluster, controller server will distribute queue routing to several clusters to improve concurrent volume, realizing infinite message retention and super-high QPS in theory.


Please refer to the following figure:
![](https://mc.qcloudimg.com/static/img/71a51a5cee46ea14a8ff0944855f68d4/image.png)
