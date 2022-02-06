import pandas as pd
import unittest
import banana

def createTestDataFrame(size):
    dataRows = []
    for i in range(size):
        row = {'name': 'foo ' + str(i), 'value': i}
        dataRows.append(row)

    df = pd.DataFrame(dataRows)
    return df

class TestSplitter(unittest.TestCase):
    def test_bananaSplit_handleValidInputs(self):
        # arrange
        test_data = createTestDataFrame(30)
        
        # act
        response = banana.split(test_data, 10)
        
        # assert
        output = response['data']        
        self.assertTrue(response)
        self.assertTrue(len(output)==3)

    def test_bananaSplit_handleLargeDataFrame(self):
        # arrange
        test_data = createTestDataFrame(300)
        
        # act
        response = banana.split(test_data, 10)
        
        # assert
        output = response['data']        
        self.assertTrue(response)
        self.assertTrue(len(output)==30)
        print(output[9])

    def test_bananaSplit_handleCaseWhereSizeBiggerThanDataFrame(self):
        # arrange
        test_data = createTestDataFrame(30)
        
        # act
        response = banana.split(test_data, 50)
        
        # assert
        output = response['data']
        print(len(output))
        self.assertTrue(response)
        self.assertTrue(len(output)==1)
        

# what if size is bigger than the data frame?

if __name__ == '__main__':
    unittest.main()

