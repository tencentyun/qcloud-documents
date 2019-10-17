## **Calculation Formula**
**BWP fee is:** monthly peak \* number of valid days (days with non-zero bandwidth value) / number of days in the billed month.
>**Note:**
> The billing methods for the two types of BWPs are identical. For the relevant parameters of different consumption modes, see the **Descriptions of Parameters** below.

## **Descriptions of Parameters**
### **Postpaid - Top 5 Monthly Peaks**
- **Daily peak**
The bandwidth value of the BWP's total bandwidth is taken every five minutes, the average value is the higher value of the inbound and outbound traffic, and the fifth highest average value is taken as the daily peak.
- **Monthly peak**
On the billing date, the taken daily peaks are sorted from high to low, and the average of the top 5 values is recorded as the monthly peak.
- **Number of valid days**
The number of days when the bandwidth is not zero.

### Postpaid - The 95th Monthly Peak
- **Monthly peak**
The bandwidth value of the BWP's total bandwidth is taken every five minutes, and the average value is the higher value of the inbound and outbound traffic; on the billing date, the taken average bandwidth values are sorted from high to low, the highest 5% of the values are removed, and the next highest value is used as the monthly peak.
