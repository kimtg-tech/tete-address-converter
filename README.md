# 주소 변환 시스템 (Address Converter)
주소 변환 시스템은 사용자가 입력한 주소 데이터를 새로운 주소 체계로 변환해주는 웹 애플리케이션입니다. 이 프로젝트는 Django를 기반으로 개발되었으며, 사용자 친화적인 UI와 API를 활용한 정확한 주소 변환 기능을 제공합니다.
## 주요 기능
- **주소 변환**:
    - 사용자가 입력한 구주소/지번주소를 새주소(도로명주소)로 변환.
    - 다중 주소 입력 지원 (한 줄에 한 개의 주소 입력).

- **결과 표시**:
    - 새 주소와 상태를 표 형식으로 표시.
    - 성공/실패 상태를 컬러로 강조하여 가독성 강화.

- **에러 처리**:
    - 입력값이 없는 경우 에러 메시지를 표시 (자동 사라짐 기능 포함).
    - API 호출 실패, 검색 결과 없음 등의 문제를 사용자에게 명확히 전달.

## 설치 및 실행 방법
1. **레포지토리 클론**:
``` bash
   git clone <REPO_URL>
   cd address_converter
```
1. **필요한 환경 설정**:
    - 파일을 생성하고 필요한 설정값 입력. 예: `.env`
``` 
     JUSO_API_KEY=<발급받은_주소_API_키>
```
1. **라이브러리 설치**:
    - Python 의존성 설치:
``` bash
     pip install -r requirements.txt
```
- Node.js 패키지 설치 (스타일 빌드 필요 시):
``` bash
     npm install
```
1. **로컬 서버 실행**:
``` bash
   python manage.py runserver
```
1. **서비스 접속**:
    - 아래 URL로 접속:
``` 
     http://127.0.0.1:8000/
```
## 파일 구조
``` 
address_converter/
├── templates/
│   ├── address_converter/
│       ├── index.html    # 메인 입력 화면
│       ├── result.html   # 변환 결과 화면
├── views.py              # 뷰 로직 (주소 변환 및 에러 처리)
├── api_client.py         # 주소 API 호출 로직
├── urls.py               # URL 라우팅
├── static/
│   ├── css/              # 스타일 파일
├── tests.py              # 애플리케이션 테스트
.env                       # 환경 변수 (.gitignore에 포함)
```
## 사용된 기술
- **백엔드**: Django
- **프론트엔드**: HTML, CSS (TailwindCSS)
- **API**: `주소 API`를 사용하여 주소를 동적으로 변환
- **데이터 시각화**: 결과를 테이블로 제공하고 UI를 컬러로 상태를 강조

## 주요 스크린샷
### 1. 주소 입력 화면

사용자가 입력한 주소 데이터를 한 줄씩 입력할 수 있습니다.
### 2. 변환 결과 화면

새 주소 변환 결과가 성공/실패 상태와 함께 표시됩니다.
## 추후 개발 예정 기능
- **주소 저장**: 변환 결과 데이터를 CSV 파일로 다운로드.
- **다국어 지원**: 한국어 외의 언어로 서비스 제공.
- **검색 개선**: 주소를 입력한 도중 실시간 검색 결과 제공.

## 기여 방법
기여를 희망하시면 다음 단계를 따라주세요:
1. 본 레포지토리를 포크합니다.
2. 새 브랜치를 생성합니다: `git checkout -b feature/YourFeature`
3. 코드를 커밋합니다: `git commit -m 'Add YourFeature'`
4. 푸시합니다: `git push origin feature/YourFeature`
5. 풀 리퀘스트를 생성합니다.

## 연락처
- 프로젝트 관리자: [kimtg-tech] ktgstar@gmail.com
- 문의사항 또는 버그 신고는 [ISSUES](GitHub%20Issues%20%EB%A7%81%ED%81%AC)를 통해 요청해주세요.

위 내용을 프로젝트와 맞게 수정한 뒤 로 저장하면 됩니다. 스크린샷 이미지 경로는 사용 전에 실제 이미지로 대체해주세요. 😊 `README.md`
