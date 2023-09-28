# how to create a class

class User:
  def __init__(self, user_id, username):
    print("new user being created")
    self.id = user_id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self, user):
    user.followers += 1
    self.following += 1
  #pass # can use pass to not do anything

user_1 = User("001", "angela")
user_2 = User("002", "Jack")
"""
user_1.id = "001"
user_1.username = "angela"
can already give attributes even without adding the attributes to the class! whoa 
"""

# user_1.followers can just be called in the init method... so cool
print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)


# user2 = User("001", "angela")
# user3 = User()