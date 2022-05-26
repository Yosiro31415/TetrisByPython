import header as hd

def main():
    core = hd.CoreManager()
    try:
        if False:
            raise ValueError("error")
        while(core.mainLoop()):
            pass

    except ValueError as error:
        print(error)
    return 0


if __name__ == "__main__":
    main()
