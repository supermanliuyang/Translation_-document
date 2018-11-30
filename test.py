import requests
import sys
import re
import execjs
import urllib
import  os
f=open(r"C:\Users\Administrator\Desktop\test.txt","r+")

def trans_getmsg():
    global gtk
    global token
    headers1 = {
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6735.400 QQBrowser/10.2.2328.400",
        "Cookie": "REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=962384A48BDBD03046D871DE8F36A036:FG=1; PSTM=1540815195; BIDUPSID=740680986F6BB26AB06F5EA14F32EF46; BDUSS=BXTjBKZnlPZDBLN0pySlE4Qk1aa35GQ1pSZzlQM0Z3aWFLSzh3SE5KSnNQdzFjQVFBQUFBJCQAAAAAAAAAAAEAAAB7ITVu16jK9NK5ze0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGyy5VtssuVbeH; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; H_PS_PSSID=; delPer=0; PSINO=1; BDRCVFR[IjAuOfhgL9_]=mk3SLVN4HKm; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1543493287,1543497366,1543497373,1543499258; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1543499258; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"
    }
    html = requests.get('https://fanyi.baidu.com', headers=headers1)
    html.encoding = 'utf-8'

    # 获取 gtk
    matches = re.findall("window.gtk = '(.*?)';", html.text, re.S)
    for match in matches:
        gtk = match

    # print('gtk = ' + gtk)

    # 正则匹配 token
    matches = re.findall("token: '(.*?)'", html.text, re.S)
    for match in matches:
        token = match

    if token == "":
        print('Get token fail.')
        exit()

    # print('token = ' + token)
def trans_rult(str):
    headers1={
        "User - Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6735.400 QQBrowser/10.2.2328.400",
        "Cookie":"REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=962384A48BDBD03046D871DE8F36A036:FG=1; PSTM=1540815195; BIDUPSID=740680986F6BB26AB06F5EA14F32EF46; BDUSS=BXTjBKZnlPZDBLN0pySlE4Qk1aa35GQ1pSZzlQM0Z3aWFLSzh3SE5KSnNQdzFjQVFBQUFBJCQAAAAAAAAAAAEAAAB7ITVu16jK9NK5ze0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGyy5VtssuVbeH; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; H_PS_PSSID=; delPer=0; PSINO=1; BDRCVFR[IjAuOfhgL9_]=mk3SLVN4HKm; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1543493287,1543497366,1543497373,1543499258; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1543499258; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"
    }
    # 计算 sign
    signCode = 'function a(r,o){for(var t=0;t<o.length-2;t+=3){var a=o.charAt(t+2);a=a>="a"?a.charCodeAt(0)-87:Number(a),a="+"===o.charAt(t+1)?r>>>a:r<<a,r="+"===o.charAt(t)?r+a&4294967295:r^a}return r}var C=null;var hash=function(r,_gtk){var o=r.length;o>30&&(r=""+r.substr(0,10)+r.substr(Math.floor(o/2)-5,10)+r.substr(-10,10));var t=void 0,t=null!==C?C:(C=_gtk||"")||"";for(var e=t.split("."),h=Number(e[0])||0,i=Number(e[1])||0,d=[],f=0,g=0;g<r.length;g++){var m=r.charCodeAt(g);128>m?d[f++]=m:(2048>m?d[f++]=m>>6|192:(55296===(64512&m)&&g+1<r.length&&56320===(64512&r.charCodeAt(g+1))?(m=65536+((1023&m)<<10)+(1023&r.charCodeAt(++g)),d[f++]=m>>18|240,d[f++]=m>>12&63|128):d[f++]=m>>12|224,d[f++]=m>>6&63|128),d[f++]=63&m|128)}for(var S=h,u="+-a^+6",l="+-3^+b+-f",s=0;s<d.length;s++)S+=d[s],S=a(S,u);return S=a(S,l),S^=i,0>S&&(S=(2147483647&S)+2147483648),S%=1e6,S.toString()+"."+(S^h)}'

    source = str
    sign = execjs.compile(signCode).call('hash', source, gtk)
    # print('source = ' + source + ', sign = ' + sign)

    # 请求接口
    fromLanguage = 'zh'
    toLanguage = 'en'

    v2transapi = 'https://fanyi.baidu.com/v2transapi?from=%s&to=%s&query=%s' \
                 '&transtype=translang&simple_means_flag=3&sign=%s&token=%s' % (
                 fromLanguage, toLanguage, urllib.parse.quote(source), sign, token)

    # print(v2transapi)

    translate_result = requests.get(v2transapi, headers=headers1)
    matches1 = re.findall("\"dst\":\"(.*?)\"", translate_result.text, re.S)
    for match in matches1:
        # print(match.replace(' ','_'))
        return match.replace(' ','_')
    # print(translate_result.text)





if __name__ == "__main__":
    gtk = ""
    token = ""
    os.chdir(r"C:\Users\Administrator\Desktop")
    if not os.path.exists('pp.txt'):  # 看一下这个文件是否存在
        exit(-1)  # ，不存在就退出
    fp = open('pp.txt', 'w')  # 打开你要写得文件pp.txt
    trans_getmsg()
    while 1:
        str = ""
        line = f.readline()
        for ch in line:
            if u'\u4e00' <= ch <= u'\u9fff':
                str += ch
            else:
                if str != "":
                    print(str)
                    a=trans_rult(str)
                    print(a)
                    line=line.replace(str,a)

                str = ""
        if not line:
            break
        print(line)
        fp.write(line)
    f.close()
    fp.close()
