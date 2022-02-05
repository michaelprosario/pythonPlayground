import pandas as pd
import unittest

def createTestDataFrame():
    dataRows = []
    for i in range(30):
        row = {'name': 'foo ' + str(i), 'value': i}
        dataRows.append(row)

    df = pd.DataFrame(dataRows)
    return df

def splitDataFrame(dataFrame, size):
    if (dataFrame == None):
        raise RuntimeError("data frame is required")
    if (size == None):
        raise RuntimeError("size is required")

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
                dataFrame.drop(index=dataFrame.index[0], axis=0, inplace=True)
                subGroup = pd.concat([topRow, subGroup],ignore_index = True)
                subGroup.reset_index()
        if (subGroup.shape[0] > 0):
            data.append(subGroup)
    
    response['data'] = data
    return response

class TestSplitter(unittest.TestCase):
    def test_splitDataFrame_handleValidInputs(self):
        # arrange
        test_data = createTestDataFrame()
        
        # act
        response = splitDataFrame(test_data, 10)
        
        # assert
        output = response['data']
        print(len(output))
        self.assertTrue(response)
        self.assertTrue(len(output)==3)


if __name__ == '__main__':
    unittest.main()

