import requests as re

def request(url):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    # 'cookie': '__cf_bm=QeAkyOd3EJgqFCnJlPy01UulC1ClQo2MkeVV9HHtR68-1776764635.321762-1.0.1.1-MMD0mSmmxqkbFzYZuErhg51HqdIGDXY6hdho2ZT3gt64pSOq801X90sXv75iwuToUOt0pWmXS5SKeMVmZZ9EcDzt3FErEN.kwiHMK_4.e84yE276_J9xjK8Uy3Pt7QtY; _gcl_au=1.1.848021645.1776764639; _fbp=fb.1.1776764639628.20373931869363233; _uetsid=9f79ef503d6611f1bac3872f7d02ad4a; _uetvid=9f7a3ba03d6611f1b2e3a96d4f60b8af; _ga_9PSV9LG5D2=GS2.1.s1776764640$o1$g0$t1776764640$j60$l0$h0; _ga=GA1.1.1502052076.1776764640; _twpid=tw.1776764640263.413158577456322015',
}



    response = re.get(url,headers = headers)
    # print(response.status_code)
    if response.status_code == 200:
        return response.text
    else:
        print("error")
