from sqlalchemy import Column, Integer, String
from database import Base, engine, SessionLocal

class Master(Base):
    __tablename__ = "masters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Таблица 'masters' создана (или уже существует).")

    db = SessionLocal()
    try:
        if db.query(Master).count() == 0:
            db.add_all([
                Master(name="Анна", specialization="Парикмахер"),
                Master(name="Мария", specialization="Визажист"),
            ])
            db.commit()
            print("Начальные мастера добавлены в БД.")
        else:
            print("ℹТаблица masters уже содержит данные — пропуск.")
    finally:
        db.close()