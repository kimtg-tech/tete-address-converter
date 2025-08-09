# 1. Python + Node 환경 기반
FROM python:3.10-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 시스템 의존성 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Node.js 설치 (LTS 버전)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# 5. 프로젝트 파일 복사
COPY . /app

# 6. Python 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 7. Node 패키지 설치 (Tailwind 등)
RUN npm install

# 8. Tailwind CSS 빌드 (watch 모드 대신 build 명령어 사용)
RUN npm run tailwind:build

# 9. 포트 노출
EXPOSE 8001

# 10. Gunicorn으로 Django 서버 실행
CMD ["gunicorn", "setting.wsgi:application", "--bind", "0.0.0.0:8001"]
