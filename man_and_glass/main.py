from logic import Man, Glass, DrinkingView


def main():
    m = Man()
    g = Glass()

    view = DrinkingView(m, g)
    view.view_drink()


if __name__ == "__main__":
    main()
