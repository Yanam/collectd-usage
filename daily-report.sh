#! /bin/sh

rrd_root=/data/collected-5.4.1/var/lib/collectd/rrd/
cd $rrd_root
for idc in `ls -A`
do
    #echo $idc
    cd $idc
    for monitorType in `ls -A`
    do
       #echo $monitorType
       for rrdfile in ${monitorType}/*;
       do
           echo $rrdfile
           filename=$idc"/"$rrdfile
           export filename

           type=MAX
           export type
           rrdtool fetch $rrd_root$idc"/"$rrdfile MAX -s -1h|/root/ikv-dailyReport-awk.awk

           type=MIN
           rrdtool fetch $rrd_root$idc"/"$rrdfile MIN -s -1h|/root/ikv-dailyReport-awk.awk

           type=AVERAGE
           rrdtool fetch $rrd_root$idc"/"$rrdfile AVERAGE -s -1h|root ikv-dailyReport-awk.awk
       done
    done
done