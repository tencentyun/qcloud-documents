Tencent Cloud Monitor provides the following monitoring metrics for CKafka instances:

| Indicator         | Name          | Description                                     | Unit   | Dimension             |
| ------------- | -------------- | ---------------------------------------- | ---- | -------------- |
| Production traffic          | pro_flow       | Instance-level production traffic. Calculate the sum at a granularity of 1 or 5 minutes                | MB   | Instance             |
| Consumption traffic          | con_flow       | Instance-level consumption traffic. Calculate the sum at a granularity of 1 or 5 minutes                | MB   | Instance             |
| Amount of retained messages         | instance_heap  | Amount of messages stored in the disk at instance level. Get the latest value at a granularity of 1 or 5 minutes               | MB   | Instance             |
| Number of production messages          | pro_count      | Number of production messages at instance level. Calculate the sum at a granularity of 1 or 5 minutes               | -    | Instance             |
| Number of consumption messages          | con_count      | Number of consumption messages at instance level. Calculate the sum at a granularity of 1 or 5 minutes               | -    | Instance             |
| Number of production requests       | pro_req_count  | Number of production requests at instance level. Calculate the sum at a granularity of 1 or 5 minutes              | -    | Instance             |
| Number of consumption requests       | con_req_count  | Number of consumption requests at instance level. Calculate the sum at a granularity of 1 or 5 minutes              | -    | Instance             |
| Number of retained messages        | msg_count      | Number of messages stored in the disk at instance level. Get the latest value at a granularity of 1 or 5 minutes               | -   | Instance             |
| Production traffic          | pro_flow       | Topic-level production traffic. Calculate the sum at a granularity of 1 or 5 minutes             | MB   | Topic          |
| Consumption traffic          | con_flow       | Topic-level consumption traffic. Calculate the sum at a granularity of 1 or 5 minutes             | MB   | Topic          |
| Amount of retained messages         | msg_heap       | Amount of messages stored in the disk at Topic level. Get the latest value at a granularity of 1 or 5 minutes            | MB   | Topic          |
| Number of production messages          | pro_count      | Number of production messages at Topic level. Calculate the sum at a granularity of 1 or 5 minutes             | -    | Topic          |
| Number of consumption messages          | con_count      | Number of consumption messages at Topic level. Calculate the sum at a granularity of 1 or 5 minutes             | -    | Topic          |
| Number of production requests       | pro_req_count  | Number of production requests at Topic level. Calculate the sum at a granularity of 1 or 5 minutes           | -    | Topic          |
| Number of consumption requests       | con_req_count  | Number of consumption requests at Topic level. Calculate the sum at a granularity of 1 or 5 minutes           | -    | Topic          |
| Number of retained messages        | msg_count      | Number of messages stored in the disk at Topic level. Get the latest value at a granularity of 1 or 5 minutes           | -    | Topic          |


For more information about how to use the monitoring metrics of CKafka, please see the API [Read Monitoring Data](https://cloud.tencent.com/document/api/248/4667) in the Cloud Monitor API.

