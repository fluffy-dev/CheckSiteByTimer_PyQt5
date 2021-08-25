#Copyright © 2021 Rauan Asetov. All rights reserved.
#License: http://opensource.org/licenses/MIT
from loguru import logger

 
class Logging(object):
    def __init__(self, status, url, datetime):
        logger.add("ResponseLogs.log", format='{name} {message}', level='INFO', rotation="10 MB")
        logger.info(f"url:{url}, status:{status}, datetime:{datetime}")
