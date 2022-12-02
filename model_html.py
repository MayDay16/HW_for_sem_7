#Отвечает за создание HTML-файла

def create_html(tel_directory):
    style = 'style="front-size:30px"'
    html = '<html>\n <head></head>\n <body>\n'
    for str in tel_directory:
        html += '<p {}> {}</p>\n'\
        .format(style, str)
    html += '</body>\n</html>'

    with open('index.html', "w") as page:
        page.write(html)

    return html