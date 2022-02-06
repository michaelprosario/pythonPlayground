import pandas as pd

def split(dataFrame, size):
    if(dataFrame.empty or dataFrame.shape[0] == 0):
        return []

    if(size == None or size < 0 ):
        raise ValueError("size is required")

    response = { 'success': True, 'data':[], 'message': 'ok' }

    data = []
    
    rowCount = dataFrame.shape[0]
    while rowCount > 0:
        subGroup = pd.DataFrame()
        for i in range(size):
            rowCount = dataFrame.shape[0]
            if (rowCount > 0):
                topRow = dataFrame.iloc[:1]
                dataFrame.drop(index=dataFrame.index[0], axis=0, inplace=True)
                subGroup = pd.concat([topRow, subGroup],ignore_index = True)
                subGroup.reset_index()
        if (subGroup.shape[0] > 0):
            data.append(subGroup)
    
    response['data'] = data
    return response