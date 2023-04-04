# 自用Qx配置

---
## [✏️重写](https://github.com/Yuanxsxs/QtumultX/tree/master/Rewrite)

|项目|一键安装|
|:---:|:---:|
|[自用重写去广告](https://github.com/Yuanxsxs/QtumultX/raw/master/Rewrite/AD_block/Self_use_Adblock.snippet)|[一键安装](https://api.boxjs.app/quanx/add-resource?remote-resource=%7B%22rewrite_remote%22%3A%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Rewrite/AD_block/Self_use_Adblock.snippet%3Fraw%3Dtrue%2Ctag%3DSelf_use_Adblock-Yuanxsxs%22%5D%7D)|
---
## [🍴分流](https://github.com/Yuanxsxs/QtumultX/tree/master/Filter)
|项目|一键安装|
|:---:|:---:|
|[自用分流](https://github.com/Yuanxsxs/QtumultX/blob/master/Filter/myself.txt)|[一键安装](https://api.boxjs.app/quanx/add-resource?remote-resource=%7B%22rewrite_remote%22%3A%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Filter/myself.txt%3Fraw%3Dtrue%2Ctag%3Dmyself-Yuanxsxs%22%5D%7D)|
|[OpenAi](https://gitlab.com/lodepuly/vpn_tool/-/raw/main/Tool/Loon/Rule/OpenAI.list)|[一键安装](https://quantumult.app/x/open-app/add-resource?remote-resource=%7B%22filter_remote%22%3A%5B%22https%3A//gitlab.com/lodepuly/vpn_tool/-/raw/main/Tool/Loon/Rule/OpenAI.list%3Fraw%3Dtrue%2Ctag%3DOpenAI-lodepuly%22%5D%7D)|

---
## [👀图标](https://github.com/Yuanxsxs/QtumultX/tree/master/Icon)

|项目|一键导入|项目|一键导入|
|:---:|:---:|:---:|:---:|
|[玖妹订阅](https://raw.githubusercontent.com/Yuanxsxs/QtumultX/master/Icon/JiuMei-icon/JiuMei-icon.json)|[一键导入](https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX%5C/master/Icon/JiuMei-icon/JiuMei-icon.json%22%5D)|[Food-Delivery](https://github.com/Yuanxsxs/QtumultX/blob/master/Icon/Food-Delivery.json)|[一键导入](https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX%5C/master/Icon/Food-Delivery.json%22%5D)|
|[Catcat](https://github.com/Yuanxsxs/QtumultX/blob/master/Icon/Catcat.json)|[一键导入](https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX%5C/master/Icon/Catcat.json%22%5D)|[QuantumultX_ICON](https://github.com/Yuanxsxs/QtumultX/blob/master/Icon/hellcell/QuantumultX_ICON.json)|[一键导入](https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX%5C/master/Icon/hellcell/QuantumultX_ICON.json%22%5D)|
|[Carton-icon](https://github.com/Yuanxsxs/QtumultX/blob/master/Icon/Carton-icon.json)|[一键导入](https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX%5C/master/Icon/Carton-icon.json%22%5D)|[QuantumultX_blackmini](https://github.com/Yuanxsxs/QtumultX/blob/master/Icon/hellcell/QuantumultX_blackmini.json)|[一键导入](https://quantumult.app/x/open-app/ui?module=gallery&type=icon&action=add&content=%5B%22https%3A//raw.githubusercontent.com/Yuanxsxs/QtumultX%5C/master/Icon/hellcell/QuantumultX_blackmini.json%22%5D)|

# [🧷Tools](https://github.com/Yuanxsxs/QtumultX/tree/master/tools)

- ### [make_quick_installation_link.py](https://github.com/Yuanxsxs/QtumultX/blob/master/tools/make_quick_installation_link.py)

  - #### 简介

    用来制作qx一键导入链接的工具,支持机场订阅,图标订阅,分流规则,重写规则,默认开启资源解析器,资源更新为48hours

  
  - ##### 原理
  
    [Quantumult-X/url-scheme.md at master/crossutility/Quantumult-X (github.com)](https://github.com/crossutility/Quantumult-X/blob/master/url-scheme.md)
  
  - ##### 准备
  
    安装依赖:```
    pip install pyperclip```    
  
  - ##### 使用
  
    1. 复制机分流规则,重写规则,图标订阅链接的raw值 例如 [GitHub的分流raw链接](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/GitHub/GitHub.list),或者文件所在位置 例如 [GitHub的分流规则](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/QuantumultX/GitHub/GitHub.list).
    2. 直接运行此脚本,不需要额外操作,待脚本运行结束,一键导入qx链接就已复制在剪切板.
  
    

