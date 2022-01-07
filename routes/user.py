from fastapi import status
from fastapi import HTTPException
from fastapi import Body
from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from fastapi.responses import RedirectResponse

from database.database import connection
from schemas.schemas import User, LoginForm
from routes.twitter import connection_twitter

router = APIRouter()

templates = Jinja2Templates(directory="./templates")

# Path Operations

## Home
@router.get(
    path="/",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
    summary="Shows login",
    tags=["Users"]
    )
def login_request():
    """
        Redirect to login.

        This path operation redirect the users to login.

        Returns a HTMLResponse.

    """
    return RedirectResponse("/login")

## Get login
@router.get(
    path="/login",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
    summary="Shows login",
    tags=["Users"]
    )
def login_request(request: Request):
    """
        Shows a login form.

        This path operation allows the users login in the portfolio web
        through a form, with the user_id.

    """
    return templates.TemplateResponse(
        name="login.html",
        context={"request": request}
        )

## Login
@router.post(
    path="/login",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
    )
async def login(request: Request):
    """
        Login a  user.

        This path operation allows to login a user.

        Parameters:

        - Path parameters:
            - request: **Request**
            - user_id: **str**
        Returns a HTMLResponse with the information of the user.
    """
    form = LoginForm(request)
    await form.load_data()
    try:
        response = show_user(request=request, user_id=form.user_id)
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

## Shows user profile
@router.get(
    path="/user/{user_id}",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
    summary="Shows a user",
    tags=["Users"]
    )
def show_user(request: Request, user_id: str):
    """
        Shows a  user.

        This path operation allows to get the information of a specific user.

        Parameters:

        - Path parameters:
            - request: **Request**
            - user_id: **str**

        Returns a HTMLResponse with the information of the user.
    """
    try:
        with connection.cursor() as cursor:
            tables = "SHOW COLUMNS FROM portfolio;"
            cursor.execute(tables)
            tables = cursor.fetchall()
            tables = [column[0] for column in tables]
            consult = "SELECT * FROM portfolio WHERE user_id={};"
            cursor.execute(consult.format(user_id))
            consult = cursor.fetchall()
            consult = [field for field in consult[0]]
            result = {v: k for v, k in zip(tables, consult)}
            user = User(**result)
            tweets = connection_twitter(user.twitter_user_id)
            context = user.dict()
            context["request"] = request
            context["tweets"] = tweets.values()
            response = templates.TemplateResponse(
                name="user.html",
                context=context
            )
            return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

## Updates user profile
@router.put(
    path="/user/{user_id}/update",
    status_code=status.HTTP_201_CREATED,
    response_class=JSONResponse,
    summary="Updates a user",
    tags=["Users"]
    )
def update_user(
    user_id: str,
    user: User = Body(
        ...
        )
):
    """
        Updates users.
        This path operation allows to update information of a specific user.

        Parameters:
        - Path parameters:
            - idportfolio: **int**
            - description: **str**
            - experience_summary **str**
            - id **int**
            - image_url **str**
            - last_names **str**
            - names **str**
            - tittle**str**
            - twitter_user_id**str**
            - twitter_user_name**str**
            - user_id: **str**
    """
    try:
        if user_id == user.user_id:
            with connection.cursor() as cursor:
                user_id = user.user_id
                user_dict = user.dict()
                user_dict_keys = [
                    str(k) + "=" + "%s" for k in user_dict.keys()
                ]
                update_fields = ", ".join(user_dict_keys)
                user_dict_values = tuple(
                    v for v in user_dict.values()
                )
                consult = "UPDATE portfolio SET " + update_fields + \
                    " WHERE user_id={};".format(user_id)
                cursor.execute(consult, (user_dict_values))
                connection.commit()
                return {"User: updated"}
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Action not allowed"
            )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
