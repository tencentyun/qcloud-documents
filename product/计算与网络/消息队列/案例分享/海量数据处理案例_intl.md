The first step to get started with big data is to extract valuable results from massive data through data mining and analysis to lead the business model in the future. Dianping.com and Didi Chuxing have obtained an extensive experience in such practices on Tencent Cloud. For instance, the popular restaurants that are shared among WeChat and QQ users will be displayed on the mobile client of Dianping app in real time and be recommended to consumers.

The data analysis system is composed of the following modules: data acquisition, data access, stream computing, offline computing and data persistence.

1) Data acquisition
It is responsible for collecting data from nodes in real time through open source flume. Data such as logs of all business servers will stream into the CMQ pipeline in the form of a funnel.

2) Data access
Since data acquisition and data processing may be out of sync, a CMQ message middleware is added as a buffer to ensure the reliability of log writing and analysis.

3) Stream computing and offline data analysis
The collected data is analyzed in real time using storm of apache. The offline data analysis achieves continuous data mining based on Spark.

4) Data output
Tencent Cloud CDB, Mysql and other solutions can be used for ensuring persistence of analyzed results.

![](//mccdn.qcloud.com/static/img/2af722aeb0303b136f73bb177928fe34/image.png)

In data processing scenarios, the input of massive amounts of log data is the message producer, and the Storm cluster for online analysis is the message consumer. Based on the experience, the business logic of the message consumer Storm in data processing may be complex (real-time computing, stream-based data processing and Topology data processing are involved). Meanwhile, the Storm fails very often, resulting in unrealizable consumption or unsmooth consumption in a short time. All in all, the efficiency of message producer is much higher than the message consumer.

In the Push model, the server cannot know the state of the current message consumer, so it will continuously push the data generated. Therefore, when the Storm cluster is highly loaded, using Push may increase the consumer's load and even make it crash, unless the message consumer has an appropriate feedback mechanism to inform the server of its state. While it will be easier if Pull is used. Since the message consumer pulls data from the server by itself, the load can be reduced by decreasing access frequency.

Tencent Cloud will launch topic model later and provide both PULL and PUSH methods for data acquisition. CMQ is used as the buffer between producer data and consumer data, which enables data to be read only when the consumer is available and ready. In this way, the problem of out of sync between message producer and message consumer is solved.
