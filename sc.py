import html
from bs4 import BeautifulSoup
import requests
print("----------Welcome to Survey No.Scrapper----------")
url="https://dharani.telangana.gov.in/knowLandStatus"
s=requests.session()
r=s.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')

element=soup.select('#districtID')
ole=[]
district_values = {}
district_value=[]
for ele in element:
		options= ele.find_all('option')
		for option in options:
			district_value.append(option.get('value'))
			ole.append(option.get_text().replace('\t','').replace('\r','').replace('\n',''))
ole = [string for string in ole if string]
for i in range(1,len(district_value)):
	district_values[district_value[i]]=ole[i]
# print(district_values)
print("Select the district from the above list:")
for i in range(1,len(ole)):
	print(str(i)+". "+ole[i])
district_number=int(input("Enter the district number:"))
district_id=""
for key in district_values:
	if district_values[key]==ole[district_number]:
		district_id=key
		break
Param={'district':district_id}
url2="https://dharani.telangana.gov.in/getMandalFromDivisionCitizenPortal"
r2=s.get(url2,params=Param)
# Check the status code
print(f"Status code: {r2.status_code}")

htmlContent2=r2.content
element2=BeautifulSoup(htmlContent2,'html.parser')
ole2=[]
mandal_values = {}
mandal_value=[]
options= element2.find_all('option')
for option in options:
	mandal_value.append(option.get('value'))
	ole2.append(option.get_text().replace('\t','').replace('\r','').replace('\n',''))
ole2 = [string for string in ole2 if string]
for i in range(1,len(mandal_value)):
	mandal_values[mandal_value[i]]=ole2[i]
print("\n\nSelect the mandal from the above list:")
for i in range(1,len(ole2)):
	print(str(i)+". "+ole2[i])
mandal_number=int(input("Enter the mandal number:"))
mandal_id=""
for key in mandal_values:
	if mandal_values[key]==ole2[mandal_number]:
		mandal_id=key
		break
Param2={'mandalId':mandal_id}
url3="https://dharani.telangana.gov.in/getVillageFromMandalCitizenPortal"
r3=s.get(url3,params=Param2)
# Check the status code
print(f"Status code: {r3.status_code}")

html3=r3.content
element3=BeautifulSoup(html3,'html.parser')
ole3=[]
village_values = {}
village_value=[]
options= element3.find_all('option')
for option in options:
	village_value.append(option.get('value'))
	ole3.append(option.get_text().replace('\t','').replace('\r','').replace('\n',''))
ole3 = [string for string in ole3 if string]
for i in range(1,len(village_value)):
	village_values[village_value[i]]=ole3[i]
# print(village_values)
print("\n\nSelect the village from the above list:")
for i in range(1,len(ole3)):
	print(str(i)+". "+ole3[i])
village_number=int(input("Enter the village number:"))
village_id=""
for key in village_values:
	if village_values[key]==ole3[village_number]:
		village_id=key
		break
Param3={'villId':village_id,'flag': 'survey'}
url4="https://dharani.telangana.gov.in/getSurveyCitizen"
r4=s.get(url4,params=Param3)
# Check the status code
print(f"Status code: {r4.status_code}")

html4=r4.content
element4=BeautifulSoup(html4,'html.parser')
ole4=[]
options= element4.find_all('option')
for option in options:
	ole4.append(option.get_text().replace('\t','').replace('\r','').replace('\n',''))
ole4 = [string for string in ole4 if string]
print("\n\nThe Servey numbers are:\n")
for i in range(1,len(ole4)):
	print(str(i)+". "+ole4[i])