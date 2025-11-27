import asyncio 
from loguru import logger
from cli import cli

async def main():
    logger.add("cmd.log", rotation="500 MB")
    cli();

if __name__ == "__main__":
    asyncio.run(main())
