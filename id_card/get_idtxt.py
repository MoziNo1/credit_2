import requests
import re
url1 = "https://doc.docsou.com/bab4341e9cc22d74cebe9ecac.html"

cookie = "ASP.NET_SessionId=pcfzgcutdsarfv2ew0pgaqry; __SessionId=FromSE1=1; Hm_lvt_dd495ba6a42fafa58a948a8f55b0a2d6=1629771349; Hm_lpvt_dd495ba6a42fafa58a948a8f55b0a2d6=1629771362; BAIDU_SSP_lcr=https://www.baidu.com/link?url=WiGLej8MMAoN7YGR4s-rfRQNNAjvWqJKOX7Q5kuT2pSQBxjRlw320Ycvrq-TiV-CMqx6Mg7KIL6JIkhikKQS4K&wd=&eqid=e8989f7800146aa60000000361245640; __gads=ID=3f40164f0af7224b-223ed8a51acb001b:T=1629771356:RT=1629771356:S=ALNI_MZAfoVclGvgMoHx9Oj0DYPhk-9zhA; UM_distinctid=17b75f1c3282ce-0a759d7c21e8368-4c3e247b-144000-17b75f1c3297e8; CNZZDATA1254514968=7274965-1629766078-https%253A%252F%252Fdoc.docsou.com%252F%7C1629766078"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
           "Sec-Fetch-Dest": "document",
           "Sec-Fetch-Mode": "navigate",
           "Sec-Fetch-Site": "same-origin",
           "Sec-Fetch-User": "?1",
           "Upgrade-Insecure-Requests": "1",
           "Cookie": "ASP.NET_SessionId=pcfzgcutdsarfv2ew0pgaqry; __SessionId=FromSE1=1; Hm_lvt_dd495ba6a42fafa58a948a8f55b0a2d6=1629771349; Hm_lpvt_dd495ba6a42fafa58a948a8f55b0a2d6=1629771362; BAIDU_SSP_lcr=https://www.baidu.com/link?url=WiGLej8MMAoN7YGR4s-rfRQNNAjvWqJKOX7Q5kuT2pSQBxjRlw320Ycvrq-TiV-CMqx6Mg7KIL6JIkhikKQS4K&wd=&eqid=e8989f7800146aa60000000361245640; __gads=ID=3f40164f0af7224b-223ed8a51acb001b:T=1629771356:RT=1629771356:S=ALNI_MZAfoVclGvgMoHx9Oj0DYPhk-9zhA; UM_distinctid=17b75f1c3282ce-0a759d7c21e8368-4c3e247b-144000-17b75f1c3297e8; CNZZDATA1254514968=7274965-1629766078-https%253A%252F%252Fdoc.docsou.com%252F%7C1629766078"
           }
for i in range(1, 26):
    url = f"https://doc.docsou.com/bab4341e9cc22d74cebe9ecac-{i}.html"
    s = requests.request("get", headers=headers, url=url)
    # print(s.text)
    res = re.findall("<br />(.+?)\s<br />", s.text)
    print(res)
    with open("D:\credit\id_card\id_card.txt", encoding="utf-8", mode='a') as f:
        for i in res:
            f.write(i + "\n")
        f.close()

