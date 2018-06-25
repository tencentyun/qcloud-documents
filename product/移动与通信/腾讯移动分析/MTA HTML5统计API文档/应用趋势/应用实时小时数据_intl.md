### Feature Description
Query App's hourly pv\uv\vv\iv data of the day.

**API URL:** `http://mta.qq.com/h5/api/ctr_realtime/get_by_hour`
**HTTP request method:** GET.

### Parameters

| Parameter Name | Type | Meaning | Note |
|---------|---------|---------|---------|
| app_id | Integer | App ID | The ID generated during application registration |
| idx | String | Metric list | For available values, please see Appendix (Metric Dictionary). Separate query metrics with "," |
| sign | String | Verification string | See the example of generation process |

### Query Metrics

| Metric | Type | Description |
|---------|---------|---------|
| pv | Number of times that a page has been opened | When a page is opened once, one page view is counted |
| uv | Number of visits per day excluding repeated visits | One unique visit is counted if the page is visited multiple times by the same visitor in a day |
| vv | Number of visits per day | A visitor opens your website until he/she closes all pages and leaves the website, and one visit view is counted |
| iv | Number of IPs used to visit a website in a day | - |

