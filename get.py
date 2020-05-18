def getSheet(spreadsheets, id, sheet):
    return spreadsheets.values().get(spreadsheetId = id, range = sheet).execute()

def getDoc(doc, id):
    return doc.get(documentId = id).execute()

def getSheetData(worksheet):
    return worksheet.get('values', [])

def getDocContent(doc):
    return doc.get('body').get('content')

def getCapacity(spreadsheet):
    capacities = spreadsheet['Production and capacity utilization details']
    for key in capacities:
        print(key, '=', capacities[key])