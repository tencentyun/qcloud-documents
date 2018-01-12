Before using Tencent Cloud CMQ, you need to get familiar with the following identifiers: queue name, message ID and receipt handle.

### 1. Queue Name
When creating a new queue, you must specify a unique queue name within the current region. The same queue name can be used among different regions. Tencent Cloud CMQ uses region plus queue name to identify a queue. You need to provide both parameters whenever you want to work with the queue.

### 2. Message ID

Each message receives a system-assigned message ID that Tencent Cloud returns to you in the SendMessage response. This identifier is used to identify messages. However, you need to provide the message's receipt handle rather than the message ID to delete a message. Example of a message ID format: "Msg-XXXXXXXX".

### 3. Receipt Handle

Every time you receive a message from a queue, you receive a receipt handle for that message. This handle is associated with the action of receiving the message, not with the message itself. To delete the message or to change the message visibility, you must provide the receipt handle (not the message ID). Thus, you must always receive a message before you can delete/change it.

> Note: If you receive a message more than once, each time you receive it, you get a different receipt handle. You must provide the most recently received receipt handle when you request to delete the message. Otherwise, the message might not be deleted.
