
## 1. Alarm Convergence 
We may receive a large number of duplicate alarms in a short period of time, which affects the failure analysis. Therefore, the "alarm convergence" feature is provided by Failure Self-recovery.

Corresponding convergence is executed when a certain rule is met.

![](https://mc.qcloudimg.com/static/img/b6bbc913516f5578455134c8ba1fcfb4/14955235563509.jpg)

As shown below, the last rule above is hit (three or more alarms are generated in 5 minutes on the same server).

![](https://mc.qcloudimg.com/static/img/dee929eef7e96cbf5ac8c7b4b7a6b2a9/14955234725854.jpg)

> Since no approval action was performed, timeout occurred in 20 minutes.

## 2. Health Diagnosis

If alarms occur on some servers frequently, Failure Self-recovery automatically analyzes these alarms and make a diagnosis to find out the risks in advance.

![](https://mc.qcloudimg.com/static/img/15a1cf5ec9986861833155e4c0934e90/14955238707264.jpg)

## 3. Alert Self-recovery

If PING alarm occurred six times this month, they might be neglected during manual processing.

"Alert Self-recovery" will analyze recent exception alarm events to help you eliminate the risks in advance with self-recovery solution, which can be found under the "Advanced Settings" menu.

![](https://mc.qcloudimg.com/static/img/95d9831c10ecc3070027b8098e7ba3cb/14955236702912.jpg)

Failure Self-recovery enables an Alert Self-recovery Package by default (if alarms of unreachable PING or server restart occurred for the same server of an idle server module five times over the last 30 days, the server will be transferred to the faulty server module).

Alert Self-recovery analyzes alarms at 8:00 a.m. every day and then perform self-recovery.

![](https://mc.qcloudimg.com/static/img/6c62349830048764c6b64a0ac308375d/14955091745764.jpg)

Alert Self-recovery is an extension of Health Diagnosis.

## 4. Combination Package

You can combine the packages of Failure Self-recovery with the official universal packages to implement the failure recovery in complex scenarios.

The configuration of combined packages is actually to maintain a binary tree. For a node, the left sub-node represents the successful subsequent package and the right sub-node represents the failed subsequent package.

The configuration page of combination packages is shown below:

![](https://mc.qcloudimg.com/static/img/84417e166add95c052e5204336c261fa/14955228844734.jpg)

Details of execution result are shown below:

![](https://mc.qcloudimg.com/static/img/eba1c07ce6701750cbbf0ca49c4bb687/14955229063739.jpg)

With combination packages, you can implement more complex OPS scenarios.








