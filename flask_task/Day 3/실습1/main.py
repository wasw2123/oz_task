from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# db connection
engine = create_engine("sqlite:///users.db", echo=True)

# db 연결통로 -> 세션
SessionLocal = sessionmaker(bind=engine)

# base calss 정의
Base = declarative_base()

# user model def
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self): #출력 알아보기 쉽게 커스텀
        return f'<<<<<User(id={self.id}, name={self.name})>>>>>'

# table generate
Base.metadata.create_all(bind=engine)


# -----------
# 연습

def run_single():
    db = SessionLocal() # db 연결 통로
    # C
    new_user = User(name="OZ_BE")
    db.add(new_user)
    db.commit()
    print("add user:", new_user)

    # R
    user = db.query(User).first()
    print("finded one user", user)

    # U
    if user:
        user.name = "OZ_BE_Updated"
        db.commit()
    print("updated one user", user)

    # D
    if user:
        db.delete(user)
        db.commit()
    print("deleted one user", user)

    db.close()

def run_bulk():
    db = SessionLocal()
    
    # C
    new_users = [User(name="OZ_BE_17"), User(name="BE_18"), User(name="BE_19")]
    # for u in new_users:
    #     db.add(u)
    db.add_all(new_users)
    db.commit()

    print("Created new users", new_users)

    # R
    #조건
    user = db.query(User).filter(User.id == 1).first()
    print("조건 조회:", user)

    # R 2
    #패턴
    patterns = db.query(User).filter(User.name.like("%BE_%")).all() # % 있는 방향에 무작위 글자 포함
    print("패턴 검색:", patterns)


    # U
    if patterns:
        for p in patterns:
            p.name = p.name + "updated"
        db.commit()
        print("복수 사용자 수정", patterns)


    # D

    db.query(User).delete()
    db.commit()
    print("모두 삭제")
    
    
    db.close()


if __name__ == "__main__":
    # run_single()
    run_bulk()