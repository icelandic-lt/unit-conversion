# unit-conversion
This repo contains scripts that can be used to create text intended for language models for ASR in Icelandic. In the file, `src/unitconversion/sentences.py` are modules that are used to define the sentence and state what inflections are expected for each word. The file `src/unitconversion/units.py` contains lists for each task where each word along with the inflection is stored. The main script loops through an input file containing numbers and generates sentences using each number with correct inflection. 

Examples of sentences generated.

Distance conversion:
```
Hversu margar tommur eru í núll komma þrem kílómetrum?
Hversu margir sentimetrar eru í fjögur hundruð fjörutíu og fjórum kílómetrum?
```
Volume conversion:
```
Hvað eru fjögur hundruð og fimmtíu grömm mörg kílógröm?
Hvað eru sjö hundruð fimmtíu og níu desilítrar margir peli?
```

Currency conversion:
```
Hversu margar íslenskar krónur fæ ég fyrir einn dollar?
Hvað er einn dalur margir mexíkóskir pesar?
```

The PIP package [Númi](https://pypi.org/project/numi/) is an offspring off the number generation script found in `generate_numbers`.


# Setup


Run the following to setup:
```
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
```

To use the script call `src/unitconversion/main.py` and provide an input file. E.g:

```
python3 src/unitconversion/main.py input/ints_1.tsv
```


# Acknowledgements
This project was funded by the Language Technology Programme for Icelandic 2019-2023. The programme, which is managed and coordinated by Almannarómur, is funded by the Icelandic Ministry of Education, Science and Culture.
