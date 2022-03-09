## My Bae's PDF Converter

### TO Do List

- Download chromedriver via this website : https://chromedriver.chromium.org/downloads, !!!NOTE!!! you must check your chrome version before downloading the driver. The following instructions helps you download the driver if needed.

	- <img src='./img/chrome_version.png' style="width:300px;">
	- <img src='./img/chrome_driver_download.png' style="width:500px;">
	- <img src='./img/chrome_driver_download_2.png' style="width:500px;">
	- <img src='./img/chrome_driver_download_3.png' style="width:500px;">
	- Then, save it in this folder.

- 接下來我們會需要繼續使用終端機，但是在那之前，先用下面的步驟來得到資料夾的路徑：
	- <img src='./img/path.png' style="width:500px;">
- 在終端機打上以下指令然後按enter
```

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
brew install python@3.8
git clone https://github.com/moooooser999/notion_pdf_converter.git
cd notion_pdf_converter
pip3 install tqdm
pip3 install pyquery
pip3 install bs4
pip3 install selenium
```
- put all your .html files into  `html` folder
```
# directory should be like this
*---html
|    |
*    +---file_name.html
|    |
*    +---file_name.html
|    |
*    +---file_name.html
```
- run the following command:
```
bash make_pdf.sh 
```

- the final output should be like this:
```
.
.
.
*---html
|    |
*----+---file_name.html
|    |
*----+---file_name.html
|    |
*----+---file_name.html
|    
*---pdf
|    |
*    +---file_name.pdf
|    |
*    +---file_name.pdf
|    |
*    +---file_name.pdf
```


