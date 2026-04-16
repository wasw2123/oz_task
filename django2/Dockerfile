FROM python:3.13-slim

# mysqlclient 빌드에 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# uv 설치
RUN pip install uv

# 의존성 파일 복사 및 설치
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# mysqlclient는 도커 내에서만 설치
RUN uv pip install mysqlclient

COPY . .

EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
