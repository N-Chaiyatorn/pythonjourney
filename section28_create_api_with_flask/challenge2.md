# Challenge 2

1. Create a POST request route in main.py to handle POST requests to our API. In order for our API to be RESTful, ideally, the route should be something like this:
```
/add-cafe/<cafe_id>
```
So the user might go to localhost:5000/add-cafe/45 and that would add new café with an id of 45

2. Create a PATCH request route in main.py to handle PATCH requests to our API. In order for our API to be RESTful, ideally, the route should be something like this:
```
/update-price/<cafe_id>
```
So the user might go to localhost:5000/update-price/22 and that would update the café with an id of 22.

HINT 1: You can use .get_or_404() easily get a café by a particular id.

HINT 2: The user will also need to provide the updated price of a single black coffee by passing it with the request as a parameter.

3. Create a PATCH request route to our server and update the database.

But we can't let just anyone delete things in our database. We might soon end up with someone accidentally deleting everything.

We can add a security feature by requiring an api-key . If they have the api-key "TopSecretAPIKey" then they're allowed to make the delete request, otherwise, we tell them they are not authorized to make that request. A 403 in HTTP speak.

Complete this challenge by adding the DELETE route to /delete-cafe/<cafe_id>. Make sure the request has the correct api-key attached and we check if it's correct in our API