import asyncio
import nest_asyncio
from gpt_bot import run_bot

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(run_bot())