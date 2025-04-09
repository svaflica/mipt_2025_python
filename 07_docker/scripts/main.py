from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import models

from database import get_db
 
app = FastAPI()


class User(BaseModel):
    email: str
    password: str


async def add_user_db(
    db: AsyncSession,
    user: User,
):
    db_item = models.User(
        email = user.email,
        password = user.password,
    )
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


@app.post('/add_user')
async def add_user(
    form_data: User,
    db: AsyncSession = Depends(get_db),
):
    user = await add_user_db(db, form_data)
    if not user:
        return {"status": "error"}
    return {"status": "success"}


async def get_users_db(
    db: AsyncSession,
):
    result = await db.execute(select(models.User))
    items = result.scalars().all()
    return items


@app.get('/get_users')
async def get_users(
    db: AsyncSession = Depends(get_db),
):
    users = await get_users_db(db)
    return users



