CMQ provides a message rewind feature similar to kafka. With this feature, you can re-consume the message that you have consumed and deleted before, and easily perform business reconciliation, business system reboot, and other operations for your core financial businesses.

## Feature Description

![](//mc.qcloudimg.com/static/img/5c1699ab442ad36b7e34a091bbcf089d/image.jpg)

As shown above, the fragments in the blue box represents the message lifecycle. After the message rewind is enabled, the message that has been consumed and deleted by a consumer will enter *message for rewind* zone. CMQ backend will still retain this message. However, once exceeding the message lifecyle specified in Queue (if it is set to 1 day), the message will be deleted automatically and cannot be rewound. Specific product logic is as follows:

- **Enabling:** If the message rewind is not enabled, the message that has been consumed and deleted by a consumer will be deleted immediately. If it is enabled, you must specify the rewindable cycle for message rewind with a range no larger than that of the message lifecycle.

- **Milestone:** Based on the above policy, after the message rewind is enabled, the number of rewindable messages will increase as messages are repeatedly consumed and deleted by the consumer.

- **Disabling:** If the message rewind is disabled, the messages in the "message for rewind" zone will be deleted immediately and cannot be rewound.

- **Queue attribute:**Message rewind is a Queue attribute, which can be configured when a queue is created or in the configuration modification section. After specifying the rewind time, all the consumers will consume the messages produced after the specified time.

- **Billing:**After the message rewind is enabled, rewindable message will generate some retention fees. The unit price will be calculated together with the message retention fee.

- **Specified rewind time:**To rewind consumption, consumers need to specify the Queue Name and the specific rewind time. You need to rewind back from the furthest point of time. Time is key, and the message cannot be consumed retroactively. As shown above, the messages can only be consumed from timeA to timeB/timeC, and cannot be consumed in a reverse way.

- **Specified rewind time range:**0 to 15 days. Only if the message rewind is enabled in the console, the deleted messages can be rewound. It is recommended that you keep the message rewind enabled for key applications. In addition, the message rewind cycle should be aligned with the message lifecycle.

- **The retained messages cannot be specified for rewind:** If a message is retained and not consumed, you cannot specify a specific location for consumption.

## Rewindable Range

**The maximum rewindable time** = Current time - the configured rewind time The messages cannot be rewound if produced before this time; otherwise, they can be rewound, as shown below:

![](//mc.qcloudimg.com/static/img/44d1295f8c6a3b63c03cc949b470cf65/image.jpg)




## Timeline

**Message rewind** The messages for rewind will be sorted based on their production time rather than the deletion time.
As shown in the figure below:

![](//mc.qcloudimg.com/static/img/7ff35a9529762ca3d832c19e643f782b/image.jpg)




