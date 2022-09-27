# <div class="cell"><div> 8:30</div></div>
# <a href="https://meet.google.com/tkv-jfru-ykg"><div class="cell"><div class="type prac">Prac</div><div class="lesson">Асинхронне програмування</div><div class="teacher"><img src="teacher.svg">Смаковський Денис Сергійович</div></div></a>

def get_data():
    data = {}
    with open('data.txt', 'r', encoding='utf-8') as file:
        data['start_date'] = file.readline().strip()
        data['times'] = file.readline().strip().split(',')
        lessons = []
        for line in file.readlines():
            lessons.append(line.strip().split(','))
        data['lessons'] = lessons
    return data


def parse_data(data):
    times = [f'<div class="cell"><div>{x}</div></div>' for x in data['times']]
    times = '\n\t\t\t'.join(times)
    start = data['times'][0].split(':')
    start = int(start[0]) * 60 + int(start[1]) - 10
    first = [times] + ['\n\t\t\t\t\t{}' * len(data['times']) + '\n\t\t\t\t'] * 12 + ['\'' + data['start_date'] + '\''] + [start]
    second = []
    for lesson in data['lessons']:
        if len(lesson) == 1:
            s = '<div class="cell"></div>'
        elif len(lesson) == 4:
            s = f'<div class="cell"><a href="{lesson[3]}"><div class="type {lesson[0].lower()}">{lesson[0]}</div><div class="lesson">{lesson[1]}</div><div class="teacher"><img src="teacher.svg">{lesson[2]}</div></a></div>'
        second.append(s)
    return [first, second]

 
def make_file(data):
    template = ''
    with open('template.txt', 'r', encoding='utf-8') as file:
        template = file.read()
    
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(template.format(*data[0]))
        
    with open('index.html', 'r', encoding='utf-8') as file:
        template = file.read()
        
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(template.format(*data[1]))

def main():
    data = get_data()
    data = parse_data(data)
    make_file(data)


if __name__ == '__main__':
    main()