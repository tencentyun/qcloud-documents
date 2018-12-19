## 1. Will the alarm recipient only receive a message when the alarm is triggered? Will this message be sent again after a certain period of time?
No. The alarm will be converged, and the same alarm will be sent only once to users. The alarm not recovered for a CVM will not be sent repeatedly; but if a recovered alarm is triggered again for a CVM, the recipient will receive the message.
## 2. For a default policy, if the user canceled its association with a CVM in Associate Alarm Object page, will it be associated automatically at backend?
No. If a user disassociates a CVM from a default policy, it will not be automatically associated again at backend.
## 3. How many alarm statuses in cloud monitoring and what do they mean?
Not recovered: The alarm is not processed or is being processed.
Recovered: The alarm has been recovered to a normal status.
Insufficient data: The alarm policy for a generated alarm has been deleted; the CVM is migrated from one project to another; no data is submitted if the Cloud Monitor Agent has not been installed or has been uninstalled.
## 4. Can a CVM be bound with only one alarm policy?
Yes. A CVM can only be bound with one alarm policy. For example: CVM "1.1.1.1" has been associated with alarm polic
y A. If a user associates CVM "1.1.1.1" with alarm policy B, the association with alarm policy A will be automatically canceled.
## 5. Can default alarm policy be set only in CVMs? What about in other products?
Yes. The default alarm policy can only be set in CVMs and others cannot.
## 6. If the alarm policy for CDN domain of project A has been associated with domain name "a.com", but the user migrates "a.com" to project B, what will happen to alarm policies?
The alarm policy for CDN domain of project A will be automatically disassociated with "a.com". After disassociating, "a.com" will no longer be associated with any alarm policy for CDN domain and the alarm will not be generated. The logic for automatic disassociation will be processed once a day, so it is normal if the data update in the console page is delayed.
## 7. Why do users still receive an alarm after the CVM is disassociated?
The system detects the monitoring data every 5 minutes, thus leading to certain latency. You may still receive the alarm in a short time after the alarm policy is disassociated with the CVM.

