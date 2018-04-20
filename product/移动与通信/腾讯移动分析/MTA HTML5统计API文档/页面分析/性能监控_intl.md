### Feature Description
Query the access latency and parsing time of corresponding provinces and cities on a daily basis.

**API URL:** `http://mta.qq.com/h5/api/ctr_page_speed`
**HTTP request method:** GET.

### Parameters

| Parameter Name | Type | Meaning | Note |
|---------|:---------:|---------|---------|
| app_id | Integer | App ID | The ID generated during application registration |
| start_date | String | Start time | Start time (Y-m-d) |
| end_date | String | End time | End time (Y-m-d) |
| type_contents | String | Province or City ID/Operator ID/Page URL | For available values of​provinces and cities, please see Appendix (Province/City). For available values of operators, please see Appendix (Operator). Page URL must be URL encoded. Separate query metrics with "," |
| type | String | Category | For available values, please see Appendix (Performance Monitor). |
| idx | String | Metric list | For available values, please see Appendix (metric dictionary). Separate query metrics with "," |
| sign | String | Verification string | See the example of generation process |

### Query Metrics

| Metric | Meaning | Calculation Method |
|---------|---------|---------|
| visitor_speed | Access latency | Average of user's total visit duration |
| dns_speed | DNS resolution time | DNS resolution time |
| tcp_speed | Duration for TCP connection | The time taken for TCP to establish connection with server |
| request_speed | Time to first byte | The time taken to receive the server response minus the time taken to initiate HTTP request |
| resource_speed | Duration for resource download | The time period from finishing loading all the resources within onload calculation range to performing dom object parsing on the document |
| dom_speed | Duration for page rendering | Time consumed in a process from building elements to displaying them in a page |


