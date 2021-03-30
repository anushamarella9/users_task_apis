First i have developed frontend work on the website (using Material Ui library)like added button for 'Add User'(it will open popup and ask for user name ,id)and showed list of users in grid format(means added users manually so that i'd know if it's working or not)
for that users, have added tasks by clicking + icon in the users block.
also i put close icon on top right if it's clicked it will delete user(i just keep it in modal and asked for delete confirmation)

now, i have added Apis for all these actions in Flask with MongoDB

imported pymongo and connected to mongo server by importing MongoClient

for users, create a collection named 'users' and added user by using insert_one i have passed the headers content-type 
get users - to get all users from the users collection
delete user - to delete particular user by user id

added tasks for user, get tasks, update tasks and delete tasks
also used CORS to enable scripts running on browser to interact with dirfferent origin resources 
