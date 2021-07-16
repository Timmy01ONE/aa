input
{
    kafka
{
    bootstrap_servers = > "172.25.24.61:9092"
topics = > ["backend_log"]
group_id = > "logstash_kafka_consumer_backendlog"
consumer_threads = > 20
# auto_offset_reset => "earliest"
}
}
filter
{
    json
{
    source = > "message"
}
mutate
{
    remove_field = > "@version"
remove_field = > "tags"
copy = > {"[log][file][path]" = > "service"}
}
mutate
{
    copy = > {"[log][file][path]" = > "file"}
}
mutate
{
    gsub = > ["service", "\/data\/\S+\/([a-zA-Z_-]+)\.\S+", "\1"]
gsub = > ["file", "\/data\/\S+\/([a-zA-Z_-]+)\.\S+", "\1"]
}

if [log][file][path] == "/data/log/lua.access.log" {
grok {
match = > {"message" = > '\[%{DATA:time_local}\]\s*"%{WORD:method}\s%{DATA:request}"\s%{NUMBER:upstream_response_time}\s%{NUMBER:status}\s%{NUMBER:body_bytes_sent}\s"%{DATA:http_referer}"\s"%{DATA:http_user_agent}"\s"%{DATA:x_request_id}"\s"%{IP:client_ip}"\s"%{DATA:uid}"'}
}
mutate {
remove_field = > "message"
}
}
}

output
{
# stdout { codec => rubydebug }
if [log][file][path] == "/data/log/lua.access.log"
{
    elasticsearch
{
    hosts = > ["172.25.24.226:9200"]
user = > "elastic"
password = > "78JqXJ9RW-b-hsq"
index = > "backend-access-log-write"
}
# stdout { codec => rubydebug }
}
else {
    elasticsearch
{
    hosts = > ["172.25.24.226:9200"]
user = > "elastic"
password = > "78JqXJ9RW-b-hsq"
index = > "backend-log-write"
}
}

}