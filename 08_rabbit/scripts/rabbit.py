import asyncio
import logging
import aio_pika

from config import settings


async def connect() -> None:
    connection = await aio_pika.connect_robust(
        settings.async_rm_url,
    )
    return connection


async def publish_rabbit(message: str, route_key: str) -> None:
    conn = await connect()

    async with conn:

        ch = await conn.channel()

        await ch.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=route_key,
        )
