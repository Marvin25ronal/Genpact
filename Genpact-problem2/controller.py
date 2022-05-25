import os
import sys
import logging
import threading
import time
from analysis import Analysis

# Runs every 5 seconds

class Controller:
    folderPath = ""
    NOT_APPLICABLE_FOLDER = "NotApplicable"
    PROCESSED_FOLDER = "Processed"
    OUTPUT_FOLDER = "Output"
    MASTER_WORKBOOK_FILE_NAME = "MasterWorkbook.xlsx"
    masterWorkbookPath = ""
    notApplicableFolderPath = ""
    processedFolderPath = ""
    watchdog = None
    observer = None

    def __init__(self, folderPath):
        self.folderPath = folderPath
        path = os.getcwd()
        self.notApplicableFolderPath = path + "\\" + self.NOT_APPLICABLE_FOLDER
        self.processedFolderPath = path + "\\" + self.PROCESSED_FOLDER
        self.masterWorkbookPath = path + "\\" +self.OUTPUT_FOLDER+"\\"+ self.MASTER_WORKBOOK_FILE_NAME

    def AnalizeFolder(self):
        if self.watchdog != None:
            self.watchdog.stop()
        self.watchdog = threading.Thread(
            target=self.WorkerTask, name="Watchdog", daemon=True
        )
        self.watchdog.start()

    def WorkerTask(self):
        analysis=Analysis(self.folderPath,
                          self.masterWorkbookPath,
                          self.notApplicableFolderPath,
                          self.processedFolderPath
                          )
        while True:
            analysis.AnalizeFolder()
            time.sleep(5)
