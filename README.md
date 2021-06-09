# Blog-site
Blog site - a dynamic HTML page made with the Flask framework (Jinja).

On the home page there is a list of all posts which are dynamicly generated in the HTML from a database.
Each post contains a "Read" button which takes the user to subpage of the chosen containing the post title, subtitle, body, difficult and duration.
It has a dropdown menu which contents depend if there is a logged user.
The dropdown menu has:
A link to a contact page. It contains a WTForm that submits after running a validation check. If successful, sends the message by email to the prespecified email. 
In order to work the host needs to write their email and password. The password is best to be submitted to the environment. Contact page button is always visible.
A login page and signup page links. They contain a WTForm that submits after running validation check. If all requirements are met, data is checked or created in the database. If user provided proper credentials, he is logged in through the LoginManager from Flask-Login. Login/singup pages are visible only if there is no user authenticated.
A "Add new post" button. It takes the user to a page consisting of WTForm. Upon submitions validation of the field runs. If successful, submitted data is commited to database and user is taken to homepage. The button is visible only if there is an authenticated user.
A logout page link. Upon clicking it redirects the user to a route that logs out the user. The button is visible only if there is an authenticated user. 

Future features: creating an admin account with sole permission to add and edit blog posts.

Possible features to be added: comment section for each blog with name of commenter and time of posting the comment.
