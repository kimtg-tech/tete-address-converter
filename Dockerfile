FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치 준비
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 프로젝트 전체 복사 (이미 빌드된 CSS 포함)
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 정적파일 수집
RUN python manage.py collectstatic --noinput

EXPOSE 8001

CMD ["gunicorn", "setting.wsgi:application", "--bind", "0.0.0.0:8001"]
