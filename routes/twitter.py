import tweepy

from pydantic import Field

from fastapi import status
from fastapi import HTTPException
from fastapi import APIRouter

from credentials import credentials_twitter as credentials


router = APIRouter()

# Path Operations

## Connecttion with Twitter API
@router.get(
    path="/{twitter_user_id}",
    status_code=status.HTTP_200_OK,
    summary="Connection with twitter API",
    tags=["Twitter API"]
    )
def connection_twitter(twitter_user_id: str = Field(
    ...,
    min_lenght=2,
    max_lenght=150
    )
):
    """
        Obtains the user's last five tweets.

        This path operation gets the last five tweets of some  
        twitter user, through Tweepi library and Twitter API v1.1.

        Parameters:
        - Path parameters:
            - twitter_user_id: str

        Returns a json object with user's last five tweets:
    
    """
    auth = tweepy.OAuthHandler(
        credentials.API_key,
        credentials.API_secret_key
    )
    auth.set_access_token(
        credentials.Access_token,
        credentials.Access_token_secret
    )
    api = tweepy.API(auth)
    try:
        tweets = api.user_timeline(screen_name=twitter_user_id, count=5)
        content_tweet = [tweet.text for tweet in tweets]
        number_tweet = [i for i in range(len(content_tweet))]
        dict_tweet = {k: v for k, v in zip(number_tweet, content_tweet)}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return dict_tweet
