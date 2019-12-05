You can write an SCF to process messages received by CMQ Topic. CMQ Topic can pass messages to the SCF and call the function using the message content and relevant information as parameters.

CMQ Topic trigger has the following features:

- **Push model**: After receiving messages, CMQ Topic pushes them to all subscribers who subscribe to the Topic. If an SCF is configured, it is also used as a subscriber to receive the messages pushed from the queue. In the push model, CMQ Topic stores the event source mapping of the SCF.
- **Asynchronous call**: CMQ Topic always calls the function asynchronously, and does not return the result to the caller. For more information about call types, please see [Call Types](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## Attributes of CMQ Topic Trigger

- (Required) CMQ Topic: Configured CMQ Topic. Only CMQ in the same region is supported.

## Binding Limit on CMQ Topic Trigger
 
For CMQ Topic, a maximum of 100 subscribers are supported under a single topic. Therefore, if this limit is reached, binding of SCF triggers may fail. A topic can bind with multiple SCFs before this limit is reached.

CMQ Topic trigger supports triggering SCF with CMQ Topic messages in the same region, that is, when you configure a CMQ Topic trigger for an SCF created in Guangzhou region, you can only choose a CMQ Topic in the Guangzhou region (South China). To trigger an SCF with CMQ Topic messages in the specified region, you can create a function in this region.

## Event Message Structure of CMQ Topic Trigger
When receiving a message, the specified CMQ Topic sends the following event data in JSON format to the bound SCF.

```
{
  "Records": [
    {
      "CMQ": {
        "type": "topic",
        "topicOwner":120xxxxx,
        "topicName": "testtopic",
        "subscriptionName":"xxxxxx",
        "publishTime": "1970-01-01T00:00:00.000Z",
        "msgId": "123345346",
        "requestId":"123345346",
        "msgBody": "Hello from CMQ!",
        "msgTag": ["tag1","tag2"]
      }
    }
  ]
}
```

The data structure is described as follows:

| Name | Content |
| ---------- | --- |
| Records | List structure. Multiple messages may be merged into the list |
| CMQ       | Identifies the data structure source as CMQ |
| type | Determines whether the message source is topic or queue |
| topicOwner | Records the topic owner account ID |
| topicName | Records the topic name |
| subscriptionName | Records the subscription name of SCF under the topic |
| publishTime | Records the time when the message is published |
| msgId | Records the unique ID of the message |
| requestId | Records the ID of the request for message push |
| msgBody | Records the message content |
| msgTag | Records the message tag via the list structure |

