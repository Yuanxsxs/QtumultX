/*

Quantumult X
unlock Egoreader PRO

[version]


[rewrite_local]
# unlock Shapr3D
^https?:\/\/api\.pxmage\.com\/egoreader\/user\/info url script-response-body Ego_reader.js
[mitm]
hostname = api.pxmage.com


*/

let obj = JSON.parse($response.body);
var sub = {
    "username": "q210948213@gmail.com",
    "membershipType": "subscription",
    "expireAt": 1669351050571,
    "serverTime": 1666672709136
}
obj.data = sub;
obj.data.expireAt = 4096586883571
$done({body: JSON.stringify(obj)});
// ;"expirationDate" : "2023-09-21T03:16:14.207Z",