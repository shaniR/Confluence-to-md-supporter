
from bs4 import BeautifulSoup
import textwrap
import os,sys
import ntpath

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

print '-------------------   Pre processing started!  -------------------------'

html_source_folder = sys.argv[1]
html_dest_folder = sys.argv[2]
for f in files(html_source_folder):

	soup = BeautifulSoup(open(html_source_folder+"/"+f), "html.parser")


	for divInfo1 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-approve confluence-information-macro-icon'}): 
		divInfo1.unwrap()

	for divInfo2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon'}): 
		divInfo2.unwrap()

	for divInfo2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-error confluence-informaftion-macro-icon'}): 
		divInfo2.unwrap()

	for divNote2 in soup.find_all("span", {'class':'aui-icon aui-icon-small aui-iconfont-warning confluence-information-macro-icon'}): 
		divNote2.unwrap()

	for emptySpan in soup.find_all("span", {'class':''}): 
		emptySpan.unwrap()

	for attachments in soup.find_all("div", {'class' :'pageSection group'}):
		attachments.extract()

	for divBody in soup.find_all("div", {'class':'confluence-information-macro-body'}):
		divBody.unwrap()

	for divTip0 in soup.find_all("div", {'class':'confluence-information-macro-tip'}):
		divTip0.insert_before('!!! tip')
		divTip0.insert_after("TEST")
		divTip0.unwrap()

	for divInfo in soup.find_all("div", {'class':' confluence-information-macro-information'}): 
		divInfo.insert_before('!!! info')
		divInfo.insert_after("TEST")
		divInfo.unwrap()

	for divWarning in soup.find_all("div", {'class':'confluence-information-macro-warning'}): 
		divWarning.insert_before('!!! warning')
		divWarning.insert_after("TEST")
		divWarning.unwrap()


	for divNote in soup.find_all("div", {'class':'confluence-information-macro-note'}): 
		divNote.insert_before('!!! note')
		divNote.insert_after("TEST")
		divNote.unwrap()

	html =soup.contents
	html = soup.prettify("utf-8")

        fileName = ntpath.basename(f)
        fileName = html_dest_folder+fileName

	with open(fileName, 'wb') as file:
            file.write(html)
            file.close

print '-------------------   Pre processing completed!  -------------------------'


