# -*- coding: utf-8 -*-
import requests
import json
import smtplib
from email.mime.text import MIMEText
from multiprocessing.dummy import Pool as ThreadPool
import time
import sys
import datetime
requests.adapters.DEFAULT_RETRIES = 5
import urllib3
urllib3.disable_warnings()

reload(sys)
sys.setdefaultencoding('utf-8')

station_list = [
    {
        "code": "AKU",
        "quanpin": "akesu",
        "name": "阿克苏",
        "duanpin": "aks"
    },
    {
        "code": "AAT",
        "quanpin": "aletai",
        "name": "阿勒泰",
        "duanpin": "alt"
    },
    {
        "code": "AKA",
        "quanpin": "ankang",
        "name": "安康",
        "duanpin": "ak"
    },
    {
        "code": "AQG",
        "quanpin": "anqing",
        "name": "安庆",
        "duanpin": "aq"
    },
    {
        "code": "BFU",
        "quanpin": "bangbu",
        "name": "蚌埠",
        "duanpin": "bb"
    },
    {
        "code": "BSD",
        "quanpin": "baoshan",
        "name": "保山",
        "duanpin": "bs"
    },
    {
        "code": "BAV",
        "quanpin": "baotou",
        "name": "包头",
        "duanpin": "bt"
    },
    {
        "code": "BHY",
        "quanpin": "beihai",
        "name": "北海",
        "duanpin": "bh"
    },
    {
        "code": "PEK",
        "quanpin": "beijing",
        "name": "北京",
        "duanpin": "bj"
    },
    {
        "code": "NAY",
        "quanpin": "beijingnanyuan",
        "name": "北京南苑",
                "duanpin": "bjny"
    },
    {
        "code": "CGQ",
        "quanpin": "changchun",
        "name": "长春",
                "duanpin": "cc"
    },
    {
        "code": "CGD",
        "quanpin": "changde",
        "name": "常德",
                "duanpin": "cd"
    },
    {
        "code": "CSX",
        "quanpin": "changsha",
        "name": "长沙",
                "duanpin": "cs"
    },
    {
        "code": "CIH",
        "quanpin": "changzhi",
        "name": "长治",
                "duanpin": "cz"
    },
    {
        "code": "CZX",
        "quanpin": "changzhou",
        "name": "常州",
                "duanpin": "cz"
    },
    {
        "code": "CHG",
        "quanpin": "chaoyang",
        "name": "朝阳",
                "duanpin": "cy"
    },
    {
        "code": "CTU",
        "quanpin": "chengdu",
        "name": "成都",
                "duanpin": "cd"
    },
    {
        "code": "CIF",
        "quanpin": "chifeng",
        "name": "赤峰",
                "duanpin": "cf"
    },
    {
        "code": "CKG",
        "quanpin": "chongqing",
        "name": "重庆",
                "duanpin": "cq"
    },
    {
        "code": "DLU",
        "quanpin": "dali",
        "name": "大理",
                "duanpin": "dl"
    },
    {
        "code": "DLC",
        "quanpin": "dalian",
        "name": "大连",
                "duanpin": "dl"
    },
    {
        "code": "DAT",
        "quanpin": "datong",
        "name": "大同",
                "duanpin": "dt"
    },
    {
        "code": "DAX",
        "quanpin": "daxian",
        "name": "达县",
                "duanpin": "dx"
    },
    {
        "code": "DDG",
        "quanpin": "dandong",
        "name": "丹东",
                "duanpin": "dd"
    },
    {
        "code": "LUM",
        "quanpin": "dehongmangshi",
        "name": "德宏芒市",
                "duanpin": "dhms"
    },
    {
        "code": "ENH",
        "quanpin": "enshi",
        "name": "恩施",
                "duanpin": "es"
    },
    {
        "code": "FUG",
        "quanpin": "fuyang",
        "name": "阜阳",
                "duanpin": "fy"
    },
    {
        "code": "FYN",
        "quanpin": "fuyun",
        "name": "富蕴",
                "duanpin": "fy"
    },
    {
        "code": "FOC",
        "quanpin": "fuzhou",
        "name": "福州",
                "duanpin": "fz"
    },
    {
        "code": "KOW",
        "quanpin": "ganzhou",
        "name": "赣州",
                "duanpin": "gz"
    },
    {
        "code": "GOQ",
        "quanpin": "geermu",
        "name": "格尔木",
                "duanpin": "gem"
    },
    {
        "code": "GHN",
        "quanpin": "guanghan",
        "name": "广汉",
                "duanpin": "gg"
    },
    {
        "code": "CAN",
        "quanpin": "guangzhou",
        "name": "广州",
                "duanpin": "gz"
    },
    {
        "code": "KWL",
        "quanpin": "guilin",
        "name": "桂林",
                "duanpin": "gl"
    },
    {
        "code": "KWE",
        "quanpin": "guiyang",
        "name": "贵阳",
                "duanpin": "gy"
    },
    {
        "code": "HMI",
        "quanpin": "hami",
        "name": "哈密",
                "duanpin": "hm"
    },
    {
        "code": "HRB",
        "quanpin": "haerbin",
        "name": "哈尔滨",
                "duanpin": "heb"
    },
    {
        "code": "HAK",
        "quanpin": "haikou",
        "name": "海口",
                "duanpin": "hk"
    },
    {
        "code": "HLD",
        "quanpin": "hailaer",
        "name": "海拉尔",
                "duanpin": "hle"
    },
    {
        "code": "HZG",
        "quanpin": "hanzhong",
        "name": "汉中",
                "duanpin": "hz"
    },
    {
        "code": "HGH",
        "quanpin": "hangzhou",
        "name": "杭州",
                "duanpin": "hz"
    },
    {
        "code": "HFE",
        "quanpin": "hefei",
        "name": "合肥",
                "duanpin": "hf"
    },
    {
        "code": "HTN",
        "quanpin": "hetian",
        "name": "和田",
                "duanpin": "ht"
    },
    {
        "code": "HEK",
        "quanpin": "heihe",
        "name": "黑河",
                "duanpin": "hh"
    },
    {
        "code": "HNY",
        "quanpin": "hengyang",
        "name": "衡阳",
                "duanpin": "hy"
    },
    {
        "code": "HET",
        "quanpin": "huhehaote",
        "name": "呼和浩特",
                "duanpin": "hhht"
    },
    {
        "code": "TXN",
        "quanpin": "huangshan",
        "name": "黄山",
                "duanpin": "hs"
    },
    {
        "code": "HYN",
        "quanpin": "taizhouhuangyan",
        "name": "台州黄岩",
                "duanpin": "tzhy"
    },
    {
        "code": "JZH",
        "quanpin": "jiuzhaigou",
        "name": "九寨沟",
                "duanpin": "jzg"
    },
    {
        "code": "KNC",
        "quanpin": "jian",
        "name": "吉安",
                "duanpin": "ja"
    },
    {
        "code": "JNG",
        "quanpin": "jining",
        "name": "济宁",
                "duanpin": "jn"
    },
    {
        "code": "JIL",
        "quanpin": "jiling",
        "name": "吉林",
                "duanpin": "jl"
    },
    {
        "code": "TNA",
        "quanpin": "jinan",
        "name": "济南",
                "duanpin": "jn"
    },
    {
        "code": "JMU",
        "quanpin": "jiamusi",
        "name": "佳木斯",
                "duanpin": "jms"
    },
    {
        "code": "JGN",
        "quanpin": "jiayuguan",
        "name": "嘉峪关",
                "duanpin": "jyg"
    },
    {
        "code": "JJN",
        "quanpin": "quanzhoujinjiang",
        "name": "泉州晋江",
                "duanpin": "qzjj"
    },
    {
        "code": "JNZ",
        "quanpin": "jinzhou",
        "name": "锦州",
                "duanpin": "jz"
    },
    {
        "code": "JDZ",
        "quanpin": "jingdezheng",
        "name": "景德镇",
                "duanpin": "jdz"
    },
    {
        "code": "JGS",
        "quanpin": "jinggangshan",
        "name": "井冈山",
                "duanpin": "jgs"
    },
    {
        "code": "JHG",
        "quanpin": "xishuangbanna",
        "name": "西双版纳",
                "duanpin": "xsbn"
    },
    {
        "code": "JIU",
        "quanpin": "jiujiang",
        "name": "九江",
                "duanpin": "jj"
    },
    {
        "code": "CHW",
        "quanpin": "jiuquan",
        "name": "酒泉",
                "duanpin": "jq"
    },
    {
        "code": "JUZ",
        "quanpin": "quzhou",
        "name": "衢州",
                "duanpin": "qz"
    },
    {
        "code": "KHG",
        "quanpin": "kashi",
        "name": "喀什",
                "duanpin": "ks"
    },
    {
        "code": "KRY",
        "quanpin": "kelamayi",
        "name": "克拉玛依",
                "duanpin": "klmy"
    },
    {
        "code": "KRL",
        "quanpin": "kuerle",
        "name": "库尔勒",
                "duanpin": "kel"
    },
    {
        "code": "KMG",
        "quanpin": "kunming",
        "name": "昆明",
                "duanpin": "km"
    },
    {
        "code": "KCA",
        "quanpin": "kuche",
        "name": "库车",
                "duanpin": "kc"
    },
    {
        "code": "LHW",
        "quanpin": "lanzhou",
        "name": "兰州",
                "duanpin": "lz"
    },
    {
        "code": "LXA",
        "quanpin": "lasa",
        "name": "拉萨",
                "duanpin": "ls"
    },
    {
        "code": "LJG",
        "quanpin": "lijiang",
        "name": "丽江",
                "duanpin": "lj"
    },
    {
        "code": "RSU",
        "quanpin": "lishui",
        "name": "丽水",
                "duanpin": "ls"
    },
    {
        "code": "LYG",
        "quanpin": "lianyungang",
        "name": "连云港",
                "duanpin": "lyg"
    },
    {
        "code": "LNJ",
        "quanpin": "lincang",
        "name": "临沧",
                "duanpin": "lc"
    },
    {
        "code": "LYI",
        "quanpin": "linyi",
        "name": "临沂",
                "duanpin": "ly"
    },
    {
        "code": "LZH",
        "quanpin": "liuzhou",
        "name": "柳州",
                "duanpin": "lz"
    },
    {
        "code": "LZO",
        "quanpin": "luzhou",
        "name": "泸州",
                "duanpin": "lz"
    },
    {
        "code": "LYA",
        "quanpin": "luoyang",
        "name": "洛阳",
                "duanpin": "ly"
    },
    {
        "code": "MIG",
        "quanpin": "mianyang",
        "name": "绵阳",
                "duanpin": "my"
    },
    {
        "code": "NZH",
        "quanpin": "manzhouli",
        "name": "满洲里",
                "duanpin": "mzl"
    },
    {
        "code": "MXZ",
        "quanpin": "meixian",
        "name": "梅县",
                "duanpin": "mx"
    },
    {
        "code": "MDG",
        "quanpin": "mudanjiang",
        "name": "牡丹江",
                "duanpin": "mdj"
    },
    {
        "code": "KHN",
        "quanpin": "nanchang",
        "name": "南昌",
                "duanpin": "nc"
    },
    {
        "code": "NAO",
        "quanpin": "nanchong",
        "name": "南充",
                "duanpin": "nc"
    },
    {
        "code": "NKG",
        "quanpin": "nanjing",
        "name": "南京",
                "duanpin": "nj"
    },
    {
        "code": "NNG",
        "quanpin": "nanning",
        "name": "南宁",
                "duanpin": "nn"
    },
    {
        "code": "NTG",
        "quanpin": "nantong",
        "name": "南通",
                "duanpin": "nt"
    },
    {
        "code": "NNY",
        "quanpin": "nanyang",
        "name": "南阳",
                "duanpin": "ny"
    },
    {
        "code": "NGB",
        "quanpin": "ningbo",
        "name": "宁波",
                "duanpin": "nb"
    },
    {
        "code": "PZI",
        "quanpin": "panzhihua",
        "name": "攀枝花",
                "duanpin": "pzh"
    },
    {
        "code": "NDG",
        "quanpin": "qiqihaer",
        "name": "齐齐哈尔",
                "duanpin": "qqhe"
    },
    {
        "code": "IQM",
        "quanpin": "qiemo",
        "name": "且末",
                "duanpin": "qm"
    },
    {
        "code": "SHP",
        "quanpin": "qinhuangdao",
        "name": "秦皇岛",
                "duanpin": "qhd"
    },
    {
        "code": "TAO",
        "quanpin": "qingdao",
        "name": "青岛",
                "duanpin": "qd"
    },
    {
        "code": "IQN",
        "quanpin": "qingyang",
        "name": "庆阳",
                "duanpin": "qy"
    },
    {
        "code": "SYX",
        "quanpin": "sanya",
        "name": "三亚",
                "duanpin": "sy"
    },
    {
        "code": "SHS",
        "quanpin": "shashi",
        "name": "沙市",
                "duanpin": "ss"
    },
    {
        "code": "SWA",
        "quanpin": "jieyang",
        "name": "揭阳",
                "duanpin": "jy"
    },
    {
        "code": "SHA",
        "quanpin": "shanghaihongqiao",
        "name": "上海",
                "duanpin": "sshq"
    },
    {
        "code": "PVG",
        "quanpin": "shanghaipudong",
        "name": "上海浦东",
                "duanpin": "sspd"
    },
    {
        "code": "SHE",
        "quanpin": "shenyang",
        "name": "沈阳",
                "duanpin": "sy"
    },
    {
        "code": "SZX",
        "quanpin": "shenzhen",
        "name": "深圳",
                "duanpin": "sz"
    },
    {
        "code": "SJW",
        "quanpin": "shijiazhuang",
        "name": "石家庄",
                "duanpin": "sjz"
    },
    {
        "code": "SYM",
        "quanpin": "simao",
        "name": "思茅",
                "duanpin": "sm"
    },
    {
        "code": "TCG",
        "quanpin": "tacheng",
        "name": "塔城",
                "duanpin": "tc"
    },
    {
        "code": "TYN",
        "quanpin": "taiyuan",
        "name": "太原",
                "duanpin": "ty"
    },
    {
        "code": "TSN",
        "quanpin": "tianjin",
        "name": "天津",
                "duanpin": "tj"
    },
    {
        "code": "TNH",
        "quanpin": "tonghua",
        "name": "通化",
                "duanpin": "th"
    },
    {
        "code": "TGO",
        "quanpin": "tongliao",
        "name": "通辽",
                "duanpin": "tl"
    },
    {
        "code": "TEN",
        "quanpin": "tongren",
        "name": "铜仁",
                "duanpin": "tr"
    },
    {
        "code": "HLH",
        "quanpin": "wulanhaote",
        "name": "乌兰浩特",
                "duanpin": "wlht"
    },
    {
        "code": "URC",
        "quanpin": "wulumuqi",
        "name": "乌鲁木齐",
                "duanpin": "wlmq"
    },
    {
        "code": "WXN",
        "quanpin": "wanzhou",
        "name": "万州",
                "duanpin": "wz"
    },
    {
        "code": "WEF",
        "quanpin": "weifang",
        "name": "潍坊",
                "duanpin": "wf"
    },
    {
        "code": "WEH",
        "quanpin": "weihai",
        "name": "威海",
                "duanpin": "wh"
    },
    {
        "code": "WNH",
        "quanpin": "wenshan",
        "name": "文山",
                "duanpin": "ws"
    },
    {
        "code": "WNZ",
        "quanpin": "wenzhou",
        "name": "温州",
                "duanpin": "wz"
    },
    {
        "code": "WUA",
        "quanpin": "wuhai",
        "name": "乌海",
                "duanpin": "wh"
    },
    {
        "code": "WUH",
        "quanpin": "wuhan",
        "name": "武汉",
                "duanpin": "wh"
    },
    {
        "code": "WUX",
        "quanpin": "wuxi",
        "name": "无锡",
                "duanpin": "wx"
    },
    {
        "code": "WUS",
        "quanpin": "wuyishan",
        "name": "武夷山",
                "duanpin": "wys"
    },
    {
        "code": "WUZ",
        "quanpin": "wuzhou",
        "name": "梧州",
                "duanpin": "wz"
    },
    {
        "code": "XIY",
        "quanpin": "xian",
        "name": "西安",
                "duanpin": "xa"
    },
    {
        "code": "XIC",
        "quanpin": "nanchang",
        "name": "西昌",
                "duanpin": "nc"
    },
    {
        "code": "XNN",
        "quanpin": "xining",
        "name": "西宁",
                "duanpin": "xn"
    },
    {
        "code": "XIL",
        "quanpin": "xilinhaote",
        "name": "锡林浩特",
                "duanpin": "xlht"
    },
    {
        "code": "XMN",
        "quanpin": "xiamen",
        "name": "厦门",
                "duanpin": "xm"
    },
    {
        "code": "XFN",
        "quanpin": "xiangfan",
        "name": "襄樊",
                "duanpin": "xf"
    },
    {
        "code": "XUZ",
        "quanpin": "xuzhou",
        "name": "徐州",
                "duanpin": "xz"
    },
    {
        "code": "ENY",
        "quanpin": "yanan",
        "name": "延安",
                "duanpin": "ya"
    },
    {
        "code": "YNZ",
        "quanpin": "yancheng",
        "name": "盐城",
                "duanpin": "yc"
    },
    {
        "code": "YNJ",
        "quanpin": "yanji",
        "name": "延吉",
                "duanpin": "yj"
    },
    {
        "code": "YNT",
        "quanpin": "yantai",
        "name": "烟台",
                "duanpin": "yt"
    },
    {
        "code": "YBP",
        "quanpin": "yibin",
        "name": "宜宾",
                "duanpin": "yb"
    },
    {
        "code": "YIH",
        "quanpin": "yichang",
        "name": "宜昌",
                "duanpin": "yc"
    },
    {
        "code": "YIN",
        "quanpin": "yining",
        "name": "伊宁",
                "duanpin": "yn"
    },
    {
        "code": "YIW",
        "quanpin": "yiwu",
        "name": "义乌",
                "duanpin": "yw"
    },
    {
        "code": "INC",
        "quanpin": "yinchuang",
        "name": "银川",
                "duanpin": "yc"
    },
    {
        "code": "ENE",
        "quanpin": "yingde",
        "name": "英德",
                "duanpin": "yd"
    },
    {
        "code": "LLF",
        "quanpin": "yongzhou",
        "name": "永州",
                "duanpin": "yz"
    },
    {
        "code": "UYN",
        "quanpin": "yulin",
        "name": "榆林",
                "duanpin": "yl"
    },
    {
        "code": "ZHA",
        "quanpin": "zhanjiang",
        "name": "湛江",
                "duanpin": "zj"
    },
    {
        "code": "DYG",
        "quanpin": "zhangjiajie",
        "name": "张家界",
                "duanpin": "zjj"
    },
    {
        "code": "ZAT",
        "quanpin": "zhaotong",
        "name": "昭通",
                "duanpin": "zt"
    },
    {
        "code": "CGO",
        "quanpin": "zhengzhou",
        "name": "郑州",
                "duanpin": "zz"
    },
    {
        "code": "HJJ",
        "quanpin": "zhijiang",
        "name": "芷江",
                "duanpin": "zj"
    },
    {
        "code": "DIG",
        "quanpin": "diqingxianggelila",
        "name": "迪庆香格里拉",
                "duanpin": "dqxgll"
    },
    {
        "code": "HSN",
        "quanpin": "zhoushan",
        "name": "舟山",
                "duanpin": "zs"
    },
    {
        "code": "ZUH",
        "quanpin": "zhuhai",
        "name": "珠海",
                "duanpin": "zh"
    },
    {
        "code": "ZYI",
        "quanpin": "zunyi",
        "name": "遵义",
                "duanpin": "zy"
    },
    {
        "code": "GYS",
        "quanpin": "guangyuan",
        "name": "广元",
                "duanpin": "gy"
    },
    {
        "code": "DNH",
        "quanpin": "dunhuang",
        "name": "敦煌",
                "duanpin": "dh"
    },
    {
        "code": "BPX",
        "quanpin": "changdu",
        "name": "昌都",
                "duanpin": "cd"
    },
    {
        "code": "YCU",
        "quanpin": "yuncheng",
        "name": "运城",
                "duanpin": "yc"
    },
    {
        "code": "ACX",
        "quanpin": "xingyi",
        "name": "兴义",
                "duanpin": "xy"
    },
    {
        "code": "DSN",
        "quanpin": "eerduosi",
        "name": "鄂尔多斯",
                "duanpin": "eeds"
    },
    {
        "code": "DOY",
        "quanpin": "dongying",
        "name": "东营",
                "duanpin": "dy"
    },
    {
        "code": "HDG",
        "quanpin": "handan",
        "name": "邯郸",
                "duanpin": "hd"
    },
    {
        "code": "LCX",
        "quanpin": "liancheng",
        "name": "连城",
                "duanpin": "lc"
    },
    {
        "code": "999",
        "quanpin": "quanguo",
        "name": "全国",
                "duanpin": "qg"
    },
    {
        "code": "OHE",
        "quanpin": "mohe",
        "name": "漠河",
                "duanpin": "mh"
    },
    {
        "code": "LZY",
        "quanpin": "linzhi",
        "name": "林芝",
                "duanpin": "lz"
    },
    {
        "code": "KJI",
        "quanpin": "kanasi",
        "name": "喀纳斯",
                "duanpin": "kns"
    },
    {
        "code": "NBS",
        "quanpin": "changbaishan",
        "name": "长白山",
                "duanpin": "cbs"
    },
    {
        "code": "AEB",
        "quanpin": "baise",
        "name": "百色",
                "duanpin": "bs"
    },
    {
        "code": "THQ",
        "quanpin": "tianshui",
        "name": "天水",
                "duanpin": "ts"
    },
    {
        "code": "LLB",
        "quanpin": "libo",
        "name": "荔波",
                "duanpin": "lb"
    },
    {
        "code": "HZH",
        "quanpin": "liping",
        "name": "黎平",
                "duanpin": "lp"
    },
    {
        "code": "TCZ",
        "quanpin": "techong",
        "name": "腾冲",
                "duanpin": "tc"
    },
    {
        "code": "ZHY",
        "quanpin": "zhongwei",
        "name": "中卫",
                "duanpin": "zw"
    },
    {
        "code": "NLT",
        "quanpin": "nalati",
        "name": "那拉提",
                "duanpin": "nlt"
    },
    {
        "code": "KGT",
        "quanpin": "kangding",
        "name": "康定",
                "duanpin": "kd"
    },
    {
        "code": "DQA",
        "quanpin": "daqing",
        "name": "大庆",
                "duanpin": "dq"
    },
    {
        "code": "YUS",
        "quanpin": "yushu",
        "name": "玉树",
                "duanpin": "ys"
    },
    {
        "code": "JXA",
        "quanpin": "jixi",
        "name": "鸡西",
                "duanpin": "jx"
    },
    {
        "code": "FUO",
        "quanpin": "foushan",
        "name": "佛山",
                "duanpin": "fs"
    },
    {
        "code": "ERL",
        "quanpin": "erlianhaote",
        "name": "二连浩特",
                "duanpin": "elht"
    },
    {
        "code": "AOG",
        "quanpin": "anshan",
        "name": "鞍山",
                "duanpin": "as"
    },
    {
        "code": "GYU",
        "quanpin": "guyuanliupanshan",
        "name": "固原六盘山",
                "duanpin": "gylps"
    },
    {
        "code": "LDS",
        "quanpin": "yichunlindu",
        "name": "伊春林都",
                "duanpin": "ycld"
    },
    {
        "code": "TVS",
        "quanpin": "tangshan",
        "name": "唐山",
                "duanpin": "ts"
    },
    {
        "code": "HIA",
        "quanpin": "huaian",
        "name": "淮安",
                "duanpin": "ha"
    },
    {
        "code": "JIQ",
        "quanpin": "chongqingzhoubai",
        "name": "重庆舟白",
                "duanpin": "cqzb"
    },
    {
        "code": "BPL",
        "quanpin": "xinjiangbole",
        "name": "新疆博乐",
                "duanpin": "xjbl"
    },
    {
        "code": "RKZ",
        "quanpin": "rikaze",
        "name": "日喀则",
                "duanpin": "rkz"
    },
    {
        "code": "NGQ",
        "quanpin": "ali",
        "name": "阿里",
                "duanpin": "al"
    },
    {
        "code": "JIC",
        "quanpin": "jinchang",
        "name": "金昌",
                "duanpin": "jc"
    },
    {
        "code": "AVA",
        "quanpin": "anshun",
        "name": "安顺",
                "duanpin": "as"
    },
    {
        "code": "YZY",
        "quanpin": "zhangye",
        "name": "张掖",
                "duanpin": "zy"
    },
    {
        "code": "RLK",
        "quanpin": "bayannaoer",
        "name": "巴彦淖尔",
                "duanpin": "byne"
    },
    {
        "code": "YIE",
        "quanpin": "baershan",
        "name": "阿尔山",
                "duanpin": "bes"
    },
    {
        "code": "YTY",
        "quanpin": "yangzhou",
        "name": "扬州",
                "duanpin": "yz"
    },
    {
        "code": "JGD",
        "quanpin": "jiagedaqi",
        "name": "加格达奇",
                "duanpin": "jgdq"
    },
    {
        "code": "ZQZ",
        "quanpin": "zhangjiakoujichang",
        "name": "张家口机场",
                "duanpin": "zjkjc"
    },
    {
        "code": "YIC",
        "quanpin": "yichun",
        "name": "宜春",
                "duanpin": "yc"
    },
    {
        "code": "TLQ",
        "quanpin": "tulufan",
        "name": "吐鲁番",
                "duanpin": "tlf"
    },
    {
        "code": "BFJ",
        "quanpin": "bijie",
        "name": "毕节",
                "duanpin": "bj"
    },
    {
        "code": "JUH",
        "quanpin": "chizhoujiuhuashanjichan",
        "name": "池州九华山机场",
                "duanpin": "czjhsjc"
    },
    {
        "code": "DCY",
        "quanpin": "daochengyading",
        "name": "稻城亚丁",
                "duanpin": "dcyd"
    },
    {
        "code": "GXH",
        "quanpin": "xiahe",
        "name": "夏河",
                "duanpin": "xh"
    },
    {
        "code": "KJH",
        "quanpin": "kailihuangpingjichang",
        "name": "凯里黄平机场",
                "duanpin": "klhpjc"
    },
    {
        "code": "AXF",
        "quanpin": "alashanzuoqi",
        "name": "阿拉善左旗",
                "duanpin": "alszq"
    },
    {
        "code": "RHT",
        "quanpin": "alashanyouqi",
        "name": "阿拉善右旗",
                "duanpin": "alsyq"
    },
    {
        "code": "EJN",
        "quanpin": "ejinaqi",
        "name": "额济纳旗",
                "duanpin": "ejnq"
    },
    {
        "code": "PKX",
        "quanpin": "beijingdaxingguojijichang",
        "name": "北京大兴国际机场",
                "duanpin": "bjdxgjjc"
    }
]

url = 'https://m.juneyaoair.com/server/v2/flight/AvFare'
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'versionCode': '17200',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'platformInfo': 'MWEB',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'channelCode': 'MWEB',
    'timeStamp': '1602432112627',
    'token': '',
    'clientVersion': '1.7.2',
    'Origin': 'https://m.juneyaoair.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://m.juneyaoair.com/flights/index.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# sendText 出发机场 ====> arrText 到达机场
def getParams(date, sendText, arrText="上海"):
    temp = {
        "returnDate": "2021-01-05",
        "flightType": "OW",
        "ffpId": "13488399",
        "blackBox": "eyJ2IjoiNGhYNnhwMGNMOXc5KzVnRnkwNDErMDVYTTNQblgrOEZHMDhXTzZ2UXJEcVQrTUJxUHhaMUFWSXF5UFgyVlQzNCIsIm9zIjoid2ViIiwiaXQiOjE1NTQsInQiOiJaRERRekhwbzR5ODZ5Uk9Ec1BYYS8wOFl5ekF2elN1TVFTbEJxU0JmajNpTFB1ODF2aVd0bkZEUzZmNWp3czN0czd0dXRpQzJFWitISzloMWlFbXBBZz09In0=",
        "sendCode": "SHA",
        "tripType": "D",
        # "sign": "c3f9c9cbc4503c1c5248ece837d61f11",
        "departureDate": "",
        "arrCode": "CSX",
        "clientVersion": "6.2.0",
        "directType": "D",
        "platformInfo": "ios",
        "channelCode": "MOBILE",
        "ffpCardNo": "3076356920",
        "loginKeyInfo": "522C87D00B02A4EE4A6EF57F5391695D"
    }
    temp["departureDate"] = date
    # temp["sign"] = sign
    temp["sendCode"] = getCode(sendText)
    temp["arrCode"] = getCode(arrText)
    return temp

def getCode(name):
    for item in station_list:
        if item["name"] == name:
            return(item["code"])

def sendemail(content):
    sendeOnemail(content, "xxxxxx@qq.com")

def sendeOnemail(content, receiverMail):
    # 发送者邮箱地址
    senderMail = 'xxxxxx@qq.com'
    # 发送者 QQ邮箱授权码
    authCode = ''
    # 接收者邮箱地址
    receiverMail = receiverMail
    # 邮件主题
    subject = content
    # 邮件内容
    content = content
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = senderMail
    msg['To'] = receiverMail
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        print('成功连接到邮件服务器')
        server.login(senderMail, authCode)
        print('成功登录邮箱')
        server.sendmail(senderMail, receiverMail, msg.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送异常')
    finally:
        server.quit()

def get_date(careinfo):
    time.sleep(10)
    s = json.dumps(careinfo['data'])
    try:
        r = requests.post(url=url, headers=headers, data=s, timeout=10, verify=False)
        jsons = json.loads(r.text)
        flightInfoList = jsons['flightInfoList']
        for flightInfo in flightInfoList:
            if (flightInfo['carrierNo'] in careinfo['flightNo']) or len(careinfo['flightNo']) == 0:
                # 只判断吉祥航空承运
                if ('HO' in flightInfo['carrierNo']):
                    for cabinFare in flightInfo['cabinFareList']:
                        if cabinFare['cabinCode'] == 'X':
                            str = u'%s (%s%s-%s%s) 起飞:%s 到达:%s ' % (
                                flightInfo['flightNo'], flightInfo['depCityName'], flightInfo['depAirportName'],
                                flightInfo['arrCityName'], flightInfo['arrAirportName'], flightInfo['depDateTime'],
                                flightInfo['arrDateTime'])
                            flightNoStatus = careinfo['flightNoCheck'].get(
                                flightInfo['flightNo'], None)
                            # 有票
                            if cabinFare['cabinNumber'] == 'A':
                                str = str + u'出现了！！！ '
                                if not (flightNoStatus) or flightNoStatus == '0':
                                    flightNoStatus = 'A'
                                    sendemail(str)
                            # 无票
                            elif cabinFare['cabinNumber'] == '0':
                                str = str + u''
                                if not (flightNoStatus) or flightNoStatus != '0':
                                    flightNoStatus = '0'
                            # 邮票
                            elif int(cabinFare['cabinNumber']) > 0:
                                str = str + u'还剩' + \
                                    cabinFare['cabinNumber'] + u'张！'
                                if not (flightNoStatus) or flightNoStatus == '0':
                                    flightNoStatus = cabinFare['cabinNumber']
                                    sendemail(str)
                            careinfo['flightNoCheck'][flightInfo['flightNo']] = flightNoStatus
                            print(str + time.strftime('%H:%M:%S', time.localtime(time.time())))
    except Exception as e:
        print(e)
