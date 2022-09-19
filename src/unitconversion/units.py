from locale import currency

verb_simple = {"ft": "eru", "et": "er"}
adj_many = {
    "ft_kk_nf": "margir",
    "ft_kvk_nf": "margar",
    "ft_hk_nf": "mörg",
    "ft_kk_þf": "marga",
    "ft_kvk_þf": "margar",
    "ft_hk_þf": "mörg",
}


verb = {
    "et_kk_nf": "er",
    "et_hk_nf": "er",
    "et_kvk_nf": "er",
    "et_kk_þf": "er",
    "ft_hk_nf": "eru",
    "ft_kvk_nf": "eru",
    "ft_kk_nf": "eru",
    "at_af": "eru",
}


volume_units = [
    {
        "et_kk_þgf": "lítra",
        "ft_kk_þgf": "lítrum",
        "et_kk_nf": "lítri",
        "ft_kk_nf": "lítrar",
        "ft_kk_þf": "lítra",
    },
    {
        "et_kk_þgf": "desilítra",
        "ft_kk_þgf": "desilítrum",
        "et_kk_nf": "desilítri",
        "ft_kk_nf": "desilítrar",
        "ft_kk_þf": "desilítra",
    },
    {
        "et_kk_þgf": "sentilítra",
        "ft_kk_þgf": "sentilítrum",
        "et_kk_nf": "sentilítri",
        "ft_kk_nf": "sentilítrar",
        "ft_kk_þf": "sentilítra",
    },
    {
        "et_kk_þgf": "rúmmetra",
        "ft_kk_þgf": "rúmmetrum",
        "et_kk_nf": "rúmmetri",
        "ft_kk_nf": "rúmmetrar",
        "ft_kk_þf": "rúmmetra",
    },
    {
        "et_kk_þgf": "rúmsentimetra",
        "ft_kk_þgf": "rúmsentimetrum",
        "et_kk_nf": "rúmsentímetri",
        "ft_kk_nf": "rúmsentímetrar",
        "ft_kk_þf": "rúmsentímetra",
    },
    {
        "et_kk_þgf": "pela",
        "ft_kk_þgf": "pelum",
        "et_kk_nf": "peli",
        "ft_kk_nf": "pelar",
        "ft_kk_þf": "pela",
    },
    {
        "et_kk_þgf": "bolla",
        "ft_kk_þgf": "bollum",
        "et_kk_nf": "bolli",
        "ft_kk_nf": "bollar",
        "ft_kk_þf": "bolla",
    },
    {
        "et_kvk_þgf": "matskeið",
        "ft_kvk_þgf": "matskeiðum",
        "et_kvk_nf": "matskeið",
        "ft_kvk_nf": "matskeiðar",
        "ft_kvk_þf": "matskeiðar",
    },
    {
        "et_kvk_þgf": "teskeið",
        "ft_kvk_þgf": "teskeiðum",
        "et_kvk_nf": "teskeið",
        "ft_kvk_nf": "teskeiðar",
        "ft_kvk_þf": "teskeiðar",
    },
    {
        "et_kvk_þgf": "könnu",
        "ft_kvk_þgf": "könnum",
        "et_kvk_nf": "únsa",
        "ft_kvk_nf": "únsur",
        "ft_kvk_þf": "únsur",
    },
    {
        "et_kvk_þgf": "könnu",
        "ft_kvk_þgf": "könnum",
        "et_kvk_nf": "kanna",
        "ft_kvk_nf": "könnur",
        "ft_kvk_þf": "könnur",
    },
    {
        "et_hk_þgf": "pinti",
        "ft_hk_þgf": "pintum",
        "et_hk_nf": "pint",
        "ft_hk_nf": "pint",
        "ft_hk_þf": "pint",
    },
]

weight_units = [
    {
        "et_hk_þgf": "pundi",
        "ft_hk_þgf": "pundum",
        "ft_hk_þf": "pund",
        "ft_hk_nf": "pund",
    },
    {
        "et_hk_þgf": "kílógrammi",
        "ft_hk_þgf": "kílógrömmum",
        "ft_hk_þf": "kílógrömm",
        "ft_hk_nf": "kílógrömm",
    },
    {
        "et_hk_þgf": "milligrammi",
        "ft_hk_þgf": "milligrömmum",
        "ft_hk_þf": "milligrömm",
        "ft_hk_nf": "milligrömm",
    },
    {
        "et_hk_þgf": "kílói",
        "ft_hk_þgf": "kílóum",
        "ft_hk_þf": "kíló",
        "ft_hk_nf": "kíló",
    },
    {
        "et_hk_þgf": "grammi",
        "ft_hk_þgf": "grömmum",
        "ft_hk_þf": "grömm",
        "ft_hk_nf": "grömm",
    },
    {
        "et_hk_þgf": "tonni",
        "ft_hk_þgf": "tonnum",
        "ft_hk_þf": "tonn",
        "ft_hk_nf": "tonn",
    },
]


heat_units = ["Celsíus", "Fahrenheit"]

distanace_units = [
    {
        "et_kk_nf": "millimetri",
        "ft_kk_nf": "millimetrar",
        "et_kk_þgf": "millimetra",
        "ft_kk_þgf": "millimetrum",
        "ft_kk_þf": "millimetra",
    },
    {
        "et_kk_nf": "sentimetri",
        "ft_kk_nf": "sentimetrar",
        "et_kk_þgf": "sentimetra",
        "ft_kk_þgf": "sentimetrum",
        "ft_kk_þf": "sentimetra",
    },
    {
        "et_kk_nf": "metri",
        "ft_kk_nf": "metrar",
        "et_kk_þgf": "metra",
        "ft_kk_þgf": "metrum",
        "ft_kk_þf": "metra",
    },
    {
        "et_kk_nf": "kílómetri",
        "ft_kk_nf": "kílómetrar",
        "et_kk_þgf": "kílómetra",
        "ft_kk_þgf": "kílómetrum",
        "ft_kk_þf": "kílómetra",
    },
    {
        "et_kvk_nf": "míla",
        "ft_kvk_nf": "mílur",
        "et_kvk_þgf": "mílu",
        "ft_kvk_þgf": "mílum",
        "ft_kvk_þf": "mílur",
    },
    {
        "et_kvk_nf": "sjómíla",
        "ft_kvk_nf": "sjómílur",
        "et_kvk_þgf": "sjómílu",
        "ft_kvk_þgf": "sjómílum",
        "ft_kvk_þf": "sjómílur",
    },
    {
        "et_kvk_nf": "tomma",
        "ft_kvk_nf": "tommur",
        "et_kvk_þgf": "tommu",
        "ft_kvk_þgf": "tommum",
        "ft_kvk_þf": "tommur",
    },
    {
        "et_hk_þgf": "feti",
        "et_hk_nf": "fet",
        "ft_hk_þgf": "fetum",
        "ft_hk_þf": "fet",
    },
]


currency_units = [
    {
        "et_kk_nf": "bandaríkjadalur",
        "et_kk_þf": "bandaríkjadal",
        "et_kk_þgf_gr": "bandaríkjadalnum",
        "et_kk_þgf": "bandaríkjadal",
        "ft_kk_nf": "bandaríkjadalir",
        "ft_kk_þf": "bandaríkjadali",
        "ft_kk_þgf": "bandaríkjadölum",
    },
    {
        "et_kk_nf": "dalur",
        "et_kk_þf": "dal",
        "et_kk_þgf_gr": "dalnum",
        "et_kk_þgf": "dal",
        "ft_kk_nf": "dalir",
        "ft_kk_þf": "dali",
        "ft_kk_þgf": "dölum",
    },
    {
        "et_kk_nf": "kanadadalur",
        "et_kk_þf": "kanadadal",
        "et_kk_þgf_gr": "kanadadalnum",
        "et_kk_þgf": "kanadadal",
        "ft_kk_nf": "kanadadalir",
        "ft_kk_þf": "kanadali",
        "ft_kk_þgf": "kandadölum",
    },
    {
        "et_kk_nf": "svissneskur franki",
        "et_kk_þf": "svissneskan franka",
        "et_kk_þgf_gr": "svissneskum frankanum",
        "et_kk_þgf": "svissneskum franka",
        "ft_kk_nf": "svissneskir frankar",
        "ft_kk_þf": "svissneska franka",
        "ft_kk_þgf": "svissneskum frönkum",
    },
    {
        "et_kk_nf": "franki",
        "et_kk_þf": "franka",
        "et_kk_þgf_gr": "frankanum",
        "et_kk_þgf": "franka",
        "ft_kk_nf": "frankar",
        "ft_kk_þf": "franka",
        "ft_kk_þgf": "frönkum",
    },
    {
        "et_kk_nf": "ástralskur dalur",
        "et_kk_þf": "ástralskan dal",
        "et_kk_þgf_gr": "ástralska dalnum",
        "et_kk_þgf": "ástralskum dal",
        "ft_kk_nf": "ástralskir dalir",
        "ft_kk_þf": "ástralska dali",
        "ft_kk_þgf": "áströlskum dölum",
    },
    {
        "et_kk_nf": "jamaískur dalur",
        "et_kk_þf": "jamaískan dal",
        "et_kk_þgf_gr": "jamaíska dalnum",
        "et_kk_þgf": "jamískum dal",
        "ft_kk_nf": "jamaískir dalir",
        "ft_kk_þf": "jamaíska dali",
        "ft_kk_þgf": "jamaískum dölum",
    },
    {
        "et_kk_nf": "nýsjálenskur dalur",
        "et_kk_þf": "nýsjálenskan dal",
        "et_kk_þgf_gr": "nýsjálenska dalnum",
        "et_kk_þgf": "nýsjálenskum dal",
        "ft_kk_nf": "nýsjálenskir dalir",
        "ft_kk_þf": "nýsjálenska dali",
        "ft_kk_þgf": "nýsjálenskum dölum",
    },
    {
        "et_kk_nf": "ísraelskur sikill",
        "et_kk_þf": "ísraelskan sikil",
        "et_kk_þgf_gr": "ísraelska siklinum",
        "et_kk_þgf": "ísrelskum sikli",
        "ft_kk_nf": "ísraelskir siklar",
        "ft_kk_þf": "ísraelska sikla",
        "ft_kk_þgf": "ísraelskum siklum",
    },
    {
        "et_kk_nf": "sikill",
        "et_kk_þf": "sikil",
        "et_kk_þgf_gr": "siklinum",
        "et_kk_þgf": "sikli",
        "ft_kk_nf": "siklar",
        "ft_kk_þf": "sikla",
        "ft_kk_þgf": "siklum",
    },
    {
        "et_kk_nf": "súrínamskur dalur",
        "et_kk_þf": "súrínamskan dal",
        "et_kk_þgf_gr": "súrínamska dalnum",
        "et_kk_þgf": "súrínömskum dal",
        "ft_kk_nf": "súrínamskir dalir",
        "ft_kk_þf": "súrínamska dali",
        "ft_kk_þgf": "súrínömskum dölum",
    },
    {
        "et_kk_nf": "hong kong dalur",
        "et_kk_þf": "hong kong dal",
        "et_kk_þgf_gr": "hong kong dalnum",
        "et_kk_þgf": "hong kong dal",
        "ft_kk_nf": "hong kong dalir",
        "ft_kk_þf": "hong kong dali",
        "ft_kk_þgf": "hong kong dölum",
    },
    {
        "et_kk_nf": "singapúrskur dalur",
        "et_kk_þf": "singapúrskan dal",
        "et_kk_þgf_gr": "singapúrska dalnum",
        "et_kk_þgf": "singapúrskum dal",
        "ft_kk_nf": "singapúrskir dalir",
        "ft_kk_þf": "singapúrska dali",
        "ft_kk_þgf": "singapúrskum dölum",
    },
    {
        "et_kk_nf": "mexíkóskur pesi",
        "et_kk_þf": "mexíkóskan pesa",
        "et_kk_þgf_gr": "mexíkóska pesanum",
        "et_kk_þgf": "mexikóskum pesa",
        "ft_kk_nf": "mexíkóskir pesar",
        "ft_kk_þf": "mexíkóska pesa",
        "ft_kk_þgf": "mexíkóskum pesum",
    },
    {
        "et_kk_nf": "pesi",
        "et_kk_þf": "pesa",
        "et_kk_þgf_gr": "pesanum",
        "et_kk_þgf": "pesa",
        "ft_kk_nf": "pesar",
        "ft_kk_þf": "pesa",
        "ft_kk_þgf": "pesum",
    },
    {
        "et_kvk_nf": "indversk rúpía",
        "et_kvk_þf": "indverska rúpíu",
        "et_kvk_þgf_gr": "indversku rúpíunni",
        "et_hvk_þgf": "indverskri rúpíu",
        "ft_kvk_nf": "indverskar rúpíur",
        "ft_kvk_þf": "indverskar rúpíur",
        "ft_kvk_þgf": "indverskum rúpíum",
    },
    {
        "et_kvk_nf": "rúpía",
        "et_kvk_þf": "rúpíu",
        "et_kvk_þgf_gr": "rúpíunni",
        "et_hvk_þgf": "rúpiu",
        "ft_kvk_nf": "rúpíur",
        "ft_kvk_þf": "rúpíur",
        "ft_kvk_þgf": "rúpíum",
    },
    {
        "et_kvk_nf": "króatísk kúna",
        "et_kvk_þf": "króatíska kúnu",
        "et_kvk_þgf_gr": "króatísku kúnunni",
        "et_hvk_þgf": "króatískri kúnu",
        "ft_kvk_nf": "króatískar kúnur",
        "ft_kvk_þf": "króatískar kúnur",
        "ft_kvk_þgf": "króatískum kúnum",
    },
    {
        "et_kvk_nf": "nígerísk næra",
        "et_kvk_þf": "nígeríska næru",
        "et_kvk_þgf_gr": "nígerísku nærunni",
        "et_hvk_þgf": "nígerískri næru",
        "ft_kvk_nf": "nígerískar nærur",
        "ft_kvk_þf": "nígerískar nærur",
        "ft_kvk_þgf": "nígerískum nærum",
    },
    {
        "et_kvk_nf": "ungversk fórinta",
        "et_kvk_þf": "ungverska fórintu",
        "et_kvk_þgf_gr": "ungversku fórintunni",
        "et_hvk_þgf": "ungversku fórintu",
        "ft_kvk_nf": "ungverskar fórintur",
        "ft_kvk_þf": "ungverskar fórintur",
        "ft_kvk_þgf": "ungverskum fórintum",
    },
    {
        "et_kvk_nf": "tékknesk króna",
        "et_kvk_þf": "tékkneska krónu",
        "et_kvk_þgf_gr": "tékknesku krónunni",
        "et_hvk_þgf": "tékkneskri krónu",
        "ft_kvk_nf": "tékkneskar krónur",
        "ft_kvk_þf": "tékkneskar krónur",
        "ft_kvk_þgf": "tékkneskum krónum",
    },
    {
        "et_kvk_nf": "tyrknesk líra",
        "et_kvk_þf": "tyrkneska líru",
        "et_kvk_þgf_gr": "tyrknesku lírunni",
        "et_hvk_þgf": "tyrkneskri líru",
        "ft_kvk_nf": "tyrkneskar lírur",
        "ft_kvk_þf": "tyrkneskar lírur",
        "ft_kvk_þgf": "tyrkneskum lírum",
    },
    {
        "et_kvk_nf": "evra",
        "et_kvk_þf": "evru",
        "et_kvk_þgf_gr": "evrunni",
        "et_hvk_þgf": "evru",
        "ft_kvk_nf": "evrur",
        "ft_kvk_þf": "evrur",
        "ft_kvk_þgf": "evrum",
    },
    {
        "et_kvk_nf": "líra",
        "et_kvk_þf": "líru",
        "et_kvk_þgf_gr": "lírunni",
        "et_hvk_þgf": "líru",
        "ft_kvk_nf": "lírur",
        "ft_kvk_þf": "lírur",
        "ft_kvk_þgf": "lírum",
    },
    {
        "et_kvk_nf": "dönsk króna",
        "et_kvk_þf": "danska krónu",
        "et_kvk_þgf_gr": "dönsku krónunni",
        "et_hvk_þgf": "danskri krónu",
        "ft_kvk_nf": "danskar krónur",
        "ft_kvk_þf": "danskar krónur",
        "ft_kvk_þgf": "dönskum krónum",
    },
    {
        "et_kvk_nf": "norsk króna",
        "et_kvk_þf": "norska krónu",
        "et_kvk_þgf_gr": "norsku krónunni",
        "et_hvk_þgf": "norskri krónu",
        "ft_kvk_nf": "norskar krónur",
        "ft_kvk_þf": "norskar krónur",
        "ft_kvk_þgf": "norskum krónum",
    },
    {
        "et_kvk_nf": "sænsk króna",
        "et_kvk_þf": "sænska krónu",
        "et_kvk_þgf_gr": "sænsku krónunni",
        "et_hvk_þgf": "sænskri krónu",
        "ft_kvk_nf": "sænskar krónur",
        "ft_kvk_þf": "sænskar krónur",
        "ft_kvk_þgf": "sænskum krónum",
    },
    {
        "et_kvk_nf": "króna",
        "et_kvk_þf": "krónu",
        "et_kvk_þgf_gr": "krónunni",
        "et_hvk_þgf": "krónu",
        "ft_kvk_nf": "krónur",
        "ft_kvk_þf": "krónur",
        "ft_kvk_þgf": "krónum",
    },
    {
        "et_hk_nf": "japanskt jen",
        "et_hk_þf": "japanskt jen",
        "et_hk_þgf_gr": "japanska jeninu",
        "et_hk_þgf": "janpönsku jeni",
        "ft_hk_nf": "japönsk jen",
        "ft_hk_þf": "japönsk jen",
        "ft_hk_þgf": "japönskum jenum",
    },
    {
        "et_hk_nf": "jen",
        "et_hk_þf": "jen",
        "et_hk_þgf_gr": "jeninu",
        "et_hk_þgf": "jeni",
        "ft_hk_nf": "jen",
        "ft_hk_þf": "jen",
        "ft_hk_þgf": "jenum",
    },
    {
        "et_hk_nf": "kínverskt júan",
        "et_hk_þf": "kínverskt júan",
        "et_hk_þgf_gr": "kínverska júaninu",
        "et_hk_þgf": "kínversku júani",
        "ft_hk_nf": "kínversk júön",
        "ft_hk_þf": "kínversk júön",
        "ft_hk_þgf": "kínverskum júönum",
    },
    {
        "et_hk_nf": "júan",
        "et_hk_þf": "júan",
        "et_hk_þgf_gr": "júaninu",
        "et_hk_þgf": "júani",
        "ft_hk_nf": "júön",
        "ft_hk_þf": "júön",
        "ft_hk_þgf": "júönum",
    },
    {
        "et_hk_nf": "búlgarskt lef",
        "et_hk_þf": "búlgarskt lef",
        "et_hk_þgf_gr": "búlgarska lefinu",
        "et_hk_þgf": "búlgarísku lefi",
        "ft_hk_nf": "búlgörsk lef",
        "ft_hk_þf": "búlgörsk lef",
        "ft_hk_þgf": "búlgörskum lefum",
    },
    {
        "et_hk_nf": "brasilískt ríal",
        "et_hk_þf": "brasilískt ríal",
        "et_hk_þgf_gr": "brasilíska ríalinu",
        "et_hk_þgf": "brasilísku ríali",
        "ft_hk_nf": "brasilísk ríöl",
        "ft_hk_þf": "brasilísk ríöl",
        "ft_hk_þgf": "brasilískum ríölum",
    },
    {
        "et_hk_nf": "taílenskt bat",
        "et_hk_þf": "taílenskt bat",
        "et_hk_þgf_gr": "taílenska batinu",
        "et_hk_þgf": "taílensku bati",
        "ft_hk_nf": "taílensk böt",
        "ft_hk_þf": "taílensk böt",
        "ft_hk_þgf": "taílenskum bötum",
    },
    {
        "et_hk_nf": "lef",
        "et_hk_þf": "lef",
        "et_hk_þgf_gr": "lefinu",
        "et_hk_þgf": "lefi",
        "ft_hk_nf": "lef",
        "ft_hk_þf": "lef",
        "ft_hk_þgf": "lefum",
    },
    {
        "et_hk_nf": "ríal",
        "et_hk_þf": "ríal",
        "et_hk_þgf_gr": "ríalinu",
        "et_hk_þgf": "ríali",
        "ft_hk_nf": "ríöl",
        "ft_hk_þf": "ríöl",
        "ft_hk_þgf": "ríölum",
    },
    {
        "et_hk_nf": "bat",
        "et_hk_þf": "bat",
        "et_hk_þgf_gr": "batinu",
        "et_hk_þgf": "bati",
        "ft_hk_nf": "böt",
        "ft_hk_þf": "böt",
        "ft_hk_þgf": "bötum",
    },
    {
        "et_hk_nf": "sádiarabískt ríal",
        "et_hk_þf": "sádiarabískt ríal",
        "et_hk_þgf_gr": "sádiarabíska ríalinu",
        "et_hk_þgf": "sádiarabísku ríali",
        "ft_hk_nf": "sádiarabísk ríöl",
        "ft_hk_þf": "sádiarabísk ríöl",
        "ft_hk_þgf": "sádiarabískum ríölum",
    },
    {
        "et_hk_nf": "suðurafrískt rand",
        "et_hk_þf": "suðurafrískt rand",
        "et_hk_þgf_gr": "suðurafríska randinu",
        "et_hk_þgf": "suðurafrísku randi",
        "ft_hk_nf": "suðurafrísk rönd",
        "ft_hk_þf": "suðurafrísk rönd",
        "ft_hk_þgf": "suðurafrískum röndum",
    },
    {
        "et_hk_nf": "sterlingspund",
        "et_hk_þf": "sterlingspund",
        "et_hk_þgf_gr": "sterlingspundinu",
        "et_hk_þgf": "sterlingspundi",
        "ft_hk_nf": "sterlingspund",
        "ft_hk_þf": "sterlingspund",
        "ft_hk_þgf": "sterlingspundum",
    },
    {
        "et_hk_nf": "pund",
        "et_hk_þf": "pund",
        "et_hk_þgf_gr": "pundinu",
        "et_hk_þgf": "pundi",
        "ft_hk_nf": "pund",
        "ft_hk_þf": "pund",
        "ft_hk_þgf": "pundum",
    },
    {
        "et_hk_nf": "pólskt slot",
        "et_hk_þf": "pólskt slot",
        "et_hk_þgf_gr": "pólska slotinu",
        "et_hk_þgf": "pólsku slotti",
        "ft_hk_nf": "pólsk slot",
        "ft_hk_þf": "pólsk slot",
        "ft_hk_þgf": "pólskum slotum",
    },
    {
        "et_hk_nf": "slot",
        "et_hk_þf": "slot",
        "et_hk_þgf_gr": "slotinu",
        "et_hk_þgf": "slotti",
        "ft_hk_nf": "slot",
        "ft_hk_þf": "slot",
        "ft_hk_þgf": "slotum",
    },
    {
        "et_hk_nf": "suðurkóreskt vonn",
        "et_hk_þf": "suðurkóreskt vonn",
        "et_hk_þgf_gr": "suðurkóreska vonninu",
        "et_hk_þgf": "suðurkóresku vonni",
        "ft_hk_nf": "suðurkóresk vonn",
        "ft_hk_þf": "suðurkóresk vonn",
        "ft_hk_þgf": "suðurkóreskum vonnum",
    },
    {
        "et_hk_nf": "vonn",
        "et_hk_þf": "vonn",
        "et_hk_þgf_gr": "vonninu",
        "et_hk_þgf": "vonni",
        "ft_hk_nf": "vonn",
        "ft_hk_þf": "vonn",
        "ft_hk_þgf": "vonnum",
    },
]
