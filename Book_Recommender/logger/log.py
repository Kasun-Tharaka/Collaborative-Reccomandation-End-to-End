import os
import logging
from datetime import datetime


Log_dir = "LOGS"
Log_dir = os.path.join(os.getcwd(), Log_dir)

os.makedirs(Log_dir, exist_ok=True)

Current_Time_Stamp = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
File_name = f"log_{Current_Time_Stamp}.log"

Log_File_Path = os.path.join(Log_dir, File_name)

logging.basicConfig(filename=Log_File_Path,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.NOTSET)