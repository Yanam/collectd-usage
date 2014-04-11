#!/bin/bash

#cat >> /data/collected-5.4.1/var/log/threshold.log
#cat|awk 'BEGIN{print "start"} {print $1"---"$2 >> "/data/collected-5.4.1/var/log/threshold.log" } END{ print "End" }'
cat|python /data/collected-5.4.1/etc/alarm.py >> /data/collected-5.4.1/var/log/threshold.log
#echo "$Notification"