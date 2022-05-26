import header as hd

def main():
    game = hd.GameManager()
    try:
        if False:
            raise ValueError("error")
        while(game.mainLoop()):
            pass

    except ValueError as error:
        print(error)
    return 0


if __name__ == "__main__":
    main()
