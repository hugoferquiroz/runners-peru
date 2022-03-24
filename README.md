# runners-peru

This repository collect and analyze data from [running races in Peru](https://pacifictiming.com/resultados/).

The objective of this repository is analyze the stat of the running races in Peru.

# Files structure

```markdown
├── Data                        -> File to download the data  in CSV format.

├── Scripts
  ├── '1 Web Scraping.py'       -> Program for web scrapping. Return a csv file with enconded utf-8 and a data frame.
```

# Steps to replicate

1. Run the script '1 Web Scraping.py'  
   * If you not installed selenium write this command in your command prompt or terminal `pip install selenium`.

   * In this project I used Google Chrome then you need the last version of Chromedriver.  Download the last version [here](https://chromedriver.chromium.org/downloads). Unzip the file and save in a path that you remember.

   * Run the function `webscraping_running_peru`. I put examples to web scrapping marathons but you can modify the code for web scrapping other running race just replace the number 11 with 10 in the lines 61, 66, 71, 76, 81, 86, 91, 96 and 101. Also you can modify the implicit wait according of your internet speed.

2. Descriptive stats (for coming)
3. Demand forecasting (for coming)

# Requirements
  - Google Chrome
  - The last version of Chromedriver
  - Python 3
