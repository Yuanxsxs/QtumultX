/*
[rewrite_local]
^https:\/\/app\.autocad360\.com\/entitlements\/v2\/me\/status url script-response-body https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Scrips/AutoCAD.js
[mitm]
hostname = app.autocad360.com

*/
var obj = JSON.parse($response.body);

obj = {
  "status": "ADSK_GRANTED_USERS_AUTODESK_EDUCATION_BUNDLE",
  "is_legacy_subscriber": true,
  "features": [
    "MyDesignStorage",
    "svc0000020",
    "svc0000087",
    "svc0000089",
    "svc0002664",
    "svc0003000"
  ],
  "is_trial": false,
  "is_authorized": true,
  "type": "ADSK_GRANTED_USERS_AUTODESK_EDUCATION_BUNDLE",
  "start_sec": 1709105997,
  "subscribed": true,
  "is_mobile_store_subscriber": true,
  "subscriptions": [],
  "expiry_sec": 4080428400,
  "is_edu_account": true,
  "recheck_sec": 1709218539
};

$done({ body: JSON.stringify(obj) });
