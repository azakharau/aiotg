import typing
from datetime import datetime
from decimal import Decimal

import asyncpgsa

import models


async def init_db(app):
    dsn = construct_db_url(app['config']['database'])
    pool = await asyncpgsa.create_pool(dsn=dsn)
    app['db_pool'] = pool
    return pool


def construct_db_url(config: dict) -> str:
    DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
    return DSN.format(
        user=config['DB_USER'],
        password=config['DB_PASS'],
        database=config['DB_NAME'],
        host=config['DB_HOST'],
        port=config['DB_PORT'],
    )


# ============== CATEGORIES CRUD OPERATIONS ==============================

async def create_category(conn,
                          name: str,
                          is_base: bool,
                          aliases: list) -> None:
    stmt = models.category.insert().values(name=name,
                                           is_base=is_base,
                                           aliases=aliases)
    await conn.execute(stmt)


async def get_category(conn,
                       name: str) -> typing.Optional[dict]:
    category = await conn.fetch(
        models.category.select().where(models.category.c.name == name)
    )
    return category


async def get_all_categories(conn) -> typing.Optional[list]:
    categories = await conn.fetch(
        models.category.select().order_by(models.category.c.name)
    )
    return categories


async def delete_category(conn,
                          name: str) -> None:
    await conn.execute(
        models.category.delete().where(models.category.c.name == name)
    )


# ================== EXPENSE CRUD OPERATIONS ============================

async def create_expense(conn,
                         category_name: str,
                         value: Decimal) -> None:
    stmt = models.expense.insert().values(
        category=get_category(conn, category_name),
        value=value
    )
    conn.execute(stmt)


async def get_today_expense(conn) -> list:
    expenses =  await conn.fetch(
        models.expense.select().where(
        models.expense.c.created == datetime.now())
    )
    return expenses