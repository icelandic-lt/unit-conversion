#!/usr/bin/env python3

curr = [
    "abkasískt apsar",
    "afganskur afgani",
    "albanskt lek",
    "Alderney pund",
    "alsírskur denari",
    "angólsk kvansa",
    "arabískt dírham",
    "argentínskur pesói",
    "aríari",
    "armenskt dramm",
    "artsakst dramm",
    "Arúbaflórína",
    "Ascension-pund",
    "aserskt manat",
    "ástralskur dalur",
    "austkarabískur dalur",
    "bahamskur dalur",
    "balbói",
    "Bandaríkjadalur",
    "bangladessnesk taka",
    "barbadoskur dalur",
    "bareinskur denari",
    "bat",
    "belískur dalur",
    "Bermúdadalur",
    "bólívari",
    "bólivískur bólivíani",
    "botsvönsk púla",
    "brasilískt ríal",
    "breskt pund",
    "Bresku Jómfrúaeyjadalur",
    "brúneiskur dalur",
    "búlgarískt lef",
    "búrúndískur franki",
    "bútanskt ngultrum",
    "caymaneyskur dalur",
    "Cookseyjadalur",
    "djíbútískur franki",
    "dóbra",
    "dóminískur pesi",
    "dong",
    "dönsk króna",
    "egypskt pund",
    "eritreönsk nakfa",
    "evra" "evra",
    "eþíópískt birr",
    "færeysk króna",
    "Falklandseyjapund",
    "fídjeyskur dalur",
    "filippeyskur pesi",
    "gambískur dalasi",
    "georgískur lari",
    "Gíbraltarspund",
    "Gíneufranki",
    "grænhöfðeyskur skúti",
    "Guernseyjarpund",
    "gúrdi",
    "gvæjanskur dalur",
    "gvaraní",
    "helenskt pund",
    "hollenskt Antillugyllini",
    "Hong Kong-dalur",
    "hvítrússnesk rúbla",
    "indónesísk rúpía",
    "indversk rúpía",
    "írakskur denari",
    "íranskt ríal",
    "íslensk króna",
    "jamaískur dalur",
    "japanskt jen",
    "jemenskt ríal",
    "Jerseyjarpund",
    "jórdanskur denari",
    "kambódískt ríal",
    "kanadískur dalur",
    "kasakst tengi",
    "katarskt ríal",
    "kenískur skildingur",
    "kína",
    "kínverskt juan",
    "kínverskt júan",
    "kip",
    "Kíribatídalur",
    "kjat",
    "kólumbískur pesi",
    "kómoreyskur franki",
    "kongóskur franki",
    "kordóva",
    "kostraríkst kólon",
    "króatísk kúna",
    "kúbverskur pesi",
    "kúveiskur denari",
    "kvetsal",
    "kyrrahafsfranki",
    "lempíra",
    "líbanskt pund",
    "líberískur dalur",
    "líbískur denari",
    "lílangeni",
    "ljóna",
    "loti",
    "makedónskur denari",
    "malavísk kvaka",
    "maldíveysk rúpía",
    "Manarpund",
    "máritísk rúpía",
    "marrokóskt dírham",
    "metikal",
    "mexíkóskur pesi",
    "miðafrískur franki",
    "míkrónesískur dalur",
    "moldavískt lei",
    "næra",
    "namibískur dalur",
    "nárúskur dalur",
    "nepölsk rúpía",
    "Niuedalur",
    "norðurkóreskt vonn",
    "norsk króna",
    "nýi ísraelski sikill",
    "nýi taívanskur dalur",
    "nýsjálenskur dalur",
    "ómanskt ríal",
    "pakistönsk rúpía",
    "Palá-dalur",
    "panga",
    "pataka",
    "Pitcairn-dalur",
    "pólskt slot",
    "púla",
    "ringit",
    "rúandskur franki",
    "rúmenskt lei",
    "rússnesk rúbla",
    "sádiarabískt ríal",
    "sænsk króna",
    "saharapeseta",
    "Salómonseyjadalur",
    "sambísk kvaka",
    "Sankti-Helenapund",
    "sedi",
    "serbneskur denari",
    "Seychellesrúpía",
    "síleskur pesi",
    "singapúrskur dalur",
    "skiptanlegurkúbverskur pesi",
    "sól",
    "som",
    "sómalílandsskildingur",
    "sómalískur skildingur",
    "somóni",
    "srílönsk rúpía",
    "súdanskt pund",
    "suðurafrískt rand",
    "Suður-Georgíu og Suður-Sandvíkureyjapund",
    "suðurkóreskt vonn",
    "suðursúdanskt pund",
    "súm",
    "súrínamskur dalur",
    "svissneskur franki",
    "sýrlenskt pund",
    "tala",
    "tansanískur skildingur",
    "tékknesk króna",
    "transnistrísk rúbla",
    "Trínidad og Tóbagó-dalur",
    # "Tristan da Cunha-pund",
    "túniskur denari",
    "túríkur",
    "túrkmenskt manat",
    "Túvalúdalur",
    "tyrknesk líra",
    "úgandskur skildingur",
    "úgía",
    "úkraínsk hrinja",
    "ungversk fórinta",
    "úrúgvæskur pesi",
    "vatú",
    "vestafrískur franki",
]


sedlabanki = [
    "Bandaríkjadalur",
    "Sterlingspund",
    "Kanadadalur",
    "Dönsk króna",
    "Norsk króna",
    "Sænsk króna",
    "Svissneskur franki",
    "Japanskt jen",
    "SDR",
    "Evra",
    "Kínverskt júan",
    "Ný-Sjálenskur dalur",
    "Ástralíudalur",
    "Hong Kong dalur",
    "Suður-Afrískt rand",
    "Tékknesk króna",
    "Ungversk forinta",
    "Tyrknesk líra",
    "Króatísk kúna",
    "Pólskt slot",
    "Nígerísk næra",
    "Tævanskur dalur",
    "Suðurkóreskt vonn",
    "Súrinamskur dalur",
    "Ísraelskur sikill",
    "Singapúrskur dalur",
    "Mexíkóskur pesi",
    "Indversk rúpía",
    "Búlgarskt lef",
    "Brasilískt ríal",
    "Taílenskt bat",
    "Jamaískur dalur",
    "Sádi-arabískt ríal",
]

curryes = [
    ["Danskur króna", "kvk"],
    ["Norskur króna", "kvk"],
    ["Sænskur króna", "kvk"],
    ["Svissneskur franki", "kk"],
    ["Japanskur jen", "hk"],
    ["Kínverskur júan", "hk"],
    ["Nýsjálenskur dalur", "kk"],
    ["Tékkneskur króna", "kvk"],
    ["Tyrkneskur líra", "kvk"],
    ["Pólskur slot", "hk"],
    ["Suðurkóreskur vonn", "hk"],
    ["Ísraelskur sikill", "kk"],
    ["Singapúrskur dalur", "kk"],
    ["Mexíkóskur pesi", "kk"],
    ["Indverskur rúpía", "kvk"],
    ["Búlgarskur lef", "hk"],
    ["Brasilískur ríal", "hk"],
    ["Taílenskur bat", "hk"],
    ["Jamaískur dalur", "kk"],
    ["sádi-arabískur ríal", "hk"],
    ["suður-afrískur ríal", "hk"],
    ["Ástralskur dalur", "kk"],
    ["Nígerískur rúpía", "kvk"],
    ["Súrínamskur dalur", "kk"],
    ["Ungverskur fórinta", "kvk"],
]


def load_bin(path="SHsnid.csv"):

    out = {}
    with open(path) as f_in:
        for line in f_in:
            line = line.rstrip()
            line = line.split(";")
            word = line[0].lower()
            if word in out:
                out[word][line[5]] = line[4]
            else:
                out[word] = {line[5]: line[4]}
    return out


def run():
    from reynir import Greynir
    from reynir import NounPhrase as Nl

    load_bin()
    with open("out2", "w") as f_out:
        f_out.write("nf\tþf\tþgf\tef")

        g = Greynir()
        for line in sedlabanki:
            sent = g.parse_single(line)
            out = []
            if sent.terminals:
                for t in sent.terminals:
                    out.append(
                        "{0}:{1}:{2}".format(t.text, t.category, ", ".join(t.variants))
                    )

            # f_out.write(str(sent) + ":" + ":".join(out) + "\n")
            nl = Nl(line)
            f_out.write("{nl:nf}\t{nl:þf}\t{nl:þgf}\t{nl:ef}".format(nl=nl) + "\n")


def run2():
    bin = load_bin()
    for line in curryes:
        gender = line[1]
        line = line[0].lower()
        adj, noun = line.split(" ")
        s = gender + ":"
        for a, b in zip(
            ["NFET", "ÞFET", "ÞGFETgr", "NFFT", "ÞFFT", "ÞGFFT"],
            ["FSB-NFET", "FSB-ÞFET", "FVB-ÞGFET", "FSB-NFFT", "FSB-ÞFFT", "FSB-ÞGFFT"],
        ):
            b = b.split("-")
            s = (
                s
                + bin[adj][f"{b[0]}-{gender.upper()}-{b[1]}"]
                + " "
                + bin[noun][a]
                + ":"
            )
        print(s)


def run3():
    curr = []
    with open("Gjaldmiðlar - Sheet4.csv") as f_in:
        for line in f_in:
            line = line.rstrip().split(",")
            curr.append(line)

    curr = curr[2:]

    curr_new = []
    for line in curr[1:]:
        t = {}
        for idx, word in enumerate(line):
            if word:
                t[curr[0][idx]] = word.lower()
        curr_new.append(t)

    with open("curr.tsv", "w") as f_out:
        for line in curr_new:
            print(line)
            # f_out.swrite(line[0] + "\t" + line[1] + "\n")


if __name__ == "__main__":
    # run()
    # run2()
    run3()
