# Blog-site
Blog site - a dynamic HTML page made with the Flask framework (Jinja).<br />

On the home page there is a list of all posts which are dynamically generated in the HTML from a database.<br />
Each post contains a "Read" button which takes the user to subpage of the chosen containing the post title, subtitle, body, difficult and duration.<br />
It has a dropdown menu which contents depend if there is a logged user.<br />
The dropdown menu has:<br />
A link to a contact page. It contains a WTForm that submits after running a validation check. If successful, sends the message by email to the prespecified email. <br />
In order to work the host needs to write their email and password. The password is best to be submitted to the environment. Contact page button is always visible.<br />
A login page and signup page links. They contain a WTForm that submits after running validation check. If all requirements are met, data is checked or created in the database. If user provided proper credentials, he is logged in through the LoginManager from Flask-Login. Login/singup pages are visible only if there is no user authenticated.<br />
A "Add new post" button. It takes the user to a page consisting of WTForm. Upon submitions validation of the field runs. If successful, submitted data is commited to database and user is taken to homepage. The button is visible only if there is an authenticated user.<br />
A logout page link. Upon clicking it redirects the user to a route that logs out the user. The button is visible only if there is an authenticated user. <br />
If logged in the admin account, each post has edit button that redirects to page with WTForm filled with the data of the post. After edit it updates the data in the database.
Also the admin can delete posts.
The adding, editing and deleting routes is protected by admin_only decorator.<br />
Has API call routes /all and /search to obtain all hikes or random hike. Response of this routes is JSON.

Possible features to be added: comment section for each blog with name of commenter and time of posting the comment and option to make other users admins (practice for relational databases)<br />
