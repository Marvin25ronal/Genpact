from os import listdir
from os.path import isfile, join
import shutil
from win32com.client import Dispatch
import re
import wx


class Analysis:
    folderPath = ""
    masterWorkbookPath = ""
    notApplicableFolderPath=""
    processedFolderPath=""

    def __init__(self, folderPath, masterWorkbookPath,notApplicableFolderPath,processedFolderPath):
        self.folderPath = folderPath
        self.masterWorkbookPath = masterWorkbookPath
        self.notApplicableFolderPath=notApplicableFolderPath
        self.processedFolderPath=processedFolderPath

    def AnalizeFolder(self):
        files = self.__getFiles()
        files = self.__filter(files)
        notprocessed=self.__getFiles()
        notprocessed=self.__notProcessed(notprocessed)
        print(files)
        for file in files:
            self.__analysisFile(file)

        self.__splitFiles(files,notprocessed)

    def __getFiles(self):
        return [f for f in listdir(self.folderPath) if isfile(join(self.folderPath, f))]

    def __filter(self, files):
        return [f for f in files if re.match(r"[a-zA-Z0-9_-]+.*\.xlsx", f)]

    def __notProcessed(self,files):
         return [f for f in files if not re.match(r"[a-zA-Z0-9_-]+.*\.xlsx", f)]
     
    def __analysisFile(self, filename):
        path = self.folderPath + "\\" + filename
        xl = Dispatch("Excel.Application")
        xl.Visible = False
        wb1=None
        wb2=None
        try:
            wb1 = xl.Workbooks.Open(Filename=path)
            wb2 = xl.Workbooks.Open(Filename=self.masterWorkbookPath)
            sheetnames=[sheet.Name for sheet in wb2.Worksheets]
            for sheet in wb1.Worksheets:
                if sheet.Name not in sheetnames:
                    sheet.Copy(Before=wb2.Worksheets(1))
        except Exception as e:
            print(e)
        finally:
            wb1.Close(SaveChanges=False)
            wb2.Close(SaveChanges=True)
            xl.Quit()
    
    def __splitFiles(self,processed,notprocessed):
        for file in processed:
            actualPath=self.folderPath+"\\"+file
            destPath=self.processedFolderPath+"\\"+file
            shutil.move(actualPath,destPath)

        for file in notprocessed:
            actualPath=self.folderPath+"\\"+file
            destPath=self.notApplicableFolderPath+"\\"+file
            shutil.move(actualPath,destPath)
        
        
        

        
        
