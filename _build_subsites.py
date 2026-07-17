# -*- coding: utf-8 -*-
"""Generate Moni Term multi-location service + projects sub-sites."""
from __future__ import annotations

import json
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
    {"slug": "pernik", "name": "Перник", "locative": "в Перник", "genitive": "Перник", "region": "съседен на София област"},
]

SERVICES = [
    {
        "slug": "gazifikaciya",
        "nav": "gaz",
        "name": "Газификация",
        "h1_hub": "Газификация — природен газ и пропан-бутан",
        "title_hub": "Газификация София и София област | Мони Терм ЕООД",
        "keyword": "газификация",
        "keyword_long": "газификация на къща",
        "desc_hub": "Газификация в София и София област от Мони Терм ЕООД: природен газ и пропан-бутан, проект, монтаж, узаконяване. Костинброд. Тел. 0886 391 729.",
        "lead": "Проектиране, изграждане и узаконяване на газови инсталации — от Костинброд за София, Сливница, Драгоман, Годеч и региона.",
        "image": "moni3.jpg",
        "gallery": ["moni3.jpg", "moni2.jpg", "moni10.jpg", "moni16.jpg"],
        "bullets": [
            "Природен газ и автономни системи с пропан-бутан",
            "Подземни резервоари, регулаторни групи, вътрешни инсталации",
            "Проект, монтаж, узаконяване, пускане и настройка",
            "Работим в София и София област",
        ],
        "faqs": [
            ("Колко струва газификация на къща?", "Цената зависи от трасето, типа газ и обхвата. След оглед Мони Терм дава оферта на 0886 391 729."),
            ("Работите ли извън Костинброд?", "Да — София, Сливница, Драгоман, Годеч, Божурище, Своге, Елин Пелин, Банкя, Нови Искър, Перник и региона."),
            ("Правите ли пропан-бутан?", "Да, включително подземни резервоари 1750 л и 2700 л."),
        ],
        "geo": True,
    },
    {
        "slug": "gazovi-kotli",
        "nav": "gaz",
        "name": "Газови котли",
        "h1_hub": "Доставка и монтаж на газови котли",
        "title_hub": "Монтаж на газов котел София и област | Мони Терм",
        "keyword": "монтаж газов котел",
        "keyword_long": "газов котел монтаж",
        "desc_hub": "Монтаж на газов котел в София и София област. Доставка, автоматизация и настройка от Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Подбор на мощност, професионален монтаж и терморегулация за домове в София и София област.",
        "image": "moni16.jpg",
        "gallery": ["moni16.jpg", "moni1.jpg", "moni8.jpg", "moni7.jpg"],
        "bullets": [
            "Доставка и монтаж на качествени газови котли",
            "Програматори и стайна терморегулация",
            "Връзка към радиатори или подово отопление",
            "Пускане и прецизна настройка",
        ],
        "faqs": [
            ("Колко струва монтаж на газов котел?", "Зависи от модела и дали се изгражда нова инсталация. Оферта след оглед: 0886 391 729."),
            ("Монтирате ли в София?", "Да — София и цяла София област, с база в Костинброд."),
            ("Работите ли с Immergas?", "Да, монтираме утвърдени марки, включително Immergas."),
        ],
        "geo": True,
    },
    {
        "slug": "otoplenie",
        "nav": "heat",
        "name": "Отоплителни инсталации",
        "h1_hub": "Отоплителни инсталации с радиатори",
        "title_hub": "Отоплителни инсталации София област | Мони Терм",
        "keyword": "отоплителни инсталации",
        "keyword_long": "отопление с радиатори",
        "desc_hub": "Отоплителни инсталации с радиатори в София и София област. Проектиране, монтаж и настройка — Мони Терм ЕООД.",
        "lead": "Балансирани отоплителни системи за къщи и обекти в София, Костинброд и региона.",
        "image": "moni8.jpg",
        "gallery": ["moni8.jpg", "moni15.jpg", "moni16.jpg", "moni4.jpg"],
        "bullets": [
            "Проектиране според топлозагубите",
            "Радиатори, тръбна мрежа, балансиране",
            "Връзка към газ, термопомпа или пелети",
            "Нови инсталации и обновяване на стари",
        ],
        "faqs": [
            ("Радиатори или подово?", "Зависи от етапа на строежа и бюджета. Предлагаме и двете, включително хибрид."),
            ("Обслужвате ли София област?", "Да — Костинброд, Сливница, Драгоман, Годеч и съседните населени места."),
            ("Как да заявя оглед?", "Обадете се на 0886 391 729."),
        ],
        "geo": True,
    },
    {
        "slug": "podovo-otoplenie",
        "nav": "heat",
        "name": "Подово отопление",
        "h1_hub": "Подово отопление — равномерен комфорт",
        "title_hub": "Подово отопление София и София област | Мони Терм",
        "keyword": "подово отопление",
        "keyword_long": "подово отопление цена",
        "desc_hub": "Подово отопление в София и София област: проектиране, монтаж, колектори и настройка. Мони Терм ЕООД — 0886 391 729.",
        "lead": "Водни системи за подово отопление за ново строителство и ремонти в София и София област.",
        "image": "moni14.jpg",
        "gallery": ["moni14.jpg", "moni15.jpg", "moni8.jpg"],
        "bullets": [
            "Оразмеряване на кръгове и стъпка",
            "Колекторни групи и автоматика",
            "Отлична комбинация с термопомпа или газов котел",
            "Изпитания и фина настройка",
        ],
        "faqs": [
            ("Колко струва подово отопление?", "Зависи от квадратурата и материалите. Оферта след оглед."),
            ("Работи ли с термопомпа?", "Да — подовото е идеален партньор заради ниската температура на подаване."),
            ("Монтирате ли в Сливница / Драгоман?", "Да, както и в Годеч, Божурище, Своге и целия регион."),
        ],
        "geo": True,
    },
    {
        "slug": "termopompi",
        "nav": "heat",
        "name": "Термопомпи",
        "h1_hub": "Термопомпи въздух–вода",
        "title_hub": "Термопомпа монтаж София и област | Мони Терм",
        "keyword": "термопомпа монтаж",
        "keyword_long": "термопомпа въздух вода",
        "desc_hub": "Монтаж на термопомпи в София и София област. Подбор на мощност, инсталация и настройка — Мони Терм ЕООД.",
        "lead": "Енергийно ефективно отопление и охлаждане за домове в София, Костинброд и региона.",
        "image": "moni13.jpg",
        "gallery": ["moni13.jpg", "moni11.jpg", "moni14.jpg"],
        "bullets": [
            "Подбор според топлозагубите",
            "Монтаж и хидравлична връзка",
            "Хибрид с газов котел при нужда",
            "Оптимизация на режимите",
        ],
        "faqs": [
            ("Колко струва монтаж на термопомпа?", "Зависи от мощността и системата. Оферта на 0886 391 729."),
            ("Подходяща ли е за къща в София област?", "Да — особено при добра изолация и подово отопление."),
            ("Правите ли хибрид газ + термопомпа?", "Да."),
        ],
        "geo": True,
    },
    {
        "slug": "omekotyavane-na-voda",
        "nav": "soft",
        "name": "Омекотяване на вода",
        "h1_hub": "Омекотяване на вода с Clack",
        "title_hub": "Омекотител за вода Clack София област | Мони Терм",
        "keyword": "омекотител за вода",
        "keyword_long": "омекотител Clack",
        "desc_hub": "Омекотител за вода Clack в София и София област. Монтаж и настройка от Мони Терм ЕООД. Тел. 0886 391 729.",
        "lead": "Защита от варовик за котли, бойлери и уреди — системи Clack за София и региона.",
        "image": "moni18.jpg",
        "gallery": ["moni18.jpg", "moni9.jpg", "moni19.jpg"],
        "bullets": [
            "Управляващи глави Clack (САЩ)",
            "Предфилтри и солна кутия",
            "Монтаж с хидрофорни системи",
            "Настройка на регенерационните цикли",
        ],
        "faqs": [
            ("Какво е Clack?", "Американски производител на управляващи глави за омекотителни системи. Работим с тази технология."),
            ("Нужен ли е при газов котел?", "При твърда вода — силно препоръчителен."),
            ("Монтирате ли в Костинброд и Сливница?", "Да — и в цяла София област."),
        ],
        "geo": True,
    },
    {
        "slug": "hidroforni-sistemi",
        "nav": "water",
        "name": "Хидрофорни системи",
        "h1_hub": "Хидрофорни и водоснабдителни системи",
        "title_hub": "Хидрофорна система София област | Мони Терм",
        "keyword": "хидрофорна система",
        "keyword_long": "хидрофор за къща",
        "desc_hub": "Хидрофорни системи в София и София област: помпи, автоматика, резервоари. Мони Терм ЕООД — 0886 391 729.",
        "lead": "Стабилно налягане за къщи и вили със сондаж или автономен водоизточник в София област.",
        "image": "moni12.jpg",
        "gallery": ["moni12.jpg", "moni19.jpg", "moni18.jpg", "moni9.jpg"],
        "bullets": [
            "Помпа + разширителен съд + автоматика",
            "Защита от сух ход",
            "Комбинация с омекотяване Clack",
            "Резервоари и пълна автоматизация",
        ],
        "faqs": [
            ("Каква хидрофорна система ми трябва?", "Зависи от дебита, напора и консумацията. Оразмеряваме след оглед."),
            ("Работите ли в Годеч и Драгоман?", "Да."),
            ("Слагате ли и омекотител?", "Да — често като цялостна водоснабдителна система."),
        ],
        "geo": True,
    },
    {
        "slug": "vodni-pompi",
        "nav": "water",
        "name": "Водни помпи",
        "h1_hub": "Сондажни, напорни и центробежни помпи",
        "title_hub": "Сондажна помпа София област | Мони Терм",
        "keyword": "сондажна помпа",
        "keyword_long": "монтаж сондажна помпа",
        "desc_hub": "Сондажни и центробежни помпи в София и София област. Подбор и монтаж — Мони Терм ЕООД.",
        "lead": "Правилната помпа за вашия сондаж или кладенец — от Костинброд за целия регион.",
        "image": "moni20.jpg",
        "gallery": ["moni20.jpg", "moni12.jpg", "moni5.jpg", "moni19.jpg"],
        "bullets": [
            "Сондажни (потопяеми) помпи",
            "Напорни, центробежни, многостъпални",
            "Автоматика и защита",
            "Реални обекти с първо водочерпене след монтаж",
        ],
        "faqs": [
            ("Как да избера сондажна помпа?", "Нужни са дълбочина, дебит и желано налягане. Помагаме с оразмеряване."),
            ("Монтирате ли в София област?", "Да — Костинброд, Сливница, Драгоман, Годеч и наоколо."),
            ("Имате ли наличности?", "Да — обадете се на 0886 391 729."),
        ],
        "geo": True,
    },
    {
        "slug": "peletni-kotli",
        "nav": "heat",
        "name": "Пелетни съоръжения",
        "h1_hub": "Пелетни котли и съоръжения",
        "title_hub": "Пелетен котел монтаж София област | Мони Терм",
        "keyword": "пелетен котел",
        "keyword_long": "пелетен котел монтаж",
        "desc_hub": "Пелетни котли в София и София област. Монтаж и настройка от Мони Терм ЕООД.",
        "lead": "Автономно отопление на пелети за къщи в София област и региона.",
        "image": "moni7.jpg",
        "gallery": ["moni7.jpg", "moni16.jpg", "moni4.jpg"],
        "bullets": [
            "Подбор на мощност и бункер",
            "Монтаж и димоотвод",
            "Връзка към отоплителна инсталация",
            "Пускане и инструкции",
        ],
        "faqs": [
            ("Пелети или газ?", "Сравняваме вариантите според обекта и цените на горивата."),
            ("Монтирате ли извън Костинброд?", "Да — София и София област."),
            ("Как да заявя?", "0886 391 729"),
        ],
        "geo": False,
    },
    {
        "slug": "klimatiizaciya",
        "nav": "heat",
        "name": "Климатизация",
        "h1_hub": "Климатизация и монтаж на климатици",
        "title_hub": "Климатизация София и София област | Мони Терм",
        "keyword": "климатизация",
        "keyword_long": "монтаж климатик",
        "desc_hub": "Климатизация в София и София област. Професионален монтаж — Мони Терм ЕООД.",
        "lead": "Монтаж на климатични системи с чисти трасета и качествено изпълнение.",
        "image": "moni11.jpg",
        "gallery": ["moni11.jpg", "moni13.jpg"],
        "bullets": [
            "Монтаж на вътрешни и външни тела",
            "Вакуумиране и пускане",
            "Утвърдени марки",
            "Част от цялостния комфорт на дома",
        ],
        "faqs": [
            ("Само климатик или цялостно решение?", "Можем и двете — според нуждата."),
            ("Обслужвате ли Банкя и Нови Искър?", "Да."),
            ("Телефон?", "0886 391 729"),
        ],
        "geo": False,
    },
]

PROJECTS = [
    {
        "slug": "sondazh-pompa-vodochurpene",
        "title": "Сондаж и монтаж на сондажна помпа",
        "h1": "Първо водочерпене след монтаж на сондажна помпа",
        "desc": "Реален проект на Мони Терм: монтаж на сондажна помпа и първо водочерпене на нов сондаж. София област.",
        "lead": "След монтажа на сондажната помпа извършваме първото водочерпене — проверка на дебита и работата на системата.",
        "image": "moni20.jpg",
        "service": "vodni-pompi",
        "tags": ["сондажна помпа", "водоснабдяване", "София област"],
        "fb": "https://www.facebook.com/reel/1485212209404773/",
    },
    {
        "slug": "propan-butan-rezervuari-1750-2700",
        "title": "Подземни резервоари пропан-бутан 1750 и 2700 л",
        "h1": "Доставка на резервоари за пропан-бутан за подземен монтаж",
        "desc": "Проект Мони Терм: резервоари за пропан-бутан 1750 л и 2700 л за подземен монтаж — газификация в София област.",
        "lead": "Автономна газификация с подземни резервоари — доставка и подготовка за монтаж на обекти в региона.",
        "image": "moni3.jpg",
        "service": "gazifikaciya",
        "tags": ["пропан-бутан", "газификация", "резервоар"],
        "fb": "https://www.facebook.com/reel/2254654764909341/",
    },
    {
        "slug": "dostavka-rezervuari-2x1750",
        "title": "Доставка на 2×1750 л резервоари пропан-бутан",
        "h1": "Доставка и разтоварване на резервоари 1750 литра",
        "desc": "Мони Терм — доставка и разтоварване на 2 броя резервоари за пропан-бутан по 1750 литра.",
        "lead": "Логистика и разтоварване на тежко оборудване за автономни газови системи.",
        "image": "moni10.jpg",
        "service": "gazifikaciya",
        "tags": ["пропан-бутан", "доставка"],
        "fb": "https://www.facebook.com/reel/436920692721489/",
    },
    {
        "slug": "podzemni-rezervuari-sedmichna-dostavka",
        "title": "Подземни резервоари — седмична доставка",
        "h1": "3×1750 л и 1×2700 л подземни резервоари",
        "desc": "Доставка на подземни резервоари за пропан-бутан: 3 броя 1750 л и един 2700 л. Мони Терм ЕООД.",
        "lead": "Редовни доставки на резервоари за обекти с автономна газификация в София област.",
        "image": "moni10.jpg",
        "service": "gazifikaciya",
        "tags": ["пропан-бутан", "подземен резервоар"],
        "fb": "https://www.facebook.com/reel/1172502387338331/",
    },
    {
        "slug": "diamanteno-probivane-stomanobeton",
        "title": "Диамантено пробиване в стоманобетон",
        "h1": "Диамантено пробиване в стоманобетон",
        "desc": "Диамантено пробиване в стоманобетон за монтажни трасета — Мони Терм ЕООД, София област.",
        "lead": "Прецизни отвори в стоманобетон при изграждане на инсталации — без компромис с конструкцията.",
        "image": "moni4.jpg",
        "service": "gazifikaciya",
        "tags": ["диамантено пробиване", "монтаж"],
        "fb": "https://www.facebook.com/reel/755281115161178/",
    },
    {
        "slug": "diamanteno-probivane-otvori",
        "title": "Диамантено пробиване на отвори",
        "h1": "Пробиване на отвори в бетон, камък и стоманобетон",
        "desc": "Диамантено пробиване на отвори в бетон, камък и стоманобетон за газови и отоплителни инсталации.",
        "lead": "Подготвителни работи за чисти и сигурни трасета при монтаж.",
        "image": "moni2.jpg",
        "service": "gazifikaciya",
        "tags": ["диамантено пробиване"],
        "fb": "https://www.facebook.com/reel/1216055908828697/",
    },
    {
        "slug": "gazov-kotel-immergas",
        "title": "Монтаж на газов котел Immergas",
        "h1": "Монтаж и настройка на газов котел Immergas",
        "desc": "Професионален монтаж на газов котел Immergas с програматор — реален обект на Мони Терм.",
        "lead": "Чист монтаж, правилна връзка към газовата и отоплителната инсталация и настройка на комфорта.",
        "image": "moni1.jpg",
        "service": "gazovi-kotli",
        "tags": ["газов котел", "Immergas"],
        "fb": FB,
    },
    {
        "slug": "omekotitel-clack-hidrofor",
        "title": "Омекотител Clack с хидрофорна система",
        "h1": "Омекотяване Clack + хидрофор",
        "desc": "Цялостна водоснабдителна система: омекотител Clack, филтри и хидрофор — Мони Терм ЕООД.",
        "lead": "Мека вода и стабилно налягане в една професионално изградена система.",
        "image": "moni18.jpg",
        "service": "omekotyavane-na-voda",
        "tags": ["Clack", "омекотител", "хидрофор"],
        "fb": FB,
    },
    {
        "slug": "podovo-otoplenie-kolektor",
        "title": "Подово отопление с колекторна група",
        "h1": "Изграждане на подово отопление — тръби и колектор",
        "desc": "Реален монтаж на водно подово отопление: системни плоскости, контури и колекторен шкаф. Мони Терм ЕООД.",
        "lead": "Прецизно разположение на контурите и професионална колекторна група за равномерен комфорт.",
        "image": "moni14.jpg",
        "service": "podovo-otoplenie",
        "tags": ["подово отопление", "колектор"],
        "fb": FB,
    },
    {
        "slug": "termopompa-bosch",
        "title": "Външно тяло термопомпа / климатизация Bosch",
        "h1": "Монтаж на външно тяло Bosch",
        "desc": "Професионален монтаж на външно тяло Bosch за отопление и климатизация — Мони Терм ЕООД.",
        "lead": "Качествено оборудване и чист външен монтаж за дълготрайна и тиха работа.",
        "image": "moni13.jpg",
        "service": "termopompi",
        "tags": ["термопомпа", "Bosch"],
        "fb": FB,
    },
    {
        "slug": "hidrofor-grundfos",
        "title": "Хидрофорна система Grundfos",
        "h1": "Хидрофор с помпа Grundfos",
        "desc": "Монтаж на хидрофорна група с помпа Grundfos за стабилно налягане — Мони Терм ЕООД.",
        "lead": "Надеждна автоматика и качествена помпа за автономно водоснабдяване.",
        "image": "moni12.jpg",
        "service": "hidroforni-sistemi",
        "tags": ["хидрофор", "Grundfos"],
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
        <a href="{p}gazifikaciya/"{cur("gaz")}>Газификация</a>
        <a href="{p}podovo-otoplenie/"{cur("heat")}>Подово</a>
        <a href="{p}omekotyavane-na-voda/"{cur("soft")}>Омекотяване</a>
        <a href="{p}hidroforni-sistemi/"{cur("water")}>Вода</a>
        <a href="{p}proekti/"{cur("proekti")}>Проекти</a>
        <a href="{p}kontakt.html">Контакт</a>
        <a class="nav-cta" href="tel:{TEL}">{PHONE}</a>
      </nav>
    </div>
  </header>"""


def footer(depth: int) -> str:
    p = rel_prefix(depth)
    links = "\n".join(
        f'            <li><a href="{p}{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES[:6]
    )
    cities = " · ".join(
        f'<a href="{p}gazifikaciya/{c["slug"]}.html">{c["name"]}</a>' for c in CITIES[:6]
    )
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="logo" href="{p}index.html">
            <img src="{p}images/logo.jpg" width="44" height="44" alt="">
            <span>Мони Терм<small>ЕООД</small></span>
          </a>
          <p style="margin-top:1rem">{ADDRESS}. Газификация, отопление и водоснабдяване за София и София област.</p>
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
            <li><a href="{p}kontakt.html">Контактна страница</a></li>
            <li><a href="{FB}" rel="noopener noreferrer" target="_blank">Facebook</a></li>
          </ul>
          <p style="margin-top:1rem;font-size:.85rem;color:var(--muted)">Райони: {cities}</p>
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
        "areaServed": ["София", "София област", "Костинброд", "Сливница", "Драгоман", "Годеч", "Божурище", "Своге", "Елин Пелин", "Банкя", "Нови Искър", "Перник"],
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
        <p class="eyebrow">София · София област</p>
        <h1>{s["h1_hub"]}</h1>
        <p class="lead">{s["lead"]}</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">Оферта {PHONE}</a>
          <a class="btn btn-secondary" href="{p}kontakt.html">Запитване</a>
        </div>
      </div>
    </header>

    <section class="section">
      <div class="container content-layout">
        <article class="prose">
          <figure><img src="{p}images/{s["image"]}" alt="{s["name"]} — професионален монтаж от Мони Терм" width="1000" height="700" loading="eager"></figure>
          <h2>Защо Мони Терм за „{s["keyword"]}“</h2>
          <p>Базирани сме в <strong>Костинброд</strong> и обслужваме <strong>София</strong> и <strong>София област</strong>. Поемаме целия процес — от оглед и проект до монтаж, узаконяване и настройка.</p>
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
          <a class="btn btn-primary" href="tel:{TEL}" style="width:100%">Обадете се</a>
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
        <h2>Нуждаете се от {s["name"].lower()} {CITIES[0]["locative"]} или в областта?</h2>
        <p>Мони Терм ЕООД — професионално изпълнение и индивидуален подход.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-cool" href="{p}proekti/">Вижте проекти</a>
        </div>
      </div>
    </section>
  </main>
{footer(depth)}
</body>
</html>
"""


def service_geo(s: dict, c: dict) -> str:
    depth = 1
    p = rel_prefix(depth)
    url = f"{DOMAIN}/{s['slug']}/{c['slug']}.html"
    title = f"{s['keyword'].capitalize()} {c['name']} | Мони Терм ЕООД"
    h1 = f"{s['name']} {c['locative']}"
    desc = f"{s['keyword'].capitalize()} {c['locative']} и региона. Мони Терм ЕООД — Костинброд. Проект, монтаж, узаконяване. Тел. {PHONE}."
    other = "\n".join(
        f'            <li><a href="{x["slug"]}.html">{s["name"]} {x["name"]}</a></li>'
        for x in CITIES
        if x["slug"] != c["slug"]
    )
    faqs = [
        (f"Правите ли {s['keyword']} {c['locative']}?", f"Да. Мони Терм обслужва {c['name']} и {c['region']}. Обадете се на {PHONE}."),
        (f"Откъде идва екипът?", "Базата ни е в Костинброд — удобно за София и цяла София област."),
        ("Как се образува цената?", "Индивидуална оферта след оглед на обекта."),
    ]
    faqs_html = "\n".join(f"""          <details><summary>{q}</summary><p>{a}</p></details>""" for q, a in faqs)
    faqs_json = ",\n".join(
        json.dumps(
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}},
            ensure_ascii=False,
        )
        for q, a in faqs
    )

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
        <p class="lead">Търсите <strong>{s["keyword"]} {c["locative"]}</strong>? Мони Терм ЕООД предлага професионално изпълнение с база в Костинброд — удобно за {c["name"]} и съседните населени места.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a>
          <a class="btn btn-secondary" href="{p}kontakt.html">Запитване</a>
        </div>
      </div>
    </header>

    <section class="section">
      <div class="container content-layout">
        <article class="prose">
          <figure><img src="{p}images/{s["image"]}" alt="{s["name"]} {c["locative"]} — Мони Терм" width="1000" height="700" loading="lazy"></figure>
          <h2>{s["keyword"].capitalize()} {c["locative"]} — какво включваме</h2>
          <p>За обекти {c["locative"]} осигуряваме оглед, оферта и изпълнение на {s["name"].lower()}. Работим прозрачно: ясен обхват, качествено оборудване и настройка до готовност за ползване.</p>
          <ul>
            <li>Оглед на обекта {c["locative"]}</li>
            <li>Индивидуално техническо решение</li>
            <li>Доставка, монтаж и пускане</li>
            <li>Узаконяване при нужда</li>
          </ul>
          <h2>Защо локална фирма от Костинброд</h2>
          <p>Костинброд е стратегическа точка за София и София област — бърз достъп до {c["name"]}, Сливница, Драгоман, Годеч и околните села.</p>
          <h2>Често задавани въпроси</h2>
          <div class="faq">{faqs_html}</div>
        </article>
        <aside class="side-panel">
          <h2>{c["name"]}</h2>
          <p class="phone"><a href="tel:{TEL}">{PHONE}</a></p>
          <a class="btn btn-primary" href="tel:{TEL}" style="width:100%">Обадете се</a>
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
        <h2>Оферта за {s["name"].lower()} {c["locative"]}</h2>
        <p>Обадете се на Мони Терм ЕООД.</p>
        <div class="cta-row"><a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a></div>
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
  <title>Проекти | Газификация, отопление и водоснабдяване | Мони Терм</title>
  <meta name="description" content="Реални проекти на Мони Терм ЕООД: сондажни помпи, пропан-бутан резервоари, газови котли, омекотители Clack, диамантено пробиване. София и София област.">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="Проекти | Мони Терм ЕООД">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{DOMAIN}/images/logo.jpg">
  <meta name="twitter:image" content="{DOMAIN}/images/logo.jpg">
{head_assets(depth)}
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"CollectionPage",
    "name":"Проекти — Мони Терм ЕООД",
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
        <p class="eyebrow">Портфолио</p>
        <h1>Реални проекти от терена</h1>
        <p class="lead">Газификация, водоснабдяване, котли и монтажни работи в София и София област — документирани обекти на Мони Терм ЕООД.</p>
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
        <h2>Искате подобен проект?</h2>
        <div class="cta-row"><a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a></div>
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
          <h2>За проекта</h2>
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
        <h2>Искате оферта за подобен обект?</h2>
        <div class="cta-row"><a class="btn btn-primary" href="tel:{TEL}">{PHONE}</a></div>
      </div>
    </section>
  </main>
{footer(depth)}
</body>
</html>
"""


def redirect_page(path: str) -> str:
    """path is site path like /gazifikaciya/ (without BASE prefix)."""
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

    # Services
    for s in SERVICES:
        hub_path = ROOT / s["slug"] / "index.html"
        write(hub_path, service_hub(s))
        sitemap_urls.append((f"/{s['slug']}/", "monthly", "0.9"))
        # redirect old flat file
        old = ROOT / f"{s['slug']}.html"
        write(old, redirect_page(f"/{s['slug']}/"))
        if s["geo"]:
            for c in CITIES:
                write(ROOT / s["slug"] / f"{c['slug']}.html", service_geo(s, c))
                sitemap_urls.append((f"/{s['slug']}/{c['slug']}.html", "monthly", "0.8"))

    # Also redirect rezervuari-za-voda if exists to hidrofor
    write(ROOT / "rezervuari-za-voda.html", redirect_page("/hidroforni-sistemi/"))

    # Projects
    write(ROOT / "proekti" / "index.html", projects_hub())
    for pr in PROJECTS:
        write(ROOT / "proekti" / f"{pr['slug']}.html", project_page(pr))
        sitemap_urls.append((f"/proekti/{pr['slug']}.html", "monthly", "0.7"))

    write(ROOT / "sitemap.xml", build_sitemap(sitemap_urls))
    print("DONE", len(sitemap_urls), "urls")


if __name__ == "__main__":
    main()
