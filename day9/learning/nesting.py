#nested lists/dictionaries
player = {
  "Player_Lives": [1,2,3],
  "Player_resources":{
    "mana": 0,
    "health": 100,
  },
}

capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg"],
}

nested_list = [1, 2, [3,4]]

#nested dictionaries
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg"], 
    "total_visits": 5
  },
}

#nesting a dictionary in a list
travel_log = [
  {
    "Country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],  
    "total_visits": 12
  }, 
  {
    "Country": "Germany",
    "cities_visited": ["Berlin", "Hamburg"],  
    "total_visits": 5
  }, 
]