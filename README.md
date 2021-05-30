# Blog-site
Blog site - a dynamic HTML page made with the Flask framework (Jinja).
All blog post contents are requested through an API which responds a predefined by me JSON data in npoint.io.
The JSON data is then split into separate objects for each post.
On the home page there is a list of all posts which are dynamicly generated in the HTML.
Each post contains a "Read" button which takes the user to subpage of the chosen containing the post title, subtitle and body.
It has a link to a contact page. It contains a form that submits the info and sends it by email to the user. In order to work the user needs to write their email and password. The password is best to be submitted to the environment.
