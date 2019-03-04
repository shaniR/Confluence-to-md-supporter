# Confluence-to-md supporter tool
The [Confluence-to-markdown](https://github.com/meridius/confluence-to-markdown) converter is able to convert most of the HTML to MD. However, some of the macros such as warning/tip/note/info etc does not get directly translated. This tool helps fill such gaps. 

## What the tool does
The script consists of two sub scripts. Pre-processing and post-processing. The pre-processing script will run pre-processing logic on the html files. These pre-processed html files will be fed in to the confluence-to-md converter tool. The converted md files will be fed into the post-processing script, for further cleanup.

Main functions of the tool:
* converts warning/tip/info/note macros correctly
* Removes attachments from end of page
* Removes unnecessary span tags
* Adds spaces infront of text for proper formatting

## Pre-requisites to run the tool
1. Install python
2. install the [confluence-to-markdown](https://github.com/meridius/confluence-to-markdown) tool.

## How to run the tool
1. Open start.sh.
2. Configure the folder paths by creating new folders as required. These folder paths will be used by the scripts.
  * html_source_folder - The folder path where the unmodified confluence HTML files are stored. 
  * html_destination_folder - The destination folder for the pre processed HTML pages.
  * conversionToolFolderPath- Path to the conversion tool
  * md_source_folder- Path to the folder that contains the md files generated from the confluence-to-markdown tool
  * md_dest_folder - Destination folder that contains the post processed .md files.
3. On the last line of the script, change the <html_dest_folder_name> to the folder name chosen for the "html_destination_folder" config. Refer to the sample below.

    ```
    python post_processing.py "$md_source_folder/html_dest_folder/" "$md_dest_folder"
    ```
 4.Run the start.sh script
    ```
     ./start.sh
    ```
