### 1. API for Flow Deletion in Channel Mode

The API is not provided to create flow in LVB Code mode, so there is no API for flow deletion in this mode.

The API is provided to create and delete flow in channel mode. API for flow deletion: https://cloud.tencent.com/document/product/267/4722

### 2. Deleting Channel

In channel mode, you can delete a channel on the console, while in the LVB code mode, you are not allowed to delete a channel. The LVB backend automatically deletes LVB code flows that are not pushed in last 7 days. The LVB code id with ongoing flows being pushed will not be deleted.

### 3. Channel Number Limit

In the LVB code mode, there is no limit on the number of created channels.

In channel mode, a maximum of 50 channels can be created by default. If more channels are needed, please apply for us to dissolve the limit on the backend.

In addition, the monthly concurrent flow pushing increases as the flow pushing increases, thus leading to more channel cost.

