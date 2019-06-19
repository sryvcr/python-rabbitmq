from connection import connect


if __name__ == "__main__":

    try:
        connect()
    except Exception as e:
        print(e)
