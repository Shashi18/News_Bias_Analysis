# News_Bias_Analysis
In this project, I'm using Selenium, Beautiful Soup, and Python to extract the news channels, its feedback ratings and bias.
The news rating, link and bias has been obtained from "https://www.allsides.com/media-bias/". 
Each news source has a rating based on agree-disagree votes that decides whether the news source is a leftist, right or center. 

**EXTRACT:**

<img src = "https://miro.medium.com/max/1200/1*xn6zhVel2AjaA7dbGgf3rg.png"  width = "100">
![BeautifulSoup](https://cdn.analyticsvidhya.com/wp-content/uploads/2021/04/56856232112.png)

To extract data, I used Selenium that scrapes the HTML elements on the website of media-bias. However, only popular new channels reviews were present. Upon scrolling more would appear. This is where Beautiful Soup fails and Selenium helps to scroll down till the end using the Chrome webdriver. After scrolling till the end, and obtained the HTML contents, we scrap the _<body>_ tags and then scrap out the _<tr>_ tags that contain data for each media Bias.

**TRANSFORM:**
After extraction of the data, I transform the it into valuable information like the number of people that agree or dissagree with the ratings, bias rating, ratio of agreement ot dissagreement and link to the news source. 

**LOAD:**

![SQL](https://media.charlesleifer.com/blog/photos/sqlite-and-python.png)
  
After transformating the extracted data, I load it into the SQL database from which I will be pulling data as per requirement for visualizations.
