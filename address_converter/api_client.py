import requests
import os
from dotenv import load_dotenv

load_dotenv() # .env 파일 로드

def get_address_info(address_keyword):
    """
    주어진 키워드로 주소를 검색하고, 구조화된 결과(dict)를 반환합니다.
    """
    api_key = os.getenv("JUSO_API_KEY")
    api_url = "https://www.juso.go.kr/addrlink/addrLinkApi.do"
    params = {
        "confmKey": api_key,
        "currentPage": 1,
        "countPerPage": 10, # 여러 개가 검색될 경우를 대비해 10개로 설정
        "keyword": address_keyword,
        "resultType": "json"
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()['results']

        if data['common']['errorCode'] != '0':
            return {'status': 'fail', 'reason': data['common']['errorMessage']}

        if not data.get('juso'):
            return {'status': 'fail', 'reason': '검색 결과 없음'}

        if len(data['juso']) > 1:
            return {'status': 'fail', 'reason': '여러 주소 검색됨'}

        return {'status': 'success', 'address': data['juso'][0]['roadAddr']}

    except Exception as e:
       return {'status': 'fail', 'reason': f'API 요청 오류: {str(e)}'}