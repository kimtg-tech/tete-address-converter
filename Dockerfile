# Base image
FROM python:3.10-slim

# 작업 디렉토리
WORKDIR /app

# 필수 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Node.js 설치 (18 LTS)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# 프로젝트 파일 복사
COPY . /app

# Python 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Node 패키지 설치 (Tailwind 포함)
RUN npm install tailwindcss postcss autoprefixer --save-dev

# Tailwind CSS 빌드
RUN npm run tailwind:build

# 포트 노출
EXPOSE 8001

# Gunicorn 실행
CMD ["gunicorn", "setting.wsgi:application", "--bind", "0.0.0.0:8001"]
