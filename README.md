# News_Bias_Analysis
In this project, I'm using Selenium, Beautiful Soup, and Python to extract the news channels, its feedback ratings and bias.
The news rating, link and bias has been obtained from "https://www.allsides.com/media-bias/". 
Each news source has a rating based on agree-disagree votes that decides whether the news source is a leftist, right or center. 

**EXTRACT:**
<p float="center">
    <img src = "https://miro.medium.com/max/1200/1*xn6zhVel2AjaA7dbGgf3rg.png"  width = "200">
    <img src = "https://cdn.analyticsvidhya.com/wp-content/uploads/2021/04/56856232112.png" width = "200">
    <img src = "https://www.fullstackpython.com/img/logos/sqlite.jpg" width = "200"
 </p>         



To extract data, I used Selenium that scrapes the HTML elements on the website of media-bias. However, only popular new channels reviews were present. Upon scrolling more would appear. This is where Beautiful Soup fails and Selenium helps to scroll down till the end using the Chrome webdriver. After scrolling till the end, and obtained the HTML contents, we scrap the _<body>_ tags and then scrap out the _<tr>_ tags that contain data for each media Bias.

**TRANSFORM:**
After extraction of the data, I transform the it into valuable information like the number of people that agree or dissagree with the ratings, bias rating, ratio of agreement ot dissagreement and link to the news source. 

**LOAD:**
  
After transformating the extracted data, I load it into the SQL database from which I will be pulling data as per requirement for visualizations.
  
  <h2> Data Analysis </h2>
  <img src = "https://imgur.com/EsEwoUA.png" width = "400">
  This plot shows the number of "Agree" and "Disagree" votes for "Left" bias. The number of outslets in the plot have top half Agree-Disagree ratio > 3.689.
  Highest Agree-Disagree ratio: 6.76
  Lowest Agree-Disagree ratio: 0.63
  
  <img src="https://imgur.com/flqoyOn.png" width = "400">
  This plot shows the number of "Agree" and "Disagree" votes for "Left" bias. The number of outslets in the plot have Agree-Disagree ratio < 3.689 and > 2.566.
  
  <img src = "https://imgur.com/ON2d8im.png" width = "800">
  This plot shows the number of "Agree" and "Disagree" votes for "Left" bias. The number of outslets in the plot have Agree-Disagree ratio < 2.566.
   
  <hr>                                                                                                                                              
  Top 10 Left biased Media Outlets with their Agree-Disagree votes.

  <img src="https://imgur.com/bgA1Ypt.png" width = "400">
  <hr>
 
  Top 10 Right biased Media Outlets with their Agree-Disagree votes.
  
  <img src="https://imgur.com/2GkSZCD.png" width = "400">
  <hr>
 
  Top 10 Left-Center biased Media Outlets with their Agree-Disagree votes.
  
  <img src="https://imgur.com/K6Qq5Pw.png" width = "400">
    <hr>
  
  Top 10 Right-Center Media Outlets with their Agree-Disagree votes.
  
  <img src="https://imgur.com/eDWhkP1.png" width = "400">
  
  <hr>
  Top 10 Center Media Outlets with their Agree-Disagree votes.
  
  <img src="https://imgur.com/RaQa2Xz.png" width = "400">
  
   <hr>                                                   
