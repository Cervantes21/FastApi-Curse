#Python
import json
from uuid import UUID 
from datetime import (date, datetime)
from typing import (Optional, List)

#PyDantic
from pydantic import(
    BaseModel,
    EmailStr,
    Field
    )
 
# FastAPI
from fastapi import(
    FastAPI,
    status,
    Body,
    )
app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date] = Field(default=None)
class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
        )

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
        )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operation

@app.get(path="/")
def home():
    return {'Twitter API': 'working!' }

## Users

### Register a User 
@app.post(
    path="/signup",
    response_model=User, 
    status_code=status.HTTP_201_CREATED,
    summary='Register a User',
    tags=["Users"]
    )
def signup(user: UserRegister = Body(...)):
    '''
    ![Signup](https://t4.ftcdn.net/jpg/04/09/12/37/360_F_409123771_SSIjSUiM9AXVyEUVfxDT2zmoKmJDQALi.jpg)
    
    This Path operation register a user in the app
    
    Parameters:
        -Request body parameter
            - user: UserRegister
    Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    '''
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user
    
### Login a User
@app.post(
    path="/login",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=["Users"]
    )
def login():
    pass

### Show all Users
@app.post(
    path="/users",
    response_model=List[User], 
    status_code=status.HTTP_200_OK,
    summary='Show all Users',
    tags=["Users"]
    )
def show_all_users():
    '''
    ![Show-users](https://www.iconpacks.net/icons/1/free-user-group-icon-296-thumb.png)
    
    This path operation shows all users in the app
    
    Parameters:
        -
    
    Returns a json list with all users is the app, with the following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    '''
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

### Show a User
@app.get(
    path="/users/{user_id}",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
    )
def show_a_user():
    pass

### Delete a User 
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
    )
def delete_a_user():
    pass

### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary='Update a User',
    tags=["Users"]
    )
def update_a_user():
    pass

## Tweets

### Show all Tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"]
    )
def home():
    '''
    # Tw-api
    ![home](https://iconomator.com/wp-content/uploads/2020/03/tweet.png)
    
    This path operation shows all tweets in the app
    
    Parameters:
        -
    
    Returns a json list with all tweets is the app, with the following keys:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    '''
    with open("tweets.json", "r", encoding="utf-8") as t:
        results = json.loads(t.read())
        return results

### Post a Tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)):
    '''
    ![Post-tw](https://thumbs.dreamstime.com/b/add-tweet-post-button-icon-vector-twitter-social-media-element-219099895.jpg)
    # Post a Tweet
    ## This Path operation post a tweet in the app
    
    Parameters:
        - Request Body parameter:
            - tweet: Tweet
            
    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - update_at: Optional[datetime]
        - by: User
    '''
    with open("tweets.json", "r+", encoding="utf-8") as t:
        results = json.loads(t.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        
        results.append(tweet_dict)
        t.seek(0)
        t.write(json.dumps(results))
        return tweet

### Show a Tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweets"]
)
def show_tweet():
    pass

### Delete a Tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def delete_tweet():
    pass

### Update a Tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"]
)
def update_tweet():
    pass