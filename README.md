# Blog-site
Blog site - a dynamic HTML page made with the Flask framework (Jinja).

On the home page there is a list of all posts which are dynamicly generated in the HTML from a database.
Each post contains a "Read" button which takes the user to subpage of the chosen containing the post title, subtitle, body, difficult and duration.
It has a link to a contact page. It contains a WTForm that submits after running a validation check. If everything is validated, sends the message by email to the prespecified email. 
In order to work the user needs to write their email and password. The password is best to be submitted to the environment.
Also features a login page. It contains a WTForm that submits after running validation check. If all requirements are met, user is returned to Home page. 
Currently there is an "Add new post" button. IT takes the user to a page consisting of WTForm. Upon submitions validation runs. If successful, submitted data is commited to database and user is taken to homepage.

Possible features to be added: signup page, logout page, function to add posts if logged into admin account, comment section for each blog with name of commenter and time of posting the comment.
