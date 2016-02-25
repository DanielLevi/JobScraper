This goal of this project was to create a website scraper that could log into a website requiring credentials, scrape the information present and determine according to a set of static criteria if a job available. Why, you might ask? Well, it just so happens that there is a website hosting jobs on a near first-come-first-serve basis. Instead of the user finding him or herself constantly checking the website like a squirrel guarding its acorns, it seems much easier to have a program notify the user. What's even better than that? Receiving the notifications straight to your phone.

Pseudocode and helpful libraries:
<ol>
    <li>Request and login to website - **Requests**</li>
    <li>Retrieve and parse HTML for some job-status indicator - **bs4 (BeautifulSoup)**</li>
    <li>Notify user - **Twilio**</li>
</ol>

Program must run on a schedule independent of the user - **Crontabs/Cronjobs**

Dependencies: BeautifulSoup from bs4, TwilioRestClient from twilio.rest and requests library
