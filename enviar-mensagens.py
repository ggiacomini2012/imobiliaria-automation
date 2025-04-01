import pywhatkit as kit
import time
import pyautogui
import json
from datetime import datetime
import random
import pyperclip
# Nome do arquivo JSON que armazena o log de envios
LOG_FILE = "log.json"

# Carrega os contatos a serem enviados
cleaned_contacts2 = [
    {
        "phone_number": "554796418638",
        "public_name": "Abreu"
    },
    {
        "phone_number": "554791879787",
        "public_name": "Joao"
    },
    {
        "phone_number": "554792052010",
        "public_name": "Suzane"
    },
    {
        "phone_number": "554591580658",
        "public_name": "Flavia"
    },
    {
        "phone_number": "555499182156",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554797588085",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554196546898",
        "public_name": "Evellyn"
    },
    {
        "phone_number": "554784145260",
        "public_name": "Michel"
    },
    {
        "phone_number": "554799720525",
        "public_name": "Jorge"
    },
    {
        "phone_number": "554799508778",
        "public_name": "Miguel"
    },
    {
        "phone_number": "554498112222",
        "public_name": "Cleso"
    },
    {
        "phone_number": "554797946550",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554195883013",
        "public_name": "Osni"
    },
    {
        "phone_number": "554788516351",
        "public_name": "Murilo"
    },
    {
        "phone_number": "554499722526",
        "public_name": "Jocimar"
    },
    {
        "phone_number": "554799854167",
        "public_name": "Jucelio"
    },
    {
        "phone_number": "554799672121",
        "public_name": "Edgar"
    },
    {
        "phone_number": "554891311800",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554399748007",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "5511950651805",
        "public_name": "Cleber"
    },
    {
        "phone_number": "554791062555",
        "public_name": "Mauro"
    },
    {
        "phone_number": "554497134514",
        "public_name": "Italo"
    },
    {
        "phone_number": "559281399000",
        "public_name": "Jorgenson"
    },
    {
        "phone_number": "554784085098",
        "public_name": "Gean"
    },
    {
        "phone_number": "554599733381",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "554796529100",
        "public_name": "Bia/chiquinho"
    },
    {
        "phone_number": "554199520408",
        "public_name": "Jeferson"
    },
    {
        "phone_number": "554799580720",
        "public_name": "Frank"
    },
    {
        "phone_number": "554898120588",
        "public_name": "Cristiano"
    },
    {
        "phone_number": "554784675784",
        "public_name": "Eliane"
    },
    {
        "phone_number": "554796791400",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554796739707",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554999834411",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554797310806",
        "public_name": "Walter"
    },
    {
        "phone_number": "554196919419",
        "public_name": "Laudemir"
    },
    {
        "phone_number": "554796559968",
        "public_name": "Jose"
    },
    {
        "phone_number": "554591491992",
        "public_name": "Luis"
    },
    {
        "phone_number": "554791190915",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554288605630",
        "public_name": "Cê"
    },
    {
        "phone_number": "554791946776",
        "public_name": "Graciela"
    },
    {
        "phone_number": "554788596355",
        "public_name": "Arlindo"
    },
    {
        "phone_number": "554799850640",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554799764758",
        "public_name": "Walter"
    },
    {
        "phone_number": "554799881343",
        "public_name": "Douglas"
    },
    {
        "phone_number": "5511958031769",
        "public_name": "Luis"
    },
    {
        "phone_number": "554791082714",
        "public_name": "Junior"
    },
    {
        "phone_number": "554499707686",
        "public_name": "Tiago"
    },
    {
        "phone_number": "554191126112",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554792636303",
        "public_name": "Cristiane"
    },
    {
        "phone_number": "554191991836",
        "public_name": "Emilio"
    },
    {
        "phone_number": "556999214600",
        "public_name": "Guida"
    },
    {
        "phone_number": "555499259027",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "556599829855",
        "public_name": "Renata"
    },
    {
        "phone_number": "555499071043",
        "public_name": "Angelica"
    },
    {
        "phone_number": "554891767007",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "554799573017",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554899733412",
        "public_name": "Raquel"
    },
    {
        "phone_number": "554797877000",
        "public_name": "Raíza"
    },
    {
        "phone_number": "554399170277",
        "public_name": "Antonio"
    },
    {
        "phone_number": "5514998812904",
        "public_name": "Lucineia"
    },
    {
        "phone_number": "554797149209",
        "public_name": "Lourival"
    },
    {
        "phone_number": "554799838938",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554196745071",
        "public_name": "Erik"
    },
    {
        "phone_number": "554199799091",
        "public_name": "Sidnei"
    },
    {
        "phone_number": "554796804811",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554599233282",
        "public_name": "Renato"
    },
    {
        "phone_number": "554791366659",
        "public_name": "Bitencourt"
    },
    {
        "phone_number": "554791912033",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554398522618",
        "public_name": "Amélia"
    },
    {
        "phone_number": "555189068619",
        "public_name": "Marília"
    },
    {
        "phone_number": "555599830363",
        "public_name": "Mario"
    },
    {
        "phone_number": "554896295658",
        "public_name": "Jonas"
    },
    {
        "phone_number": "554799160002",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554991354209",
        "public_name": "Renato"
    },
    {
        "phone_number": "554799992510",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554199734317",
        "public_name": "Vilberto"
    },
    {
        "phone_number": "555191588050",
        "public_name": "Renata"
    },
    {
        "phone_number": "554998008888",
        "public_name": "Cedriano"
    },
    {
        "phone_number": "554196577809",
        "public_name": "Liana"
    },
    {
        "phone_number": "554899903736",
        "public_name": "Meri"
    },
    {
        "phone_number": "554799830027",
        "public_name": "Laudelino"
    },
    {
        "phone_number": "554792554686",
        "public_name": "Alessandro"
    },
    {
        "phone_number": "554898412670",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554799648147",
        "public_name": "Mauricio"
    },
    {
        "phone_number": "554899920008",
        "public_name": "Marcos"
    },
    {
        "phone_number": "555191815724",
        "public_name": "Silvana"
    },
    {
        "phone_number": "554598273636",
        "public_name": "Luis"
    },
    {
        "phone_number": "555481195738",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554791044848",
        "public_name": "Junior"
    },
    {
        "phone_number": "554799851443",
        "public_name": "Vania"
    },
    {
        "phone_number": "554191269267",
        "public_name": "Willian"
    },
    {
        "phone_number": "554499149965",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554799497779",
        "public_name": "Junior"
    },
    {
        "phone_number": "5511981525623",
        "public_name": "Antonio"
    },
    {
        "phone_number": "555481449000",
        "public_name": "Ana"
    },
    {
        "phone_number": "554792198078",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "554196921828",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554796438603",
        "public_name": "Josue"
    },
    {
        "phone_number": "554799888877",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554399190084",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554884031704",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554792107711",
        "public_name": "Julie"
    },
    {
        "phone_number": "554799325052",
        "public_name": "Andreia"
    },
    {
        "phone_number": "554433660909",
        "public_name": "Ademir"
    },
    {
        "phone_number": "554499329343",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554197388079",
        "public_name": "Babi"
    },
    {
        "phone_number": "554788543963",
        "public_name": "Jader"
    },
    {
        "phone_number": "554799156502",
        "public_name": "Marinho"
    },
    {
        "phone_number": "5521982733504",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "555499988032",
        "public_name": "Arnold"
    },
    {
        "phone_number": "554797573434",
        "public_name": "Maikol"
    },
    {
        "phone_number": "5511942028835",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554899852143",
        "public_name": "Iver"
    },
    {
        "phone_number": "5511988847390",
        "public_name": "Osorio"
    },
    {
        "phone_number": "554192196189",
        "public_name": "André"
    },
    {
        "phone_number": "554799262959",
        "public_name": "Lourdes"
    },
    {
        "phone_number": "554199572772",
        "public_name": "Fhab"
    },
    {
        "phone_number": "554199320202",
        "public_name": "ProprietarioAfonso"
    },
    {
        "phone_number": "555499203060",
        "public_name": "Luiza"
    },
    {
        "phone_number": "554799778343",
        "public_name": "Davi"
    },
    {
        "phone_number": "554791981711",
        "public_name": "Valdes"
    },
    {
        "phone_number": "554396084166",
        "public_name": "Claudemir"
    },
    {
        "phone_number": "554799275627",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "556781452830",
        "public_name": "Elbio"
    },
    {
        "phone_number": "5511957733091",
        "public_name": "Jacke"
    },
    {
        "phone_number": "5521985082515",
        "public_name": "Edino"
    },
    {
        "phone_number": "554797741801",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554792666521",
        "public_name": "Ana"
    },
    {
        "phone_number": "554491251311",
        "public_name": "Miguel"
    },
    {
        "phone_number": "555491756999",
        "public_name": "Gerson"
    },
    {
        "phone_number": "554691047006",
        "public_name": "Gilmar"
    },
    {
        "phone_number": "554784948003",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554196281102",
        "public_name": "Gislene"
    },
    {
        "phone_number": "554797300325",
        "public_name": "Claudia"
    },
    {
        "phone_number": "554796388309",
        "public_name": "Edson"
    },
    {
        "phone_number": "559281179620",
        "public_name": "Davi"
    },
    {
        "phone_number": "554799414441",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "554799970880",
        "public_name": "Alessandra"
    },
    {
        "phone_number": "5518981019500",
        "public_name": "Luis"
    },
    {
        "phone_number": "554499230400",
        "public_name": "Flavia"
    },
    {
        "phone_number": "554599141515",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554199750262",
        "public_name": "Sonia"
    },
    {
        "phone_number": "554797349364",
        "public_name": "JoãSimone"
    },
    {
        "phone_number": "555591470555",
        "public_name": "Luis"
    },
    {
        "phone_number": "5511981739427",
        "public_name": "Helton"
    },
    {
        "phone_number": "554799515443",
        "public_name": "Mauro"
    },
    {
        "phone_number": "554799999400",
        "public_name": "Junior"
    },
    {
        "phone_number": "554796341930",
        "public_name": "Claudio"
    },
    {
        "phone_number": "555199866777",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554391140292",
        "public_name": "Claudia"
    },
    {
        "phone_number": "554796092009",
        "public_name": "Celia"
    },
    {
        "phone_number": "556699717487",
        "public_name": "Fernanda"
    },
    {
        "phone_number": "554888151198",
        "public_name": "Aticot"
    },
    {
        "phone_number": "554799111555",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554799031849",
        "public_name": "Jean"
    },
    {
        "phone_number": "5511989388988",
        "public_name": "Miro"
    },
    {
        "phone_number": "554799995269",
        "public_name": "Marcela"
    },
    {
        "phone_number": "554791646188",
        "public_name": "Jose"
    },
    {
        "phone_number": "554799068532",
        "public_name": "Tiago"
    },
    {
        "phone_number": "556599810403",
        "public_name": "Erick"
    },
    {
        "phone_number": "554791551165",
        "public_name": "Augustin"
    },
    {
        "phone_number": "554784834481",
        "public_name": "Agnaldo"
    },
    {
        "phone_number": "554391898686",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554788610415",
        "public_name": "Gilson"
    },
    {
        "phone_number": "554796595025",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554884064745",
        "public_name": "Osni"
    },
    {
        "phone_number": "554792557017",
        "public_name": "Rosani"
    },
    {
        "phone_number": "555191892325",
        "public_name": "Isabel"
    },
    {
        "phone_number": "554796332509",
        "public_name": "Ana"
    },
    {
        "phone_number": "554188065316",
        "public_name": "Ulisses"
    },
    {
        "phone_number": "554799430410",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554799286522",
        "public_name": "Jucelino"
    },
    {
        "phone_number": "554491324691",
        "public_name": "Roseli"
    },
    {
        "phone_number": "554299284669",
        "public_name": "Jussara"
    },
    {
        "phone_number": "5521981880809",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554396627088",
        "public_name": "Rivilini"
    },
    {
        "phone_number": "554499445566",
        "public_name": "Claudio"
    },
    {
        "phone_number": "554799162080",
        "public_name": "Julio"
    },
    {
        "phone_number": "556699688839",
        "public_name": "Giovanni"
    },
    {
        "phone_number": "554799278101",
        "public_name": "Aivans"
    },
    {
        "phone_number": "554796188818",
        "public_name": "Camila"
    },
    {
        "phone_number": "5512981464632",
        "public_name": "Danielly"
    },
    {
        "phone_number": "554396094313",
        "public_name": "Maiko"
    },
    {
        "phone_number": "554791979543",
        "public_name": "Gisiane"
    },
    {
        "phone_number": "554399318373",
        "public_name": "Karem"
    },
    {
        "phone_number": "554999230167",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554799618496",
        "public_name": "Junior"
    },
    {
        "phone_number": "554792780155",
        "public_name": "Valdelicio"
    },
    {
        "phone_number": "554896208854",
        "public_name": "Tiao"
    },
    {
        "phone_number": "554399727598",
        "public_name": "Marisol"
    },
    {
        "phone_number": "5515997163296",
        "public_name": "Henrique"
    },
    {
        "phone_number": "554796777308",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554797083949",
        "public_name": "Jerlei"
    },
    {
        "phone_number": "555381415445",
        "public_name": "Paulinho"
    },
    {
        "phone_number": "554796486677",
        "public_name": "André"
    },
    {
        "phone_number": "554991440123",
        "public_name": "Sander"
    },
    {
        "phone_number": "554499117828",
        "public_name": "Tania"
    },
    {
        "phone_number": "554484451306",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554598408899",
        "public_name": "Liz"
    },
    {
        "phone_number": "555491139930",
        "public_name": "Rosangela"
    },
    {
        "phone_number": "554899573511",
        "public_name": "Alex"
    },
    {
        "phone_number": "556799717070",
        "public_name": "JoãAntonio"
    },
    {
        "phone_number": "554191548877",
        "public_name": "Osmar"
    },
    {
        "phone_number": "554784338283",
        "public_name": "Valcir"
    },
    {
        "phone_number": "554799773278",
        "public_name": "Jose"
    },
    {
        "phone_number": "554796752420",
        "public_name": "Flavia"
    },
    {
        "phone_number": "555584248299",
        "public_name": "Denise"
    },
    {
        "phone_number": "554799228874",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554797578000",
        "public_name": "Rubens"
    },
    {
        "phone_number": "554196795959",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554199319525",
        "public_name": "Tony"
    },
    {
        "phone_number": "554788028928",
        "public_name": "Rosa"
    },
    {
        "phone_number": "554799670781",
        "public_name": "Leo"
    },
    {
        "phone_number": "559193331100",
        "public_name": "Larissa"
    },
    {
        "phone_number": "554499760889",
        "public_name": "Kennedy"
    },
    {
        "phone_number": "555496260681",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554791047233",
        "public_name": "Armandio"
    },
    {
        "phone_number": "554796333300",
        "public_name": "Ines"
    },
    {
        "phone_number": "554198047908",
        "public_name": "Sidney"
    },
    {
        "phone_number": "555599969128",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554891038558",
        "public_name": "Keithiany"
    },
    {
        "phone_number": "554899101350",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554799851021",
        "public_name": "Vilson"
    },
    {
        "phone_number": "554797786555",
        "public_name": "Adriano"
    },
    {
        "phone_number": "554797170328",
        "public_name": "Felipe"
    },
    {
        "phone_number": "559180641079",
        "public_name": "Camila"
    },
    {
        "phone_number": "555491875770",
        "public_name": "Leni"
    },
    {
        "phone_number": "554199290550",
        "public_name": "Leydi"
    },
    {
        "phone_number": "554797402686",
        "public_name": "Fabricio"
    },
    {
        "phone_number": "554799462397",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "555492069355",
        "public_name": "Gilmar"
    },
    {
        "phone_number": "554491610014",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554799124971",
        "public_name": "Luciana"
    },
    {
        "phone_number": "554396315900",
        "public_name": "Donizeti"
    },
    {
        "phone_number": "5511947008129",
        "public_name": "Stefanny"
    },
    {
        "phone_number": "554799466522",
        "public_name": "Daniela"
    },
    {
        "phone_number": "554388051684",
        "public_name": "Angelo"
    },
    {
        "phone_number": "554891881588",
        "public_name": "Cintia"
    },
    {
        "phone_number": "555182132020",
        "public_name": "Erivan"
    },
    {
        "phone_number": "5511982246370",
        "public_name": "Tiago"
    },
    {
        "phone_number": "554691140171",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554199223355",
        "public_name": "Alessandro"
    },
    {
        "phone_number": "554591075772",
        "public_name": "Geraldo"
    },
    {
        "phone_number": "554799122519",
        "public_name": "Sabrina"
    },
    {
        "phone_number": "554784459738",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554399188505",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554796377482",
        "public_name": "Rosana"
    },
    {
        "phone_number": "554396168986",
        "public_name": "Dalva"
    },
    {
        "phone_number": "554299750032",
        "public_name": "Ary"
    },
    {
        "phone_number": "554899545176",
        "public_name": "Ivo"
    },
    {
        "phone_number": "554788050958",
        "public_name": "Renato"
    },
    {
        "phone_number": "554788355851",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554799551400",
        "public_name": "Helder"
    },
    {
        "phone_number": "554399292449",
        "public_name": "Magali"
    },
    {
        "phone_number": "554399535523",
        "public_name": "Claudete"
    },
    {
        "phone_number": "554399661888",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554484241191",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554799772493",
        "public_name": "Lauro"
    },
    {
        "phone_number": "554188122531",
        "public_name": "Valdecir"
    },
    {
        "phone_number": "554498622222",
        "public_name": "Marlene"
    },
    {
        "phone_number": "554191890089",
        "public_name": "Andre"
    },
    {
        "phone_number": "554797106549",
        "public_name": "Nichollas"
    },
    {
        "phone_number": "554799111970",
        "public_name": "Sidnei"
    },
    {
        "phone_number": "554298579893",
        "public_name": "Clarice"
    },
    {
        "phone_number": "5511973311963",
        "public_name": "Duarte"
    },
    {
        "phone_number": "554799187525",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554796133200",
        "public_name": "Sandro"
    },
    {
        "phone_number": "554999216821",
        "public_name": "Edila"
    },
    {
        "phone_number": "554799498011",
        "public_name": "Wagner"
    },
    {
        "phone_number": "554791186544",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554799831188",
        "public_name": "Rita"
    },
    {
        "phone_number": "554796647898",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554788664558",
        "public_name": "Giovana"
    },
    {
        "phone_number": "554984064990",
        "public_name": "Viviane"
    },
    {
        "phone_number": "554799123000",
        "public_name": "Charles"
    },
    {
        "phone_number": "554187070808",
        "public_name": "Cristian"
    },
    {
        "phone_number": "554799837676",
        "public_name": "Bony"
    },
    {
        "phone_number": "554299629832",
        "public_name": "Samanta"
    },
    {
        "phone_number": "554799986830",
        "public_name": "Jailson"
    },
    {
        "phone_number": "554199258852",
        "public_name": "Carol"
    },
    {
        "phone_number": "554792311001",
        "public_name": "Jociel"
    },
    {
        "phone_number": "554988325323",
        "public_name": "Marcus"
    },
    {
        "phone_number": "554499912244",
        "public_name": "Joao"
    },
    {
        "phone_number": "554999412000",
        "public_name": "Vera"
    },
    {
        "phone_number": "554191070505",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554896321424",
        "public_name": "TaíMoratelli"
    },
    {
        "phone_number": "554899363336",
        "public_name": "Angelo"
    },
    {
        "phone_number": "5519988086729",
        "public_name": "Marlon"
    },
    {
        "phone_number": "554799820499",
        "public_name": "Michel"
    },
    {
        "phone_number": "554498447406",
        "public_name": "Nildo"
    },
    {
        "phone_number": "554899757477",
        "public_name": "Cristiano"
    },
    {
        "phone_number": "554799148372",
        "public_name": "Samuel"
    },
    {
        "phone_number": "554797746235",
        "public_name": "Vania"
    },
    {
        "phone_number": "554199738327",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554499488848",
        "public_name": "Cinthia"
    },
    {
        "phone_number": "554792152275",
        "public_name": "Leandro"
    },
    {
        "phone_number": "555496694152",
        "public_name": "Monika"
    },
    {
        "phone_number": "554199973183",
        "public_name": "Simone"
    },
    {
        "phone_number": "554799870860",
        "public_name": "Mariela"
    },
    {
        "phone_number": "554684132728",
        "public_name": "Joã"
    },
    {
        "phone_number": "554288491301",
        "public_name": "Giselle"
    },
    {
        "phone_number": "554799521956",
        "public_name": "Diagora"
    },
    {
        "phone_number": "554799446399",
        "public_name": "Eliane"
    },
    {
        "phone_number": "556181177574",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554799836193",
        "public_name": "Jairo"
    },
    {
        "phone_number": "554499724820",
        "public_name": "Sirley"
    },
    {
        "phone_number": "554799744415",
        "public_name": "Jubin"
    },
    {
        "phone_number": "555381419208",
        "public_name": "Daiana"
    },
    {
        "phone_number": "554891824766",
        "public_name": "Dieguinho"
    },
    {
        "phone_number": "554196862073",
        "public_name": "Adriana"
    },
    {
        "phone_number": "554797245065",
        "public_name": "JoãLima"
    },
    {
        "phone_number": "554792260634",
        "public_name": "Jairo"
    },
    {
        "phone_number": "554796844353",
        "public_name": "Cristina"
    },
    {
        "phone_number": "554799995500",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554799417869",
        "public_name": "Joselia"
    },
    {
        "phone_number": "554799740574",
        "public_name": "Larri"
    },
    {
        "phone_number": "554195739582",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554797730000",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554291242466",
        "public_name": "Ana"
    },
    {
        "phone_number": "554991353948",
        "public_name": "Idia"
    },
    {
        "phone_number": "554799475458",
        "public_name": "Jacqueline"
    },
    {
        "phone_number": "554799094722",
        "public_name": "Claudes"
    },
    {
        "phone_number": "554899849393",
        "public_name": "Simonete"
    },
    {
        "phone_number": "554199870884",
        "public_name": "Michel"
    },
    {
        "phone_number": "554799369207",
        "public_name": "Rodrteson"
    },
    {
        "phone_number": "555499155470",
        "public_name": "Michele"
    },
    {
        "phone_number": "556599958986",
        "public_name": "Lilian"
    },
    {
        "phone_number": "554797344271",
        "public_name": "Terezinha"
    },
    {
        "phone_number": "554797199291",
        "public_name": "Zilmar"
    },
    {
        "phone_number": "554799110772",
        "public_name": "Gilson"
    },
    {
        "phone_number": "554498959686",
        "public_name": "Daphene"
    },
    {
        "phone_number": "554991458511",
        "public_name": "Jonathan"
    },
    {
        "phone_number": "554399950746",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554791119090",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554796358822",
        "public_name": "Rafaela"
    },
    {
        "phone_number": "5511998872097",
        "public_name": "Marlene"
    },
    {
        "phone_number": "554999532296",
        "public_name": "Ana"
    },
    {
        "phone_number": "555499474432",
        "public_name": "Rejane"
    },
    {
        "phone_number": "554799356105",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554599755564",
        "public_name": "Ervino"
    },
    {
        "phone_number": "554799632964",
        "public_name": "Francisco"
    },
    {
        "phone_number": "554198521203",
        "public_name": "Danielle"
    },
    {
        "phone_number": "554598261212",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554799955275",
        "public_name": "Alex"
    },
    {
        "phone_number": "554691306915",
        "public_name": "Mauricio"
    },
    {
        "phone_number": "554799184447",
        "public_name": "Reginaldo"
    },
    {
        "phone_number": "5514998645353",
        "public_name": "Erico"
    },
    {
        "phone_number": "553184840172",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554799163336",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554498522411",
        "public_name": "Gulmar"
    },
    {
        "phone_number": "554199930633",
        "public_name": "Claudineia"
    },
    {
        "phone_number": "554196238811",
        "public_name": "Mike"
    },
    {
        "phone_number": "554299690900",
        "public_name": "Reni"
    },
    {
        "phone_number": "554799575812",
        "public_name": "Lucia"
    },
    {
        "phone_number": "555596522200",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554899300010",
        "public_name": "Éder"
    },
    {
        "phone_number": "555499092876",
        "public_name": "Aline"
    },
    {
        "phone_number": "554796547631",
        "public_name": "Roberta"
    },
    {
        "phone_number": "554399846838",
        "public_name": "Jean"
    },
    {
        "phone_number": "554991356332",
        "public_name": "Everton"
    },
    {
        "phone_number": "554799838338",
        "public_name": "Jonas"
    },
    {
        "phone_number": "554799199282",
        "public_name": "Lygia"
    },
    {
        "phone_number": "554499292480",
        "public_name": "Sidney"
    },
    {
        "phone_number": "554499059273",
        "public_name": "Arizona"
    },
    {
        "phone_number": "554791238342",
        "public_name": "Jair"
    },
    {
        "phone_number": "554784737645",
        "public_name": "Kamilly"
    },
    {
        "phone_number": "554797117676",
        "public_name": "Larissa"
    },
    {
        "phone_number": "553388066610",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554888250148",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554999309025",
        "public_name": "Pedro"
    },
    {
        "phone_number": "554399102162",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554791308306",
        "public_name": "Jessica"
    },
    {
        "phone_number": "554691119823",
        "public_name": "Karol"
    },
    {
        "phone_number": "554799754117",
        "public_name": "Oscar"
    },
    {
        "phone_number": "554499274747",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554791200204",
        "public_name": "Raíza"
    },
    {
        "phone_number": "554899267399",
        "public_name": "Danton"
    },
    {
        "phone_number": "554699753392",
        "public_name": "Denis"
    },
    {
        "phone_number": "554796311053",
        "public_name": "Evandro"
    },
    {
        "phone_number": "554792612877",
        "public_name": "Decio"
    },
    {
        "phone_number": "554799387469",
        "public_name": "Robson"
    },
    {
        "phone_number": "554788181180",
        "public_name": "Everton"
    },
    {
        "phone_number": "554792252710",
        "public_name": "Vilmar"
    },
    {
        "phone_number": "554488240990",
        "public_name": "Nicolas"
    },
    {
        "phone_number": "554784555544",
        "public_name": "Andre"
    },
    {
        "phone_number": "554797731832",
        "public_name": "Kleber"
    },
    {
        "phone_number": "554799836829",
        "public_name": "Jose"
    },
    {
        "phone_number": "554399859639",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554799168788",
        "public_name": "Daniele"
    },
    {
        "phone_number": "554791093152",
        "public_name": "Mauro"
    },
    {
        "phone_number": "554788060104",
        "public_name": "Andre"
    },
    {
        "phone_number": "554799963204",
        "public_name": "Marco"
    },
    {
        "phone_number": "554199971919",
        "public_name": "Tiriva"
    },
    {
        "phone_number": "556196172624",
        "public_name": "Hugo"
    },
    {
        "phone_number": "5511982775000",
        "public_name": "Flavio"
    },
    {
        "phone_number": "556699844513",
        "public_name": "Leo"
    },
    {
        "phone_number": "554791961410",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554792714701",
        "public_name": "Cristian"
    },
    {
        "phone_number": "554498021866",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554784050018",
        "public_name": "Ilair"
    },
    {
        "phone_number": "554288288698",
        "public_name": "Pedro"
    },
    {
        "phone_number": "554799357785",
        "public_name": "Glauter"
    },
    {
        "phone_number": "554498684992",
        "public_name": "Everton"
    },
    {
        "phone_number": "554199851294",
        "public_name": "Cristina"
    },
    {
        "phone_number": "554788230789",
        "public_name": "Marlene"
    },
    {
        "phone_number": "554784196409",
        "public_name": "Adriana"
    },
    {
        "phone_number": "554791580064",
        "public_name": "Lu"
    },
    {
        "phone_number": "554199784646",
        "public_name": "Rubeni"
    },
    {
        "phone_number": "5513981285974",
        "public_name": "Beto"
    },
    {
        "phone_number": "554399771212",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "15613051134",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554797705371",
        "public_name": "Daiana"
    },
    {
        "phone_number": "554797337331",
        "public_name": "Saulo"
    },
    {
        "phone_number": "554799772757",
        "public_name": "Paulo"
    },
    {
        "phone_number": "5511991658529",
        "public_name": "Daltro"
    },
    {
        "phone_number": "5511998909844",
        "public_name": "Mariana"
    },
    {
        "phone_number": "554988340132",
        "public_name": "Suian"
    },
    {
        "phone_number": "554799114402",
        "public_name": "Irineu"
    },
    {
        "phone_number": "555491149355",
        "public_name": "Romeu"
    },
    {
        "phone_number": "554784758134",
        "public_name": "Julinana"
    },
    {
        "phone_number": "554797583028",
        "public_name": "Juliana"
    },
    {
        "phone_number": "555199881210",
        "public_name": "Cristiano"
    },
    {
        "phone_number": "554796696090",
        "public_name": "Dullius"
    },
    {
        "phone_number": "554484456936",
        "public_name": "Luciellen"
    },
    {
        "phone_number": "554391541226",
        "public_name": "Jeferson"
    },
    {
        "phone_number": "554399152738",
        "public_name": "Ígor"
    },
    {
        "phone_number": "555491842507",
        "public_name": "Odair"
    },
    {
        "phone_number": "555499759980",
        "public_name": "Kuki"
    },
    {
        "phone_number": "554788011705",
        "public_name": "Daniela"
    },
    {
        "phone_number": "554196789043",
        "public_name": "Lislie"
    },
    {
        "phone_number": "554799837781",
        "public_name": "Milton"
    },
    {
        "phone_number": "555599021968",
        "public_name": "Gilmar"
    },
    {
        "phone_number": "555191720091",
        "public_name": "José"
    },
    {
        "phone_number": "554799793882",
        "public_name": "Cícero"
    },
    {
        "phone_number": "554796789003",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554791075759",
        "public_name": "Berg"
    },
    {
        "phone_number": "554799054555",
        "public_name": "Patricia"
    },
    {
        "phone_number": "5519983516706",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554799836372",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "555196463798",
        "public_name": "Renesio"
    },
    {
        "phone_number": "554191812243",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "555399426831",
        "public_name": "Fatima"
    },
    {
        "phone_number": "554899830638",
        "public_name": "Jackes"
    },
    {
        "phone_number": "555597240409",
        "public_name": "Gesselmar"
    },
    {
        "phone_number": "554799671680",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "555499290835",
        "public_name": "Vagner"
    },
    {
        "phone_number": "554791424706",
        "public_name": "Brenda"
    },
    {
        "phone_number": "554198756603",
        "public_name": "Maria"
    },
    {
        "phone_number": "555599737056",
        "public_name": "Edmilson"
    },
    {
        "phone_number": "555181316028",
        "public_name": "Rosangela"
    },
    {
        "phone_number": "554799257029",
        "public_name": "Daniel"
    },
    {
        "phone_number": "555481117635",
        "public_name": "Henrique"
    },
    {
        "phone_number": "554988461508",
        "public_name": "JoãAltair"
    },
    {
        "phone_number": "554796958720",
        "public_name": "Ivan"
    },
    {
        "phone_number": "554199273025",
        "public_name": "Newton"
    },
    {
        "phone_number": "15612613518",
        "public_name": "Cesar"
    },
    {
        "phone_number": "5513996617921",
        "public_name": "Duda"
    },
    {
        "phone_number": "555481193689",
        "public_name": "Claudia"
    },
    {
        "phone_number": "554784637088",
        "public_name": "Denir"
    },
    {
        "phone_number": "554796130636",
        "public_name": "Maria"
    },
    {
        "phone_number": "554796714181",
        "public_name": "Raquel"
    },
    {
        "phone_number": "556299655045",
        "public_name": "Jerónimo"
    },
    {
        "phone_number": "554188162003",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554584229996",
        "public_name": "Praia"
    },
    {
        "phone_number": "554792884866",
        "public_name": "William"
    },
    {
        "phone_number": "554799331743",
        "public_name": "Maicon"
    },
    {
        "phone_number": "554784140171",
        "public_name": "Nilo"
    },
    {
        "phone_number": "554498362944",
        "public_name": "Jefferson"
    },
    {
        "phone_number": "554792242867",
        "public_name": "Valdeci"
    },
    {
        "phone_number": "555581578209",
        "public_name": "Fatiana"
    },
    {
        "phone_number": "556699882618",
        "public_name": "Christian"
    },
    {
        "phone_number": "555499760607",
        "public_name": "Jair"
    },
    {
        "phone_number": "554899315100",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554288019353",
        "public_name": "Diocea"
    },
    {
        "phone_number": "555591185103",
        "public_name": "Clay"
    },
    {
        "phone_number": "5511981069810",
        "public_name": "Alander"
    },
    {
        "phone_number": "554498750213",
        "public_name": "Josseane"
    },
    {
        "phone_number": "554195953170",
        "public_name": "Rogério"
    },
    {
        "phone_number": "554796803741",
        "public_name": "Marlene"
    },
    {
        "phone_number": "554799149402",
        "public_name": "Sandro"
    },
    {
        "phone_number": "554792342838",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554899692809",
        "public_name": "Elza"
    },
    {
        "phone_number": "554799674079",
        "public_name": "Márcia"
    },
    {
        "phone_number": "554788648430",
        "public_name": "Elisangela"
    },
    {
        "phone_number": "554199234444",
        "public_name": "Jose"
    },
    {
        "phone_number": "554399026032",
        "public_name": "Paulo"
    },
    {
        "phone_number": "555499814548",
        "public_name": "Anelise"
    },
    {
        "phone_number": "555199954339",
        "public_name": "Dagoberto"
    },
    {
        "phone_number": "554799821347",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "555193896599",
        "public_name": "Dionatan"
    },
    {
        "phone_number": "554799607676",
        "public_name": "Janice"
    },
    {
        "phone_number": "554799818283",
        "public_name": "Jader"
    },
    {
        "phone_number": "554599151247",
        "public_name": "Geisa"
    },
    {
        "phone_number": "554799985298",
        "public_name": "Viktor"
    },
    {
        "phone_number": "554899612270",
        "public_name": "LuíGustavo"
    },
    {
        "phone_number": "556584034991",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "555599443570",
        "public_name": "Jean"
    },
    {
        "phone_number": "554797069393",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554899239068",
        "public_name": "Thayni"
    },
    {
        "phone_number": "554899818664",
        "public_name": "Valdir"
    },
    {
        "phone_number": "554799095671",
        "public_name": "Juçara"
    },
    {
        "phone_number": "554799483545",
        "public_name": "Maria"
    },
    {
        "phone_number": "5521999659977",
        "public_name": "Fred"
    },
    {
        "phone_number": "554799826664",
        "public_name": "Flavio"
    },
    {
        "phone_number": "554788181423",
        "public_name": "Flavia"
    },
    {
        "phone_number": "554599794580",
        "public_name": "Pedro"
    },
    {
        "phone_number": "555491193464",
        "public_name": "Itelmar"
    },
    {
        "phone_number": "554799845058",
        "public_name": "Alberto"
    },
    {
        "phone_number": "554796850904",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "555599999192",
        "public_name": "Eliane"
    },
    {
        "phone_number": "554784635104",
        "public_name": "InêGhisleri"
    },
    {
        "phone_number": "554799159998",
        "public_name": "Marcio"
    },
    {
        "phone_number": "555599638206",
        "public_name": "Leo"
    },
    {
        "phone_number": "554184890008",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554899361313",
        "public_name": "Yuri"
    },
    {
        "phone_number": "555584079192",
        "public_name": "Regina"
    },
    {
        "phone_number": "555384027951",
        "public_name": "Renan"
    },
    {
        "phone_number": "554498217739",
        "public_name": "Ana"
    },
    {
        "phone_number": "554491153127",
        "public_name": "JoãRicardo"
    },
    {
        "phone_number": "554988112944",
        "public_name": "Jair"
    },
    {
        "phone_number": "555496028793",
        "public_name": "Valeria"
    },
    {
        "phone_number": "554591547280",
        "public_name": "Leo"
    },
    {
        "phone_number": "554191937165",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554788423445",
        "public_name": "Luis"
    },
    {
        "phone_number": "554999634440",
        "public_name": "Edgar"
    },
    {
        "phone_number": "554199454911",
        "public_name": "Michael"
    },
    {
        "phone_number": "555591782822",
        "public_name": "Marcio"
    },
    {
        "phone_number": "554792005885",
        "public_name": "Filipe"
    },
    {
        "phone_number": "554184035096",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554799470128",
        "public_name": "Cristian"
    },
    {
        "phone_number": "554799883333",
        "public_name": "Corretor"
    },
    {
        "phone_number": "554796112575",
        "public_name": "Neiva"
    },
    {
        "phone_number": "554599259380",
        "public_name": "Izabel"
    },
    {
        "phone_number": "554299790061",
        "public_name": "Sodenia"
    },
    {
        "phone_number": "554197030220",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554391116597",
        "public_name": "Euclides"
    },
    {
        "phone_number": "554788976321",
        "public_name": "Devair"
    },
    {
        "phone_number": "554199239966",
        "public_name": "Marcos"
    },
    {
        "phone_number": "556699125199",
        "public_name": "Jean"
    },
    {
        "phone_number": "554799196026",
        "public_name": "Odete"
    },
    {
        "phone_number": "556791376610",
        "public_name": "Aliris"
    },
    {
        "phone_number": "554791313191",
        "public_name": "Cisso"
    },
    {
        "phone_number": "554899883189",
        "public_name": "Lili"
    },
    {
        "phone_number": "554291048689",
        "public_name": "Nadia"
    },
    {
        "phone_number": "554796297290",
        "public_name": "Casa"
    },
    {
        "phone_number": "554791240556",
        "public_name": "Jailson"
    },
    {
        "phone_number": "554899863535",
        "public_name": "Messias"
    },
    {
        "phone_number": "554999981959",
        "public_name": "Airton"
    },
    {
        "phone_number": "554796686407",
        "public_name": "Juliana"
    },
    {
        "phone_number": "554799950403",
        "public_name": "Emelize"
    },
    {
        "phone_number": "554399579464",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554792750033",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554791617535",
        "public_name": "Taryn"
    },
    {
        "phone_number": "554799837530",
        "public_name": "Cap"
    },
    {
        "phone_number": "554197800170",
        "public_name": "Adriana"
    },
    {
        "phone_number": "554199770002",
        "public_name": "Wilson"
    },
    {
        "phone_number": "556796720034",
        "public_name": "Nilza"
    },
    {
        "phone_number": "554199796679",
        "public_name": "Adriana"
    },
    {
        "phone_number": "555499091260",
        "public_name": "Arni"
    },
    {
        "phone_number": "554796462830",
        "public_name": "Cinara"
    },
    {
        "phone_number": "555499311127",
        "public_name": "José"
    },
    {
        "phone_number": "554488126699",
        "public_name": "GIUSEPPE"
    },
    {
        "phone_number": "554788248782",
        "public_name": "Silas"
    },
    {
        "phone_number": "554799020404",
        "public_name": "Airton"
    },
    {
        "phone_number": "554198460656",
        "public_name": "Marco"
    },
    {
        "phone_number": "5511998375439",
        "public_name": "Emerson"
    },
    {
        "phone_number": "554799216520",
        "public_name": "Fatima"
    },
    {
        "phone_number": "554791331084",
        "public_name": "Marcus"
    },
    {
        "phone_number": "555496801306",
        "public_name": "Dilamar"
    },
    {
        "phone_number": "554796505382",
        "public_name": "Priscila"
    },
    {
        "phone_number": "555194407050",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554799892707",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554399236342",
        "public_name": "Josi"
    },
    {
        "phone_number": "554796505404",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554699715991",
        "public_name": "Igor"
    },
    {
        "phone_number": "554796047890",
        "public_name": "Nivia"
    },
    {
        "phone_number": "554791528885",
        "public_name": "Kako"
    },
    {
        "phone_number": "555198515349",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554191561938",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554999172046",
        "public_name": "Caio"
    },
    {
        "phone_number": "554797470000",
        "public_name": "Marco"
    },
    {
        "phone_number": "554799891012",
        "public_name": "Milton"
    },
    {
        "phone_number": "554791236500",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554799128898",
        "public_name": "Giuliana"
    },
    {
        "phone_number": "554799807460",
        "public_name": "Borbinha"
    },
    {
        "phone_number": "554796520121",
        "public_name": "Iridete"
    },
    {
        "phone_number": "554799713133",
        "public_name": "Antonio"
    },
    {
        "phone_number": "555496117282",
        "public_name": "Maria"
    },
    {
        "phone_number": "554199299777",
        "public_name": "Rita"
    },
    {
        "phone_number": "554799852690",
        "public_name": "Rosita"
    },
    {
        "phone_number": "554197428492",
        "public_name": "Adriano"
    },
    {
        "phone_number": "554899056287",
        "public_name": "Romualdo"
    },
    {
        "phone_number": "554199734038",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554191578785",
        "public_name": "Edilson"
    },
    {
        "phone_number": "554792474816",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554399219093",
        "public_name": "Leonice"
    },
    {
        "phone_number": "554199204751",
        "public_name": "Giani"
    },
    {
        "phone_number": "554791306835",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554888638737",
        "public_name": "Nando"
    },
    {
        "phone_number": "554198180191",
        "public_name": "Carlos"
    },
    {
        "phone_number": "555499882824",
        "public_name": "Claudia"
    },
    {
        "phone_number": "554799748584",
        "public_name": "Clelia"
    },
    {
        "phone_number": "554799330245",
        "public_name": "Fabianne"
    },
    {
        "phone_number": "554799811839",
        "public_name": "Quer"
    },
    {
        "phone_number": "554799991479",
        "public_name": "Rodolfo"
    },
    {
        "phone_number": "555499678259",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554991351666",
        "public_name": "Joao"
    },
    {
        "phone_number": "554999963169",
        "public_name": "Maria"
    },
    {
        "phone_number": "554799003398",
        "public_name": "Franco"
    },
    {
        "phone_number": "5511945323961",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554797119000",
        "public_name": "Alcina"
    },
    {
        "phone_number": "554899891314",
        "public_name": "Edson"
    },
    {
        "phone_number": "554797693505",
        "public_name": "Delfes"
    },
    {
        "phone_number": "554799740319",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554799117744",
        "public_name": "Luciana"
    },
    {
        "phone_number": "554792212770",
        "public_name": "Kleber"
    },
    {
        "phone_number": "554799220000",
        "public_name": "Flaviano"
    },
    {
        "phone_number": "554792466647",
        "public_name": "Alessandro"
    },
    {
        "phone_number": "554195767991",
        "public_name": "Jovina"
    },
    {
        "phone_number": "554196835151",
        "public_name": "Marcela"
    },
    {
        "phone_number": "554199611593",
        "public_name": "Cassia"
    },
    {
        "phone_number": "555499738865",
        "public_name": "Fabiano"
    },
    {
        "phone_number": "555499745836",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554799838977",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554288831161",
        "public_name": "Ezequiel"
    },
    {
        "phone_number": "554199742133",
        "public_name": "Roberto"
    },
    {
        "phone_number": "559192630015",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554799799400",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "554199855678",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554691201234",
        "public_name": "Josiane"
    },
    {
        "phone_number": "5514998610332",
        "public_name": "Dion"
    },
    {
        "phone_number": "555491563453",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554799214004",
        "public_name": "Maury"
    },
    {
        "phone_number": "554898417228",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554797070101",
        "public_name": "Wilian"
    },
    {
        "phone_number": "554792590106",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554398485145",
        "public_name": "Keitilaine"
    },
    {
        "phone_number": "554991058868",
        "public_name": "Maria"
    },
    {
        "phone_number": "554799833014",
        "public_name": "Deize"
    },
    {
        "phone_number": "554799872837",
        "public_name": "Henrique"
    },
    {
        "phone_number": "554799095222",
        "public_name": "Cleusa"
    },
    {
        "phone_number": "554591489086",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554799118395",
        "public_name": "Gabriela"
    },
    {
        "phone_number": "554796095446",
        "public_name": "Michelle"
    },
    {
        "phone_number": "554799833670",
        "public_name": "Osni"
    },
    {
        "phone_number": "555197832021",
        "public_name": "Steffani"
    },
    {
        "phone_number": "554796779892",
        "public_name": "Zila"
    },
    {
        "phone_number": "555481180236",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554991225566",
        "public_name": "Gilson"
    },
    {
        "phone_number": "554799836665",
        "public_name": "Proprietário"
    },
    {
        "phone_number": "555184242229",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554999853053",
        "public_name": "Francisco"
    },
    {
        "phone_number": "554884555548",
        "public_name": "JoãMaurique"
    },
    {
        "phone_number": "556696832628",
        "public_name": "Iris"
    },
    {
        "phone_number": "5519974281856",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "555499262428",
        "public_name": "Victor"
    },
    {
        "phone_number": "554797303900",
        "public_name": "Harley"
    },
    {
        "phone_number": "554197400154",
        "public_name": "Everton"
    },
    {
        "phone_number": "554199575299",
        "public_name": "Roberto"
    },
    {
        "phone_number": "555591128998",
        "public_name": "Janice"
    },
    {
        "phone_number": "554197627777",
        "public_name": "Charles"
    },
    {
        "phone_number": "554784965836",
        "public_name": "Marli"
    },
    {
        "phone_number": "554196778171",
        "public_name": "José"
    },
    {
        "phone_number": "554187219648",
        "public_name": "Felipe"
    },
    {
        "phone_number": "5511996188762",
        "public_name": "Pericles"
    },
    {
        "phone_number": "554199971038",
        "public_name": "Magnum"
    },
    {
        "phone_number": "554199260020",
        "public_name": "Vilmar"
    },
    {
        "phone_number": "554799714306",
        "public_name": "Junior"
    },
    {
        "phone_number": "554784690064",
        "public_name": "Alessandro"
    },
    {
        "phone_number": "554888028841",
        "public_name": "Tadeu"
    },
    {
        "phone_number": "554799598998",
        "public_name": "Anderson"
    },
    {
        "phone_number": "555599991626",
        "public_name": "Jean"
    },
    {
        "phone_number": "554898622031",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554184165976",
        "public_name": "Emanuel"
    },
    {
        "phone_number": "554792750765",
        "public_name": "Sergio"
    },
    {
        "phone_number": "553182861339",
        "public_name": "GUSTAVOPH"
    },
    {
        "phone_number": "554791344763",
        "public_name": "Ana"
    },
    {
        "phone_number": "554799283800",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554784146992",
        "public_name": "Rafaella"
    },
    {
        "phone_number": "554198620025",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554391030102",
        "public_name": "Ana"
    },
    {
        "phone_number": "554288125100",
        "public_name": "Mario"
    },
    {
        "phone_number": "554791898767",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554791013100",
        "public_name": "Rovena"
    },
    {
        "phone_number": "554799254868",
        "public_name": "Tassi"
    },
    {
        "phone_number": "554196757500",
        "public_name": "Ludmila"
    },
    {
        "phone_number": "554796090854",
        "public_name": "Sabrine"
    },
    {
        "phone_number": "554799148289",
        "public_name": "Samara"
    },
    {
        "phone_number": "554788612471",
        "public_name": "Neusa"
    },
    {
        "phone_number": "554784471156",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554791757481",
        "public_name": "Suelen"
    },
    {
        "phone_number": "554188645501",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554888362505",
        "public_name": "Pedro"
    },
    {
        "phone_number": "554788166970",
        "public_name": "Francisco"
    },
    {
        "phone_number": "554799779120",
        "public_name": "Marco"
    },
    {
        "phone_number": "554799637702",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554199155531",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554691118791",
        "public_name": "Andreia"
    },
    {
        "phone_number": "554788618638",
        "public_name": "Fabricio"
    },
    {
        "phone_number": "554799834659",
        "public_name": "Marcio"
    },
    {
        "phone_number": "554799572211",
        "public_name": "Claudio"
    },
    {
        "phone_number": "554799411340",
        "public_name": "Denilson"
    },
    {
        "phone_number": "554199035995",
        "public_name": "Wania"
    },
    {
        "phone_number": "554498361568",
        "public_name": "Jose"
    },
    {
        "phone_number": "59996958133",
        "public_name": "Blanca"
    },
    {
        "phone_number": "554888450656",
        "public_name": "Mine"
    },
    {
        "phone_number": "554399945921",
        "public_name": "Abdo"
    },
    {
        "phone_number": "554991365914",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554199656513",
        "public_name": "Neusa"
    },
    {
        "phone_number": "554799830106",
        "public_name": "Sergio"
    },
    {
        "phone_number": "556499847126",
        "public_name": "Tânia"
    },
    {
        "phone_number": "555399749885",
        "public_name": "Lhoren"
    },
    {
        "phone_number": "554999638093",
        "public_name": "Laurence"
    },
    {
        "phone_number": "554799214852",
        "public_name": "Aloir"
    },
    {
        "phone_number": "554791664114",
        "public_name": "Marise"
    },
    {
        "phone_number": "554796441900",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554999142180",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554796864015",
        "public_name": "Jackson"
    },
    {
        "phone_number": "554788195588",
        "public_name": "Alessandra"
    },
    {
        "phone_number": "554784645005",
        "public_name": "William"
    },
    {
        "phone_number": "554199583121",
        "public_name": "Mari"
    },
    {
        "phone_number": "554791017675",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554792573418",
        "public_name": "Felipe"
    },
    {
        "phone_number": "556992098776",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "555199463798",
        "public_name": "Renesio"
    },
    {
        "phone_number": "555499845868",
        "public_name": "Zuleica"
    },
    {
        "phone_number": "554599126464",
        "public_name": "Filha"
    },
    {
        "phone_number": "555599632791",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554196221802",
        "public_name": "Cristine"
    },
    {
        "phone_number": "5519983834770",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554197967067",
        "public_name": "Jessica"
    },
    {
        "phone_number": "554999876374",
        "public_name": "Renato"
    },
    {
        "phone_number": "554299875089",
        "public_name": "Ana"
    },
    {
        "phone_number": "554784670494",
        "public_name": "Junior"
    },
    {
        "phone_number": "554791684793",
        "public_name": "Alaércio"
    },
    {
        "phone_number": "554791291628",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554796051476",
        "public_name": "Darli"
    },
    {
        "phone_number": "556699848810",
        "public_name": "Gerson"
    },
    {
        "phone_number": "555481217215",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554796519183",
        "public_name": "Valmir"
    },
    {
        "phone_number": "554788369387",
        "public_name": "Levi"
    },
    {
        "phone_number": "554799734959",
        "public_name": "LeoonidáDias"
    },
    {
        "phone_number": "554788496900",
        "public_name": "Marta"
    },
    {
        "phone_number": "5521994471775",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554799586641",
        "public_name": "Mayara"
    },
    {
        "phone_number": "554791477070",
        "public_name": "Elaine"
    },
    {
        "phone_number": "554984165084",
        "public_name": "Joaquim"
    },
    {
        "phone_number": "554799593729",
        "public_name": "Rodolfo"
    },
    {
        "phone_number": "554788095897",
        "public_name": "Davi"
    },
    {
        "phone_number": "554198662425",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554298031550",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554796622087",
        "public_name": "Isabela"
    },
    {
        "phone_number": "554498016974",
        "public_name": "Cristiano"
    },
    {
        "phone_number": "555198418072",
        "public_name": "Jair"
    },
    {
        "phone_number": "554599722828",
        "public_name": "Dercio"
    },
    {
        "phone_number": "554799221676",
        "public_name": "Simoni"
    },
    {
        "phone_number": "554799837707",
        "public_name": "Nelson"
    },
    {
        "phone_number": "554799238241",
        "public_name": "Vinicius"
    },
    {
        "phone_number": "554199850246",
        "public_name": "Manoel"
    },
    {
        "phone_number": "5521981017180",
        "public_name": "Taises"
    },
    {
        "phone_number": "554799493938",
        "public_name": "Rafael"
    },
    {
        "phone_number": "556999916323",
        "public_name": "Elisangela"
    },
    {
        "phone_number": "554391461488",
        "public_name": "Giuseppe"
    },
    {
        "phone_number": "554699206577",
        "public_name": "Adriano"
    },
    {
        "phone_number": "555499179217",
        "public_name": "Fabricio"
    },
    {
        "phone_number": "554599381667",
        "public_name": "Silvana"
    },
    {
        "phone_number": "554598062467",
        "public_name": "Cassio"
    },
    {
        "phone_number": "554797051692",
        "public_name": "Áurea"
    },
    {
        "phone_number": "554799834157",
        "public_name": "Dani"
    },
    {
        "phone_number": "554891019101",
        "public_name": "Davi"
    },
    {
        "phone_number": "555491668203",
        "public_name": "Renan"
    },
    {
        "phone_number": "554796194977",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554791216182",
        "public_name": "Luis"
    },
    {
        "phone_number": "554196260911",
        "public_name": "Vagner"
    },
    {
        "phone_number": "554891441980",
        "public_name": "Suzana"
    },
    {
        "phone_number": "554796619299",
        "public_name": "Renato"
    },
    {
        "phone_number": "554899916045",
        "public_name": "Alvaro"
    },
    {
        "phone_number": "554199988948",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "5511982640278",
        "public_name": "Alberto"
    },
    {
        "phone_number": "554199227787",
        "public_name": "Eveline"
    },
    {
        "phone_number": "554789144554",
        "public_name": "Mara"
    },
    {
        "phone_number": "554484033181",
        "public_name": "Bruna"
    },
    {
        "phone_number": "554899454496",
        "public_name": "Pedro"
    },
    {
        "phone_number": "554688037023",
        "public_name": "André"
    },
    {
        "phone_number": "559285905540",
        "public_name": "Davi"
    },
    {
        "phone_number": "554196429012",
        "public_name": "Lorena"
    },
    {
        "phone_number": "554199888557",
        "public_name": "Fabiano"
    },
    {
        "phone_number": "5512974093496",
        "public_name": "Kiki"
    },
    {
        "phone_number": "554699259876",
        "public_name": "Herman"
    },
    {
        "phone_number": "554192728801",
        "public_name": "Lineu"
    },
    {
        "phone_number": "554991463486",
        "public_name": "Goetten"
    },
    {
        "phone_number": "554188820306",
        "public_name": "Vlademir"
    },
    {
        "phone_number": "554799575129",
        "public_name": "Margareth"
    },
    {
        "phone_number": "554796527375",
        "public_name": "Ivo"
    },
    {
        "phone_number": "555199841204",
        "public_name": "Bejamin"
    },
    {
        "phone_number": "554198012939",
        "public_name": "Tatyane"
    },
    {
        "phone_number": "554199741455",
        "public_name": "Lilian"
    },
    {
        "phone_number": "555599611182",
        "public_name": "Passo"
    },
    {
        "phone_number": "554899874989",
        "public_name": "Marcio"
    },
    {
        "phone_number": "554799586677",
        "public_name": "Michel"
    },
    {
        "phone_number": "555591337309",
        "public_name": "AdãCambraia"
    },
    {
        "phone_number": "554499722087",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554195553334",
        "public_name": "Claudio"
    },
    {
        "phone_number": "554192666407",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554491454837",
        "public_name": "Julio"
    },
    {
        "phone_number": "554191835140",
        "public_name": "Jozafá"
    },
    {
        "phone_number": "554199327200",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554796844444",
        "public_name": "Andre"
    },
    {
        "phone_number": "5521998873200",
        "public_name": "Elena"
    },
    {
        "phone_number": "554199580166",
        "public_name": "Vitor"
    },
    {
        "phone_number": "554791409009",
        "public_name": "Camila"
    },
    {
        "phone_number": "554791389554",
        "public_name": "Zenildo"
    },
    {
        "phone_number": "555596252516",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554396360257",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554799190909",
        "public_name": "Diogo"
    },
    {
        "phone_number": "554999195302",
        "public_name": "Juarez"
    },
    {
        "phone_number": "554799278520",
        "public_name": "Isabela"
    },
    {
        "phone_number": "554799723534",
        "public_name": "Ney"
    },
    {
        "phone_number": "554799229306",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554799723388",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554792788989",
        "public_name": "Claudio"
    },
    {
        "phone_number": "555199836658",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554199947576",
        "public_name": "Valentin"
    },
    {
        "phone_number": "556183622911",
        "public_name": "Junior"
    },
    {
        "phone_number": "554891075114",
        "public_name": "Daniel"
    },
    {
        "phone_number": "556699400016",
        "public_name": "Sthefanny"
    },
    {
        "phone_number": "554391048100",
        "public_name": "Helio"
    },
    {
        "phone_number": "554797031211",
        "public_name": "Clauber"
    },
    {
        "phone_number": "5518982000187",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554791663445",
        "public_name": "Nonato"
    },
    {
        "phone_number": "554799911628",
        "public_name": "Silvana"
    },
    {
        "phone_number": "554591048681",
        "public_name": "Gianni"
    },
    {
        "phone_number": "555596142296",
        "public_name": "Fabiano"
    },
    {
        "phone_number": "555199123460",
        "public_name": "Clair"
    },
    {
        "phone_number": "554999924815",
        "public_name": "Luis"
    },
    {
        "phone_number": "554184199439",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554788533454",
        "public_name": "Neide"
    },
    {
        "phone_number": "554796051880",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "555591562443",
        "public_name": "Jardel"
    },
    {
        "phone_number": "554799110984",
        "public_name": "Robson"
    },
    {
        "phone_number": "554799510953",
        "public_name": "Maria"
    },
    {
        "phone_number": "554799013637",
        "public_name": "Neoli"
    },
    {
        "phone_number": "554999669471",
        "public_name": "Mariela"
    },
    {
        "phone_number": "554799611518",
        "public_name": "Celso"
    },
    {
        "phone_number": "554792312722",
        "public_name": "Jociano"
    },
    {
        "phone_number": "554796140007",
        "public_name": "Irene"
    },
    {
        "phone_number": "554196787272",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "555491600570",
        "public_name": "Celso"
    },
    {
        "phone_number": "554999466233",
        "public_name": "Alencar"
    },
    {
        "phone_number": "554799220008",
        "public_name": "Tabaré"
    },
    {
        "phone_number": "554799177000",
        "public_name": "Cristiano"
    },
    {
        "phone_number": "554991916907",
        "public_name": "Katia"
    },
    {
        "phone_number": "554799831324",
        "public_name": "Diego"
    },
    {
        "phone_number": "554799187858",
        "public_name": "Aline"
    },
    {
        "phone_number": "554599447463",
        "public_name": "Junior"
    },
    {
        "phone_number": "554799537098",
        "public_name": "Clovis"
    },
    {
        "phone_number": "555499540709",
        "public_name": "Marines"
    },
    {
        "phone_number": "555182094092",
        "public_name": "Dan"
    },
    {
        "phone_number": "554796587060",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "5519997260036",
        "public_name": "Andre"
    },
    {
        "phone_number": "554488164376",
        "public_name": "Luana"
    },
    {
        "phone_number": "554599239324",
        "public_name": "Maruam"
    },
    {
        "phone_number": "554792895656",
        "public_name": "Nori"
    },
    {
        "phone_number": "555496174876",
        "public_name": "Zelinda"
    },
    {
        "phone_number": "557799614041",
        "public_name": "Vital"
    },
    {
        "phone_number": "555496757575",
        "public_name": "Christian"
    },
    {
        "phone_number": "554791140090",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554199172161",
        "public_name": "Rosangela"
    },
    {
        "phone_number": "5519974063111",
        "public_name": "Everaldo"
    },
    {
        "phone_number": "13216033000",
        "public_name": "Andre"
    },
    {
        "phone_number": "554796127583",
        "public_name": "CASA"
    },
    {
        "phone_number": "554788093603",
        "public_name": "Soraia"
    },
    {
        "phone_number": "555496943008",
        "public_name": "Leonildo"
    },
    {
        "phone_number": "554797705372",
        "public_name": "Lair"
    },
    {
        "phone_number": "554797720049",
        "public_name": "Andre"
    },
    {
        "phone_number": "554797346050",
        "public_name": "Cris"
    },
    {
        "phone_number": "556599661234",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554498804343",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554796540635",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554499764801",
        "public_name": "Walmor"
    },
    {
        "phone_number": "554797090123",
        "public_name": "Janaina"
    },
    {
        "phone_number": "554784043211",
        "public_name": "Everton"
    },
    {
        "phone_number": "554799882748",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554799556265",
        "public_name": "Paty"
    },
    {
        "phone_number": "555198994056",
        "public_name": "Geraldo"
    },
    {
        "phone_number": "5511976044805",
        "public_name": "Paula"
    },
    {
        "phone_number": "554196760347",
        "public_name": "Jorge"
    },
    {
        "phone_number": "19546432431",
        "public_name": "Jose"
    },
    {
        "phone_number": "554299569633",
        "public_name": "Ana"
    },
    {
        "phone_number": "554797794330",
        "public_name": "Altair"
    },
    {
        "phone_number": "554799851775",
        "public_name": "Alex"
    },
    {
        "phone_number": "555189976020",
        "public_name": "Maria"
    },
    {
        "phone_number": "554791592609",
        "public_name": "Daniel"
    },
    {
        "phone_number": "555499444977",
        "public_name": "Luciana"
    },
    {
        "phone_number": "554884147272",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554791399136",
        "public_name": "Dany"
    },
    {
        "phone_number": "556184053824",
        "public_name": "Cleuber"
    },
    {
        "phone_number": "554199692030",
        "public_name": "Fernando"
    },
    {
        "phone_number": "5511947457393",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "555193192141",
        "public_name": "Ana"
    },
    {
        "phone_number": "555199425990",
        "public_name": "Douglas"
    },
    {
        "phone_number": "554399742186",
        "public_name": "Jaime"
    },
    {
        "phone_number": "555193085437",
        "public_name": "Rubia"
    },
    {
        "phone_number": "554799356775",
        "public_name": "Raquelli"
    },
    {
        "phone_number": "5518997522300",
        "public_name": "Julio"
    },
    {
        "phone_number": "554796644566",
        "public_name": "Fernanda"
    },
    {
        "phone_number": "554791371414",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554799156412",
        "public_name": "Jamila"
    },
    {
        "phone_number": "554799698817",
        "public_name": "Elder"
    },
    {
        "phone_number": "554191049016",
        "public_name": "Jean"
    },
    {
        "phone_number": "554199113775",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554799862790",
        "public_name": "aria"
    },
    {
        "phone_number": "555199717943",
        "public_name": "Everson"
    },
    {
        "phone_number": "554799750496",
        "public_name": "Jenice"
    },
    {
        "phone_number": "554791292022",
        "public_name": "Maria"
    },
    {
        "phone_number": "554791101798",
        "public_name": "Cris"
    },
    {
        "phone_number": "554788515553",
        "public_name": "Vinicius"
    },
    {
        "phone_number": "554599127821",
        "public_name": "Rafaela"
    },
    {
        "phone_number": "554799376899",
        "public_name": "Robson"
    },
    {
        "phone_number": "554884038223",
        "public_name": "André"
    },
    {
        "phone_number": "554799461633",
        "public_name": "Neiva"
    },
    {
        "phone_number": "554788262285",
        "public_name": "Augustin"
    },
    {
        "phone_number": "554796382283",
        "public_name": "Custodio"
    },
    {
        "phone_number": "554188187747",
        "public_name": "Ronald"
    },
    {
        "phone_number": "554199956669",
        "public_name": "Edison"
    },
    {
        "phone_number": "556281605004",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "554988031850",
        "public_name": "Julio"
    },
    {
        "phone_number": "554797220008",
        "public_name": "Cesar"
    },
    {
        "phone_number": "556792746000",
        "public_name": "Sadi"
    },
    {
        "phone_number": "554197515380",
        "public_name": "Cleber"
    },
    {
        "phone_number": "554791558007",
        "public_name": "Juliana"
    },
    {
        "phone_number": "554788179699",
        "public_name": "Regina"
    },
    {
        "phone_number": "555191928706",
        "public_name": "Denise"
    },
    {
        "phone_number": "554799931181",
        "public_name": "Neuza"
    },
    {
        "phone_number": "555496699020",
        "public_name": "Sidney"
    },
    {
        "phone_number": "554499171343",
        "public_name": "Xande"
    },
    {
        "phone_number": "554788052305",
        "public_name": "Mônica"
    },
    {
        "phone_number": "554799853300",
        "public_name": "Yamamoto"
    },
    {
        "phone_number": "554298531812",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554791748881",
        "public_name": "Sebastian"
    },
    {
        "phone_number": "555491966068",
        "public_name": "Chaiane"
    },
    {
        "phone_number": "554799704722",
        "public_name": "Ursula"
    },
    {
        "phone_number": "554191036221",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554199556039",
        "public_name": "Caue"
    },
    {
        "phone_number": "554799772032",
        "public_name": "Jose"
    },
    {
        "phone_number": "554791141966",
        "public_name": "Fretta"
    },
    {
        "phone_number": "554184823905",
        "public_name": "Graziele"
    },
    {
        "phone_number": "554999732773",
        "public_name": "Tiago"
    },
    {
        "phone_number": "554784341466",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554699105263",
        "public_name": "Osvaldo"
    },
    {
        "phone_number": "554791196000",
        "public_name": "Giovani"
    },
    {
        "phone_number": "554796178060",
        "public_name": "Errol"
    },
    {
        "phone_number": "554791927300",
        "public_name": "Elton"
    },
    {
        "phone_number": "554299750813",
        "public_name": "Mara"
    },
    {
        "phone_number": "5512997118509",
        "public_name": "Camila"
    },
    {
        "phone_number": "554888439354",
        "public_name": "Izaia"
    },
    {
        "phone_number": "556798290809",
        "public_name": "Ana"
    },
    {
        "phone_number": "554792500855",
        "public_name": "Angelo"
    },
    {
        "phone_number": "554799189588",
        "public_name": "Marquiotti"
    },
    {
        "phone_number": "554899820064",
        "public_name": "Claudio"
    },
    {
        "phone_number": "5511940354373",
        "public_name": "Emerson"
    },
    {
        "phone_number": "554799384565",
        "public_name": "Celia"
    },
    {
        "phone_number": "554788689459",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554896635152",
        "public_name": "Valdecir"
    },
    {
        "phone_number": "554788321177",
        "public_name": "Valdeci"
    },
    {
        "phone_number": "554196112280",
        "public_name": "Mauro"
    },
    {
        "phone_number": "554799887605",
        "public_name": "JoãValmir"
    },
    {
        "phone_number": "554999520760",
        "public_name": "Mauro"
    },
    {
        "phone_number": "554991943184",
        "public_name": "Nadia"
    },
    {
        "phone_number": "5511958036544",
        "public_name": "Aíssa"
    },
    {
        "phone_number": "554788031795",
        "public_name": "Jubiane"
    },
    {
        "phone_number": "554799257051",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554796013621",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554799792229",
        "public_name": "Adênis"
    },
    {
        "phone_number": "554799838623",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554791995889",
        "public_name": "Edson"
    },
    {
        "phone_number": "554784062455",
        "public_name": "Guerra"
    },
    {
        "phone_number": "554184111167",
        "public_name": "Elizabeth"
    },
    {
        "phone_number": "555596320539",
        "public_name": "Ana"
    },
    {
        "phone_number": "554187791919",
        "public_name": "Georgia"
    },
    {
        "phone_number": "554797086666",
        "public_name": "Silvano"
    },
    {
        "phone_number": "559681151763",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554499575737",
        "public_name": "Diego"
    },
    {
        "phone_number": "555599533544",
        "public_name": "Denis"
    },
    {
        "phone_number": "554791016687",
        "public_name": "Mariza"
    },
    {
        "phone_number": "554799059292",
        "public_name": "Michele"
    },
    {
        "phone_number": "554784456955",
        "public_name": "Mirella"
    },
    {
        "phone_number": "554784316839",
        "public_name": "Camila"
    },
    {
        "phone_number": "554896200805",
        "public_name": "Ivonete"
    },
    {
        "phone_number": "554199745710",
        "public_name": "Paulo"
    },
    {
        "phone_number": "555596438433",
        "public_name": "Anusca"
    },
    {
        "phone_number": "554188560449",
        "public_name": "Edivaldo"
    },
    {
        "phone_number": "554396209299",
        "public_name": "Nadia"
    },
    {
        "phone_number": "554799725114",
        "public_name": "Placido"
    },
    {
        "phone_number": "554788862322",
        "public_name": "Denise"
    },
    {
        "phone_number": "554792524771",
        "public_name": "Mílard"
    },
    {
        "phone_number": "554791054746",
        "public_name": "Elina"
    },
    {
        "phone_number": "554796189193",
        "public_name": "Cris/Eloi"
    },
    {
        "phone_number": "554791406562",
        "public_name": "Adao"
    },
    {
        "phone_number": "554791018009",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554791361006",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554799872116",
        "public_name": "Marina"
    },
    {
        "phone_number": "554896069660",
        "public_name": "Adriana"
    },
    {
        "phone_number": "554797900545",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554784466188",
        "public_name": "Rafaela"
    },
    {
        "phone_number": "556981070096",
        "public_name": "Suzana"
    },
    {
        "phone_number": "554896986404",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554796195149",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554791258540",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554799192903",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554791460860",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554796122222",
        "public_name": "Juliana"
    },
    {
        "phone_number": "554588172285",
        "public_name": "Sabrina"
    },
    {
        "phone_number": "556492140033",
        "public_name": "Thaynara"
    },
    {
        "phone_number": "554199858500",
        "public_name": "José"
    },
    {
        "phone_number": "554784369868",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554784482283",
        "public_name": "Cledinara"
    },
    {
        "phone_number": "554196813613",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554998019595",
        "public_name": "Nei"
    },
    {
        "phone_number": "554799855051",
        "public_name": "Arno"
    },
    {
        "phone_number": "556699997650",
        "public_name": "Everson"
    },
    {
        "phone_number": "554788059445",
        "public_name": "Robson"
    },
    {
        "phone_number": "554498494140",
        "public_name": "Junior"
    },
    {
        "phone_number": "554699319000",
        "public_name": "Hans"
    },
    {
        "phone_number": "554796090840",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554584072038",
        "public_name": "Devair"
    },
    {
        "phone_number": "554691119445",
        "public_name": "Fabiana"
    },
    {
        "phone_number": "554184008216",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554791782902",
        "public_name": "Bueno"
    },
    {
        "phone_number": "554799681335",
        "public_name": "Juari"
    },
    {
        "phone_number": "554799149205",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554799120553",
        "public_name": "Livia"
    },
    {
        "phone_number": "554999050051",
        "public_name": "Vanderley"
    },
    {
        "phone_number": "554499892117",
        "public_name": "Regis"
    },
    {
        "phone_number": "555599496862",
        "public_name": "Samira"
    },
    {
        "phone_number": "555198553788",
        "public_name": "Valdir"
    },
    {
        "phone_number": "554599629527",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554796076905",
        "public_name": "Valdirene"
    },
    {
        "phone_number": "554999971118",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554799828118",
        "public_name": "Levi"
    },
    {
        "phone_number": "555491170095",
        "public_name": "Noemia"
    },
    {
        "phone_number": "554195405709",
        "public_name": "Bruna"
    },
    {
        "phone_number": "554791230071",
        "public_name": "Evandro"
    },
    {
        "phone_number": "554499445913",
        "public_name": "Rocha"
    },
    {
        "phone_number": "554999876472",
        "public_name": "Tirza"
    },
    {
        "phone_number": "554799199747",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554791835214",
        "public_name": "Nilto"
    },
    {
        "phone_number": "554791246406",
        "public_name": "Lila"
    },
    {
        "phone_number": "554796048191",
        "public_name": "Roberta"
    },
    {
        "phone_number": "555599557151",
        "public_name": "Julio"
    },
    {
        "phone_number": "554788566803",
        "public_name": "Jheniffer"
    },
    {
        "phone_number": "554796120003",
        "public_name": "Dioni"
    },
    {
        "phone_number": "554188286204",
        "public_name": "Maura"
    },
    {
        "phone_number": "554896289411",
        "public_name": "Odilson"
    },
    {
        "phone_number": "554899415161",
        "public_name": "Maikon"
    },
    {
        "phone_number": "554799650664",
        "public_name": "Fernando"
    },
    {
        "phone_number": "555491291826",
        "public_name": "Marcio"
    },
    {
        "phone_number": "555181607027",
        "public_name": "Luiza"
    },
    {
        "phone_number": "554391838384",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554191024390",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554199883748",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554799747493",
        "public_name": "Maria"
    },
    {
        "phone_number": "556899872737",
        "public_name": "Cristian"
    },
    {
        "phone_number": "554792153001",
        "public_name": "Pedro"
    },
    {
        "phone_number": "554199573821",
        "public_name": "Ane"
    },
    {
        "phone_number": "554799638494",
        "public_name": "Claudia"
    },
    {
        "phone_number": "554791852277",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554899529058",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "555596141100",
        "public_name": "Luana"
    },
    {
        "phone_number": "554796290045",
        "public_name": "Raduan"
    },
    {
        "phone_number": "554599358937",
        "public_name": "Ana"
    },
    {
        "phone_number": "554999831358",
        "public_name": "Amilton"
    },
    {
        "phone_number": "557192900506",
        "public_name": "Valdemiro"
    },
    {
        "phone_number": "554299857203",
        "public_name": "Gih"
    },
    {
        "phone_number": "554898260008",
        "public_name": "Adir"
    },
    {
        "phone_number": "554891639667",
        "public_name": "Diego"
    },
    {
        "phone_number": "554188551445",
        "public_name": "Marcos"
    },
    {
        "phone_number": "34687121475",
        "public_name": "Carlos"
    },
    {
        "phone_number": "556992619611",
        "public_name": "Diego"
    },
    {
        "phone_number": "554499312016",
        "public_name": "Edvaldo"
    },
    {
        "phone_number": "554788720008",
        "public_name": "Elisabet"
    },
    {
        "phone_number": "554799082419",
        "public_name": "Fernanda"
    },
    {
        "phone_number": "554288387722",
        "public_name": "Renato"
    },
    {
        "phone_number": "554499167897",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554699050897",
        "public_name": "Daniele"
    },
    {
        "phone_number": "554799854470",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554799372296",
        "public_name": "Jair"
    },
    {
        "phone_number": "554796196666",
        "public_name": "Angelo"
    },
    {
        "phone_number": "5522988023141",
        "public_name": "Praia"
    },
    {
        "phone_number": "554791105445",
        "public_name": "Ale"
    },
    {
        "phone_number": "554788239600",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554797219223",
        "public_name": "Fabricio"
    },
    {
        "phone_number": "555499452225",
        "public_name": "Jo"
    },
    {
        "phone_number": "555581214107",
        "public_name": "Argos"
    },
    {
        "phone_number": "557799482169",
        "public_name": "Beti"
    },
    {
        "phone_number": "554799599999",
        "public_name": "Augusto"
    },
    {
        "phone_number": "554799188203",
        "public_name": "Donizetti"
    },
    {
        "phone_number": "554196527321",
        "public_name": "Gabriela"
    },
    {
        "phone_number": "554399557400",
        "public_name": "Felipe"
    },
    {
        "phone_number": "556282411263",
        "public_name": "Alysom"
    },
    {
        "phone_number": "554796054999",
        "public_name": "Shirley"
    },
    {
        "phone_number": "554198932966",
        "public_name": "Luiz"
    },
    {
        "phone_number": "557799842090",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554299724410",
        "public_name": "Luis/Beatriz"
    },
    {
        "phone_number": "554199713490",
        "public_name": "Joao"
    },
    {
        "phone_number": "554791087187",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554799823231",
        "public_name": "Delcio"
    },
    {
        "phone_number": "555597006785",
        "public_name": "Elaine"
    },
    {
        "phone_number": "554199219085",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554799832139",
        "public_name": "Renaldo"
    },
    {
        "phone_number": "555591349172",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554299237187",
        "public_name": "Dinilda"
    },
    {
        "phone_number": "554791022265",
        "public_name": "Dody"
    },
    {
        "phone_number": "554796525425",
        "public_name": "Keila"
    },
    {
        "phone_number": "554799999737",
        "public_name": "Shirley"
    },
    {
        "phone_number": "554199358490",
        "public_name": "Natasha"
    },
    {
        "phone_number": "554797008847",
        "public_name": "Maura"
    },
    {
        "phone_number": "555499001342",
        "public_name": "Elisandra"
    },
    {
        "phone_number": "554799988820",
        "public_name": "Vania"
    },
    {
        "phone_number": "554784742287",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554799850385",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554799210023",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554184038584",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "556692062310",
        "public_name": "Arlene"
    },
    {
        "phone_number": "554499019140",
        "public_name": "Carol"
    },
    {
        "phone_number": "554899613100",
        "public_name": "Newton"
    },
    {
        "phone_number": "555499349070",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554791563485",
        "public_name": "Emidio"
    },
    {
        "phone_number": "554191048225",
        "public_name": "Geraldo"
    },
    {
        "phone_number": "554999472257",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554188613601",
        "public_name": "Juarez"
    },
    {
        "phone_number": "554791966004",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554797165884",
        "public_name": "Valeria"
    },
    {
        "phone_number": "554796347312",
        "public_name": "Shirlei"
    },
    {
        "phone_number": "554999472526",
        "public_name": "Jane"
    },
    {
        "phone_number": "554199148685",
        "public_name": "Isabela"
    },
    {
        "phone_number": "554799375999",
        "public_name": "Fernanda"
    },
    {
        "phone_number": "555192129981",
        "public_name": "Milene"
    },
    {
        "phone_number": "554796724742",
        "public_name": "Aline"
    },
    {
        "phone_number": "554196190666",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554799579057",
        "public_name": "Joice"
    },
    {
        "phone_number": "555499761132",
        "public_name": "Michel"
    },
    {
        "phone_number": "554788346824",
        "public_name": "Pedro"
    },
    {
        "phone_number": "554199953146",
        "public_name": "Maurício"
    },
    {
        "phone_number": "555591187789",
        "public_name": "Kamila"
    },
    {
        "phone_number": "554799212018",
        "public_name": "Cyrus"
    },
    {
        "phone_number": "555196661199",
        "public_name": "Marlete"
    },
    {
        "phone_number": "555599979650",
        "public_name": "Jaime"
    },
    {
        "phone_number": "553189890696",
        "public_name": "Maria"
    },
    {
        "phone_number": "554899699847",
        "public_name": "Íris"
    },
    {
        "phone_number": "553184174715",
        "public_name": "José"
    },
    {
        "phone_number": "555181186077",
        "public_name": "Gislai"
    },
    {
        "phone_number": "554299750808",
        "public_name": "Ragli"
    },
    {
        "phone_number": "554799772069",
        "public_name": "Lirio"
    },
    {
        "phone_number": "557399194848",
        "public_name": "Flávio"
    },
    {
        "phone_number": "554797403044",
        "public_name": "Marilena"
    },
    {
        "phone_number": "554791269286",
        "public_name": "Marcinho"
    },
    {
        "phone_number": "554896112642",
        "public_name": "Lauro"
    },
    {
        "phone_number": "554799656818",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554196700298",
        "public_name": "Lysandro"
    },
    {
        "phone_number": "554792010787",
        "public_name": "Méri"
    },
    {
        "phone_number": "554691233317",
        "public_name": "Sandra"
    },
    {
        "phone_number": "555184661892",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554699119095",
        "public_name": "Robson"
    },
    {
        "phone_number": "554899429022",
        "public_name": "Marcio"
    },
    {
        "phone_number": "554396241896",
        "public_name": "Samir"
    },
    {
        "phone_number": "554499209139",
        "public_name": "Felippe"
    },
    {
        "phone_number": "554788198666",
        "public_name": "Artur"
    },
    {
        "phone_number": "554888063656",
        "public_name": "Jeferson"
    },
    {
        "phone_number": "554799772930",
        "public_name": "Moacir"
    },
    {
        "phone_number": "554399150202",
        "public_name": "Zé"
    },
    {
        "phone_number": "554498398787",
        "public_name": "Paulo"
    },
    {
        "phone_number": "555381341854",
        "public_name": "Huda"
    },
    {
        "phone_number": "554199944955",
        "public_name": "JoãCarlos"
    },
    {
        "phone_number": "5511996111519",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554196119151",
        "public_name": "Laura"
    },
    {
        "phone_number": "554799650380",
        "public_name": "Silvio"
    },
    {
        "phone_number": "554796857034",
        "public_name": "Belliani"
    },
    {
        "phone_number": "554499820242",
        "public_name": "Ralph"
    },
    {
        "phone_number": "554799553410",
        "public_name": "Lilian"
    },
    {
        "phone_number": "554384065000",
        "public_name": "Willian"
    },
    {
        "phone_number": "554784083084",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554799121556",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "554399229159",
        "public_name": "Tânia"
    },
    {
        "phone_number": "554799189006",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "554299305566",
        "public_name": "Alandra"
    },
    {
        "phone_number": "555499941009",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554799835100",
        "public_name": "Zaga"
    },
    {
        "phone_number": "555596743706",
        "public_name": "Lauri"
    },
    {
        "phone_number": "554396150700",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "555599266641",
        "public_name": "Jacinto"
    },
    {
        "phone_number": "554784874707",
        "public_name": "Valdir"
    },
    {
        "phone_number": "554391242200",
        "public_name": "Maria"
    },
    {
        "phone_number": "554799878880",
        "public_name": "Jorge"
    },
    {
        "phone_number": "554196012358",
        "public_name": "Valdir"
    },
    {
        "phone_number": "554791448060",
        "public_name": "Daniela"
    },
    {
        "phone_number": "555499193606",
        "public_name": "Luciane"
    },
    {
        "phone_number": "555481197978",
        "public_name": "Aguinaldo"
    },
    {
        "phone_number": "554796561477",
        "public_name": "Sabrina"
    },
    {
        "phone_number": "554199329763",
        "public_name": "Junior"
    },
    {
        "phone_number": "554199718330",
        "public_name": "Marco"
    },
    {
        "phone_number": "554884083609",
        "public_name": "Fernanda"
    },
    {
        "phone_number": "554988372922",
        "public_name": "André"
    },
    {
        "phone_number": "554896330735",
        "public_name": "Proprietário"
    },
    {
        "phone_number": "554898673731",
        "public_name": "Paulinha"
    },
    {
        "phone_number": "554788494553",
        "public_name": "Klaus"
    },
    {
        "phone_number": "554791056121",
        "public_name": "Zilma"
    },
    {
        "phone_number": "554799833598",
        "public_name": "Silvia"
    },
    {
        "phone_number": "554796525424",
        "public_name": "Claudir"
    },
    {
        "phone_number": "554799565946",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554784660617",
        "public_name": "Tiago"
    },
    {
        "phone_number": "554797841414",
        "public_name": "Nilson"
    },
    {
        "phone_number": "5519981660908",
        "public_name": "Rudner"
    },
    {
        "phone_number": "554799737679",
        "public_name": "Nestor"
    },
    {
        "phone_number": "555499946909",
        "public_name": "Edgar"
    },
    {
        "phone_number": "554198356578",
        "public_name": "Elaine"
    },
    {
        "phone_number": "555198436696",
        "public_name": "Augusto"
    },
    {
        "phone_number": "555499957788",
        "public_name": "Waleska"
    },
    {
        "phone_number": "554797120712",
        "public_name": "Larissa"
    },
    {
        "phone_number": "554797172332",
        "public_name": "Carmem"
    },
    {
        "phone_number": "554799964079",
        "public_name": "José"
    },
    {
        "phone_number": "554198890555",
        "public_name": "Leticia"
    },
    {
        "phone_number": "554191178119",
        "public_name": "Gisele"
    },
    {
        "phone_number": "554796265621",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554791400088",
        "public_name": "David"
    },
    {
        "phone_number": "554788362708",
        "public_name": "Charles"
    },
    {
        "phone_number": "5521970312397",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "556592560200",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554797030000",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554791086844",
        "public_name": "Suziani"
    },
    {
        "phone_number": "554499369191",
        "public_name": "Junior"
    },
    {
        "phone_number": "554199122164",
        "public_name": "Adriano"
    },
    {
        "phone_number": "554196501114",
        "public_name": "Paulo"
    },
    {
        "phone_number": "556183536868",
        "public_name": "Karina"
    },
    {
        "phone_number": "554799845571",
        "public_name": "Vili"
    },
    {
        "phone_number": "555195537788",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "556599037708",
        "public_name": "Heloisa"
    },
    {
        "phone_number": "555197565546",
        "public_name": "Suellen"
    },
    {
        "phone_number": "554391571966",
        "public_name": "Oscar"
    },
    {
        "phone_number": "555182602602",
        "public_name": "Cleia"
    },
    {
        "phone_number": "555484471936",
        "public_name": "Danieli"
    },
    {
        "phone_number": "556696854121",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554791134982",
        "public_name": "Edgar"
    },
    {
        "phone_number": "554799980154",
        "public_name": "Maikon"
    },
    {
        "phone_number": "554784348455",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554799057724",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554991078268",
        "public_name": "Priscila"
    },
    {
        "phone_number": "554788033440",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554899780729",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "555492678166",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554791157054",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554796006566",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554198783399",
        "public_name": "Nivaldo"
    },
    {
        "phone_number": "554988292969",
        "public_name": "Renato"
    },
    {
        "phone_number": "554796281010",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554198313541",
        "public_name": "Jean"
    },
    {
        "phone_number": "554791614794",
        "public_name": "Alana"
    },
    {
        "phone_number": "5511998339822",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554799826766",
        "public_name": "Dani"
    },
    {
        "phone_number": "554799191340",
        "public_name": "Alexandro"
    },
    {
        "phone_number": "554791950004",
        "public_name": "Robson"
    },
    {
        "phone_number": "555496094717",
        "public_name": "Airton"
    },
    {
        "phone_number": "555481077000",
        "public_name": "Silvio"
    },
    {
        "phone_number": "555496372326",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554784632797",
        "public_name": "Cleuso"
    },
    {
        "phone_number": "554791193693",
        "public_name": "Gilvan"
    },
    {
        "phone_number": "554792081501",
        "public_name": "Ezidoro"
    },
    {
        "phone_number": "554999881192",
        "public_name": "Isabel"
    },
    {
        "phone_number": "554699741498",
        "public_name": "Loraine"
    },
    {
        "phone_number": "554796220807",
        "public_name": "Geva"
    },
    {
        "phone_number": "554792541208",
        "public_name": "Cirlene"
    },
    {
        "phone_number": "554796213167",
        "public_name": "Adrian"
    },
    {
        "phone_number": "5511935051600",
        "public_name": "Tania"
    },
    {
        "phone_number": "554499911036",
        "public_name": "Elder"
    },
    {
        "phone_number": "554888154750",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554796701190",
        "public_name": "Jarrison"
    },
    {
        "phone_number": "554899776688",
        "public_name": "Joao"
    },
    {
        "phone_number": "554388289701",
        "public_name": "Gilberto"
    },
    {
        "phone_number": "5513997335616",
        "public_name": "House"
    },
    {
        "phone_number": "555499860516",
        "public_name": "Celcio"
    },
    {
        "phone_number": "555484039472",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554799468822",
        "public_name": "Indianara"
    },
    {
        "phone_number": "555191146399",
        "public_name": "Vera"
    },
    {
        "phone_number": "555596824914",
        "public_name": "Tarso"
    },
    {
        "phone_number": "555491425398",
        "public_name": "Mauricio"
    },
    {
        "phone_number": "554188586313",
        "public_name": "Marcia"
    },
    {
        "phone_number": "5511991117014",
        "public_name": "Derocilia"
    },
    {
        "phone_number": "554199867474",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554792445115",
        "public_name": "Vanise"
    },
    {
        "phone_number": "554899279320",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554599881027",
        "public_name": "Leandro"
    },
    {
        "phone_number": "555491121042",
        "public_name": "José"
    },
    {
        "phone_number": "554999858080",
        "public_name": "Cézar"
    },
    {
        "phone_number": "554699125453",
        "public_name": "Juari"
    },
    {
        "phone_number": "554599608436",
        "public_name": "Anny"
    },
    {
        "phone_number": "554899111115",
        "public_name": "Saulo"
    },
    {
        "phone_number": "554796161111",
        "public_name": "Josiane"
    },
    {
        "phone_number": "554133020090",
        "public_name": "ProprietarioAfonso"
    },
    {
        "phone_number": "554191273737",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554399914253",
        "public_name": "Rosane"
    },
    {
        "phone_number": "554384442727",
        "public_name": "Ana"
    },
    {
        "phone_number": "554799199196",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554399604000",
        "public_name": "Adriano"
    },
    {
        "phone_number": "555399947257",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "554784086749",
        "public_name": "Arno"
    },
    {
        "phone_number": "554799922761",
        "public_name": "Vanderlea"
    },
    {
        "phone_number": "555199625600",
        "public_name": "Paulo"
    },
    {
        "phone_number": "5521995636167",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554799689899",
        "public_name": "Roni"
    },
    {
        "phone_number": "554799238330",
        "public_name": "Luis"
    },
    {
        "phone_number": "554796214406",
        "public_name": "Louri"
    },
    {
        "phone_number": "555596773570",
        "public_name": "Geraldino"
    },
    {
        "phone_number": "554196440933",
        "public_name": "Fabiano"
    },
    {
        "phone_number": "554191435224",
        "public_name": "Michel"
    },
    {
        "phone_number": "554796470085",
        "public_name": "Cristiane"
    },
    {
        "phone_number": "555599702728",
        "public_name": "Ana"
    },
    {
        "phone_number": "554991275350",
        "public_name": "Fabiana"
    },
    {
        "phone_number": "554199736709",
        "public_name": "Valdecir"
    },
    {
        "phone_number": "554591224242",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554784121416",
        "public_name": "Paulo"
    },
    {
        "phone_number": "5519991338392",
        "public_name": "Robson"
    },
    {
        "phone_number": "554196752828",
        "public_name": "Werlang"
    },
    {
        "phone_number": "554188067036",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554796165542",
        "public_name": "Carina"
    },
    {
        "phone_number": "554498007776",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554799993868",
        "public_name": "Arno"
    },
    {
        "phone_number": "554196440836",
        "public_name": "Perini"
    },
    {
        "phone_number": "554196894363",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554784252140",
        "public_name": "Silas"
    },
    {
        "phone_number": "554188968361",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554797231532",
        "public_name": "Jose"
    },
    {
        "phone_number": "555496414319",
        "public_name": "Rayssa"
    },
    {
        "phone_number": "554791880900",
        "public_name": "Isabel"
    },
    {
        "phone_number": "5511981382224",
        "public_name": "Helo"
    },
    {
        "phone_number": "555381123464",
        "public_name": "Maicon"
    },
    {
        "phone_number": "5511966018365",
        "public_name": "Roberto"
    },
    {
        "phone_number": "555496616513",
        "public_name": "Vera"
    },
    {
        "phone_number": "554497549177",
        "public_name": "Daiane"
    },
    {
        "phone_number": "554896247021",
        "public_name": "Edson"
    },
    {
        "phone_number": "554299910333",
        "public_name": "Denis"
    },
    {
        "phone_number": "554199028211",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554799447991",
        "public_name": "Cesar"
    },
    {
        "phone_number": "555196398816",
        "public_name": "Francielli"
    },
    {
        "phone_number": "554799616371",
        "public_name": "Jose"
    },
    {
        "phone_number": "554799837337",
        "public_name": "Alfredo"
    },
    {
        "phone_number": "554799337228",
        "public_name": "Eraldo"
    },
    {
        "phone_number": "556684610415",
        "public_name": "Eldorado"
    },
    {
        "phone_number": "554899716565",
        "public_name": "Ana"
    },
    {
        "phone_number": "554196526150",
        "public_name": "Rafa"
    },
    {
        "phone_number": "554799830231",
        "public_name": "Rui"
    },
    {
        "phone_number": "554791628005",
        "public_name": "Marli"
    },
    {
        "phone_number": "554899928860",
        "public_name": "Aurelio"
    },
    {
        "phone_number": "554788169998",
        "public_name": "Douglas"
    },
    {
        "phone_number": "554599148696",
        "public_name": "Vanderlei"
    },
    {
        "phone_number": "554792310083",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554191214000",
        "public_name": "Aluisio"
    },
    {
        "phone_number": "554799879306",
        "public_name": "Creuza"
    },
    {
        "phone_number": "555196043009",
        "public_name": "Naira"
    },
    {
        "phone_number": "554399550460",
        "public_name": "Neto"
    },
    {
        "phone_number": "554991976111",
        "public_name": "Rose"
    },
    {
        "phone_number": "554796633388",
        "public_name": "Junior"
    },
    {
        "phone_number": "555499144433",
        "public_name": "Maria"
    },
    {
        "phone_number": "554799782210",
        "public_name": "Marcio"
    },
    {
        "phone_number": "5524999181968",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554484088906",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554498261983",
        "public_name": "Gabriela"
    },
    {
        "phone_number": "554899359198",
        "public_name": "Magda"
    },
    {
        "phone_number": "554899830080",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554788180355",
        "public_name": "Lisandro"
    },
    {
        "phone_number": "554899765141",
        "public_name": "Robe"
    },
    {
        "phone_number": "554799021644",
        "public_name": "Alessandra"
    },
    {
        "phone_number": "554792241471",
        "public_name": "Alfred"
    },
    {
        "phone_number": "554299472023",
        "public_name": "Érica"
    },
    {
        "phone_number": "554796157147",
        "public_name": "Méri"
    },
    {
        "phone_number": "554784144658",
        "public_name": "Samili"
    },
    {
        "phone_number": "554498129441",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554288633616",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "555182016368",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554391411415",
        "public_name": "Tania"
    },
    {
        "phone_number": "554796884228",
        "public_name": "Lyz"
    },
    {
        "phone_number": "5521969733273",
        "public_name": "Georgea"
    },
    {
        "phone_number": "554199766757",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554599847363",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554191024232",
        "public_name": "Abdo"
    },
    {
        "phone_number": "555491177241",
        "public_name": "Karol"
    },
    {
        "phone_number": "554796855210",
        "public_name": "Tatiana"
    },
    {
        "phone_number": "554799713869",
        "public_name": "Eliane"
    },
    {
        "phone_number": "554196145082",
        "public_name": "Mauricio"
    },
    {
        "phone_number": "555192421792",
        "public_name": "Pati"
    },
    {
        "phone_number": "554991461095",
        "public_name": "Mariani"
    },
    {
        "phone_number": "554799814299",
        "public_name": "William"
    },
    {
        "phone_number": "554796729126",
        "public_name": "Junior"
    },
    {
        "phone_number": "554792064837",
        "public_name": "Alex"
    },
    {
        "phone_number": "554391938050",
        "public_name": "Helio"
    },
    {
        "phone_number": "5491161937856",
        "public_name": "Lukas"
    },
    {
        "phone_number": "554399722829",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "554799237766",
        "public_name": "Felipe"
    },
    {
        "phone_number": "555491561976",
        "public_name": "Osmar"
    },
    {
        "phone_number": "554799890488",
        "public_name": "Simone"
    },
    {
        "phone_number": "554797636666",
        "public_name": "Valdir"
    },
    {
        "phone_number": "5527992039016",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554499559998",
        "public_name": "Milena"
    },
    {
        "phone_number": "5511968682594",
        "public_name": "Juci"
    },
    {
        "phone_number": "554999834440",
        "public_name": "Arnildo"
    },
    {
        "phone_number": "595985443099",
        "public_name": "Dhones"
    },
    {
        "phone_number": "556792757656",
        "public_name": "Maikon"
    },
    {
        "phone_number": "555499410841",
        "public_name": "Gilda"
    },
    {
        "phone_number": "554199118866",
        "public_name": "Francielle"
    },
    {
        "phone_number": "554788040027",
        "public_name": "Simone"
    },
    {
        "phone_number": "554784983147",
        "public_name": "Marlon"
    },
    {
        "phone_number": "554188315456",
        "public_name": "Jonas"
    },
    {
        "phone_number": "5517992121211",
        "public_name": "Marcus"
    },
    {
        "phone_number": "554799747574",
        "public_name": "Fabricia"
    },
    {
        "phone_number": "554799696677",
        "public_name": "Gilmar"
    },
    {
        "phone_number": "554799834400",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554799231311",
        "public_name": "Valdir"
    },
    {
        "phone_number": "555491299325",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554891607974",
        "public_name": "Agri"
    },
    {
        "phone_number": "554788024912",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554792224080",
        "public_name": "Willian"
    },
    {
        "phone_number": "554199438333",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554796622872",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554388292050",
        "public_name": "Silvia"
    },
    {
        "phone_number": "555181778711",
        "public_name": "Suelen"
    },
    {
        "phone_number": "554991434010",
        "public_name": "Helio"
    },
    {
        "phone_number": "554788360851",
        "public_name": "Lucas"
    },
    {
        "phone_number": "554396331655",
        "public_name": "Miquéias"
    },
    {
        "phone_number": "555491658775",
        "public_name": "Milton"
    },
    {
        "phone_number": "554796600324",
        "public_name": "Paula"
    },
    {
        "phone_number": "554195387005",
        "public_name": "Frank"
    },
    {
        "phone_number": "554796368566",
        "public_name": "Lidiana"
    },
    {
        "phone_number": "554799832474",
        "public_name": "Peixoto"
    },
    {
        "phone_number": "554195948870",
        "public_name": "Joao"
    },
    {
        "phone_number": "554499909446",
        "public_name": "Maria"
    },
    {
        "phone_number": "554796800064",
        "public_name": "Renan"
    },
    {
        "phone_number": "554899430222",
        "public_name": "Israel"
    },
    {
        "phone_number": "554788042203",
        "public_name": "Antonio"
    },
    {
        "phone_number": "556596426769",
        "public_name": "Fabiola"
    },
    {
        "phone_number": "555596388092",
        "public_name": "Cristiano"
    },
    {
        "phone_number": "554799795205",
        "public_name": "AbrahãAlfredo"
    },
    {
        "phone_number": "555597247977",
        "public_name": "Kelvin"
    },
    {
        "phone_number": "555184596353",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554796132252",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554291161017",
        "public_name": "Angelo"
    },
    {
        "phone_number": "554788513240",
        "public_name": "Thiago"
    },
    {
        "phone_number": "555499460046",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554791539969",
        "public_name": "Gilvan"
    },
    {
        "phone_number": "554799275903",
        "public_name": "Roberto"
    },
    {
        "phone_number": "553898135758",
        "public_name": "Juliana"
    },
    {
        "phone_number": "554799643038",
        "public_name": "Erika"
    },
    {
        "phone_number": "555584546218",
        "public_name": "Cleiton"
    },
    {
        "phone_number": "555193118215",
        "public_name": "Pablo"
    },
    {
        "phone_number": "554196438618",
        "public_name": "Alfred"
    },
    {
        "phone_number": "554899627711",
        "public_name": "Henrique"
    },
    {
        "phone_number": "554792690816",
        "public_name": "Cintia"
    },
    {
        "phone_number": "5511993224110",
        "public_name": "Ilson"
    },
    {
        "phone_number": "554198419842",
        "public_name": "Rosemar"
    },
    {
        "phone_number": "554789006715",
        "public_name": "Ana"
    },
    {
        "phone_number": "5511949702080",
        "public_name": "Alessandra"
    },
    {
        "phone_number": "554799530310",
        "public_name": "Denise"
    },
    {
        "phone_number": "554199386613",
        "public_name": "Leonilda"
    },
    {
        "phone_number": "554799673833",
        "public_name": "Juvani"
    },
    {
        "phone_number": "554791921313",
        "public_name": "Dani"
    },
    {
        "phone_number": "554188986276",
        "public_name": "Silmara"
    },
    {
        "phone_number": "554199740506",
        "public_name": "Emir"
    },
    {
        "phone_number": "556984667171",
        "public_name": "Sandro"
    },
    {
        "phone_number": "554192332564",
        "public_name": "Gil"
    },
    {
        "phone_number": "554799687929",
        "public_name": "Jessica"
    },
    {
        "phone_number": "554797078151",
        "public_name": "Nilson"
    },
    {
        "phone_number": "554799830665",
        "public_name": "Adulcio"
    },
    {
        "phone_number": "556191734101",
        "public_name": "Paulo"
    },
    {
        "phone_number": "555199226068",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554797108080",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554299973113",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554796215146",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554699101531",
        "public_name": "Eunice"
    },
    {
        "phone_number": "554799710321",
        "public_name": "Carlos"
    },
    {
        "phone_number": "556599080109",
        "public_name": "Adriano"
    },
    {
        "phone_number": "554792061087",
        "public_name": "Yeda"
    },
    {
        "phone_number": "554791357443",
        "public_name": "Sidnei"
    },
    {
        "phone_number": "554188943330",
        "public_name": "Silvio"
    },
    {
        "phone_number": "554388064858",
        "public_name": "Valdecir"
    },
    {
        "phone_number": "554784471112",
        "public_name": "Yeda"
    },
    {
        "phone_number": "554499161261",
        "public_name": "Irene"
    },
    {
        "phone_number": "554199531810",
        "public_name": "Volnei"
    },
    {
        "phone_number": "554799010368",
        "public_name": "Rose"
    },
    {
        "phone_number": "554399358001",
        "public_name": "Junior"
    },
    {
        "phone_number": "555596412806",
        "public_name": "Alessandra"
    },
    {
        "phone_number": "554791818986",
        "public_name": "Paulo"
    },
    {
        "phone_number": "555499778989",
        "public_name": "Angelisa"
    },
    {
        "phone_number": "554497764689",
        "public_name": "Dayane"
    },
    {
        "phone_number": "554299251857",
        "public_name": "Itamar"
    },
    {
        "phone_number": "555481332231",
        "public_name": "Jean"
    },
    {
        "phone_number": "554784552949",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554796191425",
        "public_name": "Suzana"
    },
    {
        "phone_number": "554791350555",
        "public_name": "Renzo"
    },
    {
        "phone_number": "554299001069",
        "public_name": "arcus"
    },
    {
        "phone_number": "554199964243",
        "public_name": "Jorge"
    },
    {
        "phone_number": "554999146370",
        "public_name": "Analu"
    },
    {
        "phone_number": "554799276868",
        "public_name": "Alex"
    },
    {
        "phone_number": "554799870760",
        "public_name": "Salomar"
    },
    {
        "phone_number": "554896127953",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554199607711",
        "public_name": "Jeferson"
    },
    {
        "phone_number": "554196886116",
        "public_name": "Joares"
    },
    {
        "phone_number": "5518997292253",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554799971414",
        "public_name": "Shirley"
    },
    {
        "phone_number": "554498356768",
        "public_name": "Mauro"
    },
    {
        "phone_number": "555499833444",
        "public_name": "Ademir"
    },
    {
        "phone_number": "554196119173",
        "public_name": "Fabio"
    },
    {
        "phone_number": "5511985249279",
        "public_name": "Nelson"
    },
    {
        "phone_number": "554491195757",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554799668449",
        "public_name": "Elis"
    },
    {
        "phone_number": "554999660282",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554499402751",
        "public_name": "Shirley"
    },
    {
        "phone_number": "555591685548",
        "public_name": "Rochelli"
    },
    {
        "phone_number": "554199780062",
        "public_name": "Arthur"
    },
    {
        "phone_number": "554999831150",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554788079996",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554791021110",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554499964121",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554799890701",
        "public_name": "Homero"
    },
    {
        "phone_number": "554196212131",
        "public_name": "Fernando"
    },
    {
        "phone_number": "555497012944",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554799627596",
        "public_name": "Joao"
    },
    {
        "phone_number": "554198593552",
        "public_name": "Tiago"
    },
    {
        "phone_number": "554791052204",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "556182179100",
        "public_name": "Marco"
    },
    {
        "phone_number": "554192851870",
        "public_name": "Daniela"
    },
    {
        "phone_number": "554796342992",
        "public_name": "Proprietário"
    },
    {
        "phone_number": "554599169102",
        "public_name": "Sissi"
    },
    {
        "phone_number": "555499985690",
        "public_name": "Mauro"
    },
    {
        "phone_number": "554988329939",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "5511971775017",
        "public_name": "Gelson"
    },
    {
        "phone_number": "555181242134",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554799651211",
        "public_name": "Jorge"
    },
    {
        "phone_number": "554199981807",
        "public_name": "Willian"
    },
    {
        "phone_number": "554199637470",
        "public_name": "Talyta"
    },
    {
        "phone_number": "554799110370",
        "public_name": "Giovano"
    },
    {
        "phone_number": "554998274633",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554788051348",
        "public_name": "Palmira"
    },
    {
        "phone_number": "554791170951",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "556796887630",
        "public_name": "Dione"
    },
    {
        "phone_number": "554797191815",
        "public_name": "Alaa"
    },
    {
        "phone_number": "554791132449",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554799762670",
        "public_name": "Vera"
    },
    {
        "phone_number": "554198590099",
        "public_name": "Alex"
    },
    {
        "phone_number": "554791467005",
        "public_name": "Canisio"
    },
    {
        "phone_number": "554797002983",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554188356521",
        "public_name": "Gisele"
    },
    {
        "phone_number": "554195866531",
        "public_name": "Diego"
    },
    {
        "phone_number": "554799002960",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "5519981479963",
        "public_name": "Fagner"
    },
    {
        "phone_number": "555584024838",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554796096539",
        "public_name": "Juliana"
    },
    {
        "phone_number": "554691036866",
        "public_name": "Olacir"
    },
    {
        "phone_number": "554799209550",
        "public_name": "JoãAloisio"
    },
    {
        "phone_number": "556581267117",
        "public_name": "Jessica"
    },
    {
        "phone_number": "555384182858",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554299252100",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554899566619",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "555599285848",
        "public_name": "Neiva"
    },
    {
        "phone_number": "554288267005",
        "public_name": "Marina"
    },
    {
        "phone_number": "554791760292",
        "public_name": "Edison"
    },
    {
        "phone_number": "554799750009",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554799830004",
        "public_name": "Airton"
    },
    {
        "phone_number": "554891064971",
        "public_name": "Marilia"
    },
    {
        "phone_number": "554784232345",
        "public_name": "Orlando"
    },
    {
        "phone_number": "554499728607",
        "public_name": "Valter"
    },
    {
        "phone_number": "554199436261",
        "public_name": "Deolinda"
    },
    {
        "phone_number": "554299727200",
        "public_name": "Silney"
    },
    {
        "phone_number": "554497677287",
        "public_name": "Ligia"
    },
    {
        "phone_number": "554799256224",
        "public_name": "Batista"
    },
    {
        "phone_number": "556681257161",
        "public_name": "Regina"
    },
    {
        "phone_number": "554498508102",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554898450070",
        "public_name": "Dejair"
    },
    {
        "phone_number": "554796445448",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554799117384",
        "public_name": "Roseli"
    },
    {
        "phone_number": "555196751027",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554791197002",
        "public_name": "Liliam"
    },
    {
        "phone_number": "554799234277",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554799859257",
        "public_name": "Celso"
    },
    {
        "phone_number": "555496171734",
        "public_name": "Wilker"
    },
    {
        "phone_number": "554797158008",
        "public_name": "Gelson"
    },
    {
        "phone_number": "554188213773",
        "public_name": "Samir"
    },
    {
        "phone_number": "554799900878",
        "public_name": "Adriano"
    },
    {
        "phone_number": "554684013798",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554791602899",
        "public_name": "Aldo"
    },
    {
        "phone_number": "554684136080",
        "public_name": "Wilson"
    },
    {
        "phone_number": "5521968109989",
        "public_name": "Ivo"
    },
    {
        "phone_number": "554799430660",
        "public_name": "Zé"
    },
    {
        "phone_number": "554788599818",
        "public_name": "Omar"
    },
    {
        "phone_number": "554791664734",
        "public_name": "Carol"
    },
    {
        "phone_number": "554199959999",
        "public_name": "Heitor"
    },
    {
        "phone_number": "554784180338",
        "public_name": "Henrique"
    },
    {
        "phone_number": "554791032077",
        "public_name": "Gelson"
    },
    {
        "phone_number": "554199155056",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554391666530",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "555481152105",
        "public_name": "Carlitos"
    },
    {
        "phone_number": "554791937979",
        "public_name": "Gelson"
    },
    {
        "phone_number": "554799445561",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554591171712",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554999832914",
        "public_name": "Margarete"
    },
    {
        "phone_number": "554796517272",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554799651692",
        "public_name": "Marcia"
    },
    {
        "phone_number": "554198952020",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554791530397",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554399774277",
        "public_name": "Renato"
    },
    {
        "phone_number": "556892535222",
        "public_name": "Ires"
    },
    {
        "phone_number": "554999177048",
        "public_name": "Carol"
    },
    {
        "phone_number": "554784823732",
        "public_name": "Maicon"
    },
    {
        "phone_number": "554799632312",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554796115059",
        "public_name": "Germano"
    },
    {
        "phone_number": "554599451072",
        "public_name": "Fabiane"
    },
    {
        "phone_number": "5514988031764",
        "public_name": "Andrez"
    },
    {
        "phone_number": "554591048670",
        "public_name": "Edson"
    },
    {
        "phone_number": "554796168973",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554684030380",
        "public_name": "Angela"
    },
    {
        "phone_number": "554384382828",
        "public_name": "Toninho"
    },
    {
        "phone_number": "554799891583",
        "public_name": "Ivanildo"
    },
    {
        "phone_number": "554797830083",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "554199216026",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554498492994",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554796814000",
        "public_name": "Wilson"
    },
    {
        "phone_number": "555181949383",
        "public_name": "Julio"
    },
    {
        "phone_number": "554791710801",
        "public_name": "Manoel"
    },
    {
        "phone_number": "554784189502",
        "public_name": "Cristhianne"
    },
    {
        "phone_number": "554792587110",
        "public_name": "Mauricio"
    },
    {
        "phone_number": "554799664595",
        "public_name": "Matheus"
    },
    {
        "phone_number": "554599591011",
        "public_name": "Adriana"
    },
    {
        "phone_number": "554788017878",
        "public_name": "Ana"
    },
    {
        "phone_number": "554799353919",
        "public_name": "Antonio"
    },
    {
        "phone_number": "555596764430",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554799583903",
        "public_name": "Joao"
    },
    {
        "phone_number": "554791830944",
        "public_name": "Wilma"
    },
    {
        "phone_number": "554799479062",
        "public_name": "Vinitus"
    },
    {
        "phone_number": "556699854292",
        "public_name": "Jonas"
    },
    {
        "phone_number": "554999732531",
        "public_name": "Juliana"
    },
    {
        "phone_number": "556181043653",
        "public_name": "Igor"
    },
    {
        "phone_number": "554799178249",
        "public_name": "Alisson"
    },
    {
        "phone_number": "554888284547",
        "public_name": "Jussara"
    },
    {
        "phone_number": "554799955612",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554799802406",
        "public_name": "Ronaldo"
    },
    {
        "phone_number": "555199775436",
        "public_name": "Maira"
    },
    {
        "phone_number": "554796098382",
        "public_name": "Eloa"
    },
    {
        "phone_number": "555491423013",
        "public_name": "Celso"
    },
    {
        "phone_number": "555199958293",
        "public_name": "Fernando"
    },
    {
        "phone_number": "555197012588",
        "public_name": "Ester"
    },
    {
        "phone_number": "554396392375",
        "public_name": "Kaue"
    },
    {
        "phone_number": "554799672007",
        "public_name": "Maria"
    },
    {
        "phone_number": "554799777897",
        "public_name": "Vanessa"
    },
    {
        "phone_number": "554799534000",
        "public_name": "Edson"
    },
    {
        "phone_number": "554999861105",
        "public_name": "Claudia"
    },
    {
        "phone_number": "554298577906",
        "public_name": "Gilherme"
    },
    {
        "phone_number": "5522981032248",
        "public_name": "Victor"
    },
    {
        "phone_number": "554797882525",
        "public_name": "Mônica"
    },
    {
        "phone_number": "554791458991",
        "public_name": "Sell"
    },
    {
        "phone_number": "554197410004",
        "public_name": "Joana"
    },
    {
        "phone_number": "554299730456",
        "public_name": "Florinda"
    },
    {
        "phone_number": "555481159341",
        "public_name": "Jones"
    },
    {
        "phone_number": "556791302060",
        "public_name": "Alex"
    },
    {
        "phone_number": "554999813077",
        "public_name": "Deize"
    },
    {
        "phone_number": "554999615550",
        "public_name": "Julian"
    },
    {
        "phone_number": "554799739872",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554999962450",
        "public_name": "Janete"
    },
    {
        "phone_number": "554197311706",
        "public_name": "Anderson"
    },
    {
        "phone_number": "554499260089",
        "public_name": "Gislaine"
    },
    {
        "phone_number": "554792412040",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554188596773",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554195881029",
        "public_name": "Jean"
    },
    {
        "phone_number": "554799858932",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554184488862",
        "public_name": "Edson"
    },
    {
        "phone_number": "554796334127",
        "public_name": "Tallyne"
    },
    {
        "phone_number": "554799923007",
        "public_name": "Pamella"
    },
    {
        "phone_number": "554191399082",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "556999037397",
        "public_name": "Daniela"
    },
    {
        "phone_number": "5517997364170",
        "public_name": "Alan"
    },
    {
        "phone_number": "5511991519139",
        "public_name": "Edu"
    },
    {
        "phone_number": "554799039180",
        "public_name": "Mika"
    },
    {
        "phone_number": "554796664221",
        "public_name": "Joel"
    },
    {
        "phone_number": "554796365636",
        "public_name": "Fabricio"
    },
    {
        "phone_number": "554799450648",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554488310442",
        "public_name": "Michelly"
    },
    {
        "phone_number": "554891691527",
        "public_name": "Ernani"
    },
    {
        "phone_number": "5521981009492",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554792555521",
        "public_name": "Bernardo"
    },
    {
        "phone_number": "554796052455",
        "public_name": "Mari"
    },
    {
        "phone_number": "554799890012",
        "public_name": "Joao"
    },
    {
        "phone_number": "554788078817",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554899280074",
        "public_name": "Maicon"
    },
    {
        "phone_number": "554192553311",
        "public_name": "Edson"
    },
    {
        "phone_number": "554791941706",
        "public_name": "Jonathan"
    },
    {
        "phone_number": "554191994440",
        "public_name": "Enzo"
    },
    {
        "phone_number": "554792690707",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554184172474",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554198560005",
        "public_name": "Sena"
    },
    {
        "phone_number": "555399714418",
        "public_name": "Regis"
    },
    {
        "phone_number": "555599815371",
        "public_name": "Olmiro"
    },
    {
        "phone_number": "556692276640",
        "public_name": "Debora"
    },
    {
        "phone_number": "554799183642",
        "public_name": "Rangel"
    },
    {
        "phone_number": "554792599948",
        "public_name": "Vinicius"
    },
    {
        "phone_number": "554891373142",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554799737056",
        "public_name": "Edmilson"
    },
    {
        "phone_number": "554799663577",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554999912787",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554796849737",
        "public_name": "Simone"
    },
    {
        "phone_number": "554792189292",
        "public_name": "Aline"
    },
    {
        "phone_number": "554792479253",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554796330845",
        "public_name": "Lourenç"
    },
    {
        "phone_number": "554799889828",
        "public_name": "Milo"
    },
    {
        "phone_number": "554898576214",
        "public_name": "Mario"
    },
    {
        "phone_number": "5521998960491",
        "public_name": "Rui"
    },
    {
        "phone_number": "555499121620",
        "public_name": "Ari"
    },
    {
        "phone_number": "554195700005",
        "public_name": "Alessandro"
    },
    {
        "phone_number": "554788278617",
        "public_name": "Giovani"
    },
    {
        "phone_number": "554299220432",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554691026590",
        "public_name": "Adegir"
    },
    {
        "phone_number": "554791668555",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554174006395",
        "public_name": "Flávio"
    },
    {
        "phone_number": "554791334067",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "554497171812",
        "public_name": "Ianco"
    },
    {
        "phone_number": "554796197004",
        "public_name": "Marianne"
    },
    {
        "phone_number": "554792113661",
        "public_name": "Lara"
    },
    {
        "phone_number": "554784112573",
        "public_name": "Joercir"
    },
    {
        "phone_number": "554884484481",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554288034557",
        "public_name": "Simone"
    },
    {
        "phone_number": "554796527761",
        "public_name": "JoãAndrietti"
    },
    {
        "phone_number": "5511941115152",
        "public_name": "Fabricio"
    },
    {
        "phone_number": "555196078043",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554796586359",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "554799613115",
        "public_name": "Liferson"
    },
    {
        "phone_number": "554799971228",
        "public_name": "Cibele"
    },
    {
        "phone_number": "14075363596",
        "public_name": "Jeni"
    },
    {
        "phone_number": "554799972897",
        "public_name": "Ivan"
    },
    {
        "phone_number": "554799746527",
        "public_name": "Salustiano"
    },
    {
        "phone_number": "554791434444",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554888324928",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554191988700",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554799870060",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554791445664",
        "public_name": "Ney"
    },
    {
        "phone_number": "554699723376",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554796067165",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554199939104",
        "public_name": "Roberta"
    },
    {
        "phone_number": "554791183388",
        "public_name": "Sonia"
    },
    {
        "phone_number": "554799116651",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554499116666",
        "public_name": "Nery"
    },
    {
        "phone_number": "554191333717",
        "public_name": "Maristela"
    },
    {
        "phone_number": "554799320070",
        "public_name": "Doca"
    },
    {
        "phone_number": "554799853643",
        "public_name": "Victor"
    },
    {
        "phone_number": "554185110422",
        "public_name": "Fernanda"
    },
    {
        "phone_number": "554199636100",
        "public_name": "Horley"
    },
    {
        "phone_number": "554799772662",
        "public_name": "Nercy"
    },
    {
        "phone_number": "554796245030",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554199150752",
        "public_name": "Livia"
    },
    {
        "phone_number": "554791138974",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554799851633",
        "public_name": "Renato"
    },
    {
        "phone_number": "555492065661",
        "public_name": "Mauricio"
    },
    {
        "phone_number": "555196865996",
        "public_name": "Cíntia"
    },
    {
        "phone_number": "556799815223",
        "public_name": "Jose"
    },
    {
        "phone_number": "556199858363",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554991661133",
        "public_name": "Sinval"
    },
    {
        "phone_number": "554784982308",
        "public_name": "Marli"
    },
    {
        "phone_number": "556792591172",
        "public_name": "Elmo"
    },
    {
        "phone_number": "554991200808",
        "public_name": "Domingos"
    },
    {
        "phone_number": "554191170773",
        "public_name": "Vilmar"
    },
    {
        "phone_number": "554191219295",
        "public_name": "Ivo"
    },
    {
        "phone_number": "554796776466",
        "public_name": "Geo"
    },
    {
        "phone_number": "554797480458",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554191859990",
        "public_name": "Scheyla"
    },
    {
        "phone_number": "554788051722",
        "public_name": "Carlos"
    },
    {
        "phone_number": "556699853480",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "555198480242",
        "public_name": "Fran"
    },
    {
        "phone_number": "554796340007",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554196846962",
        "public_name": "Otavio"
    },
    {
        "phone_number": "554796813924",
        "public_name": "Romildo"
    },
    {
        "phone_number": "554796492853",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554998061777",
        "public_name": "Youssef"
    },
    {
        "phone_number": "554799189823",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554792626969",
        "public_name": "Cyntia"
    },
    {
        "phone_number": "554684027481",
        "public_name": "Djalmo"
    },
    {
        "phone_number": "5511985888830",
        "public_name": "Nelson"
    },
    {
        "phone_number": "554191930601",
        "public_name": "Marcia"
    },
    {
        "phone_number": "555499132949",
        "public_name": "Eder"
    },
    {
        "phone_number": "554699807549",
        "public_name": "Andrey"
    },
    {
        "phone_number": "554799831963",
        "public_name": "Rodolfo"
    },
    {
        "phone_number": "554796176814",
        "public_name": "Nicolas"
    },
    {
        "phone_number": "554291019060",
        "public_name": "Rosana"
    },
    {
        "phone_number": "555591625356",
        "public_name": "Everton"
    },
    {
        "phone_number": "554799000000",
        "public_name": "Jenifer"
    },
    {
        "phone_number": "554792507711",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554191743333",
        "public_name": "Veronica"
    },
    {
        "phone_number": "554188432693",
        "public_name": "Ade"
    },
    {
        "phone_number": "554791967007",
        "public_name": "EDUARDO"
    },
    {
        "phone_number": "5521982034788",
        "public_name": "Luana"
    },
    {
        "phone_number": "555499187747",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554891325758",
        "public_name": "Roger"
    },
    {
        "phone_number": "554799732808",
        "public_name": "Tatiana"
    },
    {
        "phone_number": "554791313044",
        "public_name": "Silvia"
    },
    {
        "phone_number": "556584656617",
        "public_name": "Shirley"
    },
    {
        "phone_number": "554799838803",
        "public_name": "Arnaldo"
    },
    {
        "phone_number": "554796387231",
        "public_name": "Renata"
    },
    {
        "phone_number": "554499317544",
        "public_name": "Edina"
    },
    {
        "phone_number": "556781513038",
        "public_name": "CMA"
    },
    {
        "phone_number": "554799714944",
        "public_name": "Erlon"
    },
    {
        "phone_number": "5548920006866",
        "public_name": "Emerson"
    },
    {
        "phone_number": "554788128227",
        "public_name": "Claudinei"
    },
    {
        "phone_number": "555181895771",
        "public_name": "Mayara"
    },
    {
        "phone_number": "554999369877",
        "public_name": "Alda"
    },
    {
        "phone_number": "554791871053",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "554598208940",
        "public_name": "Jeferson"
    },
    {
        "phone_number": "554792566617",
        "public_name": "José"
    },
    {
        "phone_number": "554196162835",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554599760569",
        "public_name": "Fabi"
    },
    {
        "phone_number": "554188489727",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554699359536",
        "public_name": "Junior"
    },
    {
        "phone_number": "5512982197530",
        "public_name": "Mister"
    },
    {
        "phone_number": "555499729709",
        "public_name": "Bianca"
    },
    {
        "phone_number": "554796210200",
        "public_name": "Cleiton"
    },
    {
        "phone_number": "554788259846",
        "public_name": "Gym"
    },
    {
        "phone_number": "555199858026",
        "public_name": "Sergio"
    },
    {
        "phone_number": "554499418604",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554799215193",
        "public_name": "Gabriel"
    },
    {
        "phone_number": "554199872997",
        "public_name": "Vanderlei"
    },
    {
        "phone_number": "554388625932",
        "public_name": "Elias"
    },
    {
        "phone_number": "554999187585",
        "public_name": "Aristofolis"
    },
    {
        "phone_number": "5517981336020",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554991609121",
        "public_name": "Su"
    },
    {
        "phone_number": "554188211966",
        "public_name": "Vitor"
    },
    {
        "phone_number": "555481118024",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554792616045",
        "public_name": "Amanda"
    },
    {
        "phone_number": "554791736336",
        "public_name": "Adilson"
    },
    {
        "phone_number": "555499746046",
        "public_name": "Laura"
    },
    {
        "phone_number": "554788099647",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554788356542",
        "public_name": "Wilmar"
    },
    {
        "phone_number": "554199763001",
        "public_name": "Alcione"
    },
    {
        "phone_number": "554796614546",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "554185063140",
        "public_name": "Rubia"
    },
    {
        "phone_number": "555491062290",
        "public_name": "Rossana"
    },
    {
        "phone_number": "554191357755",
        "public_name": "Altivo"
    },
    {
        "phone_number": "554591477771",
        "public_name": "Chadi"
    },
    {
        "phone_number": "554797571147",
        "public_name": "Wal"
    },
    {
        "phone_number": "554799777588",
        "public_name": "Carine"
    },
    {
        "phone_number": "554999227227",
        "public_name": "Francisco"
    },
    {
        "phone_number": "554599761445",
        "public_name": "Norlei"
    },
    {
        "phone_number": "554796366552",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554999633713",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554792770016",
        "public_name": "Luis"
    },
    {
        "phone_number": "554399743377",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554396297473",
        "public_name": "Josiele"
    },
    {
        "phone_number": "554799249781",
        "public_name": "Josiele"
    },
    {
        "phone_number": "554399848270",
        "public_name": "Alisson"
    },
    {
        "phone_number": "554388017835",
        "public_name": "Marcos"
    },
    {
        "phone_number": "555195000259",
        "public_name": "Gilson"
    },
    {
        "phone_number": "554499948717",
        "public_name": "Osni"
    },
    {
        "phone_number": "554396162839",
        "public_name": "Vilmar"
    },
    {
        "phone_number": "554792768989",
        "public_name": "Leandro"
    },
    {
        "phone_number": "554891663234",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554799169231",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554799126499",
        "public_name": "Alexandro"
    },
    {
        "phone_number": "554799736660",
        "public_name": "Augir"
    },
    {
        "phone_number": "554799270541",
        "public_name": "Atalavio"
    },
    {
        "phone_number": "554792265039",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554792768400",
        "public_name": "Jonatas"
    },
    {
        "phone_number": "556999533844",
        "public_name": "Natanael"
    },
    {
        "phone_number": "554791173616",
        "public_name": "Batista"
    },
    {
        "phone_number": "555193201007",
        "public_name": "Caroline"
    },
    {
        "phone_number": "554999410798",
        "public_name": "Guido"
    },
    {
        "phone_number": "554799855967",
        "public_name": "Juarez"
    },
    {
        "phone_number": "554188030029",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554384072048",
        "public_name": "Jied"
    },
    {
        "phone_number": "555191619965",
        "public_name": "Tiárlei"
    },
    {
        "phone_number": "554791973020",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554784262988",
        "public_name": "Jose"
    },
    {
        "phone_number": "554791678005",
        "public_name": "Dany"
    },
    {
        "phone_number": "554188026188",
        "public_name": "Luciane"
    },
    {
        "phone_number": "556699985120",
        "public_name": "Luiz"
    },
    {
        "phone_number": "554399145153",
        "public_name": "Joceyr"
    },
    {
        "phone_number": "554796916900",
        "public_name": "Alexandra"
    },
    {
        "phone_number": "554999642727",
        "public_name": "Aurelio"
    },
    {
        "phone_number": "554599328088",
        "public_name": "Juliana"
    },
    {
        "phone_number": "555496698500",
        "public_name": "Patricia"
    },
    {
        "phone_number": "554191071489",
        "public_name": "Ney"
    },
    {
        "phone_number": "554797017611",
        "public_name": "Paty"
    },
    {
        "phone_number": "557799718772",
        "public_name": "Jean"
    },
    {
        "phone_number": "554691039009",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554799737464",
        "public_name": "Silvio"
    },
    {
        "phone_number": "554291661307",
        "public_name": "Cassiano"
    },
    {
        "phone_number": "554796331164",
        "public_name": "Pauline"
    },
    {
        "phone_number": "554899784885",
        "public_name": "Liete"
    },
    {
        "phone_number": "554796026971",
        "public_name": "Meia"
    },
    {
        "phone_number": "554799128180",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554799021103",
        "public_name": "Augusto"
    },
    {
        "phone_number": "554799219328",
        "public_name": "Rafaela"
    },
    {
        "phone_number": "554991680605",
        "public_name": "Sandra"
    },
    {
        "phone_number": "5518997171155",
        "public_name": "Fran"
    },
    {
        "phone_number": "5511982673287",
        "public_name": "Marisa"
    },
    {
        "phone_number": "554899627505",
        "public_name": "Sílvia"
    },
    {
        "phone_number": "554888362608",
        "public_name": "Samira"
    },
    {
        "phone_number": "554199883712",
        "public_name": "Ari"
    },
    {
        "phone_number": "554396065623",
        "public_name": "Remilton"
    },
    {
        "phone_number": "554791375515",
        "public_name": "Dalila"
    },
    {
        "phone_number": "554799474455",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "5524981153455",
        "public_name": "Jorge"
    },
    {
        "phone_number": "554999922616",
        "public_name": "Sergio"
    },
    {
        "phone_number": "5511976203088",
        "public_name": "Antonio"
    },
    {
        "phone_number": "556599871901",
        "public_name": "Ieda"
    },
    {
        "phone_number": "554299378511",
        "public_name": "Vera"
    },
    {
        "phone_number": "554791051102",
        "public_name": "Flavio"
    },
    {
        "phone_number": "555499112377",
        "public_name": "Laila"
    },
    {
        "phone_number": "554792860636",
        "public_name": "Thais"
    },
    {
        "phone_number": "5511996391648",
        "public_name": "Raphael"
    },
    {
        "phone_number": "554399874494",
        "public_name": "Cris"
    },
    {
        "phone_number": "556699570418",
        "public_name": "Luciano"
    },
    {
        "phone_number": "554797323500",
        "public_name": "Glenio"
    },
    {
        "phone_number": "554999920995",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554799616368",
        "public_name": "George"
    },
    {
        "phone_number": "554499278877",
        "public_name": "Lia"
    },
    {
        "phone_number": "556599871042",
        "public_name": "Danilo"
    },
    {
        "phone_number": "554299770649",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554799230380",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554796172324",
        "public_name": "Caio"
    },
    {
        "phone_number": "554792883233",
        "public_name": "Dorateia"
    },
    {
        "phone_number": "554797037081",
        "public_name": "Camila"
    },
    {
        "phone_number": "554396607707",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "555491438310",
        "public_name": "Roberson"
    },
    {
        "phone_number": "554188532737",
        "public_name": "Ivanor"
    },
    {
        "phone_number": "554796019296",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554788383769",
        "public_name": "Miranda"
    },
    {
        "phone_number": "559192800083",
        "public_name": "Silvany"
    },
    {
        "phone_number": "554498383474",
        "public_name": "Franciely"
    },
    {
        "phone_number": "554188891429",
        "public_name": "Andrei"
    },
    {
        "phone_number": "555181483175",
        "public_name": "Guilherme"
    },
    {
        "phone_number": "554185043508",
        "public_name": "Diego"
    },
    {
        "phone_number": "554192149266",
        "public_name": "Diego"
    },
    {
        "phone_number": "554199887569",
        "public_name": "Cleber"
    },
    {
        "phone_number": "554699298282",
        "public_name": "Marcia"
    },
    {
        "phone_number": "556699327753",
        "public_name": "Gilberto"
    },
    {
        "phone_number": "554799054234",
        "public_name": "Antonio"
    },
    {
        "phone_number": "554799810338",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554688280109",
        "public_name": "Geraldo"
    },
    {
        "phone_number": "554799235945",
        "public_name": "Olimpierri"
    },
    {
        "phone_number": "554797244180",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554784487914",
        "public_name": "Beathriz"
    },
    {
        "phone_number": "554191531610",
        "public_name": "Ludwiggilson"
    },
    {
        "phone_number": "555599423270",
        "public_name": "Elaine"
    },
    {
        "phone_number": "555481590810",
        "public_name": "Katia"
    },
    {
        "phone_number": "555491581730",
        "public_name": "Eunice"
    },
    {
        "phone_number": "554791922400",
        "public_name": "Luciane"
    },
    {
        "phone_number": "554796546905",
        "public_name": "Pri"
    },
    {
        "phone_number": "556293914339",
        "public_name": "Nathalia"
    },
    {
        "phone_number": "554599715464",
        "public_name": "Gelson"
    },
    {
        "phone_number": "554291254092",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554799408989",
        "public_name": "Luciano"
    },
    {
        "phone_number": "5527998210312",
        "public_name": "Vinicius"
    },
    {
        "phone_number": "554885001691",
        "public_name": "William"
    },
    {
        "phone_number": "554791373455",
        "public_name": "Maria"
    },
    {
        "phone_number": "554791179996",
        "public_name": "Sedrez"
    },
    {
        "phone_number": "554788293631",
        "public_name": "Joelma"
    },
    {
        "phone_number": "559182985030",
        "public_name": "Nubia"
    },
    {
        "phone_number": "554399149177",
        "public_name": "Suellen"
    },
    {
        "phone_number": "557598801623",
        "public_name": "Gilmagno"
    },
    {
        "phone_number": "554491517060",
        "public_name": "Vagner"
    },
    {
        "phone_number": "554784487353",
        "public_name": "Alex"
    },
    {
        "phone_number": "554796215325",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554788021908",
        "public_name": "Diomar"
    },
    {
        "phone_number": "554799236084",
        "public_name": "Ticiane"
    },
    {
        "phone_number": "554591397444",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554799141736",
        "public_name": "Peterson"
    },
    {
        "phone_number": "554899118900",
        "public_name": "Rafael"
    },
    {
        "phone_number": "559181268581",
        "public_name": "Marco"
    },
    {
        "phone_number": "554799834899",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "554299774013",
        "public_name": "Hilde"
    },
    {
        "phone_number": "554799870800",
        "public_name": "Mara"
    },
    {
        "phone_number": "554396142273",
        "public_name": "Lilian"
    },
    {
        "phone_number": "554796133290",
        "public_name": "Marlene"
    },
    {
        "phone_number": "554791255151",
        "public_name": "Celso"
    },
    {
        "phone_number": "554899935432",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554799021440",
        "public_name": "Aldo"
    },
    {
        "phone_number": "554791194664",
        "public_name": "Vivian"
    },
    {
        "phone_number": "5511955581978",
        "public_name": "Proprietario"
    },
    {
        "phone_number": "553499711761",
        "public_name": "Ronaldo"
    },
    {
        "phone_number": "554799151645",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "555599635439",
        "public_name": "Claudio"
    },
    {
        "phone_number": "554799161094",
        "public_name": "Heraldo"
    },
    {
        "phone_number": "554796407126",
        "public_name": "Oliveira"
    },
    {
        "phone_number": "554384040820",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554799729330",
        "public_name": "Denise"
    },
    {
        "phone_number": "554797681448",
        "public_name": "Gabriela"
    },
    {
        "phone_number": "554196556480",
        "public_name": "Andreia"
    },
    {
        "phone_number": "554796215001",
        "public_name": "Beto"
    },
    {
        "phone_number": "554784051123",
        "public_name": "Frank"
    },
    {
        "phone_number": "554799752242",
        "public_name": "Leticia"
    },
    {
        "phone_number": "554799117476",
        "public_name": "Giovana"
    },
    {
        "phone_number": "554499841662",
        "public_name": "Fabio"
    },
    {
        "phone_number": "554788541515",
        "public_name": "Salvio"
    },
    {
        "phone_number": "554796245180",
        "public_name": "Aguinaldo"
    },
    {
        "phone_number": "554198078288",
        "public_name": "Fatima"
    },
    {
        "phone_number": "554291187090",
        "public_name": "Alcidio"
    },
    {
        "phone_number": "554196018877",
        "public_name": "Berenise"
    },
    {
        "phone_number": "554598216138",
        "public_name": "Barbara"
    },
    {
        "phone_number": "554192770103",
        "public_name": "Alison"
    },
    {
        "phone_number": "554498747628",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554991264516",
        "public_name": "Maristella"
    },
    {
        "phone_number": "554799948655",
        "public_name": "Luci"
    },
    {
        "phone_number": "556593157724",
        "public_name": "Lu"
    },
    {
        "phone_number": "554896785330",
        "public_name": "Mario"
    },
    {
        "phone_number": "554791692443",
        "public_name": "Laureci"
    },
    {
        "phone_number": "554788467057",
        "public_name": "Thiago"
    },
    {
        "phone_number": "554192345299",
        "public_name": "Cleverson"
    },
    {
        "phone_number": "554599189969",
        "public_name": "Romindo"
    },
    {
        "phone_number": "554788035663",
        "public_name": "Solange"
    },
    {
        "phone_number": "555197428139",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554896043083",
        "public_name": "Augusto"
    },
    {
        "phone_number": "554799744578",
        "public_name": "Zaniolo"
    },
    {
        "phone_number": "555399790412",
        "public_name": "Ana"
    },
    {
        "phone_number": "554796523402",
        "public_name": "Eliane"
    },
    {
        "phone_number": "554192140474",
        "public_name": "Alex"
    },
    {
        "phone_number": "554196131567",
        "public_name": "Eliana"
    },
    {
        "phone_number": "554299140291",
        "public_name": "Mayrus"
    },
    {
        "phone_number": "5493764350222",
        "public_name": "Augustin"
    },
    {
        "phone_number": "5516997620303",
        "public_name": "Carlos"
    },
    {
        "phone_number": "554788319460",
        "public_name": "Marlene"
    },
    {
        "phone_number": "554799460246",
        "public_name": "Tiago"
    },
    {
        "phone_number": "555499320212",
        "public_name": "Osmar"
    },
    {
        "phone_number": "5516981953344",
        "public_name": "Dini"
    },
    {
        "phone_number": "555499848985",
        "public_name": "Scherly"
    },
    {
        "phone_number": "554988522626",
        "public_name": "Lisete"
    },
    {
        "phone_number": "554799831925",
        "public_name": "Cezario"
    },
    {
        "phone_number": "554797689996",
        "public_name": "Zeli"
    },
    {
        "phone_number": "554999295013",
        "public_name": "Marilda"
    },
    {
        "phone_number": "554191195511",
        "public_name": "Dulcio"
    },
    {
        "phone_number": "554796966300",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "555496473585",
        "public_name": "Mi"
    },
    {
        "phone_number": "554797543923",
        "public_name": "Thalles"
    },
    {
        "phone_number": "554199980636",
        "public_name": "Junior"
    },
    {
        "phone_number": "554899141437",
        "public_name": "Celso"
    },
    {
        "phone_number": "554791959391",
        "public_name": "Ariel"
    },
    {
        "phone_number": "554896896035",
        "public_name": "Alessandro"
    },
    {
        "phone_number": "554199147300",
        "public_name": "Luciane"
    },
    {
        "phone_number": "554899575795",
        "public_name": "Silvio"
    },
    {
        "phone_number": "554199087614",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554199700203",
        "public_name": "Mesquita"
    },
    {
        "phone_number": "554188621282",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554599890854",
        "public_name": "Milton"
    },
    {
        "phone_number": "554799474511",
        "public_name": "Israel"
    },
    {
        "phone_number": "554499640066",
        "public_name": "Matheus"
    },
    {
        "phone_number": "554187479379",
        "public_name": "Igor"
    },
    {
        "phone_number": "5521981720055",
        "public_name": "Luis"
    },
    {
        "phone_number": "5511988147063",
        "public_name": "Rogui"
    },
    {
        "phone_number": "556196675346",
        "public_name": "Alexandre"
    },
    {
        "phone_number": "555496198342",
        "public_name": "Gisele"
    },
    {
        "phone_number": "554784545333",
        "public_name": "Silvana"
    },
    {
        "phone_number": "554788706132",
        "public_name": "Lenon"
    },
    {
        "phone_number": "554797320003",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "555199231300",
        "public_name": "Maytha"
    },
    {
        "phone_number": "554796489763",
        "public_name": "Keli"
    },
    {
        "phone_number": "554799973134",
        "public_name": "Noryan"
    },
    {
        "phone_number": "554784716612",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554792155301",
        "public_name": "Pedro"
    },
    {
        "phone_number": "5519996921126",
        "public_name": "Amanda"
    },
    {
        "phone_number": "554188294280",
        "public_name": "Vitor"
    },
    {
        "phone_number": "554491757893",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "555491062838",
        "public_name": "Rogerio"
    },
    {
        "phone_number": "554799120601",
        "public_name": "Maria"
    },
    {
        "phone_number": "554291017086",
        "public_name": "Dario"
    },
    {
        "phone_number": "5519994989836",
        "public_name": "Rangel"
    },
    {
        "phone_number": "554799888230",
        "public_name": "Toni"
    },
    {
        "phone_number": "554799619078",
        "public_name": "Lara"
    },
    {
        "phone_number": "554792812500",
        "public_name": "Andreia"
    },
    {
        "phone_number": "554599655157",
        "public_name": "Patrick"
    },
    {
        "phone_number": "554784074142",
        "public_name": "Edson"
    },
    {
        "phone_number": "554799710600",
        "public_name": "Roberto"
    },
    {
        "phone_number": "554799461018",
        "public_name": "Erick"
    },
    {
        "phone_number": "554988326121",
        "public_name": "Carolina"
    },
    {
        "phone_number": "554599185682",
        "public_name": "Elisa"
    },
    {
        "phone_number": "554791358111",
        "public_name": "Ailton"
    },
    {
        "phone_number": "554197111334",
        "public_name": "Isabela"
    },
    {
        "phone_number": "554796203000",
        "public_name": "Rafael"
    },
    {
        "phone_number": "554797140022",
        "public_name": "Alecssandra"
    },
    {
        "phone_number": "554988436017",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "558888210100",
        "public_name": "Rodrigo"
    },
    {
        "phone_number": "554388131423",
        "public_name": "Raquel"
    },
    {
        "phone_number": "554791032639",
        "public_name": "Christian"
    },
    {
        "phone_number": "554784445903",
        "public_name": "Adriana"
    },
    {
        "phone_number": "555591641145",
        "public_name": "Edson"
    },
    {
        "phone_number": "554792221434",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "555499232641",
        "public_name": "Gustavo"
    },
    {
        "phone_number": "554199671998",
        "public_name": "Marya"
    },
    {
        "phone_number": "554796509897",
        "public_name": "Henrique"
    },
    {
        "phone_number": "554198125004",
        "public_name": "Silvia"
    },
    {
        "phone_number": "554799654343",
        "public_name": "Cláudio"
    },
    {
        "phone_number": "554784047503",
        "public_name": "Joao"
    },
    {
        "phone_number": "554195669414",
        "public_name": "Isaura"
    },
    {
        "phone_number": "554784207571",
        "public_name": "Renato"
    },
    {
        "phone_number": "554197886705",
        "public_name": "Adilaine"
    },
    {
        "phone_number": "554791222839",
        "public_name": "Lariane"
    },
    {
        "phone_number": "554891278885",
        "public_name": "Felipe"
    },
    {
        "phone_number": "554184079650",
        "public_name": "Jair"
    },
    {
        "phone_number": "554799837019",
        "public_name": "Odacio"
    },
    {
        "phone_number": "554788442677",
        "public_name": "Iolanda"
    },
    {
        "phone_number": "554599556175",
        "public_name": "Celio"
    },
    {
        "phone_number": "554488354735",
        "public_name": "Wilson"
    },
    {
        "phone_number": "554784048191",
        "public_name": "Frederico"
    },
    {
        "phone_number": "554891355193",
        "public_name": "Janio"
    },
    {
        "phone_number": "554792876060",
        "public_name": "Irene"
    },
    {
        "phone_number": "554399659150",
        "public_name": "Juliano"
    },
    {
        "phone_number": "554796095485",
        "public_name": "Felipe"
    },
    {
        "phone_number": "555591724415",
        "public_name": "Rosi"
    },
    {
        "phone_number": "555499766602",
        "public_name": "Vera"
    },
    {
        "phone_number": "554288125494",
        "public_name": "Carla"
    },
    {
        "phone_number": "557181676253",
        "public_name": "Marcos"
    },
    {
        "phone_number": "554484059061",
        "public_name": "Noemia"
    },
    {
        "phone_number": "554797017000",
        "public_name": "Julio"
    },
    {
        "phone_number": "554788483888",
        "public_name": "Valdir"
    },
    {
        "phone_number": "554791934333",
        "public_name": "Arthur"
    },
    {
        "phone_number": "554788036271",
        "public_name": "Marcelo"
    },
    {
        "phone_number": "554288204847",
        "public_name": "Allan"
    },
    {
        "phone_number": "554199987888",
        "public_name": "Augustinho"
    },
    {
        "phone_number": "554999797339",
        "public_name": "Cesar"
    },
    {
        "phone_number": "554188968748",
        "public_name": "Super"
    },
    {
        "phone_number": "554488598604",
        "public_name": "Ro"
    },
    {
        "phone_number": "554799979343",
        "public_name": "Daniel"
    },
    {
        "phone_number": "554796148716",
        "public_name": "Priscila"
    },
    {
        "phone_number": "556696249069",
        "public_name": "Josi"
    },
    {
        "phone_number": "554196182611",
        "public_name": "Jair"
    },
    {
        "phone_number": "554499199696",
        "public_name": "Ricardo"
    },
    {
        "phone_number": "557799741128",
        "public_name": "Thalita"
    },
    {
        "phone_number": "556281281818",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "554191892330",
        "public_name": "Bruno"
    },
    {
        "phone_number": "554195193333",
        "public_name": "Joselito"
    },
    {
        "phone_number": "554791427284",
        "public_name": "Anne"
    },
    {
        "phone_number": "554899836592",
        "public_name": "Paulo"
    },
    {
        "phone_number": "554988321617",
        "public_name": "Allan"
    },
    {
        "phone_number": "554498981510",
        "public_name": "Leonardo"
    },
    {
        "phone_number": "555499594599",
        "public_name": "Sander"
    },
    {
        "phone_number": "554799149285",
        "public_name": "Jair"
    },
    {
        "phone_number": "5491141466029",
        "public_name": "Franklin"
    },
    {
        "phone_number": "554184115059",
        "public_name": "Mariana"
    },
    {
        "phone_number": "554399054395",
        "public_name": "Sandra"
    },
    {
        "phone_number": "554797192065",
        "public_name": "Arthur"
    },
    {
        "phone_number": "554999295655",
        "public_name": "Adilson"
    },
    {
        "phone_number": "554791374807",
        "public_name": "Marcus"
    },
    {
        "phone_number": "554899706681",
        "public_name": "Jean"
    },
    {
        "phone_number": "554791551070",
        "public_name": "Simone"
    },
    {
        "phone_number": "554196716240",
        "public_name": "Eduardo"
    },
    {
        "phone_number": "554599124989",
        "public_name": "John"
    },
    {
        "phone_number": "554784320383",
        "public_name": "Fredemar"
    },
    {
        "phone_number": "555481117633",
        "public_name": "Marcia"
    },
    {
        "phone_number": "556592198465",
        "public_name": "Lourival"
    },
    {
        "phone_number": "554797408081",
        "public_name": "Gislene"
    },
    {
        "phone_number": "554792793131",
        "public_name": "André"
    },
    {
        "phone_number": "554792934408",
        "public_name": "Allamo"
    },
    {
        "phone_number": "554184461177",
        "public_name": "Ingrid"
    },
    {
        "phone_number": "554788094540",
        "public_name": "Nildo"
    },
    {
        "phone_number": "555499657354",
        "public_name": "Roselene"
    },
    {
        "phone_number": "554999786977",
        "public_name": "Nelci"
    },
    {
        "phone_number": "554796022448",
        "public_name": "Fernando"
    },
    {
        "phone_number": "554198042880",
        "public_name": "Ricardo"
    }
];

cleaned_contacts = [
    {
        "phone_number": "5547997676797",
        "public_name": "Gui"
    },
    {
        "phone_number": "5547991674477",
        "public_name": "Gabi"
    }
]

# Função para carregar o log existente ou criar um novo
def load_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"enviados": []}  # Retorna estrutura vazia se o arquivo não existir ou estiver corrompido

# Função para salvar o log atualizado
def save_log(log_data):
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(log_data, file, indent=4, ensure_ascii=False)

# Carregar o log
log = load_log()

def already_sent(phone_number):
    """Verifica se o número já recebeu a mensagem."""
    return any(entry["phone_number"] == phone_number for entry in log["enviados"])

# Loop pelos contatos e envio de mensagem
for contact in cleaned_contacts2:
    phone_number = contact["phone_number"]
    name = contact["public_name"]

    # Se o contato já recebeu, pula
    if already_sent(phone_number):
        print(f"{name} já recebeu a mensagem. Pulando...")
        continue

    # Mensagem personalizada
    message = f"""Olá {name}, tudo bem?
    
Estou passando por aqui para compartilhar algo muito especial com você.

Tenho me dedicado cada vez mais em trazer opções exclusivas de investimentos aqui do litoral de Santa Catarina, por isso gostaria de convidá-lo a conhecer minha Landing Page e saber um pouco mais do meu trabalho!

Acesse o link abaixo para conferir tudo com calma e, se surgir alguma dúvida ou se você quiser conversar mais sobre algum investimento, estarei à disposição para te ajudar:
https://lp.corazzaequityimob.com.br/

Fico muito feliz em poder compartilhar essa jornada com você e espero que as informações te ajudem a tomar as melhores decisões.

Grande abraço, atenciosamente  
Dieison Corazza."""

    message2 = f"""Olá {name}, tudo bem? 🌞 

Estou com um negócio na mão para *entrar como investidor na construção de casas* aqui na Região de Balneário Camboriú. 

*Retorno de 30 á 50% entre 12 á 24 meses.*

Caso lhe interesse, me retorna.

Boa semana. 🙌"""
    
    # Envia a mensagem
    # kit.sendwhatmsg_instantly(f"+{phone_number}", message, 40, True, 6)
    
    # time.sleep(6)  # Aguarda para garantir que a mensagem foi enviada
    pyautogui.click(412, 751) #browser
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write(f'wa.me/{phone_number}')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    # pyautogui.click(457, 751) #whats
    time.sleep(1)
    # pyautogui.click(137, 115)
    # time.sleep(0.5)
    # pyautogui.click(137, 115)
    # time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'a')
    # time.sleep(0.5)
    # pyautogui.write(phone_number[5:])
    # time.sleep(2.5)
    # pyautogui.click(219, 188)
    # time.sleep(0.5)

    pyperclip.copy(message2)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    # Fecha a aba do WhatsApp Web (atalho: CTRL + W)
    # pyautogui.hotkey("ctrl", "w")
    
    # Atualiza o log com a nova entrada
    log["enviados"].append({
        "phone_number": phone_number,
        "name": name,
        "date_sent": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # Salva o log atualizado
    save_log(log)
    
    print(f"Mensagem enviada para {name} e log atualizado!")
    
    time.sleep(random.uniform(2, 5))  # Pequena pausa antes de enviar para o próximo contato

print("Processo finalizado. Todas as mensagens foram enviadas!")
