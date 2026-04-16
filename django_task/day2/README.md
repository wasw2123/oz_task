## 1. ImageField

- ImageField 특징과 사용법: 텍스트필드이나 이미지 경로를 저장
- Pillow:
    - 어떤 라이브러리? 장고에서 이미지 처리를 하기위한 라이브러리
- django-cleanup
    - 어떤 라이브러리? 파일이 변경되거나 삭제될 때 서버내에 있는 파일도 삭제해주는 라이브러리
- MEDIA_ROOT 파일이 저장되는 위치
- MEDIA_URL 브라우저가 접근하는 위치 둘다 스태틱을 이용해 개발환경에서 사용

## 2. Django-summernote

- django-summernote 란?
    - 어떤 라이브러리? 문서 작성을 도와주는 에디터
    - 특징 admin에서도 사용 가능, 에디터 기능 구성 가능
- django-summernote 세팅 settings에 apps에 추가하고 및에 설정(툴바, 언어 등) 작성
- django-summernote 사용법 적용 후 마이그레이션 후 어드민에서 적용 필드 작성 후 적용된 에디터 사용

## 3. Django-extensions

- django-extensions 란?
    - 어떤 라이브러리? shell에 편의성을 더해주는 라이브러리, 자동 import
    - Python shell 장고 인터프리터, 코드 입력시 즉시 실행해주는 대화형 환경
    - 특징 필요할 때마다 import해줘야하던 불편함 개선
- django-extensions 사용법 settings에 추가 후 터미널에서 python manage.py shell_plus후 사용

## 4. OAuth2

- OAuth2 정리하기
- Naver Social Login
    - 아래 사진을 바탕으로 네이버 로그인 절차 분석하기
    클라이언트에서 로그인 링크 -> 네이버 로그인, 콜백 state, code 수신 -> 토큰요청(code, state담아서) -> 토큰 수신 -> 프로필 요청(토큰 담아서)
    -> 프로필 수신 이후 데이터 가공

    - 네이버 로그인 환경변수 설정하기: 클라이언트, 시크릿 키 저장 필요
    - 네이버 로그인 기능 개발하기