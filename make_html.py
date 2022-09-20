def get_data():
    data = []
    with open('lessons.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            data.append(line.strip().split(','))
    return data


def parse_data(data):
    res = []
    for d in data:
        if len(d) == 1:
            res.append('')
        elif len(d) == 4:
            s = f'<a href="{d[3]}"><div class="type {d[0].lower()}">{d[0]}</div><div class="lesson">{d[1]}</div><div class="teacher"><img src="teacher.svg">{d[2]}</div></a>'
            res.append(s)
    return res

 
def make_file(data):
    template = ''
    with open('template.txt', 'r', encoding='utf-8') as file:
        template = file.read()
        
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(template.format(*data))


def main():
    data = get_data()
    data = parse_data(data)
    make_file(data)


if __name__ == '__main__':
    main()