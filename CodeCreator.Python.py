FILENAME = "output.txt"


def main():
    while True:
        href_link = input("Gib den Link für href ein: ")
        bild_link = input("Gib den Link für data-src ein: ")
        title = input("Gib den Title ein: ")
        name = input("Gib den Namen ein: ")
        output = f'<li><a href="{href_link}" target="_blank"><img data-src="{bild_link}" class="lazyload" loading="lazy" title="{title}" border="2"/>{name}</a></li>\n '
        with open(FILENAME, "a", encoding='UTF-8') as output_file:
            output_file.write(output)
        print(f"Element erstellt: \n{output}")


if __name__ == '__main__':
    main()
