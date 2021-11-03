# News_Bias_Analysis
In this project, I'm using Selenium, Beautiful Soup, and Python to extract the news channels, its feedback ratings and bias.
The news rating, link and bias has been obtained from "https://www.allsides.com/media-bias/". 
Each news source has a rating based on agree-disagree votes that decides whether the news source is a leftist, right or center. 

**EXTRACT:**
To extract data, i used Selenium to scroll through the webpage as it doesn't have pages and more content appears as we scroll down. After scrolling till the end, we collect the html content which is later parsed using Beautiful Soup. 

**TRANSFORM:**
After extraction of the data, I transform the it into valuable information like th enu ber of people that agree or dissagree with the ratings, bias rating, ratio of agreement ot dissagreement and link to the news source. 

**LOAD:**
After transformating the extracted data, I load it into the SQL database from which I will be pulling data as per requirement for visualizations.
