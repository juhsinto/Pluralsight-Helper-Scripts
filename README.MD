# Pluralsight Helper Scripts
I wasn't able to get `youtube-dl` to work with Pluralsight. Hence, I created these scripts because I wanted to make the most of the "Free Pluralsight Weekend". 

I have had success (for downloading the videos) using the following chrome extensions:
- https://chrome.google.com/webstore/detail/one-click-video-downloade/bhepgcoaibmmehlmckhlmbdgcemhidcg
- https://chrome.google.com/webstore/detail/video-downloader-professi/elicpjhcidhpjomhibiffojpinpmmpil

## 1. Pluralsight TOC Generator
This will generate a *somewhat* organized table of contents from the Pluralsight page. Make sure to copy the HTML from the inspector. You will need the whole div with id "tab-table-of-contents".
See example file 'page.html' for reference

### Running this script:
`python scrape.py > output.txt`

The output that it would produce would like like this:
![alt text](https://i.ibb.co/KNfnxnJ/Screen-Shot-2019-09-13-at-11-13-33-am.png "TOC output")

### Note
You will have to (manually) paste the Chapter title section with a tab indent
___
## 2. Pluralsight File & Directory Renamer
This python script helps you organize and rename your pluralsight downloaded videos.

Input:
![alt text](https://i.ibb.co/5jW2rW2/Screen-Shot-2019-09-13-at-11-26-53-am.png "Input")

Output:
![alt text](https://i.ibb.co/Zmhs8W7/Screen-Shot-2019-09-13-at-11-27-29-am.png "Input")

### Running this script:
`python file_renamer.py`

### Important
- When downloading the files, rename the file in serial order (don't add a 0 [zero] to the start of the file name)
- Make sure your toc.txt file is structured (with tabs), try to remove all forward slashes '/'
- See example `toc.txt` for sample TOC
___
#### Notice
I am not responsible if this script messes up your computer, or if you get in trouble for using these scripts. Please support the content creators