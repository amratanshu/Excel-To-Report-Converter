def getTablePositions(contents):
    tablePositions = []
    for content in contents:
        if content.get('paragraph') != None:
            paragraphElements = content.get('paragraph').get('elements')
            for element in paragraphElements:
                if element.get('textRun') != None and element.get('textRun').get('content') == "##\n":
                    tablePositions.append(element)

    print(tablePositions)