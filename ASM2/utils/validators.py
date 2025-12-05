def catch_exception(func):
    while True:
        try:
            return func()
        except Exception as e:
            print(f"Error > {type(e).__name__}: {e}")
