"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "DidController@index").name("index"),
        Get("/@id", "DidController@show").name("show"),
        Post("/", "DidController@create").name("create"),
        Put("/@id", "DidController@update").name("update"),
        Delete("/@id", "DidController@destroy").name("destroy")
    ], prefix="/dids", name="dids")
]
