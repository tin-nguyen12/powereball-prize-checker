# powereball-prize-checker

What does this do? Well basically, I think the lottery is fun even though it's scam which is why I will only buy when it's over a certain amount. Rather than checking it everyday I wrote this script so that it will automatically check for me every day at a certain time. It will notify me by email once the jackpot has reached a certain amonut (personally it's 40 for me).

##How To Use

1. Download the correct version of ChromeDriver from https://chromedriver.chromium.org/downloads
2. In main.py, find where the driver is instantiated (line 15) and remove the current directory and add in the directory where you have saved ChromeDriver
3. In the if statement at the end, change the number to whatever number that you desire
4. For the login, select the email that you wish to use to email
5. After the email, enter your "App Password" for that email account. (Use this link for guidance: https://support.google.com/accounts/answer/185833?hl=en)
6. In the argumrnet for "sendmail", add in the email which you desire the email to be sent to
7. Followed by that will be the emails' contents. Modify it how you want.
8. Open up the Batch file and remove the current directory and add in your own directory to the python script.
9. Create an automatic task scheduler as specified by your OS (i.e. Windows: Task Schedular).
10. PROFIT.
