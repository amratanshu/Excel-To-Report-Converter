from spreadsheet_utils import isSrNo, getNestingLevel

def createSheetDataStructure(worksheet, current_nesting_level = 0, startindex = 4):
    num_of_rows = len(worksheet)
    data_structure = {}
    i = startindex
    while i < num_of_rows:
        if len(worksheet[i]) > 1 and isSrNo(worksheet[i][0]):
            if getNestingLevel(worksheet[i][0]) > current_nesting_level:
                object, j = createSheetDataStructure(worksheet, getNestingLevel(worksheet[i][0]), i)
                data_structure[worksheet[i - 1][1]] = object
                i = j
                if i >= num_of_rows:
                    return data_structure, i
            elif getNestingLevel(worksheet[i][0]) == current_nesting_level:
                data_structure[worksheet[i][1]] = worksheet[i]
                if i == num_of_rows - 1:
                    i = i + 1
                    return data_structure, i
                i = i + 1
            else:
                return data_structure, i
        else:
            i = i + 1

    return data_structure


