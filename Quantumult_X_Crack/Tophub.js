/*

Quantumult X
unlock tophub PRO

[version]


[rewrite_local]
# unlock tophub
^https?:\/\/api2\.tophub\.app\/account\/sync\?.* url script-response-body Tophub.js
[mitm]
hostname = api2.tophub.app

*/

let obj = JSON.parse($response.body);
var sub = {
    "is_vip": "1",
    "vip_expired": "1669563067",
    "is_vip_now": true
}
obj.data = sub;
obj.data.vip_expired = 4096798847
$done({body: JSON.stringify(obj)});
