# FinAI - Python Test

This project's purpouse was to create a script able to obtain characters usage statistics on FinAI website (https://www.finai.pl/blog), from the first 20 titles each 10 minutes repeating the process.  
To achieve the purpoused result, i chose Python to handle the tasks, due to its major ability to scrap webpagees easily, with access to multiple packages that could help achieve the objective.  
It was suppose to also store the latest 5 fetches to the website. I chose to do in .txt format.  
Executable can be find in the /dist/ folder for testing purpouses. The .txt file will be created in the same folder as the executable.
Comments are present in the code to help you understand the thought process.  
In some anti-virus it can be be detected as a False-Positive, due to the pyinstaller package introducing some dependencies that create it.
To compile yourself, use the following command  

#Using pyinstaller
```bash
pyinstaller --onefile script.py
```
