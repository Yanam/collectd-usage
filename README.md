collectd-usage
==============

这是collectd工具的使用总结

首先是[colldctd官网](https://collectd.org/)

collectd经过一段时间的使用，感觉还是很方便的，各项监控数据都可以通过插件形式配置完成，各类插件基本覆盖了常见需求，阀值报警的配置也十分方便，
监控数据可以选择csv、rrd等多种形式存储，基本可以满足一般监控系统的展示需求。

###启动collectd

sbin/collectd

###关闭collectd

ps -ef|grep collectd
kill -9 pid


###日志、rrd文件等文件的路径
所有文件的路径都可以collectd.conf文件中进行配置

tail -f /data/collected-5.4.1/var/log/threshold.log 

tail -f /data/collected-5.4.1/var/log/collectd.log 

/data/collected-5.4.1/var/lib/collectd/rrd/yudf-204194/cpu-0


###collectd-web
需要下载[collectd-web官网](http://collectdweb.appspot.com/)，[GitHub地址](https://github.com/httpdss/collectd-web)

####collectd-web的启动
cd collectd-web
python runserver.py

启动成功后访问http://127.0.0.1:8888即可

####启动失败？
启动失败可能是collectd-web有几个依赖包没有安装，我遇到的是下面这三个
centos
yum install rrdtool-perl
yum install perl-libwww-perl
yum install perl-JSON


###各种文件(自己定制的)的介绍
下面这些文件都是当时在使用collectd时根据具体业务需求编写的，仅供参考，不具有普遍意义。

我们采用的是单服务端多客户端的方式进行部署的，所有数据都汇总到服务端的rrd文件中，配置了阀值报警，并通过触发脚本将报警信息上报到相关监控系统。

collectd.conf.client 客户端配置文件
collectd.conf.server 服务端配置文件

alarm.py、alarm.sh 是报警需要的相关脚本，在collectd.conf.server文件中可以看到相关的配置，目的是将collectd本身的报警信息发送到外部接口中。

dialy-report.sh、dialy-report.py、daily-report-awk.awk 目的是从rrd文件中生成日报（各监控插件的状态汇总），日报的调用需要在Linux的crontab中使用下面这句命令来定时启动

> ./daily-report.sh |awk '{ a[$1] =a[$1]"#"$2" "$3}END{for (i in a) print i"~~"a[i]}'
