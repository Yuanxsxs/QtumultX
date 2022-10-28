/*

Quantumult X
unlock Shapr:3D PRO

[version]
5.214.0.4058 #1c6d065d

[rewrite_local]
# unlock Shapr3D local
^https?:\/\/prod\.api\.shapr3d\.com\/user-management\/profile-with-device url script-response-body Shapr3D.js
[mitm]
hostname = api.pxmage.com,

*/

let obj = JSON.parse($response.body);
var sub = {"period" : "yearly","expirationDate" : "2023-09-21T03:16:14.207Z","purchaseDate" : "2022-09-21T03:16:14.207Z","id" : 611416,"isTrial" : false,"tier" : "pro","effectiveFeatureSet" : "pro","type" : "edu","autoRenewStatus" : false};
obj.subscriptions[0] = sub;
obj.subscriptions[0].expirationDate = "2100-01-01T00:00:00.000Z";
obj.subscriptionType = "edu";
obj.subscriptionExpires = "2100-01-01T00:00:00.000Z";
$done({body: JSON.stringify(obj)});
// ;"expirationDate" : "2023-09-21T03:16:14.207Z",
