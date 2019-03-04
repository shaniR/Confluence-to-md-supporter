#!/bin/bash

#The folder path where the unmodified confluence HTML files are stored. 
html_source_folder='/home/shani/RnD/TC/html_to_md_supporter/AM260'

#The destination folder for the pre processed HTML pages.
html_destination_folder='/home/shani/RnD/TC/html_to_md_supporter/html_dest_folder/'

#Path to the conversion tool
conversionToolFolderPath='/home/shani/RnD/github_conv/confluence-to-markdown'

#Path to the modified HTML files
FILES='/home/shani/RnD/github_conv/convertedFiles'

#Path to the folder that contains the md files generated from the confluence-to-markdown tool
md_source_folder='/home/shani/RnD/TC/html_to_md_supporter/md_source_folder/'

#Destination folder that contains the post processed .md files.
md_dest_folder='/home/shani/RnD/TC/html_to_md_supporter/md_dest_folder/'

python pre_processing.py "$html_source_folder" "$html_destination_folder"

echo '-------------------   Converting to md - Started !  -------------------------'
for f in $html_destination_folder
do
   npm run start --prefix $conversionToolFolderPath $f $md_source_folder
done

echo '-------------------   Converting to md - Completed!  -------------------------'

python post_processing.py "$md_source_folder/html_dest_folder/" "$md_dest_folder"


