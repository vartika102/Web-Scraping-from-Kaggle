# Web-Scraping-from-Kaggle
Web scraping of data related to the ongoing computer vision competitions on Kaggle, using scrapy.

In order to run the code:
-Open command line
-Change the directory to 'ourfirstscraper1'
-Run 'scrapy crawl kaggle -t csv -o ->kaggle.csv
#this command shows the desired output and stores it into a csv file named 'kaggle.csv'.
#'kaggle.csv' is saved in 'ourfirstscrapper1' folder.

In order to add more attributes to the outout, yield new attributes from the dictionary 'competition' in the 'kaggle.py' file.
