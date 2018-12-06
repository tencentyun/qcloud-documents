You can write an SCF to process messages received by CKafka. The SCF backend module can be used as a consumer to consume the messages in CKafka and then send them to SCF.

CKafka trigger has the following features:

- **Pull model**: The backend module of SCF, as a consumer, connects to the CKafka instance and consumes messages. After receiving messages, the backend module encapsulates them into the data structure and calls the specified function to pass the data structure to the SCF.
- **Asynchronous call**: CKafka trigger always calls the function asynchronously, and does not return the result to the caller. For more information about call types, please see [Call Types](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## Attributes of CKafka Trigger

- CKafka instance: CKafka instance configured for connection. Only instance in the same region is supported.
- Topic: Supports topics already created in the CKafka instance.
- Maximum number of messages: The maximum number of messages pulled and sent in batches to the current SCF. The number of messages that are sent every time the SCF is triggered may not reach the limit depending on the size of massages and write speed. So it is a variable ranging from 1 to the maximum number.

## How to Consume and Send CKafka Messages

Since CKafka messages cannot be pushed automatically, but must be pulled by consumers for consumption. Therefore, after a CKafka trigger is configured, the SCF backend launches a CKafka consumer module as the consumer to consume messages in an independent consumer group it created in CKafka.

After consuming messages, the SCF backend consumer module encapsulates them into an event structure according to timeout, number and size of accumulated messages and maximum number of messages, and then sends it to the SCF. During the consumption, the number of encapsulated messages is different in each event structure, which ranges from **1 to the maximum number**. If the maximum number of messages configured is too large, the number of messages in the event structure will never reach the limit.

After obtaining the event content, the SCF can process messages on a loop to make sure every message is processed, rather than assuming that the number of message passed each time is constant.

## Event Message Structure of CKafka Trigger

When the specified CKafka Topic receive a message, the SCF backend consumer module consumes the message and encapsulates it into the following event structure in JSON format, then triggers the bound function and passes it the data content as input parameters.

```
{
  "Records": [
    {
      "Ckafka": {
        "topic": "test-topic",
        "partition":1,
        "offset":36,
        "msgKey": "None",
        "msgBody": "Hello from Ckafka!"
      }
    },
    {
      "Ckafka": {
        "topic": "test-topic",
        "partition":1,
        "offset":37,
        "msgKey": "None",
        "msgBody": "Hello from Ckafka again!"
      }
    }
  ]
}
```

The data structure is described as follows:

| Name | Content |
| ---------- | --- |
| Records | List structure. Multiple messages may be merged into the list |
| Ckafka   | Identifies the event source as CKafka |
| topic | Message source topic |
| partition | Partition ID of message source |
| offset | Consumption offset number |
| msgKey | Message key |
| msgBody | Message content |

