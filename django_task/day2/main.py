# 샘플 Python 스크립트입니다.
from django.utils import timezone
from datetime import datetime, timedelta

from todo.models import Todo


# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.

def make_db_data(how_many):
    data = [Todo(
        title=f'todo{i}번',
        description=f'{i}번 todo의 설명',
        start_date=timezone.now(),
        end_date=timezone.now() + timedelta(days=7)
    ) for i in range(how_many)]

    Todo.objects.bulk_create(data)



def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 ⌘F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print_hi('PyCharm')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
