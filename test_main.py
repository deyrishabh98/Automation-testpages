from selenium import webdriver
from selenium.webdriver.common.by import By

input_data = [{"name" : "Bob", "age" : 20, "gender": "male"}, {"name": "George", "age" : 42, "gender": "male"}, {"name":
"Sara", "age" : 42, "gender": "female"}, {"name": "Conor", "age" : 40, "gender": "male"}, {"name":
"Jennifer", "age" : 42, "gender": "female"}]

browser = webdriver.Firefox(executable_path="/Users/rishabhdey/UI-Automation/gecko_driver")
browser.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/details').click()
browser.find_element(by=By.ID, value='jsondata').clear()
json_data = str(input_data).replace("'", '"')
browser.find_element(by=By.ID, value='jsondata').send_keys(json_data)
browser.find_element(by=By.ID, value='refreshtable').click()

#Getting data from the table
table = browser.find_element(by=By.ID, value='dynamictable')
rows = table.find_elements(by=By.TAG_NAME, value='tr')
header = [col.text for col in rows[0].find_elements(by=By.TAG_NAME, value='th')]
table_data = [[col.text for col in row.find_elements(by=By.TAG_NAME, value='td')] for row in rows[1:]]
actual_data = [header] + table_data


expected_data = [header]
for data in input_data:
    expected_data.append([data["name"], str(data["age"]), data["gender"]])

print("Actual Data:")
print(actual_data)
print("Expected Data:")
print(expected_data)

assert expected_data == actual_data, "Table data doesn't match with the expected data."

browser.quit()
