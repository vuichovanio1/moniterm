# -*- coding: utf-8 -*-
"""Generate Moni Term service hubs + projects (no geo doorway pages)."""
from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

from _hub_content import HUB_CONTENT

ROOT = Path(r"C:\repos\moniterm")
DOMAIN = "https://vuichovanio1.github.io/moniterm"
TEL = "+359886391729"
PHONE = "0886 391 729"
EMAIL = "moni.term@abv.bg"
ADDRESS = "ул. Славянска, 2230 Костинброд"
FB = "https://www.facebook.com/profile.php?id=100063597367628"
TODAY = date.today().isoformat()

# Coverage shown as on-page area grid (not separate URLs)
CITIES = [
    {"slug": "sofia", "name": "София", "blurb": "Столицата и кварталите — монтаж с внимание към достъпа и етажната собственост."},
    {"slug": "kostinbrod", "name": "Костинброд", "blurb": "Нашата база — най-бърз оглед и реакция тук и в близките села."},
    {"slug": "slivnitsa", "name": "Сливница", "blurb": "Удобно разстояние от Костинброд за оглед и монтаж в същия ден."},
    {"slug": "dragoman", "name": "Драгоман", "blurb": "Къщи и вили — планираме доставка според достъпа на терена."},
    {"slug": "godech", "name": "Годеч", "blurb": "Уточняваме маршрута предварително, за да приключим без излишни посещения."},
    {"slug": "bozhurishte", "name": "Божурище", "blurb": "Близо до София — бърз оглед в работни дни."},
    {"slug": "svoge", "name": "Своге", "blurb": "По Искърското дефиле отчитаме терена още на огледа."},
    {"slug": "elin-pelin", "name": "Елин Пелин", "blurb": "Жилищни и индустриални обекти — оразмеряване след оглед."},
    {"slug": "bankya", "name": "Банкя", "blurb": "Жилищни обекти с внимание към шума и графика на живущите."},
    {"slug": "novi-iskar", "name": "Нови Искър", "blurb": "Северните квартали — удобен дневен монтаж от Костинброд."},
]

SERVICES = [
    {
        "slug": "gazovi-kotli",
        "nav": "kotli",
        "name": "Газови котли",
        "h1_hub": "Монтаж на газови котли",
        "title_hub": "Монтаж на газов котел | София област — Мони Терм",
        "keyword": "монтаж газов котел",
        "keyword_long": "газов котел монтаж",
        "desc_hub": "Монтаж на газови котли в София и София област. Доставка, връзка към инсталацията и настройка — Мони Терм ЕООД, Костинброд. Тел. 0886 391 729.",
        "lead": "Професионален монтаж на газови котли за домове и обекти — от подбора на модела до пускане и настройка.",
        "detail": "Работим с утвърдени марки, включително Immergas. След оглед уточняваме дали е смяна на съществуващ котел или нова връзка към газовата и отоплителната инсталация. Целта е чист монтаж, стабилна работа и ясен инструктаж.",
        "image": "moni1.jpg",
        "gallery": ["moni1.jpg", "moni16.jpg", "moni8.jpg", "moni7.jpg"],
        "bullets": [
            "Доставка и монтаж на газови котли",
            "Връзка към газовата и отоплителната инсталация",
            "Програматори и терморегулация",
            "Пускане и прецизна настройка",
        ],
        "process": [
            ("Оглед", "Преглед на инсталацията, комина/отвеждането и мястото за котела."),
            ("Оферта", "Модел, труд и срокове — без изненади след старта."),
            ("Монтаж", "Свързване, изпитания и настройка на комфорта."),
            ("Пускане", "Инструктаж и съвети за експлоатация."),
        ],
        "faqs": [
            ("Колко струва монтаж на газов котел?", "Зависи от модела и дали се изгражда нова връзка. Оферта след оглед: 0886 391 729."),
            ("Монтирате ли в София и областта?", "Да — база Костинброд, обслужваме София и София област."),
            ("Работите ли с Immergas?", "Да, монтираме утвърдени марки, включително Immergas."),
        ],
    },
    {
        "slug": "rezervuari-propan-butan",
        "nav": "rezervuari",
        "name": "Резервоари пропан-бутан",
        "h1_hub": "Доставка и монтаж на резервоари за пропан-бутан",
        "title_hub": "Резервоари пропан-бутан | София област — Мони Терм",
        "keyword": "резервоар пропан-бутан",
        "keyword_long": "подземен резервоар газ",
        "desc_hub": "Доставка и монтаж на резервоари за пропан-бутан в София област. Подземни резервоари 1750 и 2700 л — Мони Терм ЕООД, Костинброд.",
        "lead": "Автономно газоснабдяване с подземни резервоари — доставка, разтоварване, монтаж и връзка към регулаторната група.",
        "detail": "Подбираме обем според консумацията и мястото на обекта. Доставяме резервоари 1750 л и 2700 л, организираме разтоварването и подготовката за подземен монтаж. Често комбинираме с газови трасета и котел.",
        "image": "moni3.jpg",
        "gallery": ["moni3.jpg", "moni10.jpg", "moni2.jpg", "moni16.jpg"],
        "bullets": [
            "Резервоари 1750 л и 2700 л за подземен монтаж",
            "Доставка и разтоварване на обекта",
            "Монтаж и връзка към регулаторна група",
            "Координация с котли и газови трасета",
        ],
        "process": [
            ("Оглед", "Място, достъп за техника и нужен обем."),
            ("Доставка", "Резервоарът пристига на обекта с организирано разтоварване."),
            ("Монтаж", "Подземен монтаж и връзки към системата."),
            ("Готовност", "Проверки преди експлоатация."),
        ],
        "faqs": [
            ("Какъв резервоар ми трябва?", "Зависи от консумацията и пространството. След оглед предлагаме подходящ обем."),
            ("Правите ли подземен монтаж?", "Да — подземни резервоари за пропан-бутан."),
            ("Обслужвате ли Сливница и Драгоман?", "Да — и целия регион около Костинброд."),
        ],
    },
    {
        "slug": "gazovi-trasea",
        "nav": "trasea",
        "name": "Газови трасета",
        "h1_hub": "Изграждане на газови трасета",
        "title_hub": "Газови трасета | София област — Мони Терм",
        "keyword": "газови трасета",
        "keyword_long": "газова тръбна мрежа",
        "desc_hub": "Изграждане на газови трасета в София област. Тръбен път, връзки и изпитания — Мони Терм ЕООД, Костинброд.",
        "lead": "Сигурни външни и вътрешни газови трасета — качествен монтаж и изпитания на тръбния път.",
        "detail": "Изграждаме тръбния път като самостоятелна услуга или като част от цялостна газова инсталация с котел и резервоар. Работният ред е ясен: трасе, връзки, изпитания, координация със следващите монтажни стъпки.",
        "image": "moni8.jpg",
        "gallery": ["moni8.jpg", "moni16.jpg", "moni4.jpg", "moni2.jpg"],
        "bullets": [
            "Външни и вътрешни газови трасета",
            "Качествени материали и чист монтаж",
            "Изпитания на тръбния път",
            "Координация с котли и резервоари",
        ],
        "process": [
            ("Оглед", "Маршрут на трасето и преминавания през стени/плочи."),
            ("Изграждане", "Монтаж на тръбния път и връзките."),
            ("Изпитания", "Проверки преди пускане."),
            ("Свързване", "Координация с котел или резервоар."),
        ],
        "faqs": [
            ("Правите ли само трасето?", "Да — или като част от цялостна газова инсталация."),
            ("Работите ли в София?", "Да — София, Костинброд и София област."),
            ("Как да заявя оглед?", "Обадете се на 0886 391 729."),
        ],
    },
    {
        "slug": "uzakonyavane-gazovi-instalacii",
        "nav": "uzakonyavane",
        "name": "Узаконяване на газови инсталации",
        "h1_hub": "Узаконяване на сградни газови инсталации",
        "title_hub": "Узаконяване на газова инсталация | София област — Мони Терм",
        "keyword": "узаконяване газова инсталация",
        "keyword_long": "узаконяване сградна газова инсталация",
        "desc_hub": "Узаконяване на сградни газови инсталации в София област. Документация и съдействие — Мони Терм ЕООД, Костинброд. Тел. 0886 391 729.",
        "lead": "Съдействие за узаконяване на сградна газова инсталация — ясно какво е нужно и какви са следващите стъпки.",
        "detail": "Тази услуга е за документацията и процеса по узаконяване — не е общ „монтаж на всичко“. Работим самостоятелно или заедно с монтажа на котел, резервоар и трасета, когато обектът го изисква.",
        "image": "moni16.jpg",
        "gallery": ["moni16.jpg", "moni8.jpg", "moni3.jpg"],
        "bullets": [
            "Съдействие за узаконяване на сградни газови инсталации",
            "Координация с нужната документация",
            "Работа в пакет с монтаж или самостоятелно",
            "Ясна комуникация за следващите стъпки",
        ],
        "process": [
            ("Преглед", "Състояние на инсталацията и налични документи."),
            ("План", "Какво липсва и какво да подготвим."),
            ("Документация", "Съдействие по нужните стъпки."),
            ("Координация", "Връзка с монтажа при нужда."),
        ],
        "faqs": [
            ("Узаконявате ли съществуващи инсталации?", "Да — след оглед уточняваме какво е необходимо."),
            ("Комбинирате ли с монтаж?", "Да — често узаконяването е част от цялостния процес."),
            ("Къде работите?", "София и София област."),
        ],
    },
    {
        "slug": "vodni-pompi",
        "nav": "pompi",
        "name": "Водни помпи",
        "h1_hub": "Водни помпи и помпено оборудване",
        "title_hub": "Водни помпи и помпено оборудване | София област — Мони Терм",
        "keyword": "водни помпи",
        "keyword_long": "сондажна помпа монтаж",
        "desc_hub": "Водни помпи и помпено оборудване в София област. Сондажни, напорни и центробежни помпи — Мони Терм ЕООД, Костинброд.",
        "lead": "Подбор и монтаж на помпи за сондаж, кладенец или напорна система — оразмерени за вашия обект.",
        "detail": "Оразмеряваме според дълбочина, дебит и желано налягане. Монтираме сондажни (потопяеми), напорни и центробежни помпи с автоматика и защита от сух ход. Често комбинираме с водопроводно трасе или омекотител.",
        "image": "moni20.jpg",
        "gallery": ["moni20.jpg", "moni12.jpg", "moni5.jpg", "moni19.jpg"],
        "bullets": [
            "Сондажни (потопяеми) помпи",
            "Напорни, центробежни и многостъпални",
            "Автоматика и защита от сух ход",
            "Помпено оборудване за къщи и обекти",
        ],
        "process": [
            ("Данни", "Дълбочина, дебит, налягане, захранване."),
            ("Подбор", "Подходяща помпа и автоматика."),
            ("Монтаж", "Монтаж, връзки и настройки."),
            ("Проверка", "Първо пускане и контрол на работата."),
        ],
        "faqs": [
            ("Как да избера помпа?", "Нужни са дълбочина, дебит и желано налягане. Помагаме с оразмеряване."),
            ("Монтирате ли в София област?", "Да — Костинброд, Сливница, Драгоман, Годеч и наоколо."),
            ("Имате ли наличности?", "Обадете се на 0886 391 729."),
        ],
    },
    {
        "slug": "vodoprovodni-trasea",
        "nav": "voda-trasea",
        "name": "Водопроводни трасета",
        "h1_hub": "Изграждане на водопроводни трасета",
        "title_hub": "Водопроводни трасета | София област — Мони Терм",
        "keyword": "водопроводни трасета",
        "keyword_long": "изграждане водопровод",
        "desc_hub": "Изграждане на нови водопроводни трасета в София област. Тръбни мрежи от източника до обекта — Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Нови водопроводни трасета и тръбни мрежи — от източника до сградата. За локални ремонти вижте ВИК услуги.",
        "detail": "Тази страница е за изграждане на тръбна мрежа (ново трасе), не за дребни ВИК ремонти. Правим външни и вътрешни трасета към сондаж, резервоар или сградна мрежа, с изпитания преди пускане.",
        "image": "moni19.jpg",
        "gallery": ["moni19.jpg", "moni12.jpg", "moni9.jpg", "moni18.jpg"],
        "bullets": [
            "Изграждане на външни и вътрешни водопроводни трасета",
            "Тръбен път към сондаж, резервоар или сградна мрежа",
            "Качествени тръби, фитинги и изпитания",
            "Връзка към помпи и омекотители при нужда",
        ],
        "process": [
            ("Оглед", "Маршрут, дължини и връзки към източника."),
            ("Изграждане", "Тръбен път и фитинги."),
            ("Изпитания", "Проверка преди експлоатация."),
            ("Свързване", "Към помпа, омекотител или сградна мрежа."),
        ],
        "faqs": [
            ("Каква е разликата с ВИК услуги?", "Водопроводните трасета са изграждане на тръбна мрежа. ВИК услугите покриват връзки, ремонти и локални монтажи."),
            ("Правите ли трасе към сондаж?", "Да — често заедно с помпено оборудване."),
            ("Как да заявя?", "0886 391 729"),
        ],
    },
    {
        "slug": "klimatici",
        "nav": "klimatici",
        "name": "Климатици",
        "h1_hub": "Монтаж и доставка на климатици",
        "title_hub": "Монтаж на климатици | София област — Мони Терм",
        "keyword": "монтаж климатик",
        "keyword_long": "доставка климатик монтаж",
        "desc_hub": "Доставка и монтаж на климатици в София област. Професионален монтаж — Мони Терм ЕООД, Костинброд. Тел. 0886 391 729.",
        "lead": "Доставка и монтаж на климатични системи с чисти трасета, вакуумиране и пускане.",
        "detail": "Монтираме вътрешни и външни тела с внимание към отвода, шума и естетиката на трасето. Работим с утвърдени марки — казваме честно какво е подходящо за помещението след кратък оглед.",
        "image": "moni11.jpg",
        "gallery": ["moni11.jpg", "moni13.jpg"],
        "bullets": [
            "Доставка и монтаж на климатици",
            "Монтаж на вътрешни и външни тела",
            "Вакуумиране и пускане",
            "Утвърдени марки",
        ],
        "process": [
            ("Оглед", "Място за вътрешно/външно тяло и трасе."),
            ("Доставка", "Техниката на обекта."),
            ("Монтаж", "Монтаж, вакуумиране, пускане."),
            ("Инструктаж", "Как да ползвате системата ефективно."),
        ],
        "faqs": [
            ("Само монтаж или и доставка?", "И двете — според нуждата."),
            ("Обслужвате ли Банкя и Нови Искър?", "Да."),
            ("Телефон?", "0886 391 729"),
        ],
    },
    {
        "slug": "omekotyavane-na-voda",
        "nav": "soft",
        "name": "Омекотителни системи",
        "h1_hub": "Омекотителни системи за варовита вода",
        "title_hub": "Омекотители за вода | София област — Мони Терм",
        "keyword": "омекотител за вода",
        "keyword_long": "омекотителна система варовита вода",
        "desc_hub": "Омекотителни системи за варовита вода в София област. Монтаж и настройка — Мони Терм ЕООД, Костинброд. Тел. 0886 391 729.",
        "lead": "Защита от варовик за котли, бойлери и уреди — омекотителни системи с правилна настройка.",
        "detail": "Монтираме системи с управляващи глави Clack, предфилтри и солна кутия. Настройваме регенерационните цикли според твърдостта на водата. Особено полезно при газов котел и битова техника.",
        "image": "moni18.jpg",
        "gallery": ["moni18.jpg", "moni9.jpg", "moni19.jpg"],
        "bullets": [
            "Системи за омекотяване на варовита вода",
            "Управляващи глави Clack",
            "Предфилтри и солна кутия",
            "Настройка на регенерационните цикли",
        ],
        "process": [
            ("Оценка", "Твърдост на водата и консумация."),
            ("Подбор", "Подходяща система и място за монтаж."),
            ("Монтаж", "Връзки, солна кутия, настройки."),
            ("Пускане", "Проверка на работата и инструктаж."),
        ],
        "faqs": [
            ("Нужен ли е при газов котел?", "При твърда/варовита вода — силно препоръчителен."),
            ("Какво е Clack?", "Американски производител на управляващи глави за омекотителни системи."),
            ("Монтирате ли в Костинброд и Сливница?", "Да — и в цяла София област."),
        ],
    },
    {
        "slug": "vik-uslugi",
        "nav": "vik",
        "name": "ВИК услуги",
        "h1_hub": "ВИК услуги — връзки, ремонти и локален монтаж",
        "title_hub": "ВИК услуги | София област — Мони Терм",
        "keyword": "ВИК услуги",
        "keyword_long": "ВИК монтаж ремонт",
        "desc_hub": "ВИК услуги в София област: връзки, ремонти и локален монтаж — не магистрални водопроводи. Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Локални ВИК работи на обекта — връзки, арматура, течове и ремонти. За нови тръбни мрежи: водопроводни трасета.",
        "detail": "ВИК тук означава локални работи: връзки, арматура, отстраняване на течове и запушвания, санитарни връзки. Ако ви трябва ново дълго трасе от сондаж или улица — това е услугата водопроводни трасета.",
        "image": "moni19.jpg",
        "gallery": ["moni19.jpg", "moni9.jpg", "moni12.jpg", "moni18.jpg"],
        "bullets": [
            "ВИК връзки и монтаж на арматура",
            "Отстраняване на течове и запушвания",
            "Санитарни и локални водопроводни връзки",
            "Координация с помпи и омекотители при нужда",
        ],
        "process": [
            ("Оглед", "Какъв е проблемът и обхватът."),
            ("Оферта", "Ясен обхват на ремонта/монтажа."),
            ("Изпълнение", "Работа на място."),
            ("Проверка", "Тест и кратко обяснение."),
        ],
        "faqs": [
            ("Каква е разликата с водопроводни трасета?", "ВИК услугите са локални връзки и ремонти. Водопроводните трасета са изграждане на нова тръбна мрежа."),
            ("Работите ли извън Костинброд?", "Да — София и София област."),
            ("Как да се обадя?", "0886 391 729"),
        ],
    },
    {
        "slug": "elektrodifuzno-zavarqvane-pe-hd",
        "nav": "pehd",
        "name": "Електродифузно заваряване РЕ-HD",
        "h1_hub": "Електродифузно заваряване на РЕ-HD полиетилен",
        "title_hub": "Електродифузно заваряване РЕ-HD | Мони Терм",
        "keyword": "електродифузно заваряване",
        "keyword_long": "заваряване РЕ-HD полиетилен",
        "desc_hub": "Електродифузно заваряване на РЕ-HD полиетилен. Мони Терм ЕООД — София област. Подходящо при газови и водопроводни монтажи.",
        "lead": "Надеждни електродифузни съединения на РЕ-HD тръби — част от сигурен монтаж на трасета.",
        "detail": "Използваме електродифузно заваряване там, където са нужни здрави и дълготрайни съединения на полиетиленови тръби. Най-често като част от газови или водопроводни трасета на обекта.",
        "image": "moni5.jpg",
        "gallery": ["moni5.jpg", "moni8.jpg", "moni19.jpg"],
        "bullets": [
            "Електродифузно заваряване на РЕ-HD",
            "За газови и водопроводни трасета",
            "Качествени съединения и контрол",
            "Част от цялостния монтаж на обекта",
        ],
        "process": [
            ("Подготовка", "Тръби, фитинги и място за работа."),
            ("Заваряване", "Електродифузни съединения."),
            ("Контрол", "Проверка на съединенията."),
            ("Интеграция", "Продължение на трасето/монтажа."),
        ],
        "faqs": [
            ("За какво се ползва?", "За надеждни съединения на полиетиленови тръби РЕ-HD."),
            ("Комбинирате ли с газови/водопроводни трасета?", "Да — често като част от монтажа."),
            ("Как да заявя?", "0886 391 729"),
        ],
    },
    {
        "slug": "diamanteno-probivane",
        "nav": "diamant",
        "name": "Диамантено пробиване",
        "h1_hub": "Диамантено пробиване на отвори в стоманобетон",
        "title_hub": "Диамантено пробиване стоманобетон | Мони Терм",
        "keyword": "диамантено пробиване",
        "keyword_long": "диамантено пробиване стоманобетон",
        "desc_hub": "Диамантено пробиване на отвори в стоманобетон за монтажни трасета. Мони Терм ЕООД — София област.",
        "lead": "Прецизни отвори в бетон, камък и стоманобетон при преминаване на газови и водопроводни трасета.",
        "detail": "Пробиваме чисти отвори за тръби през стени и плочи, без да компрометираме конструкцията. Услугата е подготвителна към монтажа — често заедно с газови или ВИК трасета.",
        "image": "moni4.jpg",
        "gallery": ["moni4.jpg", "moni2.jpg", "moni8.jpg"],
        "bullets": [
            "Диамантено пробиване в стоманобетон",
            "Отвори за газови и ВИК трасета",
            "Прецизна работа без компромис с конструкцията",
            "Реални обекти в региона",
        ],
        "process": [
            ("Маркиране", "Къде и с какъв диаметър."),
            ("Пробиване", "Чист отвор в бетона/стоманобетона."),
            ("Почистване", "Готовност за преминаване на тръби."),
            ("Монтаж", "Продължаваме с трасето при нужда."),
        ],
        "faqs": [
            ("За какво служи?", "За чисти отвори при преминаване на тръби през стени и плочи."),
            ("Работите ли в София?", "Да — София и София област."),
            ("Как да заявя?", "0886 391 729"),
        ],
    },
]

# One strong case study per theme (no cluster cannibalization)
PROJECTS = [
    {
        "slug": "gazov-kotel-immergas",
        "title": "Кейс: газов котел Immergas",
        "h1": "Обект — монтаж и настройка на газов котел Immergas",
        "desc": "Кейс Мони Терм: монтаж на газов котел Immergas с програматор — чиста връзка и настройка.",
        "lead": "Чист монтаж, правилна връзка към газовата инсталация и настройка на комфорта.",
        "image": "moni1.jpg",
        "service": "gazovi-kotli",
        "tags": ["газов котел", "Immergas"],
        "fb": FB,
    },
    {
        "slug": "propan-butan-rezervuari-1750-2700",
        "title": "Кейс: подземни резервоари пропан-бутан",
        "h1": "Обект — доставка и подготовка на резервоари 1750 и 2700 л",
        "desc": "Кейс Мони Терм: подземни резервоари пропан-бутан 1750/2700 л — доставка, разтоварване и подготовка за монтаж в София област.",
        "lead": "Автономно газоснабдяване: логистика на тежки резервоари и подготовка за подземен монтаж.",
        "image": "moni3.jpg",
        "service": "rezervuari-propan-butan",
        "tags": ["пропан-бутан", "резервоар"],
        "fb": "https://www.facebook.com/reel/2254654764909341/",
    },
    {
        "slug": "sondazh-pompa-vodochurpene",
        "title": "Кейс: сондажна помпа и първо водочерпене",
        "h1": "Обект — първо водочерпене след монтаж на сондажна помпа",
        "desc": "Кейс Мони Терм: монтаж на сондажна помпа и първо водочерпене — проверка на дебита и системата.",
        "lead": "След монтажа извършваме първото водочерпене — проверка на дебита и работата на системата.",
        "image": "moni20.jpg",
        "service": "vodni-pompi",
        "tags": ["сондажна помпа", "водни помпи"],
        "fb": "https://www.facebook.com/reel/1485212209404773/",
    },
    {
        "slug": "omekotitel-clack-hidrofor",
        "title": "Кейс: омекотител Clack",
        "h1": "Обект — омекотителна система Clack",
        "desc": "Кейс Мони Терм: омекотител Clack с филтри — мека вода и защита за уредите.",
        "lead": "Мека вода и стабилна работа на системата след професионален монтаж и настройка.",
        "image": "moni18.jpg",
        "service": "omekotyavane-na-voda",
        "tags": ["Clack", "омекотител"],
        "fb": FB,
    },
    {
        "slug": "diamanteno-probivane-stomanobeton",
        "title": "Кейс: диамантено пробиване",
        "h1": "Обект — диамантено пробиване в стоманобетон",
        "desc": "Кейс Мони Терм: диамантено пробиване в стоманобетон за преминаване на монтажни трасета.",
        "lead": "Прецизни отвори в стоманобетон при изграждане на газови и водопроводни инсталации.",
        "image": "moni4.jpg",
        "service": "diamanteno-probivane",
        "tags": ["диамантено пробиване", "стоманобетон"],
        "fb": "https://www.facebook.com/reel/755281115161178/",
    },
]


def rel_prefix(depth: int) -> str:
    return "../" * depth if depth else ""


def header(depth: int, current: str = "") -> str:
    p = rel_prefix(depth)

    def cur(key: str) -> str:
        return ' aria-current="page"' if current == key else ""

    svc_links = "\n".join(
        f'          <a href="{p}{s["slug"]}/"{cur(s["nav"])}>{s["name"]}</a>' for s in SERVICES
    )
    return f"""  <a class="skip-link" href="#main">Към съдържанието</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="{p}index.html" aria-label="Мони Терм ЕООД — начало">
        <img src="{p}images/logo.jpg" width="44" height="44" alt="Лого Мони Терм ЕООД">
        <span>Мони Терм<small>ЕООД · Костинброд</small></span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Меню" aria-expanded="false" aria-controls="site-nav">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav" id="site-nav" aria-label="Основна навигация">
        <div class="nav-dd">
          <button type="button" class="nav-dd-toggle" aria-expanded="false" aria-controls="nav-services">Услуги</button>
          <div class="nav-dd-panel" id="nav-services">
{svc_links}
          </div>
        </div>
        <a href="{p}proekti/"{cur("proekti")}>Обекти</a>
        <a href="{p}oferta.html">Оферта</a>
        <a href="{p}kontakt.html">Контакт</a>
        <a class="nav-cta" href="tel:{TEL}">{PHONE}</a>
      </nav>
    </div>
  </header>"""


def footer(depth: int) -> str:
    p = rel_prefix(depth)
    links = "\n".join(
        f'            <li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES
    )
    cities = ", ".join(c["name"] for c in CITIES)
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="logo" href="{p}index.html">
            <img src="{p}images/logo.jpg" width="44" height="44" alt="">
            <span>Мони Терм<small>ЕООД</small></span>
          </a>
          <p style="margin-top:1rem">{ADDRESS}. Газ, вода и монтаж за София и София област.</p>
          <p style="font-size:.85rem;color:var(--muted)">Райони: {cities}.</p>
        </div>
        <div>
          <h3>Услуги</h3>
          <ul>
{links}
            <li><a href="{p}proekti/">Реални обекти</a></li>
          </ul>
        </div>
        <div>
          <h3>Контакт</h3>
          <ul>
            <li><a href="tel:{TEL}">{PHONE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="{p}oferta.html">Безплатна оферта</a></li>
            <li><a href="{p}kontakt.html">Контакт</a></li>
            <li><a href="{FB}" rel="noopener noreferrer" target="_blank">Facebook</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-note">
        <span>© 2026 Мони Терм ЕООД</span>
        <span><a href="{p}llms.txt">llms.txt</a> · <a href="{p}sitemap.xml">Sitemap</a></span>
      </div>
    </div>
  </footer>
  <script src="{p}js/main.js" defer></script>"""


def head_assets(depth: int) -> str:
    p = rel_prefix(depth)
    return f"""  <meta name="theme-color" content="#0c1118">
  <link rel="icon" href="{p}images/logo.jpg" type="image/jpeg">
  <link rel="apple-touch-icon" href="{p}images/logo.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Unbounded:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}css/styles.css">"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("Wrote", path.relative_to(ROOT))


def areas_section(s: dict) -> str:
    extra = HUB_CONTENT[s["slug"]]
    cards = "\n".join(
        f'          <article class="area-card"><h3>{c["name"]}</h3><p>{extra["areas"][c["slug"]]}</p></article>'
        for c in CITIES
    )
    return f"""
    <section class="section section-alt" id="rayoni">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Райони · {s["keyword"]}</p>
          <h2>{s["name"]} в София и София област</h2>
          <p>{extra["local"]}</p>
        </div>
        <div class="areas-grid">
{cards}
        </div>
      </div>
    </section>"""


def hub_process_blurb(s: dict) -> str:
    if s["slug"] == "uzakonyavane-gazovi-instalacii":
        return (
            "Базирани сме в <strong>Костинброд</strong> и обслужваме <strong>София</strong> и "
            "<strong>София област</strong>. Фокусът тук е документацията и узаконяването на сградни газови инсталации."
        )
    return (
        "Базирани сме в <strong>Костинброд</strong> и обслужваме <strong>София</strong> и "
        "<strong>София област</strong>. Поемаме процеса — от оглед и оферта до монтаж и настройка."
    )


def service_hub(s: dict) -> str:
    depth = 1
    p = rel_prefix(depth)
    url = f"{DOMAIN}/{s['slug']}/"
    extra = HUB_CONTENT[s["slug"]]
    related = [pr for pr in PROJECTS if pr["service"] == s["slug"]]
    related_html = ""
    if related:
        items = "\n".join(
            f'            <li><a href="{p}proekti/{pr["slug"]}.html">{pr["title"]}</a></li>'
            for pr in related
        )
        related_html = f"""
          <h2>От реален обект</h2>
          <ul>
{items}
          </ul>"""

    more_html = "\n".join(f"          <p>{para}</p>" for para in extra["more"])
    process_html = "\n".join(
        f'          <article class="process-item"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["process"]
    )
    # Merge base FAQs + price + long-tail city FAQs
    faqs = list(s["faqs"])
    faqs.insert(0, ("Какъв е ценовият ориентир?", extra["price_note"]))
    faqs.append(
        (
            f"Правите ли {s['keyword']} в София и София област?",
            f"Да — база Костинброд. Обслужваме София, Костинброд, Сливница, Драгоман, Годеч, Божурище, Своге, Елин Пелин, Банкя и Нови Искър. Обадете се на {PHONE}.",
        )
    )
    faqs.append(
        (
            f"Има ли разлика за {s['keyword']} в Костинброд и в София?",
            "Обхватът на услугата е същият; в Костинброд реакцията е най-бърза, защото е нашата база. В София планираме достъпа и логистиката предварително.",
        )
    )
    faqs_html = "\n".join(
        f"""          <details><summary>{q}</summary><p>{a}</p></details>""" for q, a in faqs
    )
    faqs_json = ",\n".join(
        json.dumps(
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}},
            ensure_ascii=False,
        )
        for q, a in faqs
    )
    bullets = "\n".join(f"            <li>{b}</li>" for b in s["bullets"])
    gallery = s.get("gallery") or [s["image"]]
    gallery_html = "\n".join(
        f'          <figure><img src="{p}images/{img}" alt="{s["name"]} — Мони Терм" width="800" height="600" loading="lazy"></figure>'
        for img in gallery
    )
    # Prefer thematically related services in sidebar
    related_services = [x for x in SERVICES if x["slug"] != s["slug"]]
    related_svc_html = "\n".join(
        f'            <li><a href="{p}{x["slug"]}/">{x["name"]}</a></li>' for x in related_services
    )

    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{s["title_hub"]}</title>
  <meta name="description" content="{s["desc_hub"]} {extra["price_short"]}.">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="bg_BG">
  <meta property="og:title" content="{s["title_hub"]}">
  <meta property="og:description" content="{s["desc_hub"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/{s["image"]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="{DOMAIN}/images/{s["image"]}">
{head_assets(depth)}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type":"ListItem","position":1,"name":"Начало","item":"{DOMAIN}/"}},
          {{"@type":"ListItem","position":2,"name":"{s["name"]}","item":"{url}"}}
        ]
      }},
      {{
        "@type": "Service",
        "name": "{s["name"]}",
        "serviceType": "{s["keyword"]}",
        "provider": {{
          "@type": "LocalBusiness",
          "name": "Мони Терм ЕООД",
          "telephone": "{TEL}",
          "email": "{EMAIL}",
          "address": {{
            "@type": "PostalAddress",
            "streetAddress": "ул. Славянска",
            "addressLocality": "Костинброд",
            "postalCode": "2230",
            "addressRegion": "София област",
            "addressCountry": "BG"
          }}
        }},
        "areaServed": ["София", "София област", "Костинброд", "Сливница", "Драгоман", "Годеч", "Божурище", "Своге", "Елин Пелин", "Банкя", "Нови Искър"],
        "url": "{url}",
        "description": "{s["desc_hub"]}",
        "image": "{DOMAIN}/images/{s["image"]}"
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [{faqs_json}]
      }}
    ]
  }}
  </script>
</head>
<body>
{header(depth, s["nav"])}
  <main id="main">
    <header class="page-hero">
      <div class="container">
        <nav class="breadcrumbs" aria-label="Breadcrumb">
          <a href="{p}index.html">Начало</a><span aria-hidden="true">/</span><span>{s["name"]}</span>
        </nav>
        <p class="eyebrow">София област · Костинброд · {extra["price_short"]}</p>
        <h1>{s["h1_hub"]}</h1>
        <p class="lead">{s["lead"]}</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-secondary" href="{p}oferta.html">Безплатна оферта</a>
        </div>
      </div>
    </header>

    <section class="section">
      <div class="container content-layout">
        <article class="prose">
          <figure><img src="{p}images/{s["image"]}" alt="{s["name"]} — Мони Терм ЕООД" width="1000" height="700" loading="eager"></figure>
          <h2>Какво включва „{s["keyword"]}“</h2>
          <p>{hub_process_blurb(s)}</p>
          <p>{s["detail"]}</p>
{more_html}
          <ul>
{bullets}
          </ul>
          <h2>Ценови ориентир</h2>
          <p>{extra["price_note"]}</p>
          <p><strong>Какво не е включено / уточняваме честно:</strong> {extra["not_included"]}</p>
          <h2>Как работим</h2>
          <div class="process" style="margin:1.2rem 0 1.5rem">
{process_html}
          </div>
          <h2>Къде работим — {s["keyword"]} по населени места</h2>
          <p>{extra["local"]}</p>
          <h2>От терена</h2>
          <div class="gallery">
{gallery_html}
          </div>
{related_html}
          <h2>Често задавани въпроси</h2>
          <div class="faq">{faqs_html}</div>
        </article>
        <aside class="side-panel">
          <h2>Оглед и оферта</h2>
          <p class="price-chip">{extra["price_short"]}</p>
          <p>{ADDRESS}</p>
          <p class="phone"><a href="tel:{TEL}">{PHONE}</a></p>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <a class="btn btn-primary" href="{p}oferta.html" style="width:100%;margin-bottom:.6rem">Безплатна оферта</a>
          <a class="btn btn-secondary" href="tel:{TEL}" style="width:100%">Обадете се</a>
          <p style="margin-top:1.2rem;font-size:.85rem;color:var(--muted)">Всички услуги</p>
          <ul class="checklist">
{related_svc_html}
          </ul>
          <div class="share-box">
            <label for="share-{s["slug"]}">Споделете</label>
            <input id="share-{s["slug"]}" type="text" readonly data-share-url value="{url}">
          </div>
        </aside>
      </div>
    </section>
{areas_section(s)}
    <section class="cta-band">
      <div class="container">
        <h2>Нуждаете се от {s["name"].lower()}?</h2>
        <p>{extra["price_short"]}. Обадете се или поискайте безплатна оферта — Мони Терм ЕООД, Костинброд.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-cool" href="{p}oferta.html">Безплатна оферта</a>
        </div>
      </div>
    </section>
  </main>
{footer(depth)}
</body>
</html>
"""


def projects_hub() -> str:
    depth = 1
    p = rel_prefix(depth)
    url = f"{DOMAIN}/proekti/"
    cards = "\n".join(
        f"""          <a class="service-link" href="{pr["slug"]}.html">
            <h3>{pr["title"]}</h3>
            <p>{pr["lead"][:140]}</p>
            <span class="arrow">Виж обекта →</span>
          </a>"""
        for pr in PROJECTS
    )
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Реални обекти | Мони Терм ЕООД</title>
  <meta name="description" content="Кейсове от обекти на Мони Терм: газови котли, резервоари пропан-бутан, помпи, омекотители, диамантено пробиване. София област.">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="Реални обекти | Мони Терм">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/moni1.jpg">
{head_assets(depth)}
</head>
<body>
{header(depth, "proekti")}
  <main id="main">
    <header class="page-hero">
      <div class="container">
        <nav class="breadcrumbs"><a href="{p}index.html">Начало</a><span aria-hidden="true">/</span><span>Обекти</span></nav>
        <p class="eyebrow">Кейсове</p>
        <h1>Реални обекти от терена</h1>
        <p class="lead">Доказателства към услугите — не отделни SEO страници за всяка снимка.</p>
      </div>
    </header>
    <section class="section">
      <div class="container">
        <div class="service-grid">
{cards}
        </div>
      </div>
    </section>
    <section class="cta-band">
      <div class="container">
        <h2>Искате подобен обект?</h2>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-cool" href="{p}oferta.html">Безплатна оферта</a>
        </div>
      </div>
    </section>
  </main>
{footer(depth)}
</body>
</html>
"""


def project_page(pr: dict) -> str:
    depth = 1
    p = rel_prefix(depth)
    url = f"{DOMAIN}/proekti/{pr['slug']}.html"
    svc = next((s for s in SERVICES if s["slug"] == pr["service"]), None)
    svc_link = (
        f'<p>Свързана услуга: <a href="{p}{svc["slug"]}/">{svc["name"]}</a></p>' if svc else ""
    )
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{pr["title"]} | Мони Терм</title>
  <meta name="description" content="{pr["desc"]}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{pr["title"]} | Мони Терм">
  <meta property="og:image" content="{DOMAIN}/images/{pr["image"]}">
{head_assets(depth)}
</head>
<body>
{header(depth, "proekti")}
  <main id="main">
    <header class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="{p}index.html">Начало</a><span aria-hidden="true">/</span>
          <a href="./">Обекти</a><span aria-hidden="true">/</span>
          <span>{pr["title"]}</span>
        </nav>
        <p class="eyebrow">{", ".join(pr["tags"])}</p>
        <h1>{pr["h1"]}</h1>
        <p class="lead">{pr["lead"]}</p>
      </div>
    </header>
    <section class="section">
      <div class="container content-layout">
        <div>
          <img src="{p}images/{pr["image"]}" alt="{pr["title"]}" width="1100" height="750" loading="lazy">
        </div>
        <div class="prose">
          <h2>За обекта</h2>
          <p>{pr["desc"]}</p>
          {svc_link}
          <p>Изпълнител: <strong>Мони Терм ЕООД</strong>, Костинброд.</p>
          <p><a href="{pr["fb"]}" target="_blank" rel="noopener noreferrer">Свързана публикация във Facebook →</a></p>
        </div>
      </div>
    </section>
    <section class="cta-band">
      <div class="container">
        <h2>Искате подобен обект?</h2>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-cool" href="{p}oferta.html">Безплатна оферта</a>
        </div>
      </div>
    </section>
  </main>
{footer(depth)}
</body>
</html>
"""


def build_sitemap(urls: list[tuple[str, str, str]]) -> str:
    body = "\n".join(
        f"""  <url>
    <loc>{DOMAIN}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>"""
        for path, freq, prio in urls
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


def main() -> None:
    sitemap_urls: list[tuple[str, str, str]] = [
        ("/", "weekly", "1.0"),
        ("/proekti/", "weekly", "0.8"),
        ("/za-nas.html", "yearly", "0.5"),
        ("/kontakt.html", "yearly", "0.7"),
        ("/oferta.html", "monthly", "0.75"),
        ("/llms.txt", "monthly", "0.2"),
        ("/llms-full.txt", "monthly", "0.2"),
        ("/llms-faq.txt", "monthly", "0.2"),
    ]

    active_slugs = {s["slug"] for s in SERVICES}

    for s in SERVICES:
        write(ROOT / s["slug"] / "index.html", service_hub(s))
        sitemap_urls.append((f"/{s['slug']}/", "monthly", "0.9"))

        # Remove any leftover geo / orphan html inside service folder
        svc_dir = ROOT / s["slug"]
        for f in svc_dir.glob("*.html"):
            if f.name != "index.html":
                f.unlink()
                print("Removed", f.relative_to(ROOT))

        # Remove obsolete root redirect stub if present
        stub = ROOT / f"{s['slug']}.html"
        if stub.exists():
            stub.unlink()
            print("Removed", stub.name)

    # Remove obsolete service folders
    for path in list(ROOT.iterdir()):
        if not path.is_dir():
            continue
        if path.name in {"css", "js", "images", "proekti", "__pycache__"} or path.name.startswith("."):
            continue
        if path.name not in active_slugs:
            shutil.rmtree(path)
            print("Removed dir", path.name)

    for slug in (
        "gazifikaciya",
        "otoplenie",
        "podovo-otoplenie",
        "termopompi",
        "peletni-kotli",
        "hidroforni-sistemi",
        "klimatiizaciya",
        "rezervuari-za-voda",
    ):
        flat = ROOT / f"{slug}.html"
        if flat.exists():
            flat.unlink()
            print("Removed", flat.name)
        legacy_dir = ROOT / slug
        if legacy_dir.is_dir():
            shutil.rmtree(legacy_dir)
            print("Removed dir", slug)

    write(ROOT / "proekti" / "index.html", projects_hub())
    keep_projects = {pr["slug"] for pr in PROJECTS}
    for pr in PROJECTS:
        write(ROOT / "proekti" / f"{pr['slug']}.html", project_page(pr))
        sitemap_urls.append((f"/proekti/{pr['slug']}.html", "monthly", "0.65"))

    proekti_dir = ROOT / "proekti"
    if proekti_dir.exists():
        for f in proekti_dir.glob("*.html"):
            if f.name == "index.html":
                continue
            if f.stem not in keep_projects:
                f.unlink()
                print("Removed", f.relative_to(ROOT))

    write(ROOT / "sitemap.xml", build_sitemap(sitemap_urls))
    print("DONE", len(sitemap_urls), "urls")


if __name__ == "__main__":
    main()
