import requests

# API URL 및 요청 데이터 설정
url = "https://tools.kinds.or.kr/search/news"
headers = {"Content-Type": "application/json"}



payload = {
    "access_key": api_key,  # API 키를 여기에 입력
    "argument": {
        "query": "인공지능 OR AI",
        "published_at": {
            "from": "2024-01-01",
            "until": "2024-09-30"
        },
        "provider": ["01100101"], ####### 코드 값은 하단 코드 테이블 참조
        "category": ["정치>정치일반", "IT_과학"],
        "category_incident": ["범죄", "교통사고", "재해>자연재해"],
        "byline": "", #### 기자 이름 (언론사에서 기자 이름을 제공한 News인 경우에만 검색이 가능합니다.)
        "provider_subject": ["경제", "부동산"],
        "subject_info": [""],
        "subject_info1": [""],
        "subject_info2": [""],
        "subject_info3": [""],
        "subject_info4": [""],
        "sort": {"date": "desc"}, # date,desc : 날짜 최신순 / title, asc : 제목 오름차순 정력 
        "hilight": 200,
        "return_from": 0,
        "return_size": 5,
        "fields": ["byline", "category", "category_incident", "provider_news_id"]
    }
}
# POST 요청 보내기
response = requests.post(url, headers=headers, json=payload)

# 응답 확인 및 제목만 출력
if response.status_code == 200:
    data = response.json()
    
    # 제목 필드를 반복문으로 출력
    for article in data.get("return_object", {}).get("documents", []):
        print(article.get("title", "제목 없음"))
else:
    print(f"요청 실패: {response.status_code}")