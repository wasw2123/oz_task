from datetime import datetime, timedelta

DELIVERY_DAYS = 2

def _is_holiday(day: datetime) -> bool:
    return day.weekday() > 5

def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1
    return current_date

def test_get_eta_2023_12_1() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)

def test_get_eta_2024_12_31() -> None:
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)

def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)

def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
"""
# 제품코드
def add(a: int, b: int) -> int:
    return a + b

# 테스트 코드
def test_add() -> None:
    # given: 재료 준비
    a, b = 1, 1

    # when: 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b) #type: int

    # then:
    assert result == 2

"""