/*

Quantumult X
unlock Neat-reader PRO

[version]


[rewrite_local]
# unlock Neatreader
^https?:\/\/www\.neat-reader\.cn\/app\/api_v2\/getUserProfile url script-response-body Near-reader.js
[mitm]
hostname = api.pxmage.com


*/

let obj = JSON.parse($response.body);
var sub = {"code":1,"msg":"获取所有信息成功","userName":"q210948213@gmail.com","nickName":"","avatar":null,"registerTime":"2021-10-13T03:43:47.000Z","registerSource":0,"qqId":null,"weixinId":null,"weiboId":null,"googleId":null,"facebookId":null,"membershipExpireTime":1634701427000,"membershipType":2,"trial":1}
obj = sub;
obj.membershipExpireTime = 4102414159000
$done({body: JSON.stringify(obj)});
// ;"expirationDate" : "2023-09-21T03:16:14.207Z",