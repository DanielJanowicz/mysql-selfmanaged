# Here are the errors I encountered for this assignment: 

The major error I encountered was in the main.py file, when trying to run a query from the mySQL database.  When running line 24, the error given was 2003 (server timed out).  I am currently running on a GCP VM with the correct ports opened, and mysql settings switched to 0.0.0.0, however I am still running into the timed out problem.  The error can be viewed here: 

![TimedOutError](/Errors/timedouterror.png)

I went to try to redo the entire process over on Azure, however I was getting a similar, but different error.  It continued to refuse connection, but it was due to the matter that it flat out refused, rather than time out.  

![ClosedConnectionError](/Errors/azureerror.png)