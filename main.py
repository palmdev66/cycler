import time
import subprocess

# Укажите путь к вашей рабочей папке
working_directory = "/путь/к/вашей/рабочей/папке"

command = ["yarn", "cli", "mint", "-i", "45ee725c2c5993b3e4d308842d87e973bf1951f5f7a804b21e4dd964ecd12d6b_0", "5"]

while True:
    subprocess.run(command, cwd=working_directory)
    time.sleep(30)
