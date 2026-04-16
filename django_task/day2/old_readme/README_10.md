## 1. Django Form

- Form 생성하는 법
app 패키지내에 forms.py로 관리하며 html문서에서 화면을 생성화는 역활
class 기능+Form을 사용하며 기본적으로 forms.ModelForm을 상속받아 생성한다
이후 Meta에 내용을 작성하는 편
- widgets
입력 형태를 변경하기 위해서 사용하고 파라미터로는 대체로 attrs만 사용되는 편이다.
attrs는 태그뒤에 속성을 추가하는 파라미터로 딕셔너리 형태로 받는다
- CreationForm
회원가입 기능이 내장된 클래스, 커스텀을 위해 상속받은 후 오버라이드하여 사용.
- AuthentiactionForm
로그인의 기본 기능이 들어있는 클래스,  커스텀을 위해 상속받은 후 오버라이드하여 사용.
- is_valid()
검증을 통과했는지 불리언타입으로 반환하는 폼 클래스의 메서드

## 2. Django ORM

- ORM 이란?
db를 파이썬의 언어로 접근하고 데이터를 핸들링하기 위한 기능
- Django ORM 의 특징
mysql, postgresql, sqlite에 특화, 필요할 떄만 사용되는 쿼리 layz,
- Django ORM 의 기본적인 사용방법
    - objects: 디비 접근하는 매니저, 쿼리 인터페이스
    - filter: 조건 검색, 여러개, 리스트형식
    - get: 조건 검색, 한개
    - order_by: 정렬
    - create: 데이터 생성
    - delete: 삭제
    - update: 수정
    - get_object_or_404: 1개의 데이터를 가져오거나 없으면 404를 반환

## 3. Django Auth

- Django UserModel
    - accounts: 기본으로 장고에 내장된 유저 관리 라이브러리
    - Custom UserModel:
        - AbstractUser: 기본 기능에 필드만 추가하여 사용할 때
        - AbstractBaseUser: 로그인을 username에서 email로 바꾸는 등의 커스텀이 필요할 때 사용
        - PermissionMixin: 권한에 대한 커스텀을 위해 사용
        - BaseUserManager: 유저를 생성에 관한 로직을 커스텀할 때 사용
        - UserManager: 기본 유저 생성 매니저, AbstractUser사용 중 생성 로직을 바꿀 때 사용한다고 함
- Authenticate(): 아이디와 비밀번호가 일치하는지 불리언으로 반환하는 함수
- Login() 위 함수가 참일 때 세션에 유저 정보를 저장
- Logout() 세션에서 유저 정보 삭제
- login_required 데코레이터 함수: 로그인 한 상태에서만 동작하도록하는 데코레이터, 로그인 안했다면 로그인으로 리다이렉트를 보냄

## 4. CBV(Class Base View)

- CBV 란?
클래스 기반으로 뷰를 작성하는 방식
- View: 최상위 뷰 클래스 def get, post로 요청을 처리
- Generic Views
    - CreateView: 데이터 생성 클래스에 상속, model, (폼 or fields)으로 기본 구성, success_url로 생성 후 이동 경로 설정
    get - 빈 폼, post - 검증, 생성, 이동
    - UpdateView: 데이터 수정 클래스에 상속, 기본적으로 CreateView와 동일
    get - 채워진 폼, post - 상동
    - ListView: 목록 클래스에 상속, 모델, 페이지네이터를 쉽게 사용할 수 있음
    - DetailView: 상세 페이지 url의 id, pk로 객체를 조회함
    - DeleteView: 데이터 제거 get - 삭제 확인페이지 post - 삭제
    - TemplateView: 고유 로직 없이 페이지 렌더링
    - FormView: 데이터 저장 없이 폼 처리 로직이 필요할 경우에 사용
- request
    - user 가져오기 request.user
    - data 가져오기 request.POST or GET.get('data')
    - URL 파라미터 (Path Parameter) url내에 <int:pk>영역에 해당되는 값 pk인자를 받아 사용
    - 쿼리 파라미터 (Query Parameter) ?이후 q=abc 일때 request.GET.get('q')를 하면 abc를 가져온다.
- response
    - HttpResponseRedirect: url로 이동 - reverse(urlsname, kwargs={'pk':pk})
    - HttpResponse: 텍스트나 content_type에 형식에 맞춰 작성, 상태 코드 같이 전달 가능
           return HttpResponse(<h1>제목</h1>, content_type='text/html', status=200)
    - status code 요청을 처리한 코드 status에 직접 담거나, 내장된 코드 전달
    - response data: return render(request, htmlpage, context)를 넘겨 렌더링하거나
    jsonResponse로 json데이터 넘기기

## 5. Django Mail

- django.core.mail.send_mail 이메일을 보내는 함수 send_mail(제목, 내용, 보내는사람, 받는사람)
- django.core.signing 암호화를 위해 사용하는 라이브러리 signing.dumps로 이메일까지 암호화한 뒤 ?쿼리파라미터로 전달
- django.core.signing.TimestampSigner 시간제한이 있는 암호화를 만들기 위해 사용, unsign(code, max_age)