CMQ Message Timers allow you to specify an initial invisibility period for a message that you add to a queue, which is called "in flight". For example, if you send a message with the DelaySeconds parameter set to 45, the message isn't visible to consumers for the first 45 seconds during which the message stays in the queue. The default value for DelaySeconds is 0.

**Configuration range for delay messages:** When you specify a queue to produce messages, you can configure the QueueDelaySeconds parameter with a value range of 0-3600 seconds, which means the maximum invisibility period for a message is 1 hour. If this parameter is left empty, there is no delay.

**Note:** There can be a maximum of 1,000,000 inflight messages per queue. If you reach this limit, the extra messages will be invisible in the queue. Currently, this feature is not supported under the Topic mode.

