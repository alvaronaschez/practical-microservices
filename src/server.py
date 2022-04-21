from application import create_app, run_app


configuration = dict(
    host="0.0.0.0",
    port=8000,
    debug=True,
    auto_reload=True,
    access_log=True,
)


if __name__ == "__main__":
    run_app(create_app(), configuration)
