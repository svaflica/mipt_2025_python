import os
import json
import asyncio
import json
import aio_pika
import logging

from aio_pika import connect, IncomingMessage
from main import User, add_user_db, get_users_db
from rabbit import publish_rabbit
from config import settings
from database import AsyncSessionLocal


queue_name= "listening_queue"


async def add_user_rabbit(msg):
    logging.info('started adding user')
    async with AsyncSessionLocal() as db:
        user = await add_user_db(db, User(**msg))
    if not user:
        await publish_rabbit(json.dumps({"status": "error"}), 'result')
        return
    await publish_rabbit(json.dumps({"status": "success"}), 'result')
    logging.info('ended adding users')


async def get_users_rabbit(msg):
    logging.info('started getting users')
    async with AsyncSessionLocal() as db:
        users = await get_users_db(db)
    await publish_rabbit(json.dumps(users), 'result')
    logging.info('ended getting users')



handlers = {
    'add_user': add_user_rabbit,
    'get_users': get_users_rabbit
}


async def callback(message: IncomingMessage):
    try:
        data = message.body.decode("utf-8")
        if len(data) > 0:
            data = json.loads(data)

        msg_type = message.headers['app_message_type']
        await handlers[msg_type](data)
    except Exception as e:
        logging.error(f'Error while processing message: {e}')
        await publish_rabbit(message.body.decode("utf-8"), queue_name + '_error')


async def connect(loop) -> None:
    connection = await aio_pika.connect_robust(
        settings.async_rm_url,
        loop=loop,
    )
    return connection


async def main(loop):
    connection = await connect(loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue(queue_name)

    await queue.consume(callback, no_ack = True)
    logging.info("start consuming")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()