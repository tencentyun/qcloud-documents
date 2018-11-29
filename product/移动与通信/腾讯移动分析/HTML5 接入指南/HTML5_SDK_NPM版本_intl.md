### Installation
```
npm install mta-h5-analysis --save
```
### Importing and Reporting

```
import MtaH5 from 'mta-h5-analysis';
```

### Related Code

```
// Initialize
MtaH5.init({
  "sid":'********', //Required; appid for statistics
  "cid":'********',, //If you enable the custom event, this item is required, otherwise leave it empty.
  "autoReport":0,//Whether to enable automatic reporting (1: report upon completion of init; 0: report only when pgv method is used)
  "senseHash":0, //Whether the hash anchor is included in url statistics
  "senseQuery":0, //Whether url parameter is included in url statistics
  "performanceMonitor":0,//Whether performance monitoring is enabled
  "ignoreParams":[] //When url parameter reporting is enabled, ignore some parameters and stitch the remaining parameters and report
});

// Page reporting
MtaH5.pgv();

// Custom event reporting
MtaH5.clickStat("ico_search", {"query":"Tesla"});
```


