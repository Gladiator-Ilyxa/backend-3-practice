from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from schemas import MasterOut
from task1 import Master 

app = FastAPI(title="Salon Masters API")

@app.get("/masters", response_model=list[MasterOut])
def get_masters(
    specialization: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Master)
    if specialization is not None:
        query = query.filter(Master.specialization == specialization)
    return query.all()

@app.get("/masters/{master_id}", response_model=MasterOut)
def get_master(master_id: int, db: Session = Depends(get_db)):
    """
    Получить одного мастера по id.
    Если мастер не найден — вернуть 404 Not Found.
    """
    master = db.query(Master).filter(Master.id == master_id).first()
    if master is None:
        raise HTTPException(status_code=404, detail="Master not found")
    return master