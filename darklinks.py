darklist = {
    'Докс/осинт/пасты': {
        'https://probiv.my/',
        'doxbin.com',
        'doxbin.org',
        'pastebim.com'
    },

    "Поисковики": {
        "Torch": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
        "Danex": "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/",
        "Sentor": "http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/",
        "Hidden Answers": "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/",
        "riseup searx": "http://ozmh2zkwx5cjuzopui64csb5ertcooi5vya6c2gm4e3vcvf2c2qvjiyd.onion/",
    },
    "Крипта": {
        "Dark Mixer": "http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/",
        "Mixabit": "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/",
        "EasyCoin": "http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/",
        "Onionwallet": "http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/",
        "VirginBitcoin": "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/",
        "Cryptostamps": "http://lgh3eosuqrrtvwx3s4nurujcqrm53ba5vqsbim5k5ntdpo33qkl7buyd.onion/",
    },
    "Стрессеры(Ddos)": {
        "Stresser": "http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/",
    },

    "ДаркнетВики": {
        "Hidden Wiki": "http://wikitjerrta4qgz4.onion/",
        "Deep Web Wiki": "http://wikicbtbf7rgjjbqe.onion/",
    },

}

def print_darklist(darklist):
    for category, links in darklist.items():
        print(f"Категория: {category}")
        if isinstance(links, dict):
            for key, value in links.items():
                print(f"  {key}: {value}")
        elif isinstance(links, set):
            for link in links:
                print(f"  {link}")
        print()