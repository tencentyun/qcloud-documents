### Feature Description
Query the terminal information data on a daily basis.

**API URL:** `http://mta.qq.com/h5/api/ctr_client/get_by_content`
**HTTP request method:** GET.

### Parameters

| Parameter Name | Type | Meaning | Note |
|---------|---------|---------|---------|
| app_id | Integer | App ID | The ID generated during application registration |
| start_date | String | Start time | Start time (Y-m-d) |
| end_date | String | End time | End time (Y-m-d) |
| type_id | Integer | Terminal attribute | For available values, please see Appendix (Terminal Attribute). |
| type_contents | String | Terminal name | Available values are the client value returned by terminal attribute list, which must be URL-encoded. Separate query metrics with "," |
| idx | String | Metric list | For available values, please see Appendix (metric dictionary). Separate query metrics with "," |
| sign | String | Verification string | See the example of generation process |

### Query Metrics

| Metric | Meaning | Calculation Method |
|---------|---------|---------|
| pv | Number of times that a page has been opened | When a page is opened once, one page view is counted |
| uv | Number of visits per day excluding repeated visits | One unique visit is counted if the page is visited multiple times by the same visitor in a day |
| vv | Number of visits per day | A visitor opens your website until he/she closes all pages and leaves the website, and one visit view is counted |
| iv | Number of IPs used to visit a website in a day | - |
