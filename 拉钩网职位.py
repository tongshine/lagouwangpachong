import requests
from bs4 import BeautifulSoup

url = 'https://www.lagou.com/wn/jobs?labelWords=sug&fromSearch=true&suginput=%E6%95%B0%E6%8D%AE&kd=%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590'
headers={
 "Cookie": "sajssdk_2015_cross_new_user=1; _ga=GA1.2.1177219948.1662002460; _gid=GA1.2.1746084955.1662002460; user_trace_token=20220901112059-4604b4c2-9a7d-435e-a912-f8f80bedd204; LGUID=20220901112059-16bf8688-4f0d-448e-9efd-44cff099b24c; gate_login_token=e7fd0455f3fadfd2164aa46a573339b21a6133c2e3c04ad0a8ff14251e2782aa; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; RECOMMEND_TIP=true; __SAFETY_CLOSE_TIME__25221033=1; __lg_stoken__=4bb11cc42e1cd2120bf622f0e85e968e7a6ebf222583ad484fee9c0382773f346ab37d40368a2debf8871532ba89b9e73d29035788b7462966c814c79dcc0e78d378e7281dfc; index_location_city=%E5%B9%BF%E5%B7%9E; WEBTJ-ID=20220901121645-182f7440104197-056d117d065e0a-e726559-1049088-182f7440105125; JSESSIONID=ABAAAECABIEACCA51407E73DF330053142CC06DE5894946; sensorsdata2015session=%7B%7D; _putrc=5F8BCA81E6BB2D1E123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B73490; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1662002460,1662008517; X_HTTP_TOKEN=851c9b05fd8cf3777369002661a92d764661e008ac; TG-TRACK-CODE=index_search; LGSID=20220901135804-e8856437-09d3-48b4-9bec-6b8e8f015cb0; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1662011885; LGRID=20220901135912-a25ea956-8b36-4827-87c8-8b0050974eff; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2225221033%22%2C%22%24device_id%22%3A%22182f710f211111-0a108b051c8d3e-e726559-1049088-182f710f21376%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2280.0.3987.87%22%7D%2C%22first_id%22%3A%22182f710f211111-0a108b051c8d3e-e726559-1049088-182f710f21376%22%7D",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
alist=main_page.find("div", class_="list__YibNq").find_all("div",class_="position__21iOS")
for item in alist:
    name = item.find("a").text
    price = item.find("span", class_="money__3Lkgq").text
    print(name,price)
