## 1. Django 프로젝트 세팅
- 가상환경 구축하는 방법 (with Poetry)
pyenv virtualenv를 통해 파이썬 버전을 고정 및 가상환경이름(프로젝트 이름)을 정하고
폴더에 들어오면 자동으로 가상환경 상태로 진입하게 된다.
poetry init으로 프로젝트에 대한 기본 정보를 pyproject에 넣어주고 시작
poetry add ... 사용되는 라이브러리 의존성 쉽게 말하면
우리 프로젝트에 이거 사용했어요 버전은 이거에요 적어서 관리하고 어느버전 구간을 사용합니다
대략 이런 내용을 기록하고 추가 인원에 대한 편의성을 제공하는 역할이라 보면 좋겠다
poetry install을 하면 적혀있는 내용으로 동일한 환경이 구성된다

개인적 의견으론 pyenv + poetry 보단 그냥 uv쓰는게 편한 느낌을 받는다.
이유는 pyenv + poetry는 처음에 다 잡고 시작한다면 uv는 내가 필요할 때 바꾼다.
그리고 짧다 poetry 보단 uv를 쓰는게 빠르고
pyenv를 사용하는 환경을 만드는 것보단 uv init uv venv하는게 편하게 느껴진다.
다만 터미널로 경로에 접근하면 자동으로 가상환경에 진입한다는 것은 좋게 보고는 있다.

- Django 설치 및 프로젝트 구성, 앱 세팅하는 방법
poetry add django - 장고 설치
django-admin startproject config . or python -m django startproject config .
장고를 하는 이상 하나의 기능으로 끝날 경우는 별로 없다 그래서 프로젝트 이름보단
설정 파일만 두는 것이 이상적이라 위와 같은 명령어를 사용하게 된다.

python manage.py startapp appname 서비스나 기능 만들기
구성할 때 신경쓰면 좋은 것은 온전하게 작동하는 덩어리 하나를 만드는 것이라 보는데
다른 app에 의존하지 않고 작동할 수 있는 정도라고 이야기 하는데 어느정도 경험이나
동료들과의 의사소통이 필요하다 느낌
앱을 만든 뒤에는 settings에 installed apps에 추가하도록 하자

- templates 경로 지정하기
처음에 config . 으로 프로젝트를 만들었으니 해당 config안에는 설정파일이 있게된다.
settings 내에 TEMPLATES를 보게되면 DIRS가 비어있다

우선 BASE_DIR 설정은 settings기준으로 프로젝트 폴더를 의미한다.
BASE_DIR를 사용해 TEMPLATES의 DIRS를 templates 경로를 입력하면 된다.

- static 경로 지정하기
STATIC_URL 웹에서 접근하기 위한 주소
STATIC_DIR 내가 파일을 넣어두는 임의의 폴더 - 선언하지 않고 바로 STATICFILES_DIRS에 작성 가능
STATICFILES_DIRS 개발용 파일 모아두는 폴더의 모음
STATIC_ROOT 배포할 때 파일을 모아두는 폴더 python manage.py collectstatic을 하면 모이게 되는 폴더

- media 경로 지정하기
배포환경에서는 클라우드 저장소로 설정하겠지만
개발 단계에서 테스트를 위해 필요하기에 로컬로 설정
실제론 미디어를 서빙해주는 기능이 없지만 스태틱을 이용해 환경을 만든다
그를 위해 urls에 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
추가하고 settings에서도 각 경로를 잡아줘야한다.
static에는 if not settings.DEBUG: return [] 이 있어서 배포환경에서 작동이 안되게 설정돼 있음

## 2. Database Model
- 데이터베이스 모델 정의하기
class Model(models.Model): 모델에는 단수를 사용하여 작성한다.
내부에 def __str__(self): 가 정의돼 있다면 항목을 어떻게 표시할지 정할 수 있다.
내부에 class Meta:가 정의돼 있다면 어떻게 표시할지 정할 수 있다.

- 각 필드별 특징 정리하기
name = models.Field(options)로 정하며 Field앞에 Char, Text Datetime등으로 타입을 표시
null - db에서 비어있을 수 있는지를 표시
blank - 클라이언트가 서버로 요청할 때 비어있을 수 있는지를 표시

- Migration에 대해서 정리하기
디비의 상태를 개발자끼리 공유하기 위한 기능
python manage.py makemigrations - 현재 models에 작성된 상태를 migrations폴더 내에 저장한다.
python manage.py migrate - migrations에 저장된 상태를 내 디비에 적용한다.

협업을 한다면 github에서 pull받은 다음에 migrate 한다면 프로젝트의 디비환경을 동일하게 만들 수 있다.

## 3. Jinja

- Jinja 문법 정리하기
html을 동적으로 랜더링하는 문법으로 for를 이용해 반복 등 기능을 하기위해 사용한다
{% %} 기능을 위해 사용 {{ }} 호출을 위해 사용


- block 사용법
공통으로 사용될 html문서에 {% block ... %}{% endblock %}를 작성해두고
현재 html문서에서 동일한 block 내에 내용을 작성하면 공통 문서의 내용을 불러와 작성한 것처럼 작성할 수 있다.

- extends 사용법
block을 사용하기 위해 extends 또한 사용해야한느데 공통문서를 불러오는 기능을 수행한다
{% extends "base.html" %} 처럼 불러올 html 문서를 작성해주면 된다.

## 4. FBV(Function Base View)

- FBV란?
뷰에 작성하는 방식 중 하나로 동작을 하나하나 직접 작성해야하는 것이 특징으로 보인다
클래스 방식으로 할 경우 상속을 받으나 펑션은 상속을 받지 않기에 기능을 직접 작성하게 된다

- 간단한 View 메소드 작성법
    - render
    랜더는 어떤 html문서에서 요청을 받아 작동할 지 작성하게 된다
    - redirect
    작업 이 끝난 후 보내질 경로를 작성하며 urls에서 작성된 name이나 url주소를 통해 경로를 설정할 수 있다.

## 5. Urls

- URL 엔드포인트란?
요청이 도달하는 위치의 url https:// .../list
- urlspatterns
엔드포인트를 모아두는 리스트
- URL Include 개념 및 방법
분류해둔 urlspatterns를 가져오는 방법으로
path('기본경로', include('app.urls')) 앱이름 혹은 패키지이름 혹은 경로이름과 urls로 작성하여 가져온다
- path
path(엔드포인트, 기능, 이름)으로 작성하고
기능은 함수 혹은 클래스를 가져와 사용한다.
이름은 해당 부분을 쉽게 호출하여 쓰기 위해 사용하게 된다.
- include
위 개념부분의 설명과 동일