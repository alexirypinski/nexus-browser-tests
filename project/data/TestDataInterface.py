from curses import raw
import json
import io
import json

class TestDataInterface():

    __dataFile = 'files/TestData.json'

    #public method for writing a value to the name field in a file files/testData.json
    def save_data(self, fieldName, newValue):

        dataJson = self.__get_json_from_file(self.__dataFile)
        dataJson = self.__modify_json(dataJson, fieldName, newValue)
        self.__write_json_to_file(dataJson, self.__dataFile)

        
    
    #gets the value of the name variable from its corres
    def get_data(self, fieldName):

        dataJson = self.__get_json_from_file(self.__dataFile)
        return self.__get_variable_from_json(dataJson, fieldName)


    
    #private methods

    
    #gets the json object from the specified file (ie TestData.json)
    def __get_json_from_file(self, file):
        
        with open(file, "r", encoding="utf-8") as rawFile:
            text = rawFile.read()
            fileJson = json.loads(text)
        return fileJson
        

    
    #gets the value stored in the fieldName field from the json object
    def __get_variable_from_json(self, myjson, fieldName):

        return myjson[fieldName]



    #writes the json object to the specified file (ie TestData.json)
    def __write_json_to_file(self, myjson, file):

        with open(file, "w", encoding="utf-8") as rawFile:
            rawFile.seek(0)
            toWrite = json.dump(myjson, rawFile)
            rawFile.truncate()


    
    #overwrites the name variable with newValue
    def __modify_json(self, myjson, fieldName, newValue):
        
        myjson[fieldName] = newValue
        return myjson


        

    
    
if __name__ == '__main__':
    
    interface = TestDataInterface()

    #test reading from JSON
    print(interface.get_data("numTestsRun"))
    interface.save_data("numTestsRun", "2")
    print(interface.get_data("numTestsRun"))


    #test writing to JSON
    interface.save_data("numTestsRun", "3")
    print(interface.get_data("numTestsRun"))
    interface.save_data("numTestsRun", "4")
    print(interface.get_data("numTestsRun"))
    
