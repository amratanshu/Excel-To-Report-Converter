from __future__ import print_function
from gauth import getGSuite
from get import getDoc, getSheet, getSheetData, getDocContent, getCapacity
from ParsingDocument import getTablePositions
from ParsingSpreadsheet import createSheetDataStructure

DOCUMENT_ID = '17G3rUWvHHqfIiPwBB_BbkHr-lYC54hEUcH0GOY2mEwU'
SPREADSHEET_ID = '1h8X-5k5qiQi0uJhMLUEJ1g7k94kq4OMryuxXfBFeiD0'
WORK_SHEET_NAME = 'Form-Se2!A1:H226'

def main():
    gsheets, gdocs = getGSuite()

    worksheet = getSheet(gsheets, SPREADSHEET_ID, WORK_SHEET_NAME)
    document = getDoc(gdocs, DOCUMENT_ID)

    values = getSheetData(worksheet)
    spreadsheetDataStructure, n = createSheetDataStructure(values)

    print(getCapacity(spreadsheetDataStructure))




if __name__ == '__main__':
    main()