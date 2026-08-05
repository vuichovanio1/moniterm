# -*- coding: utf-8 -*-
"""Generate Moni Term multi-location service + projects sub-sites."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(r"C:\repos\moniterm")
DOMAIN = "https://vuichovanio1.github.io/moniterm"
BASE = "/moniterm"  # GitHub Pages project path (root-absolute browser URLs)
TEL = "+359886391729"
PHONE = "0886 391 729"
EMAIL = "moni.term@abv.bg"
ADDRESS = "ул. Славянска, 2230 Костинброд"
FB = "https://www.facebook.com/profile.php?id=100063597367628"

CITIES = [
    {"slug": "sofia", "name": "София", "locative": "в София", "genitive": "София", "region": "столицата и околностите"},
    {"slug": "kostinbrod", "name": "Костинброд", "locative": "в Костинброд", "genitive": "Костинброд", "region": "София област"},
    {"slug": "slivnitsa", "name": "Сливница", "locative": "в Сливница", "genitive": "Сливница", "region": "София област"},
    {"slug": "dragoman", "name": "Драгоман", "locative": "в Драгоман", "genitive": "Драгоман", "region": "София област"},
    {"slug": "godech", "name": "Годеч", "locative": "в Годеч", "genitive": "Годеч", "region": "София област"},
    {"slug": "bozhurishte", "name": "Божурище", "locative": "в Божурище", "genitive": "Божурище", "region": "София област"},
    {"slug": "svoge", "name": "Своге", "locative": "в Своге", "genitive": "Своге", "region": "София област"},
    {"slug": "elin-pelin", "name": "Елин Пелин", "locative": "в Елин Пелин", "genitive": "Елин Пелин", "region": "София област"},
    {"slug": "bankya", "name": "Банкя", "locative": "в Банкя", "genitive": "Банкя", "region": "район на София"},
    {"slug": "novi-iskar", "name": "Нови Искър", "locative": "в Нови Искър", "genitive": "Нови Искър", "region": "район на София"},
]

# Unique local notes for geo pages (anti-doorway)
CITY_NOTES = {
    "sofia": "В София често работим по апартаменти и къщи в кварталите с по-лесен достъп за техника; важна е координацията с етажната собственост и паркирането на обекта.",
    "kostinbrod": "Костинброд е нашата база — огледите тук и в близките села са най-бързи, с кратък път за екипа и оборудването.",
    "slivnitsa": "В Сливница и околностите често комбинираме газови или водни работи с оглед в същия ден — удобно разстояние от Костинброд.",
    "dragoman": "Около Драгоман обектите често са къщи и вили; планираме доставка и монтаж според достъпа на терена.",
    "godech": "За Годеч и селата наоколо уточняваме предварително трасето и времето за път, за да приключим монтажа без излишни посещения.",
    "bozhurishte": "Божурище е близо до София — подходящо за бърз оглед и монтаж в работни дни без дълго пътуване.",
    "svoge": "В Своге и по Искърското дефиле отчитаме терена и достъпа; огледът предварително спестява изненади при монтажа.",
    "elin-pelin": "Елин Пелин и индустриалната зона често изискват по-големи мощности или по-дълги трасета — оразмеряваме след оглед.",
    "bankya": "В Банкя преобладават жилищни обекти; работим с внимание към шума и графика на живущите.",
    "novi-iskar": "Нови Искър и северните квартали са удобни за дневен монтаж от Костинброд с ясен прозорец за доставка.",
}

SERVICES = [
    {
        "slug": "gazovi-kotli",
        "nav": "kotli",
        "name": "Газови котли",
        "h1_hub": "Монтаж на газови котли",
        "title_hub": "Монтаж на газов котел | София област — Мони Терм",
        "keyword": "монтаж газов котел",
        "keyword_long": "газов котел монтаж",
        "desc_hub": "Монтаж на газови котли в София и София област. Доставка, връзка към инсталацията и настройка — Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Професионален монтаж на газови котли за домове и обекти в София, Костинброд и региона.",
        "image": "moni1.jpg",
        "gallery": ["moni1.jpg", "moni16.jpg", "moni8.jpg", "moni7.jpg"],
        "bullets": [
            "Доставка и монтаж на газови котли",
            "Връзка към газовата и отоплителната инсталация",
            "Програматори и терморегулация",
            "Пускане и прецизна настройка",
        ],
        "faqs": [
            ("Колко струва монтаж на газов котел?", "Зависи от модела и дали се изгражда нова връзка. Оферта след оглед: 0886 391 729."),
            ("Монтирате ли в София?", "Да — София и цяла София област, с база в Костинброд."),
            ("Работите ли с Immergas?", "Да, монтираме утвърдени марки, включително Immergas."),
        ],
        "geo": True,
    },
    {
        "slug": "rezervuari-propan-butan",
        "nav": "rezervuari",
        "name": "Резервоари пропан-бутан",
        "h1_hub": "Доставка и монтаж на резервоари за пропан-бутан",
        "title_hub": "Резервоари пропан-бутан | София област — Мони Терм",
        "keyword": "резервоар пропан-бутан",
        "keyword_long": "подземен резервоар газ",
        "desc_hub": "Доставка и монтаж на резервоари за пропан-бутан в София и София област. Подземни резервоари 1750 и 2700 л — Мони Терм ЕООД.",
        "lead": "Автономно газоснабдяване с подземни резервоари — доставка, монтаж и подготовка за експлоатация.",
        "image": "moni3.jpg",
        "gallery": ["moni3.jpg", "moni10.jpg", "moni2.jpg", "moni16.jpg"],
        "bullets": [
            "Резервоари 1750 л и 2700 л за подземен монтаж",
            "Доставка и разтоварване на обекта",
            "Монтаж и връзка към регулаторна група",
            "Работим в София и София област",
        ],
        "faqs": [
            ("Какъв резервоар ми трябва?", "Зависи от консумацията и пространството. След оглед предлагаме подходящ обем."),
            ("Правите ли подземен монтаж?", "Да — подземни резервоари за пропан-бутан."),
            ("Обслужвате ли Сливница и Драгоман?", "Да — и целия регион около Костинброд."),
        ],
        "geo": True,
    },
    {
        "slug": "gazovi-trasea",
        "nav": "trasea",
        "name": "Газови трасета",
        "h1_hub": "Изграждане на газови трасета",
        "title_hub": "Газови трасета | София област — Мони Терм",
        "keyword": "газови трасета",
        "keyword_long": "газова тръбна мрежа",
        "desc_hub": "Изграждане на газови трасета в София област. Тръбен път, връзки и изпитания — Мони Терм ЕООД.",
        "lead": "Сигурни газови трасета за сгради и обекти — от проекта до изпълнението на място.",
        "image": "moni8.jpg",
        "gallery": ["moni8.jpg", "moni16.jpg", "moni4.jpg", "moni2.jpg"],
        "bullets": [
            "Външни и вътрешни газови трасета",
            "Качествени материали и чист монтаж",
            "Изпитания на тръбния път",
            "Координация с котли и резервоари",
        ],
        "faqs": [
            ("Правите ли само трасето?", "Да — или като част от цялостна газова инсталация."),
            ("Работите ли в София?", "Да — София, Костинброд и София област."),
            ("Как да заявя оглед?", "Обадете се на 0886 391 729."),
        ],
        "geo": True,
    },
    {
        "slug": "uzakonyavane-gazovi-instalacii",
        "nav": "uzakonyavane",
        "name": "Узаконяване на газови инсталации",
        "h1_hub": "Узаконяване на сградни газови инсталации",
        "title_hub": "Узаконяване на газова инсталация | София област — Мони Терм",
        "keyword": "узаконяване газова инсталация",
        "keyword_long": "узаконяване сградна газова инсталация",
        "desc_hub": "Узаконяване на сградни газови инсталации в София и София област. Документация и съдействие — Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Помагаме да приключите процеса по узаконяване на сградната газова инсталация коректно и навреме.",
        "image": "moni16.jpg",
        "gallery": ["moni16.jpg", "moni8.jpg", "moni3.jpg"],
        "bullets": [
            "Съдействие за узаконяване на сградни газови инсталации",
            "Координация с нужната документация",
            "Работа в пакет с монтаж или самостоятелно",
            "Ясна комуникация за следващите стъпки",
        ],
        "faqs": [
            ("Узаконявате ли съществуващи инсталации?", "Да — след оглед уточняваме какво е необходимо."),
            ("Комбинирате ли с монтаж?", "Да — често узаконяването е част от цялостния процес."),
            ("Къде работите?", "София и София област."),
        ],
        "geo": True,
    },
    {
        "slug": "vodni-pompi",
        "nav": "pompi",
        "name": "Водни помпи",
        "h1_hub": "Водни помпи и помпено оборудване",
        "title_hub": "Водни помпи и помпено оборудване | София област — Мони Терм",
        "keyword": "водни помпи",
        "keyword_long": "сондажна помпа монтаж",
        "desc_hub": "Водни помпи и помпено оборудване в София и София област. Сондажни, напорни и центробежни помпи — Мони Терм ЕООД.",
        "lead": "Подбор и монтаж на помпи за сондаж, кладенец или напорна система — от Костинброд за целия регион.",
        "image": "moni20.jpg",
        "gallery": ["moni20.jpg", "moni12.jpg", "moni5.jpg", "moni19.jpg"],
        "bullets": [
            "Сондажни (потопяеми) помпи",
            "Напорни, центробежни и многостъпални",
            "Автоматика и защита от сух ход",
            "Помпено оборудване за къщи и обекти",
        ],
        "faqs": [
            ("Как да избера помпа?", "Нужни са дълбочина, дебит и желано налягане. Помагаме с оразмеряване."),
            ("Монтирате ли в София област?", "Да — Костинброд, Сливница, Драгоман, Годеч и наоколо."),
            ("Имате ли наличности?", "Обадете се на 0886 391 729."),
        ],
        "geo": True,
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
        "lead": "Нови водопроводни трасета и тръбни мрежи за къщи и обекти — не само локални ВИК връзки.",
        "image": "moni19.jpg",
        "gallery": ["moni19.jpg", "moni12.jpg", "moni9.jpg", "moni18.jpg"],
        "bullets": [
            "Изграждане на външни и вътрешни водопроводни трасета",
            "Тръбен път към сондаж, резервоар или сградна мрежа",
            "Качествени тръби, фитинги и изпитания",
            "Връзка към помпи и омекотители при нужда",
        ],
        "faqs": [
            ("Каква е разликата с ВИК услуги?", "Водопроводните трасета са изграждане на тръбна мрежа. ВИК услугите покриват връзки, ремонти и локални монтажи."),
            ("Правите ли трасе към сондаж?", "Да — често заедно с помпено оборудване."),
            ("Как да заявя?", "0886 391 729"),
        ],
        "geo": True,
    },
    {
        "slug": "klimatici",
        "nav": "klimatici",
        "name": "Климатици",
        "h1_hub": "Монтаж и доставка на климатици",
        "title_hub": "Монтаж на климатици | София област — Мони Терм",
        "keyword": "монтаж климатик",
        "keyword_long": "доставка климатик монтаж",
        "desc_hub": "Доставка и монтаж на климатици в София и София област. Професионален монтаж — Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Доставка и монтаж на климатични системи с чисти трасета и качествено изпълнение.",
        "image": "moni11.jpg",
        "gallery": ["moni11.jpg", "moni13.jpg"],
        "bullets": [
            "Доставка и монтаж на климатици",
            "Монтаж на вътрешни и външни тела",
            "Вакуумиране и пускане",
            "Утвърдени марки",
        ],
        "faqs": [
            ("Само монтаж или и доставка?", "И двете — според нуждата."),
            ("Обслужвате ли Банкя и Нови Искър?", "Да."),
            ("Телефон?", "0886 391 729"),
        ],
        "geo": True,
    },
    {
        "slug": "omekotyavane-na-voda",
        "nav": "soft",
        "name": "Омекотителни системи",
        "h1_hub": "Омекотителни системи за варовита вода",
        "title_hub": "Омекотители за вода | София област — Мони Терм",
        "keyword": "омекотител за вода",
        "keyword_long": "омекотителна система варовита вода",
        "desc_hub": "Омекотителни системи за варовита вода в София област. Монтаж и настройка — Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Защита от варовик за котли, бойлери и уреди — омекотителни системи за София и региона.",
        "image": "moni18.jpg",
        "gallery": ["moni18.jpg", "moni9.jpg", "moni19.jpg"],
        "bullets": [
            "Системи за омекотяване на варовита вода",
            "Управляващи глави Clack",
            "Предфилтри и солна кутия",
            "Настройка на регенерационните цикли",
        ],
        "faqs": [
            ("Нужен ли е при газов котел?", "При твърда/варовита вода — силно препоръчителен."),
            ("Какво е Clack?", "Американски производител на управляващи глави за омекотителни системи."),
            ("Монтирате ли в Костинброд и Сливница?", "Да — и в цяла София област."),
        ],
        "geo": True,
    },
    {
        "slug": "vik-uslugi",
        "nav": "vik",
        "name": "ВИК услуги",
        "h1_hub": "ВИК услуги — връзки, ремонти и локален монтаж",
        "title_hub": "ВИК услуги | София област — Мони Терм",
        "keyword": "ВИК услуги",
        "keyword_long": "ВИК монтаж ремонт",
        "desc_hub": "ВИК услуги в София област: връзки, ремонти и локален монтаж — не изграждане на нови магистрални водопроводи. Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Локални ВИК работи на обекта — връзки, арматура, течове и ремонти. За нови тръбни мрежи вижте водопроводни трасета.",
        "image": "moni19.jpg",
        "gallery": ["moni19.jpg", "moni9.jpg", "moni12.jpg", "moni18.jpg"],
        "bullets": [
            "ВИК връзки и монтаж на арматура",
            "Отстраняване на течове и запушвания",
            "Санитарни и локални водопроводни връзки",
            "Координация с помпи и омекотители при нужда",
        ],
        "faqs": [
            ("Каква е разликата с водопроводни трасета?", "ВИК услугите са локални връзки и ремонти. Водопроводните трасета са изграждане на нова тръбна мрежа."),
            ("Работите ли извън Костинброд?", "Да — София и София област."),
            ("Как да се обадя?", "0886 391 729"),
        ],
        "geo": True,
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
        "lead": "Професионални електродифузни съединения на РЕ-HD тръби за сигурни и дълготрайни инсталации.",
        "image": "moni5.jpg",
        "gallery": ["moni5.jpg", "moni8.jpg", "moni19.jpg"],
        "bullets": [
            "Електродифузно заваряване на РЕ-HD",
            "За газови и водопроводни трасета",
            "Качествени съединения и контрол",
            "Част от цялостния монтаж на обекта",
        ],
        "faqs": [
            ("За какво се ползва?", "За надеждни съединения на полиетиленови тръби РЕ-HD."),
            ("Комбинирате ли с газови/водопроводни трасета?", "Да — често като част от монтажа."),
            ("Как да заявя?", "0886 391 729"),
        ],
        "geo": False,
    },
    {
        "slug": "diamanteno-probivane",
        "nav": "diamant",
        "name": "Диамантено пробиване",
        "h1_hub": "Диамантено пробиване на отвори в стоманобетон",
        "title_hub": "Диамантено пробиване стоманобетон | Мони Терм",
        "keyword": "диамантено пробиване",
        "keyword_long": "диамантено пробиване стоманобетон",
        "desc_hub": "Диамантено пробиване на отвори в стоманобетон за монтажни трасета. Мони Терм ЕООД — София и София област.",
        "lead": "Прецизни отвори в бетон, камък и стоманобетон при изграждане на газови и водопроводни инсталации.",
        "image": "moni4.jpg",
        "gallery": ["moni4.jpg", "moni2.jpg", "moni8.jpg"],
        "bullets": [
            "Диамантено пробиване в стоманобетон",
            "Отвори за газови и ВИК трасета",
            "Прецизна работа без компромис с конструкцията",
            "Реални обекти в региона",
        ],
        "faqs": [
            ("За какво служи?", "За чисти отвори при преминаване на тръби през стени и плочи."),
            ("Работите ли в София?", "Да — София и София област."),
            ("Как да заявя?", "0886 391 729"),
        ],
        "geo": False,
    },
]

PROJECTS = [
    {
        "slug": "sondazh-pompa-vodochurpene",
        "title": "Кейс: сондажна помпа и първо водочерпене",
        "h1": "Обект — първо водочерпене след монтаж на сондажна помпа",
        "desc": "Кейс на Мони Терм: монтаж на сондажна помпа и първо водочерпене на нов сондаж. София област.",
        "lead": "След монтажа на сондажната помпа извършваме първото водочерпене — проверка на дебита и работата на системата.",
        "image": "moni20.jpg",
        "service": "vodni-pompi",
        "tags": ["сондажна помпа", "водни помпи", "София област"],
        "fb": "https://www.facebook.com/reel/1485212209404773/",
    },
    {
        "slug": "propan-butan-rezervuari-1750-2700",
        "title": "Кейс: подземни резервоари 1750 и 2700 л",
        "h1": "Обект — доставка на резервоари пропан-бутан за подземен монтаж",
        "desc": "Кейс Мони Терм: резервоари за пропан-бутан 1750 л и 2700 л за подземен монтаж.",
        "lead": "Автономно газоснабдяване с подземни резервоари — доставка и подготовка за монтаж.",
        "image": "moni3.jpg",
        "service": "rezervuari-propan-butan",
        "tags": ["пропан-бутан", "резервоар"],
        "fb": "https://www.facebook.com/reel/2254654764909341/",
    },
    {
        "slug": "dostavka-rezervuari-2x1750",
        "title": "Кейс: доставка 2×1750 л резервоари",
        "h1": "Обект — доставка и разтоварване на резервоари 1750 литра",
        "desc": "Кейс Мони Терм — доставка и разтоварване на 2 броя резервоари за пропан-бутан по 1750 литра.",
        "lead": "Логистика и разтоварване на тежко оборудване за автономни газови системи.",
        "image": "moni10.jpg",
        "service": "rezervuari-propan-butan",
        "tags": ["пропан-бутан", "доставка"],
        "fb": "https://www.facebook.com/reel/436920692721489/",
    },
    {
        "slug": "podzemni-rezervuari-sedmichna-dostavka",
        "title": "Кейс: седмична доставка подземни резервоари",
        "h1": "Обект — 3×1750 л и 1×2700 л подземни резервоари",
        "desc": "Кейс: доставка на подземни резервоари за пропан-бутан — 3×1750 л и 1×2700 л. Мони Терм ЕООД.",
        "lead": "Редовни доставки на резервоари за обекти с автономно газоснабдяване в София област.",
        "image": "moni10.jpg",
        "service": "rezervuari-propan-butan",
        "tags": ["пропан-бутан", "подземен резервоар"],
        "fb": "https://www.facebook.com/reel/1172502387338331/",
    },
    {
        "slug": "diamanteno-probivane-stomanobeton",
        "title": "Кейс: диамантено пробиване в стоманобетон",
        "h1": "Обект — диамантено пробиване в стоманобетон",
        "desc": "Кейс: диамантено пробиване в стоманобетон за монтажни трасета — Мони Терм ЕООД, София област.",
        "lead": "Прецизни отвори в стоманобетон при изграждане на инсталации.",
        "image": "moni4.jpg",
        "service": "diamanteno-probivane",
        "tags": ["диамантено пробиване", "стоманобетон"],
        "fb": "https://www.facebook.com/reel/755281115161178/",
    },
    {
        "slug": "diamanteno-probivane-otvori",
        "title": "Кейс: отвори с диамантено пробиване",
        "h1": "Обект — пробиване на отвори в бетон, камък и стоманобетон",
        "desc": "Кейс: диамантено пробиване на отвори в бетон, камък и стоманобетон за монтажни трасета.",
        "lead": "Подготвителни работи за чисти и сигурни трасета при монтаж.",
        "image": "moni2.jpg",
        "service": "diamanteno-probivane",
        "tags": ["диамантено пробиване"],
        "fb": "https://www.facebook.com/reel/1216055908828697/",
    },
    {
        "slug": "gazov-kotel-immergas",
        "title": "Кейс: газов котел Immergas",
        "h1": "Обект — монтаж и настройка на газов котел Immergas",
        "desc": "Кейс: професионален монтаж на газов котел Immergas с програматор — реален обект на Мони Терм.",
        "lead": "Чист монтаж, правилна връзка към газовата инсталация и настройка на комфорта.",
        "image": "moni1.jpg",
        "service": "gazovi-kotli",
        "tags": ["газов котел", "Immergas"],
        "fb": FB,
    },
    {
        "slug": "omekotitel-clack-hidrofor",
        "title": "Кейс: омекотител Clack с водоснабдяване",
        "h1": "Обект — омекотителна система Clack",
        "desc": "Кейс: омекотител Clack с филтри и помпена група — Мони Терм ЕООД.",
        "lead": "Мека вода и стабилно налягане в професионално изградена система.",
        "image": "moni18.jpg",
        "service": "omekotyavane-na-voda",
        "tags": ["Clack", "омекотител"],
        "fb": FB,
    },
]


def rel_prefix(depth: int) -> str:
    return "../" * depth if depth else ""


def header(depth: int, current: str = "") -> str:
    p = rel_prefix(depth)

    def cur(key: str) -> str:
        return ' aria-current="page"' if current == key else ""

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
        <a href="{p}gazovi-kotli/"{cur("kotli")}>Газови котли</a>
        <a href="{p}rezervuari-propan-butan/"{cur("rezervuari")}>Резервоари</a>
        <a href="{p}omekotyavane-na-voda/"{cur("soft")}>Омекотяване</a>
        <a href="{p}vodni-pompi/"{cur("pompi")}>Помпи</a>
        <a href="{p}proekti/"{cur("proekti")}>Проекти</a>
        <a href="{p}kontakt.html">Контакт</a>
        <a class="nav-cta" href="tel:{TEL}">{PHONE}</a>
      </nav>
    </div>
  </header>"""


def footer(depth: int, service_slug: str | None = None) -> str:
    p = rel_prefix(depth)
    links = "\n".join(
        f'            <li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES
    )
    geo_svc = next((s for s in SERVICES if s["slug"] == service_slug and s.get("geo")), None)
    if geo_svc:
        cities = " · ".join(
            f'<a href="{p}{geo_svc["slug"]}/{c["slug"]}.html">{c["name"]}</a>' for c in CITIES
        )
        cities_block = f'\n          <p style="margin-top:1rem;font-size:.85rem;color:var(--muted)">Райони: {cities}</p>'
    else:
        cities_block = ""
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="logo" href="{p}index.html">
            <img src="{p}images/logo.jpg" width="44" height="44" alt="">
            <span>Мони Терм<small>ЕООД</small></span>
          </a>
          <p style="margin-top:1rem">{ADDRESS}. Газови котли, резервоари, помпи, климатици и ВИК за София и София област.</p>
        </div>
        <div>
          <h3>Услуги</h3>
          <ul>
{links}
            <li><a href="{p}proekti/">Проекти</a></li>
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
          </ul>{cities_block}
        </div>
      </div>
      <div class="footer-note">
        <span>© 2026 Мони Терм ЕООД</span>
        <span><a href="{p}llms.txt">llms.txt</a> · <a href="{p}sitemap.xml">Sitemap</a></span>
      </div>
    </div>
  </footer>
  <script src="{p}js/main.js" defer></script>"""


def geo_meta_tail(s: dict) -> str:
    if s["slug"] == "uzakonyavane-gazovi-instalacii":
        return f"Документация и узаконяване. Тел. {PHONE}."
    tails = {
        "gazovi-kotli": f"Доставка, монтаж и настройка. Тел. {PHONE}.",
        "rezervuari-propan-butan": f"Доставка и монтаж на резервоар. Тел. {PHONE}.",
        "gazovi-trasea": f"Тръбен път, връзки и изпитания. Тел. {PHONE}.",
        "vodni-pompi": f"Подбор, монтаж и пускане. Тел. {PHONE}.",
        "vodoprovodni-trasea": f"Изграждане на водопроводна мрежа. Тел. {PHONE}.",
        "klimatici": f"Доставка, монтаж и пускане. Тел. {PHONE}.",
        "omekotyavane-na-voda": f"Монтаж и настройка на омекотител. Тел. {PHONE}.",
        "vik-uslugi": f"ВИК връзки, ремонти и локален монтаж. Тел. {PHONE}.",
    }
    return tails.get(s["slug"], f"Оглед, оферта и професионален монтаж. Тел. {PHONE}.")


def geo_include_bullets(s: dict, c: dict) -> list[str]:
    if s["slug"] == "uzakonyavane-gazovi-instalacii":
        return [
            f"Преглед на обекта и документацията {c['locative']}",
            "Подготовка на нужните документи",
            "Съдействие за узаконяване на сградна газова инсталация",
            "Координация с монтажа при нужда",
        ]
    bullets = [
        f"Оглед на обекта {c['locative']}",
        "Индивидуално техническо решение",
        "Доставка, монтаж и пускане",
    ]
    if s["slug"] in ("gazovi-trasea", "gazovi-kotli", "rezervuari-propan-butan"):
        bullets.append("Координация с останалите газови работи на обекта")
    elif s["slug"] == "vodoprovodni-trasea":
        bullets.append("Изпитания на новото водопроводно трасе")
    elif s["slug"] == "vik-uslugi":
        bullets.append("Локални ВИК връзки и ремонти (не магистрални трасета)")
    else:
        bullets.append("Инструктаж след пускане")
    return bullets


def hub_process_blurb(s: dict) -> str:
    if s["slug"] == "uzakonyavane-gazovi-instalacii":
        return (
            "Базирани сме в <strong>Костинброд</strong> и обслужваме <strong>София</strong> и "
            "<strong>София област</strong>. Помагаме с документацията и узаконяването на сградни газови инсталации."
        )
    return (
        "Базирани сме в <strong>Костинброд</strong> и обслужваме <strong>София</strong> и "
        "<strong>София област</strong>. Поемаме процеса — от оглед и оферта до монтаж и настройка."
    )


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


def service_hub(s: dict) -> str:
    depth = 1
    p = rel_prefix(depth)
    url = f"{DOMAIN}/{s['slug']}/"
    geo_links = ""
    if s["geo"]:
        items = "\n".join(
            f'          <a class="service-link" href="{c["slug"]}.html"><h3>{s["name"]} {c["name"]}</h3><p>{s["keyword"].capitalize()} {c["locative"]} — оглед и оферта от Мони Терм.</p><span class="arrow">Отвори →</span></a>'
            for c in CITIES
        )
        geo_links = f"""
    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Локации</p>
          <h2>{s["name"]} по населени места</h2>
          <p>SEO страници за София и София област — изберете вашия град.</p>
        </div>
        <div class="service-grid">
{items}
        </div>
      </div>
    </section>"""

    faqs_html = "\n".join(
        f"""          <details><summary>{q}</summary><p>{a}</p></details>""" for q, a in s["faqs"]
    )
    faqs_json = ",\n".join(
        json.dumps(
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}},
            ensure_ascii=False,
        )
        for q, a in s["faqs"]
    )
    bullets = "\n".join(f"            <li>{b}</li>" for b in s["bullets"])
    gallery = s.get("gallery") or [s["image"]]
    gallery_html = "\n".join(
        f'          <figure><img src="{p}images/{img}" alt="{s["name"]} — Мони Терм" width="800" height="600" loading="lazy"></figure>'
        for img in gallery
    )

    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{s["title_hub"]}</title>
  <meta name="description" content="{s["desc_hub"]}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="bg_BG">
  <meta property="og:title" content="{s["title_hub"]}">
  <meta property="og:description" content="{s["desc_hub"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/logo.jpg">
  <meta name="twitter:image" content="{DOMAIN}/images/logo.jpg">
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
        <p class="eyebrow">София област · Костинброд</p>
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
          <figure><img src="{p}images/{s["image"]}" alt="{s["name"]} — професионален монтаж от Мони Терм" width="1000" height="700" loading="eager"></figure>
          <h2>Защо Мони Терм за „{s["keyword"]}“</h2>
          <p>{hub_process_blurb(s)}</p>
          <ul>
{bullets}
          </ul>
          <h2>От реални обекти</h2>
          <div class="gallery">
{gallery_html}
          </div>
          <h2>Често търсени заявки</h2>
          <p>Оптимизирали сме тази страница за заявки като <strong>{s["keyword"]}</strong>, <strong>{s["keyword_long"]}</strong>, както и комбинации с градовете в региона.</p>
          <h2>Често задавани въпроси</h2>
          <div class="faq">{faqs_html}</div>
        </article>
        <aside class="side-panel">
          <h2>Оглед и оферта</h2>
          <p>{ADDRESS}</p>
          <p class="phone"><a href="tel:{TEL}">{PHONE}</a></p>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <a class="btn btn-primary" href="{p}oferta.html" style="width:100%;margin-bottom:.6rem">Безплатна оферта</a>
          <a class="btn btn-secondary" href="tel:{TEL}" style="width:100%">Обадете се</a>
          <div class="share-box">
            <label for="share-{s["slug"]}">Споделете</label>
            <input id="share-{s["slug"]}" type="text" readonly data-share-url value="{url}">
          </div>
        </aside>
      </div>
    </section>
{geo_links}
    <section class="cta-band">
      <div class="container">
        <h2>Нуждаете се от {s["name"].lower()} в региона?</h2>
        <p>Мони Терм ЕООД — професионално изпълнение и индивидуален подход.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-cool" href="{p}oferta.html">Безплатна оферта</a>
          <a class="btn btn-cool" href="{p}proekti/">Вижте проекти</a>
        </div>
      </div>
    </section>
  </main>
{footer(depth, s["slug"])}
</body>
</html>
"""


def service_geo(s: dict, c: dict) -> str:
    depth = 1
    p = rel_prefix(depth)
    url = f"{DOMAIN}/{s['slug']}/{c['slug']}.html"
    note = CITY_NOTES.get(c["slug"], "")
    if c["slug"] == "sofia":
        title = f"{s['keyword'].capitalize()} в София (столицата) | Мони Терм"
        h1 = f"{s['name']} в София — столицата"
        lead = (
            f"Търсите <strong>{s['keyword']} в София</strong>? Мони Терм ЕООД работи в столицата "
            f"с база в Костинброд — удобно за квартали и крайните зони."
        )
    else:
        title = f"{s['keyword'].capitalize()} {c['name']} | Мони Терм ЕООД"
        h1 = f"{s['name']} {c['locative']}"
        lead = (
            f"Търсите <strong>{s['keyword']} {c['locative']}</strong>? Мони Терм ЕООД предлага "
            f"професионално изпълнение с база в Костинброд — удобно за {c['name']} и съседните населени места."
        )
    desc = f"{s['keyword'].capitalize()} {c['locative']} и региона. Мони Терм ЕООД — Костинброд. {geo_meta_tail(s)}"
    include = "\n".join(f"            <li>{b}</li>" for b in geo_include_bullets(s, c))
    other = "\n".join(
        f'            <li><a href="{x["slug"]}.html">{s["name"]} {x["name"]}</a></li>'
        for x in CITIES
        if x["slug"] != c["slug"]
    )
    if s["slug"] == "vik-uslugi":
        scope = (
            f"За обекти {c['locative']} поемаме локални ВИК връзки, ремонти и монтаж на арматура. "
            f"Нови магистрални водопроводи са отделна услуга — "
            f'<a href="{p}vodoprovodni-trasea/{c["slug"]}.html">водопроводни трасета {c["locative"]}</a>.'
        )
    elif s["slug"] == "vodoprovodni-trasea":
        scope = (
            f"За обекти {c['locative']} изграждаме водопроводни трасета и тръбни мрежи от източника до сградата. "
            f"Локални ремонти и връзки вижте при "
            f'<a href="{p}vik-uslugi/{c["slug"]}.html">ВИК услуги {c["locative"]}</a>.'
        )
    elif s["slug"] == "uzakonyavane-gazovi-instalacii":
        scope = (
            f"За обекти {c['locative']} съдействаме с документацията и узаконяването на сградна газова инсталация. "
            "Работим прозрачно: ясен обхват и координация с монтажа при нужда."
        )
    else:
        scope = (
            f"За обекти {c['locative']} осигуряваме оглед, оферта и изпълнение на {s['name'].lower()}. "
            "Работим прозрачно: ясен обхват, качествено оборудване и настройка до готовност за ползване."
        )
    faqs = [
        (
            f"Правите ли {s['keyword']} {c['locative']}?",
            f"Да. Мони Терм обслужва {c['name']} и {c['region']}. Обадете се на {PHONE}.",
        ),
        (
            "Откъде идва екипът?",
            f"Базата ни е в Костинброд — удобно за {c['name']} и София област.",
        ),
        ("Как се образува цената?", "Индивидуална оферта след оглед на обекта."),
    ]
    if note:
        faqs.insert(
            1,
            (f"Има ли особености {c['locative']}?", note),
        )
    faqs_html = "\n".join(f"""          <details><summary>{q}</summary><p>{a}</p></details>""" for q, a in faqs)
    faqs_json = ",\n".join(
        json.dumps(
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}},
            ensure_ascii=False,
        )
        for q, a in faqs
    )
    note_html = f"<p>{note}</p>" if note else ""

    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/logo.jpg">
  <meta name="twitter:image" content="{DOMAIN}/images/logo.jpg">
{head_assets(depth)}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type":"ListItem","position":1,"name":"Начало","item":"{DOMAIN}/"}},
          {{"@type":"ListItem","position":2,"name":"{s["name"]}","item":"{DOMAIN}/{s["slug"]}/"}},
          {{"@type":"ListItem","position":3,"name":"{c["name"]}","item":"{url}"}}
        ]
      }},
      {{
        "@type": "Service",
        "name": "{s["name"]} {c["name"]}",
        "serviceType": "{s["keyword"]} {c["name"]}",
        "areaServed": {{"@type":"City","name":"{c["name"]}"}},
        "provider": {{"@type":"LocalBusiness","name":"Мони Терм ЕООД","telephone":"{TEL}","url":"{DOMAIN}/"}},
        "url": "{url}",
        "description": "{desc}"
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
          <a href="{p}index.html">Начало</a><span aria-hidden="true">/</span>
          <a href="./">{s["name"]}</a><span aria-hidden="true">/</span>
          <span>{c["name"]}</span>
        </nav>
        <p class="eyebrow">{c["region"]}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-secondary" href="{p}oferta.html">Безплатна оферта</a>
        </div>
      </div>
    </header>

    <section class="section">
      <div class="container content-layout">
        <article class="prose">
          <figure><img src="{p}images/{s["image"]}" alt="{s["name"]} {c["locative"]} — Мони Терм" width="1000" height="700" loading="lazy"></figure>
          <h2>{s["keyword"].capitalize()} {c["locative"]} — какво включваме</h2>
          <p>{scope}</p>
          {note_html}
          <ul>
{include}
          </ul>
          <h2>Защо локална фирма от Костинброд</h2>
          <p>Костинброд е стратегическа точка за София и София област — бърз достъп до {c["name"]} и съседните населени места.</p>
          <h2>Често задавани въпроси</h2>
          <div class="faq">{faqs_html}</div>
        </article>
        <aside class="side-panel">
          <h2>{c["name"]}</h2>
          <p class="phone"><a href="tel:{TEL}">{PHONE}</a></p>
          <a class="btn btn-primary" href="{p}oferta.html" style="width:100%;margin-bottom:.6rem">Безплатна оферта</a>
          <a class="btn btn-secondary" href="tel:{TEL}" style="width:100%">Обадете се</a>
          <p style="margin-top:1.2rem;font-size:.85rem;color:var(--muted)">Също предлагаме:</p>
          <ul class="checklist">
{other}
          </ul>
          <p style="margin-top:1rem"><a href="./">← Всички локации · {s["name"]}</a></p>
        </aside>
      </div>
    </section>

    <section class="cta-band">
      <div class="container">
        <h2>{s["name"]} {c["locative"]} — следваща стъпка</h2>
        <p>Обадете се на Мони Терм ЕООД или поискайте безплатна оферта онлайн.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-cool" href="{p}oferta.html">Безплатна оферта</a>
        </div>
      </div>
    </section>
  </main>
{footer(depth, s["slug"])}
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
            <p>{pr["lead"][:120]}…</p>
            <span class="arrow">Виж проекта →</span>
          </a>"""
        for pr in PROJECTS
    )
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Реални обекти (кейсове) | Мони Терм</title>
  <meta name="description" content="Кейсове от обекти на Мони Терм ЕООД: резервоари пропан-бутан, газови котли, водни помпи, диамантено пробиване. София област.">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="Реални обекти | Мони Терм ЕООД">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/logo.jpg">
  <meta name="twitter:image" content="{DOMAIN}/images/logo.jpg">
{head_assets(depth)}
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"CollectionPage",
    "name":"Реални обекти — Мони Терм ЕООД",
    "url":"{url}",
    "isPartOf":{{"@type":"WebSite","url":"{DOMAIN}/"}}
  }}
  </script>
</head>
<body>
{header(depth, "proekti")}
  <main id="main">
    <header class="page-hero">
      <div class="container">
        <nav class="breadcrumbs"><a href="{p}index.html">Начало</a><span aria-hidden="true">/</span><span>Проекти</span></nav>
        <p class="eyebrow">Кейсове</p>
        <h1>Реални обекти от терена</h1>
        <p class="lead">Кратки кейсове: газови котли, резервоари, помпи и монтажни работи в София област.</p>
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
    tags = ", ".join(pr["tags"])
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{pr["title"]} | Проекти Мони Терм</title>
  <meta name="description" content="{pr["desc"]}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{pr["title"]} | Мони Терм">
  <meta property="og:description" content="{pr["desc"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/logo.jpg">
  <meta name="twitter:image" content="{DOMAIN}/images/logo.jpg">
{head_assets(depth)}
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"CreativeWork",
    "name":"{pr["title"]}",
    "description":"{pr["desc"]}",
    "image":"{DOMAIN}/images/{pr["image"]}",
    "url":"{url}",
    "creator":{{"@type":"Organization","name":"Мони Терм ЕООД"}},
    "about":"{tags}"
  }}
  </script>
</head>
<body>
{header(depth, "proekti")}
  <main id="main">
    <header class="page-hero">
      <div class="container">
        <nav class="breadcrumbs">
          <a href="{p}index.html">Начало</a><span aria-hidden="true">/</span>
          <a href="./">Проекти</a><span aria-hidden="true">/</span>
          <span>{pr["title"]}</span>
        </nav>
        <p class="eyebrow">Проект</p>
        <h1>{pr["h1"]}</h1>
        <p class="lead">{pr["lead"]}</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">Подобен проект — {PHONE}</a>
          <a class="btn btn-secondary" href="{p}{pr["service"]}/">Към услугата</a>
        </div>
      </div>
    </header>
    <section class="section">
      <div class="container split">
        <div class="split-media">
          <img src="{p}images/{pr["image"]}" alt="{pr["title"]}" width="1100" height="750" loading="lazy">
        </div>
        <div class="prose">
          <h2>За обекта</h2>
          <p>{pr["desc"]}</p>
          <p>Изпълнител: <strong>Мони Терм ЕООД</strong>, Костинброд. Работим в София и София област.</p>
          <ul class="checklist">
            <li>Професионален монтаж</li>
            <li>Качествено оборудване</li>
            <li>Индивидуален подход</li>
          </ul>
          <p><a href="{pr["fb"]}" target="_blank" rel="noopener noreferrer">Вижте свързаната публикация във Facebook →</a></p>
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


def redirect_page(path: str) -> str:
    """path is site path like /gazovi-kotli/ (without BASE prefix)."""
    abs_url = f"{DOMAIN}{path}"
    browser = f"{BASE}{path}"
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={browser}">
  <link rel="canonical" href="{abs_url}">
  <title>Преместване…</title>
  <script>location.replace("{browser}");</script>
</head>
<body>
  <p>Страницата е преместена: <a href="{browser}">{abs_url}</a></p>
</body>
</html>
"""


def build_sitemap(urls: list[tuple[str, str, str]]) -> str:
    body = "\n".join(
        f"""  <url>
    <loc>{DOMAIN}{path}</loc>
    <lastmod>2026-07-17</lastmod>
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
        ("/proekti/", "weekly", "0.85"),
        ("/za-nas.html", "yearly", "0.5"),
        ("/kontakt.html", "yearly", "0.7"),
        ("/oferta.html", "monthly", "0.75"),
        ("/llms.txt", "monthly", "0.2"),
        ("/llms-full.txt", "monthly", "0.2"),
        ("/llms-faq.txt", "monthly", "0.2"),
    ]

    active_slugs = {s["slug"] for s in SERVICES}

    # Services
    for s in SERVICES:
        hub_path = ROOT / s["slug"] / "index.html"
        write(hub_path, service_hub(s))
        sitemap_urls.append((f"/{s['slug']}/", "monthly", "0.9"))
        # Convenience redirect: /slug.html → /slug/
        write(ROOT / f"{s['slug']}.html", redirect_page(f"/{s['slug']}/"))
        if s["geo"]:
            keep_cities = {c["slug"] for c in CITIES}
            for c in CITIES:
                write(ROOT / s["slug"] / f"{c['slug']}.html", service_geo(s, c))
                sitemap_urls.append((f"/{s['slug']}/{c['slug']}.html", "monthly", "0.8"))
            svc_dir = ROOT / s["slug"]
            if svc_dir.exists():
                for f in svc_dir.glob("*.html"):
                    if f.name == "index.html":
                        continue
                    if f.stem not in keep_cities:
                        f.unlink()
                        print("Removed", f.relative_to(ROOT))
        else:
            svc_dir = ROOT / s["slug"]
            if svc_dir.exists():
                for f in svc_dir.glob("*.html"):
                    if f.name == "index.html":
                        continue
                    f.unlink()
                    print("Removed", f.relative_to(ROOT))

    # Remove obsolete service folders/files that are not in SERVICES
    for path in ROOT.iterdir():
        if not path.is_dir():
            continue
        if path.name in {"css", "js", "images", "proekti"} or path.name.startswith("."):
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

    # Projects
    write(ROOT / "proekti" / "index.html", projects_hub())
    keep_projects = {pr["slug"] for pr in PROJECTS}
    for pr in PROJECTS:
        write(ROOT / "proekti" / f"{pr['slug']}.html", project_page(pr))
        sitemap_urls.append((f"/proekti/{pr['slug']}.html", "monthly", "0.7"))

    # Remove obsolete project pages
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
