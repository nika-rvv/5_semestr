import datetime

from django.shortcuts import render
from datetime import date


def GetDogs(request):
    return render(request, 'dogs.html', {'data' : {
        'current_date': date.today(),
        'current_time': datetime.datetime.now().time(),
        'dogs': [
            {'name': 'Бивер йорк'},
            {'name': 'Кане корсо'},
            {'name': 'Золотистый ретривер'},
        ]
    }})

def GetDog(request, name):
    return render(request, 'dog.html', {'data' : {
        'current_date': date.today(),
        'name': name,
        'dogs': [
            {'name': 'Бивер йорк', 'desc': '– прекрасный компаньон. Он готов сопровождать хозяина везде, вызывая добродушные улыбки у прохожих. Это не диванная собака, а полноценный терьер с выразительной харизмой и серьезным характером. У бивер-йорка много энергии, поэтому с ним не будет скучно.',
             'img': 'images/biver_jork.jpg'},
            {'name': 'Кане корсо', 'desc': '- собаки данной породы – крупные и мощные молоссы. Это одна из итальянских пород собак, заслуженно ставшая настоящей гордостью этой страны. Молоссы — группа пород собак, в которую входят пастушьи собаки, догообразные (потомки боевых и травильных собак) и гуртовые собаки.',
             'img': 'images/cane_corso.jpg'},
            {'name': 'Золотистый ретривер', 'desc': '— это нежная собака со спокойным характером. Обычно она хорошо адаптируется к семейной жизни. Собака любит участвовать в разныхактивностях: в помещении или на улице. В первую очередь это охотничья поисковая собака. Она будет пытаться тащить, тянуть или нести всё, что вместится в её рот. Ретриверы очень любят воду. Будьте осторожны, если поблизости есть вода. Золотистые ретриверы — это также и беспокоящиеся собаки. В ходе дрессировки следует соблюдать осторожность, учитывая их нежность и чувствительность.',
             'img': 'images/gold_retriver.jpg'}
        ]
    }})