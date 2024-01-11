import asyncio
import time
from PyQt5.QtCore import QByteArray, QUrl, QFile
import PyQt5.QtNetwork
import sys, json

async def say_later(delay, info):
    await asyncio.sleep(delay)
    print(info)

async def main():
    #await say_later(1,"ok")
    #await asyncio.sleep(2)
    #await say_later(2,"kkkkk")
    task1 = asyncio.create_task(say_later(3,"ppppp"))
    task2 = asyncio.create_task(say_later(1,"ooooo"))
    print(asyncio.get_running_loop())

    await asyncio.gather(say_later(3,"11111"), say_later(2,"22222"), say_later(1,"3333"))

    #await task1
    #await task2


asyncio.run(main())