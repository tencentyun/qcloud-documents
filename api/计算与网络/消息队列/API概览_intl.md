
## Queue Model

### Queue-related APIs
| Feature | Action ID | Description
|---------|---------|---------|
| [Create a queue](/doc/api/431/5832) | CreateQueue | It is used to create a new queue under the user's account. |
| [Get queue list](/doc/api/431/5833) | ListQueue | It is used to display the queue list under the account, and the list can be obtained by page. |
| [Get queue attributes](/doc/api/431/5834) | GetQueueAttributes | It is used to get attributes of a created queue. |
| [Modify queue attributes](/doc/api/431/5835) | SetQueueAttributes | It is used to modify attributes of a message queue. |
| [Delete a queue](/doc/api/431/5836) | DeleteQueue | It is used to delete a created queue. |


### Message-related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| [Send a message](/doc/api/431/5837) | SendMessage | It is used to send a message to a specified queue. |
| [Send a batch of messages](/doc/api/431/5838) | BatchSendMessage | It is used to send a batch of messages to a specified queue. |
| [Consume a message](/doc/api/431/5839) | ReceiveMessage | It is used to consume a message in the queue. |
| [Consume a batch of messages](/doc/api/431/5924) | BatchReceiveMessage | It is used to consume multiple messages in the queue. |
| [Delete a message](/doc/api/431/5840) | DeleteMessage | It is used to delete a message that has been consumed. |
| [Delete a batch of messages](/doc/api/431/5841) | BatchDeleteMessage | It is used to delete a batch of messages that have been consumed. |


## Topic Model

### Topic-related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| [Create a topic](/doc/api/406/7405) | CreateTopic | It is used to create a new topic under the user's account. |
| [Modify topic attributes](/doc/api/406/7406) | SetTopicAttributes | It is used to modify attributes of a created topic. |
| [Get topic list](/doc/api/406/7407) | ListTopic | It is used to display the topic list under the account, and the list can be obtained by page. |
| [Get topic attributes](/doc/api/406/7408) | GetTopicAttributes | It is used to get attributes of a created topic. |
| [Delete a topic](/doc/api/406/7409) | DeleteTopic | It is used to delete a created topic. |


### Message-related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| [Publish a message](/doc/api/406/7411) | PublishMessage | It is used to publish a message on a specified topic. |
| [Publish a batch of messages](/doc/api/406/7412) | BatchPublishMessage | It is used to publish a batch of messages on a specified topic. |
| [Deliver messages](/doc/api/406/7420) |||


### Subscription-related APIs
| Feature | Action ID | Description |
|---------|---------|---------|
| [Create a subscription](/doc/api/406/7414) | Subscribe | It is used to create a new subscription under the user's account. |
| [Get subscription list](/doc/api/406/7415) | ListSubscriptionByTopic | It is used to display the subscription list under the topic, and the list can be obtained by page. |
| [Modify subscription attributes](/doc/api/406/7416) | SetSubscriptionAttributes | It is used to set attributes of a created subscription. |
| [Get subscription attributes](/doc/api/406/7418) | GetSubscriptionAttributes | It is used to get attributes of a created subscription. |
| [Delete a subscription](/doc/api/406/7417) | Unsubscribe | It is used to delete a created subscription. |

