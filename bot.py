import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


nonebot.init()

driver = nonebot.get_driver()
config = driver.config
driver.register_adapter(ONEBOT_V11Adapter)

# SETTINGS
config.command_start = {""}
config.command_sep = {"."}


nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()