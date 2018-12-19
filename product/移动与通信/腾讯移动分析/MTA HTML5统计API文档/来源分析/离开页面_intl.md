### Feature Description
Query the number of times that a visitor leaves the last page he/she accesses on a daily basis.

**API URL:** `http://mta.qq.com/h5/api/ctr_page_exit`
**HTTP request method:** GET.

### Parameters

| Parameter Name | Type | Meaning | Note |
|---------|---------|---------|---------|
| app_id | Integer | App ID | The ID generated during application registration |
| urls | String | url address | Multiple url addresses are separated with "," and must be URL-encoded |
| start_date | String | Start time | Start time (Y-m-d) |
| end_date | String | End time | End time (Y-m-d) |
| sign | String | Verification string | See the example of generation process |

