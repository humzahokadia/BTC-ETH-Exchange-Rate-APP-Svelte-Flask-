# Questionarre
1. Are there any sub-optimal choices( or short-cuts taken due to limited time ) in your implementation?

To retrieve the Exchange rate data I used fetch() but could have used Axios as it supports older browsers.

2. Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)

There are no over-designed parts of this implementation.

3. If you have to scale your solution to 100 users/second traffic what changes would you make, if any?

If scaling my solution to 100 user/second I would change the back end from Flask to Nodejs as 
both the front end and backend would be javascript resulting in more consistency between the front end and backend.
Nodejs is also designed as an event-driven environment, allowing for easier and quicker asynchronous input/output.

4. What are some other enhancements you would have made, if you had more time to do this implementation

Some other enhancements I would make if given more time is improve the front end.
The front end is basic, with more time I could make it more appealing along with display the
data in different ways such as graphs and charts for both prices and recommendations. I would also write unit tests along 
with add more error handling.
