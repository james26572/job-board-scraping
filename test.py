import requests
from bs4 import BeautifulSoup




def get_page_content(url):
    import sys
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    
    if sys.version_info[0]==3:
        import urllib.request
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(
                {'http': 'http://brd-customer-hl_a4d34049-zone-unblocker:4rc3q2njeh4a@brd.superproxy.io:22225',
                'https': 'http://brd-customer-hl_a4d34049-zone-unblocker:4rc3q2njeh4a@brd.superproxy.io:22225'}))
        return str(opener.open(url).read())





def get_job_description(description_url):
    
    response = get_page_content(description_url)
    soup = BeautifulSoup(response,'html.parser')
    description = soup.find('div',class_ ='show-more-less-html__markup')
    
    cleaned_description = description.text.strip()
    
    return cleaned_description



with open('test.txt','a+',encoding='utf-8') as f:
   f.write(str(get_job_description('https://www.linkedin.com/jobs/view/3861957968')))
    #f.write(get_page_content('https://www.linkedin.com/jobs/view/3859652165'))






