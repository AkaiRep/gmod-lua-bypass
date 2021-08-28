import pymem
import re
import time
pm = pymem.Pymem('hl2.exe')
server = pymem.process.module_from_name(pm.process_handle,'server.dll')
luaallow = server.lpBaseOfDll + 0x954BE0
pm.write_uchar(luaallow, 1)
print("GMOD готов к загрузке LUA скрипта!")
time.sleep(3)
