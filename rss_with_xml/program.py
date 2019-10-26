import service


def main():
    print("Bienvenido a descargardor de TalkPython")
    service.download_info()
    for show_id in range(100, 130):
        info = service.get_episodio(show_id)
        print("{}: {}".format(info.title, info.link))


if __name__ == '__main__':
    main()
