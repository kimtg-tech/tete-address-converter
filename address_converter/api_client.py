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

        # --- 이 아래 부분이 수정된 로직입니다 ---
        if not data.get('juso'):
            return {'status': 'fail', 'reason': '검색 결과 없음'}

        juso_list = data['juso']

        # 1. 한 개의 결과만 정확히 나온 경우 (가장 좋은 케이스)
        if len(juso_list) == 1:
            return {'status': 'success', 'address': juso_list[0]['roadAddr']}

        # 2. 여러 개의 결과가 나온 경우, 입력값과 정확히 일치하는 주소가 있는지 확인
        # (이미 새주소인 경우 이 로직을 통해 "성공"으로 처리 가능)
        cleaned_input_addr = address_keyword.strip()
        for juso in juso_list:
            if juso['roadAddr'].strip() == cleaned_input_addr:
                return {'status': 'success', 'address': juso['roadAddr']}  # 정확히 일치하는 주소 반환

        # 3. 정확히 일치하는 주소가 없는, 진짜 애매한 여러 개의 결과인 경우
        return {'status': 'fail', 'reason': f'여러 주소 검색됨 ({len(juso_list)}개)'}
        # --- 여기까지가 수정된 로직입니다 ---

    except Exception as e:
        return {'status': 'fail', 'reason': f'API 요청 오류: {str(e)}'}