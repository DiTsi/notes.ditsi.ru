# telegraf

```bash
# # Stream and parse log file(s).
[[inputs.logparser]]
#   ## Log files to parse.
#   ## These accept standard unix glob matching rules, but with the addition of
#   ## ** as a "super asterisk". ie:
#   ##   /var/log/**.log     -> recursively find all .log files in /var/log
#   ##   /var/log/*/*.log    -> find all .log files with a parent dir in /var/log
#   ##   /var/log/apache.log -> only tail the apache log file
   files = ["/var/log/mikrotik/mikrotik_syslog"]
#  
#   ## Read files that currently exist from the beginning. Files that are created
#   ## while telegraf is running (and that match the "files" globs) will always
#   ## be read from the beginning.
   from_beginning = true
#  
#   ## Method used to watch for file updates.  Can be either "inotify" or "poll".
#   # watch_method = "inotify"
#
#   ## Parse logstash-style "grok" patterns:
   [inputs.logparser.grok]
#     ## This is a list of patterns to check the given log file(s) for.
#     ## Note that adding patterns here increases processing time. The most
#     ## efficient configuration is to have one pattern per logparser.
#     ## Other common built-in patterns are:
#     ##   %{COMMON_LOG_FORMAT}   (plain apache & nginx access logs)
#     ##   %{COMBINED_LOG_FORMAT} (access logs + referrer & agent)
     #patterns = ["%{MONTH:month} %{DAY:day} %{TIME:time} %{GREEDYDATA:message}"]
     patterns = ["%{MONTH:month} %{MONTHDAY:day} %{HOUR:hour}:%{MINUTE:minute}:%{SECOND:second} %{MIKHOST:host} %{GREEDYDATA:message}"]
#
#     ## Name of the outputted measurement name.
#     measurement = "apache_access_log"
#
#     ## Full path(s) to custom pattern files.
#     custom_pattern_files = []
#
#     ## Custom patterns can also be defined here. Put one pattern per line.
     custom_patterns = 'MIKHOST ([a-zA-Z\-]+)'
```