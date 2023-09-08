from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import FileResponse, JSONResponse
from models import models

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("public/index.html")


@app.get("/api/rows")
def get_table(db: Session = Depends(get_db)):
    return db.query(ResultTable).all()


@app.get("/api/rows/{id}")
def get_person(number: int, db: Session = Depends(get_db)):
    row = db.query(ResultTable).filter(number == ResultTable.id).first()
    if row is None:
        return JSONResponse(status_code=404, content={"message": "Запись не найдена"})
    return row


@app.post("/api/add_row")
def add_row(data: models.PostRow = Body(), db: Session = Depends(get_db)):
    row = ResultTable(
        taxonname=data.taxonname,
        composition=data.composition,
        change_in_abundance=data.change_in_abundance,
        frequency=data.frequency,
        additive_type=data.additive_type
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@app.put("/api/edit_row")
def edit_row(data: models.PutRow = Body(), db: Session = Depends(get_db)):
    row = db.query(ResultTable).filter(data.id == ResultTable.id).first()
    if row is None:
        return JSONResponse(status_code=404, content={"message": "Запись не найдена"})
    row.taxonname = data.taxonname,
    row.composition = data.composition,
    row.change_in_abundance = data.change_in_abundance,
    row.frequency = data.frequency,
    row.additive_type = data.additive_type
    db.commit()
    db.refresh(row)
    return row


@app.delete("/api/delete_row/{id}")
def delete_person(number: int, db: Session = Depends(get_db)):
    row = db.query(ResultTable).filter(number == ResultTable.id).first()
    if row is None:
        return JSONResponse(status_code=404, content={"message": "Запись не найдена"})
    db.delete(row)
    db.commit()
    return row
