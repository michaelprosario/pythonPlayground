import pandas as pd

def createTestDataFrame():
    dataRows = []
    for i in range(30):
        row = {'name': 'foo ' + str(i), 'value': i}
        dataRows.append(row)

    df = pd.DataFrame(dataRows)
    return df

def splitDataFrame(dataFrame, size):
    response = { 'success': True, 'data':[], 'message': 'ok' }

    data = []
    # while source data frame has stuff
    rowCount = dataFrame.shape[0]
    while rowCount > 0:
        subGroup = pd.DataFrame()
        for i in range(size):
            rowCount = dataFrame.shape[0]
            if (rowCount > 0):
                topRow = dataFrame.iloc[:1]
                dataFrame.drop(index=df.index[0], axis=0, inplace=True)
                subGroup = pd.concat([topRow, subGroup],ignore_index = True)
                subGroup.reset_index()
                
        data.append(subGroup)
    
    response['data'] = data
    return response

df = createTestDataFrame()

response = splitDataFrame(df, 10)

frames = response['data']
print(frames[2])