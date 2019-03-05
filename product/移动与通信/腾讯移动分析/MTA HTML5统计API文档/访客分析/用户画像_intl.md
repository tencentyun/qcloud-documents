### Feature Description
Query the user profile data on the H5 tracking platform, including gender proportion, age distribution, education distribution, occupation distribution. The data of the API is pv.

**API URL:** `http://mta.qq.com/h5/api/ctr_user_portrait`;
**HTTP request method:** GET.

### Parameters

| Parameter Name | Type | Meaning | Note |
|---------|---------|---------|---------|
| app_id | Integer | App ID | The ID generated during application registration |
| start_date | String | Start time | Start time (Y-m-d) |
| end_date | String | End time | End time (Y-m-d) |
| idx | String | Metric list | For available values, please see Appendix (metric dictionary). Separate query metrics with "," |
| sign | String | Verification string | See the example of generation process |

### Query Metrics

| Metric | Meaning | Calculation Method |
|---------|---------|---------|
| sex | Gender | - |
| age | Age | - |
| grade | Education | - |
| profession | Occupation | - |


