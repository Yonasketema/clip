import asyncio
from pathlib import Path

from config.conf import BASE_DIR
from tiktokUploader.main_chrome import tiktok_setup

if __name__ == '__main__':
    account_file = Path(BASE_DIR / "tiktokUploader" / "account.json")
    cookie_setup = asyncio.run(tiktok_setup(str(account_file), handle=True))
