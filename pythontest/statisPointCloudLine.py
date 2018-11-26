#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from proscan import scans
import aiomysql
import asyncio


async def create__pool(loop, **kw):
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', '127.0.0.1'),
        port=kw.get('port', 3306),
        user=kw.get('user', 'root'),
        password=kw.get('password', 'Yupont@1101'),
        db=kw['db'],
        autocommit=kw.get('autocommit', True),
        minsize=kw.get('minsize', 1),
        maxsize=kw.get('maxsize', 10),
        charset=kw.get('charset', 'utf8'),
        loop=loop
    )


async def save(args):
    valuea = "','".join(args)
    valueb = ',null'*(30-len(args))
    sql = "insert into statislines values('" + valuea + "'" + valueb + ')'
    # print(sql)
    async with __pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                await cur.execute(sql, ())
                affected = cur.rowcount
            except BaseException as e:
                raise
            return affected


loop = asyncio.get_event_loop()
async def test(loop):
    await create__pool(loop, db='statispclines')
    for i in scans('H:\cesiumData\cloud'):
        if len(i.split('\\')) == 7:
            await save(i.split('\\'))


loop.run_until_complete(test(loop))
