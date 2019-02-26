Tencent Cloud Monitor provides the following monitoring metrics for CMQ message queue:

| Indicator Name      | Description                  | Unit   | Dimension   |
| ---------- | --------------------- | ---- | ---- |
| Number of invisible messages in queue  | Number of messages with a status of "invisible" in message queue     | -    | Per queue  |
| Number of visible messages in queue   | Number of messages with a status of "visible" in message queue      | -    | Per queue  |
| Number of requests for sending messages    | Number of requests for sending messages to message queue by producers     | -    | Per queue  |
| Number of messages sent    | Number of messages sent to message queue by producers     | -    | Per queue  |
| Number of requests for receiving messages    | Number of requests for pulling messages from message queue by consumers     | -    | Per queue  |
| Number of received messages    | Number of messages pulled from message queue by consumers     | -    | Per queue  |
| Number of received empty messages   | Number of empty messages pulled from message queue by consumers      | -    | Per queue  |
| Number of empty messages received in batches | Number of empty messages pulled from message queue in batches by consumers    | -    | Per queue  |
| Number of requests for message deletion   | Number of requests for message deletion sent to message queue by consumers | -    | Per queue  |
| Number of deleted messages    | Number of messages deleted by consumers          | -    | Per queue  |
| Size of the messages sent    | Size of messages sent to message queue by producers     | -    | Per queue  |
| Size of the messages sent in batches  | Total size of the massages sent to message queue in batches by producers  | -    | Per queue  |
| Number of requests for batch sending of messages | Number of requests for sending messages to message queue in batches by producers    | -    | Per queue  |
| Number of requests for batch receiving of messages | Number of requests for pulling messages from message queue in batches by consumers   | -    | Per queue  |
| Number of requests for batch deletion of messages | Number of requests for sending messages in batches by consumers        | -    | Per queue  |

Tencent Cloud Monitor provides monitoring data for CMQ topic subscription:

| Indicator Name       |  Description               | Unit   | Dimension   |
| ----------- |  ------------------ | ---- | ---- |
| Number of published messages     | Number of messages sent to topic by producers    | -    | Per topic  |
| Number of messages published in batches     | Number of messages sent to topic in batches by producers    | -    | Per topic  |
| Number of requests for publishing messages    | Number of requests for sending messages to topic by producers     | -    | Per topic  |
| Number of requests for batch publishing of messages | Number of requests for sending messages to topic in batches by producers  | -    | Per topic  |
| Size of published messages    | Size of messages sent to topic by producers     | -    | Per topic  |
| Size of messages published in batches  | Total size of the messages sent to topic in batches by producers | -    | Per topic  |


For more information about how to use the monitoring metrics of CMQ, please see the API [Read Monitoring Data from Message Queue](https://cloud.tencent.com/document/product/248/11013) in the Cloud Monitor API.
