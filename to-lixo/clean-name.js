const fs = require('fs');

const contacts = [
    {
        "phone_number": "+554796418638",
        "public_name": "Abreu Proprietario Magnifique 2202"
    },
    {
        "phone_number": "+554791879787",
        "public_name": "AT 1.3M -Joao Guilherme Murta Cliente"
    },
    {
        "phone_number": "+554792052010",
        "public_name": "At 3.5m Suzane Ferreira Cliente"
    },
    {
        "phone_number": "+554591580658",
        "public_name": "AT 800 Mil Flavia Cliente Parcelado"
    },
    {
        "phone_number": "+555499182156",
        "public_name": "Paulo Cliente Organica"
    },
    {
        "phone_number": "+554797588085",
        "public_name": "AT 1.3M- Carlos Cliente"
    },
    {
        "phone_number": "+554196546898",
        "public_name": "AT 2M- Evellyn Dallagnol Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554784145260",
        "public_name": "AT 1M- Michel Cliente"
    },
    {
        "phone_number": "+554799720525",
        "public_name": "Jorge Cliente BC"
    },
    {
        "phone_number": "+554799508778",
        "public_name": "Miguel Angelo Rossi Cliente"
    },
    {
        "phone_number": "+554498112222",
        "public_name": "Cleso Lopes Cliente"
    },
    {
        "phone_number": "+554797946550",
        "public_name": "At 1.6m Gustavo De Mello Cliente"
    },
    {
        "phone_number": "+554195883013",
        "public_name": "Osni Proprietario Luar Biasa 2401"
    },
    {
        "phone_number": "+554788516351",
        "public_name": "Murilo Proprietario Santillana Del Mare"
    },
    {
        "phone_number": "+554499722526",
        "public_name": "Jocimar Cardoso Contimar Cliente Maringa"
    },
    {
        "phone_number": "+554799854167",
        "public_name": "Jucelio Proprietário Rocca Di Mare"
    },
    {
        "phone_number": "+554799672121",
        "public_name": "Edgar Olsson Cliente Frente Mar"
    },
    {
        "phone_number": "+554891311800",
        "public_name": "At 3m Marcos Dornelles Cliente"
    },
    {
        "phone_number": "+554399748007",
        "public_name": "At 3.5m Marcelo Izelli Cliente"
    },
    {
        "phone_number": "+5511950651805",
        "public_name": "AT 800K - Cleber Cliente - Casa"
    },
    {
        "phone_number": "+554791062555",
        "public_name": "Mauro Rocha Proprietario Costa Arvoredo"
    },
    {
        "phone_number": "+554497134514",
        "public_name": "AT 800K - Italo Cliente Maringa"
    },
    {
        "phone_number": "+559281399000",
        "public_name": "AT 1.3M - Jorgenson Lavor Cliente"
    },
    {
        "phone_number": "+554784085098",
        "public_name": "Gean Cliente Blumenau"
    },
    {
        "phone_number": "+554599733381",
        "public_name": "Leonardo Link Cliente Hyde"
    },
    {
        "phone_number": "+554796529100",
        "public_name": "Bia/chiquinho Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554199520408",
        "public_name": "At 8m Jeferson Cliente"
    },
    {
        "phone_number": "+554799580720",
        "public_name": "At 2m Frank Cliente"
    },
    {
        "phone_number": "+554898120588",
        "public_name": "Cristiano Cliente Indicacao Franklin"
    },
    {
        "phone_number": "+554784675784",
        "public_name": "AT 800K -Eliane Cliente"
    },
    {
        "phone_number": "+554796791400",
        "public_name": "AT 1M Rodrigo Cliente Praia Brava"
    },
    {
        "phone_number": "+554796739707",
        "public_name": "Patricia Cliente Organica"
    },
    {
        "phone_number": "+554999834411",
        "public_name": "Cesar Cliente Curitibanos"
    },
    {
        "phone_number": "+554797310806",
        "public_name": "Walter Proprietario Casa Na Barra"
    },
    {
        "phone_number": "+554196919419",
        "public_name": "Laudemir Cliente Indicacao Leonildo"
    },
    {
        "phone_number": "+554796559968",
        "public_name": "Jose Proprietario Bellas Artes 2 Domitorios 700 Mil"
    },
    {
        "phone_number": "+554591491992",
        "public_name": "Luis Henrique Cliente"
    },
    {
        "phone_number": "+554791190915",
        "public_name": "AT 2.5M- Carlos Cliente  Frente Mar Ou Quadra"
    },
    {
        "phone_number": "+554288605630",
        "public_name": "AT 2.5m Cê Cliente Tem Permuta Em Curitiba"
    },
    {
        "phone_number": "+554791946776",
        "public_name": "AT 500K - Graciela Cliente"
    },
    {
        "phone_number": "+554788596355",
        "public_name": "Arlindo Proprietario Notre Dame 001"
    },
    {
        "phone_number": "+554799850640",
        "public_name": "At 2m Rogerio Hirt Cliente"
    },
    {
        "phone_number": "+554799764758",
        "public_name": "Walter Teske Cliente Frente Mar Mkt"
    },
    {
        "phone_number": "+554799881343",
        "public_name": "Douglas Cunha Cliente Investidor"
    },
    {
        "phone_number": "+5511958031769",
        "public_name": "AT 1M- Luis Cliente"
    },
    {
        "phone_number": "+554791082714",
        "public_name": "Junior Proprietario Gran Torino"
    },
    {
        "phone_number": "+554499707686",
        "public_name": "Tiago Cliente Maringa Parcelado"
    },
    {
        "phone_number": "+554191126112",
        "public_name": "Marcos Ruon Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554792636303",
        "public_name": "AT 1M-Cristiane Cliente"
    },
    {
        "phone_number": "+554191991836",
        "public_name": "Emilio Cliente Curitiba"
    },
    {
        "phone_number": "+556999214600",
        "public_name": "Guida Cliente Mkt Cota"
    },
    {
        "phone_number": "+555499259027",
        "public_name": "Gabriel Mezzomo Cliente Mkt Até"
    },
    {
        "phone_number": "+556599829855",
        "public_name": "At 3.5m Renata Cortese Cliente"
    },
    {
        "phone_number": "+555499071043",
        "public_name": "At 1.3m Angelica Franceschi Cliente"
    },
    {
        "phone_number": "+554891767007",
        "public_name": "Guilherme Cliente Aluguel Indicacao Junior E Josi"
    },
    {
        "phone_number": "+554799573017",
        "public_name": "Lucas Cliente Loteamento"
    },
    {
        "phone_number": "+554899733412",
        "public_name": "At 3m Raquel Rckss Cliente"
    },
    {
        "phone_number": "+554797877000",
        "public_name": "Raíza Cliente Proprietário Diferenciado Promenade"
    },
    {
        "phone_number": "+554399170277",
        "public_name": "AT 800K - Antonio Carlos Cliente"
    },
    {
        "phone_number": "+5514998812904",
        "public_name": "At 2m Lucineia Bolognini Cliente"
    },
    {
        "phone_number": "+554797149209",
        "public_name": "AT 800K - Lourival Cliente"
    },
    {
        "phone_number": "+554799838938",
        "public_name": "Sergio Araujo Sens Proprietario Barra Tower 3701"
    },
    {
        "phone_number": "+554196745071",
        "public_name": "Erik Cliente"
    },
    {
        "phone_number": "+554199799091",
        "public_name": "AT 800K - Sidnei Cliente"
    },
    {
        "phone_number": "+554796804811",
        "public_name": "Juliano Bongiolo Cliente Gales"
    },
    {
        "phone_number": "+554599233282",
        "public_name": "AT 1M- Renato Cliente - Parcelado"
    },
    {
        "phone_number": "+554791366659",
        "public_name": "AT 1M-Bitencourt Rocha Rodrigues Cliente"
    },
    {
        "phone_number": "+554791912033",
        "public_name": "Cesar Heining Cliente"
    },
    {
        "phone_number": "+554398522618",
        "public_name": "AT 500K -Amélia Cliente Mkt"
    },
    {
        "phone_number": "+555189068619",
        "public_name": "Marília Gomes Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+555599830363",
        "public_name": "AT 500K -Mario Bueno Cliente Praia Brava Mkt"
    },
    {
        "phone_number": "+554896295658",
        "public_name": "Jonas Cliente Organica"
    },
    {
        "phone_number": "+554799160002",
        "public_name": "Daniel Carda Cliente Praia Brava"
    },
    {
        "phone_number": "+554991354209",
        "public_name": "AT 500K -Renato Ferrari Cliente Praia Brava"
    },
    {
        "phone_number": "+554799992510",
        "public_name": "Paulo Barros Proprietario Casa Praia Brava"
    },
    {
        "phone_number": "+554199734317",
        "public_name": "Vilberto Petri Proprietário Real Park 1302"
    },
    {
        "phone_number": "+555191588050",
        "public_name": "Renata Zago Cliente"
    },
    {
        "phone_number": "+554998008888",
        "public_name": "AT 2.5M- Cedriano Ciotta Cliente Mkt"
    },
    {
        "phone_number": "+554196577809",
        "public_name": "At 2m Liana Cliente"
    },
    {
        "phone_number": "+554899903736",
        "public_name": "AT 2M Meri Terezinha Melo Cliente"
    },
    {
        "phone_number": "+554799830027",
        "public_name": "At 4m Laudelino Veiga Cliente"
    },
    {
        "phone_number": "+554792554686",
        "public_name": "Alessandro Cliente Organica"
    },
    {
        "phone_number": "+554898412670",
        "public_name": "At 2m Eduardo Carlos Faust Cliente"
    },
    {
        "phone_number": "+554799648147",
        "public_name": "Mauricio Cliente Marido Pri"
    },
    {
        "phone_number": "+554899920008",
        "public_name": "AT 1.6M- Marcos Cliente Frente Mar"
    },
    {
        "phone_number": "+555191815724",
        "public_name": "Silvana Cliente Dom Gabriel"
    },
    {
        "phone_number": "+554598273636",
        "public_name": "Luis Henrique Cliente"
    },
    {
        "phone_number": "+555481195738",
        "public_name": "At 3.5m Sergio Muller Cliente"
    },
    {
        "phone_number": "+554791044848",
        "public_name": "At 2m Junior Silva Cliente Casa"
    },
    {
        "phone_number": "+554799851443",
        "public_name": "Vania Schulz Cliente Italian"
    },
    {
        "phone_number": "+554191269267",
        "public_name": "AT 1.6M Willian Cliente Proprietario Citta Di Vinci"
    },
    {
        "phone_number": "+554499149965",
        "public_name": "AT 500K - Fernando Cliente"
    },
    {
        "phone_number": "+554799497779",
        "public_name": "Junior Ferreira Cliente Aurora"
    },
    {
        "phone_number": "+5511981525623",
        "public_name": "Antonio Proprietário D Itália 1301"
    },
    {
        "phone_number": "+555481449000",
        "public_name": "At 3M Ana Sagebin Cliente"
    },
    {
        "phone_number": "+554792198078",
        "public_name": "Gabriel Franz Cliente Vendido"
    },
    {
        "phone_number": "+554196921828",
        "public_name": "Lucas Cliente Organica"
    },
    {
        "phone_number": "+554796438603",
        "public_name": "Josue Cliente Permuta Casa Rua Italia"
    },
    {
        "phone_number": "+554799888877",
        "public_name": "AT 1.6M Ricardo Willian Cliente"
    },
    {
        "phone_number": "+554399190084",
        "public_name": "AT 1M-  Rogerio Cliente"
    },
    {
        "phone_number": "+554884031704",
        "public_name": "Luciano Proprietário Bellas Artes B 1704"
    },
    {
        "phone_number": "+554792107711",
        "public_name": "AT 3M Julie Cliente"
    },
    {
        "phone_number": "+554799325052",
        "public_name": "AT 500K - Andreia Cliente Sobrado"
    },
    {
        "phone_number": "+554433660909",
        "public_name": "Ademir Construtora Cidade Verde Maringa Cliente"
    },
    {
        "phone_number": "+554499329343",
        "public_name": "Paulo Cliente Maringa"
    },
    {
        "phone_number": "+554197388079",
        "public_name": "At 3m Babi Garcia Cliente"
    },
    {
        "phone_number": "+554788543963",
        "public_name": "At 3m Jader Alberto Pazinato Cliente"
    },
    {
        "phone_number": "+554799156502",
        "public_name": "Marinho Biz Cliente Organica"
    },
    {
        "phone_number": "+5521982733504",
        "public_name": "AT 1M- Guilherme Cardoso Cliente -Frente Praia Brava"
    },
    {
        "phone_number": "+555499988032",
        "public_name": "Arnold Demarco Knapik Cliente Vendido"
    },
    {
        "phone_number": "+554797573434",
        "public_name": "AT 500k Maikol Cliente"
    },
    {
        "phone_number": "+5511942028835",
        "public_name": "AT 1M - Antonio Cliente"
    },
    {
        "phone_number": "+554899852143",
        "public_name": "AT 1M Iver Cliente"
    },
    {
        "phone_number": "+5511988847390",
        "public_name": "Osorio Proprietário Nina Schirmamm 702"
    },
    {
        "phone_number": "+554192196189",
        "public_name": "AT 1.6M André Zamprieri Cliente"
    },
    {
        "phone_number": "+554799262959",
        "public_name": "AT 500K - Lourdes Silva Cliente Praia Brava"
    },
    {
        "phone_number": "+554199572772",
        "public_name": "Fhab Thoaldo Cliente Hyde"
    },
    {
        "phone_number": "+554199320202",
        "public_name": "Proprietario-Afonso  1501 E 3401 Vision"
    },
    {
        "phone_number": "+555499203060",
        "public_name": "Luiza Demarco Cliente Indicacao Mauro Conapik"
    },
    {
        "phone_number": "+554799778343",
        "public_name": "AT 1M-Davi Landim Cliente"
    },
    {
        "phone_number": "+554791981711",
        "public_name": "AT 1M- Valdes Sanche Cliente"
    },
    {
        "phone_number": "+554396084166",
        "public_name": "Claudemir Nardini Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799275627",
        "public_name": "AT 800K - Ricardo Cliente Quer Casa"
    },
    {
        "phone_number": "+556781452830",
        "public_name": "Elbio Proprietário Pérolas Do Atlântico 902"
    },
    {
        "phone_number": "+5511957733091",
        "public_name": "AT 4M- Jacke Carlot Cliente"
    },
    {
        "phone_number": "+5521985082515",
        "public_name": "Edino Cliente Eberti"
    },
    {
        "phone_number": "+554797741801",
        "public_name": "Proprietario 02 Suites Praia Brava"
    },
    {
        "phone_number": "+554792666521",
        "public_name": "Ana Silvia Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554491251311",
        "public_name": "Miguel Proprietário Le Majestique 2603 Troca Por Fazenda"
    },
    {
        "phone_number": "+555491756999",
        "public_name": "Gerson Cliente Organica"
    },
    {
        "phone_number": "+554691047006",
        "public_name": "At 4m Gilmar Gambetta Cliente"
    },
    {
        "phone_number": "+554784948003",
        "public_name": "Bruno Cruz Proprietario Real Park 1405"
    },
    {
        "phone_number": "+554196281102",
        "public_name": "Gislene Cliente Brava Beach"
    },
    {
        "phone_number": "+554797300325",
        "public_name": "AT 500k Claudia Cliente Novo Num"
    },
    {
        "phone_number": "+554796388309",
        "public_name": "AT 2.5m Edson Bello Cliente"
    },
    {
        "phone_number": "+559281179620",
        "public_name": "Davi Alexandre Belota Sabba Cliente"
    },
    {
        "phone_number": "+554799414441",
        "public_name": "At 3m Leonardo Fayad Cliente"
    },
    {
        "phone_number": "+554799970880",
        "public_name": "Alessandra Cliente Sobrado"
    },
    {
        "phone_number": "+5518981019500",
        "public_name": "AT 500k Luis Henrique Cliente Amigo Edi"
    },
    {
        "phone_number": "+554499230400",
        "public_name": "At 3m Flavia Carluccio Cliente"
    },
    {
        "phone_number": "+554599141515",
        "public_name": "At 1.3m Wilson Cliente"
    },
    {
        "phone_number": "+554199750262",
        "public_name": "At 1.6M Sonia De Sa Cliente"
    },
    {
        "phone_number": "+554797349364",
        "public_name": "AT 1M- João Simone Cliente -Praia Brava"
    },
    {
        "phone_number": "+555591470555",
        "public_name": "AT 500K - Luis Fernando Cliente Mkt  Pronto"
    },
    {
        "phone_number": "+5511981739427",
        "public_name": "AT 800K - Helton Mourao Cliente -Praia Brava"
    },
    {
        "phone_number": "+554799515443",
        "public_name": "AT 2M Mauro Cliente"
    },
    {
        "phone_number": "+554799999400",
        "public_name": "AT 1.3M Junior Cliente"
    },
    {
        "phone_number": "+554796341930",
        "public_name": "Claudio Cliente"
    },
    {
        "phone_number": "+555199866777",
        "public_name": "AT 500K - Sergio Oliveira Cliente"
    },
    {
        "phone_number": "+554391140292",
        "public_name": "AT 2M Claudia Cliente Royal"
    },
    {
        "phone_number": "+554796092009",
        "public_name": "Celia Cliente"
    },
    {
        "phone_number": "+556699717487",
        "public_name": "Fernanda Setter Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554888151198",
        "public_name": "At 600k Aticot Cliente Serentity"
    },
    {
        "phone_number": "+554799111555",
        "public_name": "AT 1M - Alexandre Cliente"
    },
    {
        "phone_number": "+554799031849",
        "public_name": "Jean C. Paulo Proprietario Torre D Monaco"
    },
    {
        "phone_number": "+5511989388988",
        "public_name": "AT 500K -Miro Vakimoto Cliente Praia Brava Mkt"
    },
    {
        "phone_number": "+554799995269",
        "public_name": "Marcela Ramos Cliente"
    },
    {
        "phone_number": "+554791646188",
        "public_name": "Jose Luis Proprietario Baleia Branca 102"
    },
    {
        "phone_number": "+554799068532",
        "public_name": "Tiago Brandes Cliente Orbita"
    },
    {
        "phone_number": "+556599810403",
        "public_name": "AT 1 M Erick Cliente Investidor"
    },
    {
        "phone_number": "+554791551165",
        "public_name": "AT 1M- Augustin Cliente"
    },
    {
        "phone_number": "+554784834481",
        "public_name": "Agnaldo Cliente Bc"
    },
    {
        "phone_number": "+554391898686",
        "public_name": "Carlos Eduardo Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554788610415",
        "public_name": "Gilson Proprietario Garden Plaza 1502"
    },
    {
        "phone_number": "+554796595025",
        "public_name": "Rafael Proprietário Restaurante 1500"
    },
    {
        "phone_number": "+554884064745",
        "public_name": "Osni Proprietário Tour Royalle Apto 1801"
    },
    {
        "phone_number": "+554792557017",
        "public_name": "At 2m Rosani Schafaschek Cliente"
    },
    {
        "phone_number": "+555191892325",
        "public_name": "Isabel Cliente POA"
    },
    {
        "phone_number": "+554796332509",
        "public_name": "Ana Carolina Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554188065316",
        "public_name": "At 10m Ulisses Cliente"
    },
    {
        "phone_number": "+554799430410",
        "public_name": "AT 500K - Antonio Cliente"
    },
    {
        "phone_number": "+554799286522",
        "public_name": "AT 1.3M -Jucelino Cliente"
    },
    {
        "phone_number": "+554491324691",
        "public_name": "AT 800K - Roseli Teixeira Cliente"
    },
    {
        "phone_number": "+554299284669",
        "public_name": "AT 500K - Jussara Cliente Mkt"
    },
    {
        "phone_number": "+5521981880809",
        "public_name": "Eduardo Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554396627088",
        "public_name": "AT 800K - Rivilini Cliente"
    },
    {
        "phone_number": "+554499445566",
        "public_name": "Claudio e Rose Clientes"
    },
    {
        "phone_number": "+554799162080",
        "public_name": "AT 800K -Julio Carmo Cliente Casa"
    },
    {
        "phone_number": "+556699688839",
        "public_name": "AT 3.5M- Giovanni Brondani Cliente Casa"
    },
    {
        "phone_number": "+554799278101",
        "public_name": "At 8m Aivans Ivan Paz Cliente"
    },
    {
        "phone_number": "+554796188818",
        "public_name": "Camila Grah Cliente"
    },
    {
        "phone_number": "+5512981464632",
        "public_name": "Danielly Arnaut Cliente Organica"
    },
    {
        "phone_number": "+554396094313",
        "public_name": "Maiko Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554791979543",
        "public_name": "AT 1.3M -Gisiane Souza Cliente"
    },
    {
        "phone_number": "+554399318373",
        "public_name": "At 2m Karem Christian Chaowiche Nassar Cliente"
    },
    {
        "phone_number": "+554999230167",
        "public_name": "AT 1M- Rodrigo Cliente"
    },
    {
        "phone_number": "+554799618496",
        "public_name": "At 7m Junior Cliente"
    },
    {
        "phone_number": "+554792780155",
        "public_name": "AT 800K - Valdelicio Cliente"
    },
    {
        "phone_number": "+554896208854",
        "public_name": "At 1m Tiao Goulart Cliente"
    },
    {
        "phone_number": "+554399727598",
        "public_name": "At 3m Marisol Gardoqui Cliente"
    },
    {
        "phone_number": "+5515997163296",
        "public_name": "AT 800K - Henrique Cliente"
    },
    {
        "phone_number": "+554796777308",
        "public_name": "AT 500K - Vanessa Cliente"
    },
    {
        "phone_number": "+554797083949",
        "public_name": "Jerlei Saad Proprietario Figueira Da Foz"
    },
    {
        "phone_number": "+555381415445",
        "public_name": "Paulinho Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796486677",
        "public_name": "At 2m André Lima Cliente"
    },
    {
        "phone_number": "+554991440123",
        "public_name": "AT 1.6M- Sander Ceccatto Cliente  Mkt"
    },
    {
        "phone_number": "+554499117828",
        "public_name": "At 2.5m Tania Cliente Tem Permuta Em Maringa"
    },
    {
        "phone_number": "+554484451306",
        "public_name": "Rafael E Alice Proprietario"
    },
    {
        "phone_number": "+554598408899",
        "public_name": "Liz Vida Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555491139930",
        "public_name": "Rosangela Cliente Ranking"
    },
    {
        "phone_number": "+554899573511",
        "public_name": "AT 1M- Alex Cliente"
    },
    {
        "phone_number": "+556799717070",
        "public_name": "At 6m João Antonio Gonçalves Cliente"
    },
    {
        "phone_number": "+554191548877",
        "public_name": "Osmar Cliente Curitiba"
    },
    {
        "phone_number": "+554784338283",
        "public_name": "Valcir Proprietario Briggen Noruega"
    },
    {
        "phone_number": "+554799773278",
        "public_name": "Jose Proprietario Casa Nacoes"
    },
    {
        "phone_number": "+554796752420",
        "public_name": "Flavia Matteussi Cliente Organica"
    },
    {
        "phone_number": "+555584248299",
        "public_name": "At 3m Denise Maria Cliente"
    },
    {
        "phone_number": "+554799228874",
        "public_name": "Luiz Carlos Teixeira Proprietário Montreux 1901"
    },
    {
        "phone_number": "+554797578000",
        "public_name": "AT 1.3M -Rubens Cliente"
    },
    {
        "phone_number": "+554196795959",
        "public_name": "Ricardo Proprietario Essence"
    },
    {
        "phone_number": "+554199319525",
        "public_name": "Tony Cliente"
    },
    {
        "phone_number": "+554788028928",
        "public_name": "AT 800K - Rosa Cliente Casa"
    },
    {
        "phone_number": "+554799670781",
        "public_name": "Leo Cliente"
    },
    {
        "phone_number": "+559193331100",
        "public_name": "AT 1.6m Larissa Liborio Cliente"
    },
    {
        "phone_number": "+554499760889",
        "public_name": "AT 500K - Kennedy Cliente"
    },
    {
        "phone_number": "+555496260681",
        "public_name": "Marcelo Mazzuco Cliente Lagoa Vermelha Parcelado Investimento"
    },
    {
        "phone_number": "+554791047233",
        "public_name": "AT 1.3M- Armandio Cliente"
    },
    {
        "phone_number": "+554796333300",
        "public_name": "AT 500K - Ines Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554198047908",
        "public_name": "Sidney Cliente Frente Mar Investidor"
    },
    {
        "phone_number": "+555599969128",
        "public_name": "AT 500K - Antonio De Lima Cliente Mkt"
    },
    {
        "phone_number": "+554891038558",
        "public_name": "At 3.5m Keithiany Miguel Cliente"
    },
    {
        "phone_number": "+554899101350",
        "public_name": "Thiago Cliente Village Dos Ipês"
    },
    {
        "phone_number": "+554799851021",
        "public_name": "Vilson Proprietário Golden Alliance 1302"
    },
    {
        "phone_number": "+554797786555",
        "public_name": "AT 500K - Adriano Cliente"
    },
    {
        "phone_number": "+554797170328",
        "public_name": "At 2.5m Felipe Aquino Cliente Quer Brava Beach"
    },
    {
        "phone_number": "+559180641079",
        "public_name": "At 2.5m Camila Pina Cliente"
    },
    {
        "phone_number": "+555491875770",
        "public_name": "Leni Fior Cliente Ibirubá"
    },
    {
        "phone_number": "+554199290550",
        "public_name": "AT 5M Leydi Cliente Rubens"
    },
    {
        "phone_number": "+554797402686",
        "public_name": "AT 500K - Fabricio Cliente Casa"
    },
    {
        "phone_number": "+554799462397",
        "public_name": "Vanessa Juliana Cliente"
    },
    {
        "phone_number": "+555492069355",
        "public_name": "At 3.5m Gilmar Chesties Cliente"
    },
    {
        "phone_number": "+554491610014",
        "public_name": "AT 1.3M - Antonio Helio Cliente Casa"
    },
    {
        "phone_number": "+554799124971",
        "public_name": "Luciana Proprietario"
    },
    {
        "phone_number": "+554396315900",
        "public_name": "Donizeti Cliente Londrina"
    },
    {
        "phone_number": "+5511947008129",
        "public_name": "AT 2.5M- Stefanny Cliente"
    },
    {
        "phone_number": "+554799466522",
        "public_name": "AT 1M Daniela Ribeiro Cliente"
    },
    {
        "phone_number": "+554388051684",
        "public_name": "AT 1.3M -Angelo Cliente Londrina"
    },
    {
        "phone_number": "+554891881588",
        "public_name": "AT 1M Cintia Fernandes Cliente"
    },
    {
        "phone_number": "+555182132020",
        "public_name": "Erivan Proprietario Santillana Del Mar 2101"
    },
    {
        "phone_number": "+5511982246370",
        "public_name": "AT 1.3M -Tiago Cliente - Tem Permuta Em Curitiba"
    },
    {
        "phone_number": "+554691140171",
        "public_name": "Rafael Carneiro Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554199223355",
        "public_name": "Alessandro Cliente Indicação Luiz Nebes"
    },
    {
        "phone_number": "+554591075772",
        "public_name": "Geraldo Campelo Cliente Hyde"
    },
    {
        "phone_number": "+554799122519",
        "public_name": "Sabrina Cliente Camboriu"
    },
    {
        "phone_number": "+554784459738",
        "public_name": "AT 500k Rafael Blackout Cliente"
    },
    {
        "phone_number": "+554399188505",
        "public_name": "Paulo Oliveira Cliente Londrina"
    },
    {
        "phone_number": "+554796377482",
        "public_name": "AT 500K - Rosana Zicka Cliente Praia Brava"
    },
    {
        "phone_number": "+554396168986",
        "public_name": "At 3m Dalva Costa Cliente"
    },
    {
        "phone_number": "+554299750032",
        "public_name": "At 3.5m Ary Carneiro Junior Cliente"
    },
    {
        "phone_number": "+554899545176",
        "public_name": "Ivo Cliente Ate 2m"
    },
    {
        "phone_number": "+554788050958",
        "public_name": "Renato Cliente"
    },
    {
        "phone_number": "+554788355851",
        "public_name": "Eduardo Cliente BC"
    },
    {
        "phone_number": "+554799551400",
        "public_name": "Helder Corretor Proprietario Serendipty 3102"
    },
    {
        "phone_number": "+554399292449",
        "public_name": "Magali Cliente Apucarana Maringa"
    },
    {
        "phone_number": "+554399535523",
        "public_name": "Claudete Fachina Cliente Organica"
    },
    {
        "phone_number": "+554399661888",
        "public_name": "Marcos Cliente Londrina"
    },
    {
        "phone_number": "+554484241191",
        "public_name": "At 6.5m Anderson Akira Horita Cliente"
    },
    {
        "phone_number": "+554799772493",
        "public_name": "Lauro Joao Proprietario Torre Atlantica"
    },
    {
        "phone_number": "+554188122531",
        "public_name": "At 1.3m Valdecir De Souza Cliente"
    },
    {
        "phone_number": "+554498622222",
        "public_name": "At 2m Marlene Chagas Lopes Cliente"
    },
    {
        "phone_number": "+554191890089",
        "public_name": "AT 800K -Andre Cliente Tem Lancha De 800 Mil"
    },
    {
        "phone_number": "+554797106549",
        "public_name": "Nichollas Santos Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799111970",
        "public_name": "Sidnei Proprietário"
    },
    {
        "phone_number": "+554298579893",
        "public_name": "At 3m Clarice Sander Carneiro Cliente"
    },
    {
        "phone_number": "+5511973311963",
        "public_name": "Duarte Castelo Branco Proprietario Casa Caledonia"
    },
    {
        "phone_number": "+554799187525",
        "public_name": "Juliano Colares Cliente Sala Brava Vision"
    },
    {
        "phone_number": "+554796133200",
        "public_name": "AT 1M- Sandro Cliente"
    },
    {
        "phone_number": "+554999216821",
        "public_name": "At 2M Edila Cliente Comprou"
    },
    {
        "phone_number": "+554799498011",
        "public_name": "Wagner Rocha Cliente"
    },
    {
        "phone_number": "+554791186544",
        "public_name": "Alexandre Cliente Casa Olx"
    },
    {
        "phone_number": "+554799831188",
        "public_name": "AT 1.6m Rita De Cassia Cliente"
    },
    {
        "phone_number": "+554796647898",
        "public_name": "Sandra Cliente"
    },
    {
        "phone_number": "+554788664558",
        "public_name": "Giovana Cliente Orbita"
    },
    {
        "phone_number": "+554984064990",
        "public_name": "Viviane Cliente Mkt Boreal Quer Comprar 3 Apts"
    },
    {
        "phone_number": "+554799123000",
        "public_name": "Charles Cliente Proprietário Emanuel 201"
    },
    {
        "phone_number": "+554187070808",
        "public_name": "AT 1.3M- Cristian Feronatto Cliente"
    },
    {
        "phone_number": "+554799837676",
        "public_name": "AT 1M-Bony Cliente Invetidor"
    },
    {
        "phone_number": "+554299629832",
        "public_name": "Samanta Regina Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799986830",
        "public_name": "Jailson Cliente"
    },
    {
        "phone_number": "+554199258852",
        "public_name": "At 3.5m Carol Savassi Cliente"
    },
    {
        "phone_number": "+554792311001",
        "public_name": "AT 800K - Jociel Cliente"
    },
    {
        "phone_number": "+554988325323",
        "public_name": "Marcus Proprietario Phoenix 40"
    },
    {
        "phone_number": "+554499912244",
        "public_name": "Joao Carlos Perre Proprietário Horizon"
    },
    {
        "phone_number": "+554999412000",
        "public_name": "AT 500K - Vera Lucia Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554191070505",
        "public_name": "Alexandre Cliente CTB brava Beach"
    },
    {
        "phone_number": "+554896321424",
        "public_name": "At 1.6m Taís Moratelli Cliente"
    },
    {
        "phone_number": "+554899363336",
        "public_name": "Angelo Mellos Proprietario"
    },
    {
        "phone_number": "+5519988086729",
        "public_name": "AT 4m Marlon Oliveira Cliente"
    },
    {
        "phone_number": "+554799820499",
        "public_name": "Michel Proprietario Quadra Mar"
    },
    {
        "phone_number": "+554498447406",
        "public_name": "AT 500K - Nildo Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554899757477",
        "public_name": "Cristiano Proprietario Imperador 1503"
    },
    {
        "phone_number": "+554799148372",
        "public_name": "Samuel Boschi Proprietario Lago Maggiore"
    },
    {
        "phone_number": "+554797746235",
        "public_name": "Vania Cliente BC"
    },
    {
        "phone_number": "+554199738327",
        "public_name": "Proprietario Noblesse"
    },
    {
        "phone_number": "+554499488848",
        "public_name": "Cinthia Palmira Barbosa Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554792152275",
        "public_name": "Leandro Proprietario Lote Reserva Golf"
    },
    {
        "phone_number": "+555496694152",
        "public_name": "Monika Stein Cliente Parceria Magnum"
    },
    {
        "phone_number": "+554199973183",
        "public_name": "At 3m Simone Peres Cliente"
    },
    {
        "phone_number": "+554799870860",
        "public_name": "Mariela Cliente"
    },
    {
        "phone_number": "+554684132728",
        "public_name": "João Cliente Eberti"
    },
    {
        "phone_number": "+554288491301",
        "public_name": "AT 1.3M -Giselle Cliente"
    },
    {
        "phone_number": "+554799521956",
        "public_name": "AT 1M-Diagora Fusinato Cliente"
    },
    {
        "phone_number": "+554799446399",
        "public_name": "AT 800k Eliane Pedrini Cliente"
    },
    {
        "phone_number": "+556181177574",
        "public_name": "Ricardo Proprietário Hamptons"
    },
    {
        "phone_number": "+554799836193",
        "public_name": "Jairo Proprietario Cobertura Villa Germanica 1401"
    },
    {
        "phone_number": "+554499724820",
        "public_name": "Sirley Cliente Maringa"
    },
    {
        "phone_number": "+554799744415",
        "public_name": "AT 1.6m Jubin Mira Cliente"
    },
    {
        "phone_number": "+555381419208",
        "public_name": "AT 1M- Daiana Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554891824766",
        "public_name": "Dieguinho Pasqualotto Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554196862073",
        "public_name": "AT 3M Adriana Cliente"
    },
    {
        "phone_number": "+554797245065",
        "public_name": "João Lima Cliente Organica"
    },
    {
        "phone_number": "+554792260634",
        "public_name": "Jairo Ricardes Rodrigues Cliente"
    },
    {
        "phone_number": "+554796844353",
        "public_name": "AT 1.3M Cristina Cliente"
    },
    {
        "phone_number": "+554799995500",
        "public_name": "AT 500K -Felipe Cliente"
    },
    {
        "phone_number": "+554799417869",
        "public_name": "AT Joselia Cliente"
    },
    {
        "phone_number": "+554799740574",
        "public_name": "AT 5M Larri Hartmann Cliente"
    },
    {
        "phone_number": "+554195739582",
        "public_name": "AT 800K - Paulo Cliente Curitiba Casa"
    },
    {
        "phone_number": "+554797730000",
        "public_name": "AT 1.6M-  Rodrigo Espelho Cliente  Motorhome"
    },
    {
        "phone_number": "+554291242466",
        "public_name": "At 3.5m Ana Slusarz Cliente"
    },
    {
        "phone_number": "+554991353948",
        "public_name": "AT 1.6M- Idia Machado Cliente"
    },
    {
        "phone_number": "+554799475458",
        "public_name": "At 500k Jacqueline Cliente"
    },
    {
        "phone_number": "+554799094722",
        "public_name": "AT 800K - Claudes Cliente - Casa"
    },
    {
        "phone_number": "+554899849393",
        "public_name": "At 3.5m Simonete Fuchter Junkes Cliente"
    },
    {
        "phone_number": "+554199870884",
        "public_name": "AT 500K -Michel Lisboa Cliente Sobrado"
    },
    {
        "phone_number": "+554799369207",
        "public_name": "Rodrteson Proprietário Riviera Frente Mar"
    },
    {
        "phone_number": "+555499155470",
        "public_name": "Michele Leite Cliente Orbita Perequê"
    },
    {
        "phone_number": "+556599958986",
        "public_name": "At 3.5m Lilian Ribas Cliente"
    },
    {
        "phone_number": "+554797344271",
        "public_name": "Terezinha Cliente"
    },
    {
        "phone_number": "+554797199291",
        "public_name": "AT 500k Zilmar Cliente"
    },
    {
        "phone_number": "+554799110772",
        "public_name": "Gilson De Aguiar Cliente"
    },
    {
        "phone_number": "+554498959686",
        "public_name": "Daphene Cliente Aluguel"
    },
    {
        "phone_number": "+554991458511",
        "public_name": "Jonathan Proprietário Cartagena 1802"
    },
    {
        "phone_number": "+554399950746",
        "public_name": "At 2m Patricia Monteiro Cliente"
    },
    {
        "phone_number": "+554791119090",
        "public_name": "Paulo Sabatke Proprietário Imperial Tower"
    },
    {
        "phone_number": "+554796358822",
        "public_name": "Rafaela Cliente BC"
    },
    {
        "phone_number": "+5511998872097",
        "public_name": "AT 800K - Marlene Cliente"
    },
    {
        "phone_number": "+554999532296",
        "public_name": "AT 1.6M- Ana Gaio Cliente"
    },
    {
        "phone_number": "+555499474432",
        "public_name": "Rejane Baseggio Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554799356105",
        "public_name": "Daniel Proprietario Sobrado 720 Mil"
    },
    {
        "phone_number": "+554599755564",
        "public_name": "Ervino Cliente"
    },
    {
        "phone_number": "+554799632964",
        "public_name": "At 700k Francisco Costa Cliente"
    },
    {
        "phone_number": "+554198521203",
        "public_name": "Danielle Sarruf Cliente Organica"
    },
    {
        "phone_number": "+554598261212",
        "public_name": "Vanessa Cliente Yaschthouse"
    },
    {
        "phone_number": "+554799955275",
        "public_name": "AT 1.3M- Alex Cliente"
    },
    {
        "phone_number": "+554691306915",
        "public_name": "AT 1.6M- Mauricio Cliente Mkt Parcelado"
    },
    {
        "phone_number": "+554799184447",
        "public_name": "Reginaldo Granja Cliente Organica"
    },
    {
        "phone_number": "+5514998645353",
        "public_name": "AT 1.6M - Erico Fabricio Cliente"
    },
    {
        "phone_number": "+553184840172",
        "public_name": "AT 800K -Luiz Rogerio Cliente -Casa"
    },
    {
        "phone_number": "+554799163336",
        "public_name": "Rafael Proprietario Frente Mar"
    },
    {
        "phone_number": "+554498522411",
        "public_name": "Gulmar Magalhaes Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554199930633",
        "public_name": "Claudineia Cliente Do Laurence"
    },
    {
        "phone_number": "+554196238811",
        "public_name": "AT 1M Mike Cliente"
    },
    {
        "phone_number": "+554299690900",
        "public_name": "Reni Cliente Organica"
    },
    {
        "phone_number": "+554799575812",
        "public_name": "AT 800k Lucia Santos Cliente Casa"
    },
    {
        "phone_number": "+555596522200",
        "public_name": "AT 2M- Marcos Rogerio Cliente Mkt"
    },
    {
        "phone_number": "+554899300010",
        "public_name": "Éder Marido Cliente Fabricia"
    },
    {
        "phone_number": "+555499092876",
        "public_name": "Aline Bertamone  Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796547631",
        "public_name": "Roberta Fontana Marchezan Cliente Yachthouse"
    },
    {
        "phone_number": "+554399846838",
        "public_name": "Jean Cliente Village Dos Ipes"
    },
    {
        "phone_number": "+554991356332",
        "public_name": "At 3M Everton Sandrin Cliente"
    },
    {
        "phone_number": "+554799838338",
        "public_name": "AT 2M Jonas Cliente"
    },
    {
        "phone_number": "+554799199282",
        "public_name": "Lygia Esposa Do Ze Proprietario Pioner Tower"
    },
    {
        "phone_number": "+554499292480",
        "public_name": "AT 800M Sidney Vidal Cliente"
    },
    {
        "phone_number": "+554499059273",
        "public_name": "Arizona FoodTruck Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554791238342",
        "public_name": "AT 800K - Jair Nunes Cliente"
    },
    {
        "phone_number": "+554784737645",
        "public_name": "Kamilly Klug Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554797117676",
        "public_name": "AT 500K - Larissa Cliente"
    },
    {
        "phone_number": "+553388066610",
        "public_name": "At 2m Carlos Dantes Britto Gondim Cliente"
    },
    {
        "phone_number": "+554888250148",
        "public_name": "AT 1.6M- Luiz Carlos Cliente"
    },
    {
        "phone_number": "+554999309025",
        "public_name": "AT 1M-Pedro Cliente - Parcelado"
    },
    {
        "phone_number": "+554399102162",
        "public_name": "AT 800K -Juliano Cliente-Praia Brava"
    },
    {
        "phone_number": "+554791308306",
        "public_name": "AT 800K -Jessica Santos Cliente Casa"
    },
    {
        "phone_number": "+554691119823",
        "public_name": "Karol Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799754117",
        "public_name": "AT 500K - Oscar Cliente"
    },
    {
        "phone_number": "+554499274747",
        "public_name": "At 2m Lucas Marques Cliente"
    },
    {
        "phone_number": "+554791200204",
        "public_name": "AT 500k Raíza Esposa Gui Cliente"
    },
    {
        "phone_number": "+554899267399",
        "public_name": "AT 1M-Danton Medeiros Cliente"
    },
    {
        "phone_number": "+554699753392",
        "public_name": "Denis Cliente Investidor"
    },
    {
        "phone_number": "+554796311053",
        "public_name": "Evandro Proprietario Casa Arririba"
    },
    {
        "phone_number": "+554792612877",
        "public_name": "Decio Cliente Vendido"
    },
    {
        "phone_number": "+554799387469",
        "public_name": "AT 800K - Robson Cliente Praia Brava"
    },
    {
        "phone_number": "+554788181180",
        "public_name": "Everton Proprietário Privilége 3002"
    },
    {
        "phone_number": "+554792252710",
        "public_name": "Vilmar Cliente Organica"
    },
    {
        "phone_number": "+554488240990",
        "public_name": "Nicolas Beck Cliente"
    },
    {
        "phone_number": "+554784555544",
        "public_name": "AT 1.3M - Andre Cliente"
    },
    {
        "phone_number": "+554797731832",
        "public_name": "Kleber Aramis Braun Cliente"
    },
    {
        "phone_number": "+554799836829",
        "public_name": "Jose Augusto Proprietario Vision Tower 1400"
    },
    {
        "phone_number": "+554399859639",
        "public_name": "Lucas Proprietario Varandas Do Atlantico"
    },
    {
        "phone_number": "+554799168788",
        "public_name": "At 2m Daniele Cliente"
    },
    {
        "phone_number": "+554791093152",
        "public_name": "Mauro Proprietário Pedras Brancas 306"
    },
    {
        "phone_number": "+554788060104",
        "public_name": "Andre Cliente Comprou The Place"
    },
    {
        "phone_number": "+554799963204",
        "public_name": "At 3m Marco Cliente Indicação Sergio"
    },
    {
        "phone_number": "+554199971919",
        "public_name": "Tiriva Proprietário D. Irma"
    },
    {
        "phone_number": "+556196172624",
        "public_name": "At 1.6m Hugo Cliente"
    },
    {
        "phone_number": "+5511982775000",
        "public_name": "Flavio Adriano Paulo Cliente Organica"
    },
    {
        "phone_number": "+556699844513",
        "public_name": "AT 1M- Leo Cliente Mkt -Parcelado"
    },
    {
        "phone_number": "+554791961410",
        "public_name": "Bruno Proprietário Maria Raquel 901"
    },
    {
        "phone_number": "+554792714701",
        "public_name": "AT 1.3M- Cristian Cliente Joinville"
    },
    {
        "phone_number": "+554498021866",
        "public_name": "AT 500K - Ricardo Cliente Sobrado"
    },
    {
        "phone_number": "+554784050018",
        "public_name": "AT 400K Ilair Tomazelli Cliente -"
    },
    {
        "phone_number": "+554288288698",
        "public_name": "AT 500K -Pedro Valentim Cliente  Praia Brava Mkt"
    },
    {
        "phone_number": "+554799357785",
        "public_name": "Glauter Luiz Tibau Proprietario Barramares 802"
    },
    {
        "phone_number": "+554498684992",
        "public_name": "AT 800K - Everton Cliente Mkt  Parcelado"
    },
    {
        "phone_number": "+554199851294",
        "public_name": "Cristina Cliente Curitiba"
    },
    {
        "phone_number": "+554788230789",
        "public_name": "AT 1M Marlene Scheller Cliente"
    },
    {
        "phone_number": "+554784196409",
        "public_name": "AT 800K - Adriana Cliente BC"
    },
    {
        "phone_number": "+554791580064",
        "public_name": "AT 1.2m Lu Avila Cliente"
    },
    {
        "phone_number": "+554199784646",
        "public_name": "Rubeni Proprietario Maria Augusta 802 Investidor"
    },
    {
        "phone_number": "+5513981285974",
        "public_name": "AT 500K - Beto Cliente"
    },
    {
        "phone_number": "+554399771212",
        "public_name": "At 2.5m Ricardo Duarte Cliente"
    },
    {
        "phone_number": "+15613051134",
        "public_name": "At 3.5m Cesar E Mari Favareto Cliente"
    },
    {
        "phone_number": "+554797705371",
        "public_name": "Daiana Freitas Cliente Serenity"
    },
    {
        "phone_number": "+554797337331",
        "public_name": "AT 800k Saulo Cliente Casa"
    },
    {
        "phone_number": "+554799772757",
        "public_name": "Paulo Proprietário Villa Siena nações"
    },
    {
        "phone_number": "+5511991658529",
        "public_name": "AT 500K - Daltro Cliente SP"
    },
    {
        "phone_number": "+5511998909844",
        "public_name": "At 4m Mariana Santos Cliente"
    },
    {
        "phone_number": "+554988340132",
        "public_name": "AT 1M- Suian Carvalho Cliente - Tem Permuta Em BC"
    },
    {
        "phone_number": "+554799114402",
        "public_name": "Irineu Proprietário Casa Condominio Aririba"
    },
    {
        "phone_number": "+555491149355",
        "public_name": "AT 1.6M Romeu Lovato Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554784758134",
        "public_name": "At 800k Julinana Freitas Cliente Casa"
    },
    {
        "phone_number": "+554797583028",
        "public_name": "AT 800K -Juliana Chagas Cliente"
    },
    {
        "phone_number": "+555199881210",
        "public_name": "AT 1M- Cristiano Cliente Parcelado Tem Motor Home E Jaguar"
    },
    {
        "phone_number": "+554796696090",
        "public_name": "Dullius Cliente Investidor"
    },
    {
        "phone_number": "+554484456936",
        "public_name": "Luciellen Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554391541226",
        "public_name": "At 6.5m Jeferson Marcelino Cliente"
    },
    {
        "phone_number": "+554399152738",
        "public_name": "At 4m Ígor Zanini Cliente"
    },
    {
        "phone_number": "+555491842507",
        "public_name": "At 3.5m Odair Nardi Cliente Marau"
    },
    {
        "phone_number": "+555499759980",
        "public_name": "Kuki Cliente Bento Gonçalves"
    },
    {
        "phone_number": "+554788011705",
        "public_name": "AT 800 Mil Daniela Cliente Casa"
    },
    {
        "phone_number": "+554196789043",
        "public_name": "AT 1.3M -Lislie Cliente"
    },
    {
        "phone_number": "+554799837781",
        "public_name": "Milton Proprietário Maria Eduarda 300"
    },
    {
        "phone_number": "+555599021968",
        "public_name": "Gilmar Prevedello Cliente"
    },
    {
        "phone_number": "+555191720091",
        "public_name": "At 7m José Paulinho Primaz Cliente"
    },
    {
        "phone_number": "+554799793882",
        "public_name": "Cícero Cliente"
    },
    {
        "phone_number": "+554796789003",
        "public_name": "Roberto Proprietário Malibu 1403"
    },
    {
        "phone_number": "+554791075759",
        "public_name": "AT 800K -J Berg Cliente - Praia Brava"
    },
    {
        "phone_number": "+554799054555",
        "public_name": "AT 2.5m Patricia Souto Cliente"
    },
    {
        "phone_number": "+5519983516706",
        "public_name": "Marcos Antonio Proprietario"
    },
    {
        "phone_number": "+554799836372",
        "public_name": "Marcelo Proprietario Frankfurt 7/8 Duplex Frente Mar"
    },
    {
        "phone_number": "+555196463798",
        "public_name": "At 1.3m Renesio Cliente Indicacao Geovane Lageado"
    },
    {
        "phone_number": "+554191812243",
        "public_name": "AT 3M Leonardo Sepulcri Cliente Comprou"
    },
    {
        "phone_number": "+555399426831",
        "public_name": "Fatima Teodoro Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554899830638",
        "public_name": "Jackes Proprietario La Majestique FG 1101"
    },
    {
        "phone_number": "+555597240409",
        "public_name": "Gesselmar Bolico Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799671680",
        "public_name": "Gabriel Proprietario Torremolinos 1802"
    },
    {
        "phone_number": "+555499290835",
        "public_name": "Vagner Sperotto Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554791424706",
        "public_name": "AT 800K - Brenda Cliente Casa"
    },
    {
        "phone_number": "+554198756603",
        "public_name": "AT 500K -Maria Cristina Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+555599737056",
        "public_name": "Edmilson Cliente Marido Dani"
    },
    {
        "phone_number": "+555181316028",
        "public_name": "Rosangela Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799257029",
        "public_name": "Daniel Cliente Lead Rocket"
    },
    {
        "phone_number": "+555481117635",
        "public_name": "Henrique Romani Cliente Filho Ademir"
    },
    {
        "phone_number": "+554988461508",
        "public_name": "João Altair Dos Santos Cliente Organica"
    },
    {
        "phone_number": "+554796958720",
        "public_name": "Ivan Rodrigo Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554199273025",
        "public_name": "At 1m Newton Cliente"
    },
    {
        "phone_number": "+15612613518",
        "public_name": "At 3.5m Cesar Favareto Cliente"
    },
    {
        "phone_number": "+5513996617921",
        "public_name": "At 2.5m Duda Mascari Cliente"
    },
    {
        "phone_number": "+555481193689",
        "public_name": "Claudia Cliente Rs"
    },
    {
        "phone_number": "+554784637088",
        "public_name": "Denir Proprietário Tropical Summer 1801"
    },
    {
        "phone_number": "+554796130636",
        "public_name": "At 2.5m Maria Lucia Merdes Furtado Cliente"
    },
    {
        "phone_number": "+554796714181",
        "public_name": "At 2m Raquel Gunther Cliente"
    },
    {
        "phone_number": "+556299655045",
        "public_name": "Jerónimo Volpato Ocean Proprietário"
    },
    {
        "phone_number": "+554188162003",
        "public_name": "AT 1M- Anderson Cliente Sobrado"
    },
    {
        "phone_number": "+554584229996",
        "public_name": "AT 800K - Cliente Praia Brava"
    },
    {
        "phone_number": "+554792884866",
        "public_name": "At 3.5m William Echterhoff Cliente"
    },
    {
        "phone_number": "+554799331743",
        "public_name": "AT 800K - Maicon Maschio Cliente"
    },
    {
        "phone_number": "+554784140171",
        "public_name": "AT 1.3M -Nilo Cliente - Vista Mar"
    },
    {
        "phone_number": "+554498362944",
        "public_name": "AT 800K -Jefferson Fernandes Cliente Casa"
    },
    {
        "phone_number": "+554792242867",
        "public_name": "At 2m Valdeci Ferreira Diniz Cliente"
    },
    {
        "phone_number": "+555581578209",
        "public_name": "Fatiana Cliente Mkt Boreal"
    },
    {
        "phone_number": "+556699882618",
        "public_name": "At 3.5m Christian Viriato Cliente"
    },
    {
        "phone_number": "+555499760607",
        "public_name": "Jair Luiz Proprietario Beach Tower"
    },
    {
        "phone_number": "+554899315100",
        "public_name": "Marcelo Cliente Indicacao Raul"
    },
    {
        "phone_number": "+554288019353",
        "public_name": "AT 2M- Diocea Oliveira Cliente Mkt"
    },
    {
        "phone_number": "+555591185103",
        "public_name": "Clay Cliente Vendido"
    },
    {
        "phone_number": "+5511981069810",
        "public_name": "AT 2.5m Alander Brandão Cliente"
    },
    {
        "phone_number": "+554498750213",
        "public_name": "AT 1M-Josseane Cliente Mkt"
    },
    {
        "phone_number": "+554195953170",
        "public_name": "At 2.5m Rogério Riva Cliente"
    },
    {
        "phone_number": "+554796803741",
        "public_name": "AT 800K - Marlene Cliente Quer Casa"
    },
    {
        "phone_number": "+554799149402",
        "public_name": "AT 1M- Sandro Cliente- Tem Permuta De 500 Mil"
    },
    {
        "phone_number": "+554792342838",
        "public_name": "AT 1.6M Luciano Valandro Cliente"
    },
    {
        "phone_number": "+554899692809",
        "public_name": "AT 2.5m Elza De Avila Cliente"
    },
    {
        "phone_number": "+554799674079",
        "public_name": "Márcia Poletti Cliente Italian"
    },
    {
        "phone_number": "+554788648430",
        "public_name": "AT 500K -Elisangela Cliente"
    },
    {
        "phone_number": "+554199234444",
        "public_name": "Jose Sampaio Proprietario BMW"
    },
    {
        "phone_number": "+554399026032",
        "public_name": "Paulo Bertucci Proprietario Cristale 501"
    },
    {
        "phone_number": "+555499814548",
        "public_name": "AT 4.5M- Anelise Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555199954339",
        "public_name": "Dagoberto Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799821347",
        "public_name": "AT 3M Rogerio Roedel Cliente"
    },
    {
        "phone_number": "+555193896599",
        "public_name": "Dionatan Dos Reis Bobsin Cliente Organica"
    },
    {
        "phone_number": "+554799607676",
        "public_name": "Janice Cliente"
    },
    {
        "phone_number": "+554799818283",
        "public_name": "Jader Cliente Ranking"
    },
    {
        "phone_number": "+554599151247",
        "public_name": "Geisa Cliente Cascavel"
    },
    {
        "phone_number": "+554799985298",
        "public_name": "AT 800K - Viktor Cliente"
    },
    {
        "phone_number": "+554899612270",
        "public_name": "AT 1.6M- Luíz Gustavo Moises Cliente Tem Permuta Em Mariscal"
    },
    {
        "phone_number": "+556584034991",
        "public_name": "Alexandre Proprietario Amores Da brava Frente 16"
    },
    {
        "phone_number": "+555599443570",
        "public_name": "Jean Cliente Studio 25"
    },
    {
        "phone_number": "+554797069393",
        "public_name": "Rafael Yared Cliente"
    },
    {
        "phone_number": "+554899239068",
        "public_name": "At 3.5m Thayni Librelato Cliente"
    },
    {
        "phone_number": "+554899818664",
        "public_name": "Valdir Tomazzi cliente 1 Dorm"
    },
    {
        "phone_number": "+554799095671",
        "public_name": "Juçara Soares Flor Cliente"
    },
    {
        "phone_number": "+554799483545",
        "public_name": "AT 800K - Maria Salete Cliente"
    },
    {
        "phone_number": "+5521999659977",
        "public_name": "Fred Proprietario Villa Vicenza"
    },
    {
        "phone_number": "+554799826664",
        "public_name": "AT 800K -Flavio Cliente BC -Barra Norte Pioneiros"
    },
    {
        "phone_number": "+554788181423",
        "public_name": "Flavia Cliente Olx"
    },
    {
        "phone_number": "+554599794580",
        "public_name": "Pedro Cliente Frente Mar"
    },
    {
        "phone_number": "+555491193464",
        "public_name": "Itelmar Proprietario Pacoste 16"
    },
    {
        "phone_number": "+554799845058",
        "public_name": "At 3.5m Alberto Cliente"
    },
    {
        "phone_number": "+554796850904",
        "public_name": "Marcelo Professor Cliente Avantis"
    },
    {
        "phone_number": "+555599999192",
        "public_name": "Eliane Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554784635104",
        "public_name": "AT 2.5M Inês Ghisleri Cliente"
    },
    {
        "phone_number": "+554799159998",
        "public_name": "Marcio Proprietário D Itália 501"
    },
    {
        "phone_number": "+555599638206",
        "public_name": "Leo Zollner Cliente Mkt"
    },
    {
        "phone_number": "+554184890008",
        "public_name": "At 3m Sandra Cristina Biscouto Cliente"
    },
    {
        "phone_number": "+554899361313",
        "public_name": "AT 1.6M Yuri Botega Cliente"
    },
    {
        "phone_number": "+555584079192",
        "public_name": "AT 500K - Regina Cliente"
    },
    {
        "phone_number": "+555384027951",
        "public_name": "At 1m Renan Lopes Cliente"
    },
    {
        "phone_number": "+554498217739",
        "public_name": "AT 800K - Ana Cliente"
    },
    {
        "phone_number": "+554491153127",
        "public_name": "João Ricardo Esteves Proprietario Vitra 2002"
    },
    {
        "phone_number": "+554988112944",
        "public_name": "Jair De Azevedo Cliente Tem Apt Em Meia Praia"
    },
    {
        "phone_number": "+555496028793",
        "public_name": "AT 800K - Valeria Meneguini Cliente"
    },
    {
        "phone_number": "+554591547280",
        "public_name": "Leo Holler Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554191937165",
        "public_name": "At 3m Rodrigo Lima Cliente"
    },
    {
        "phone_number": "+554788423445",
        "public_name": "At 3m Luis Garzon Cliente"
    },
    {
        "phone_number": "+554999634440",
        "public_name": "Edgar Cliente Organica"
    },
    {
        "phone_number": "+554199454911",
        "public_name": "AT 1M- Michael Cliente"
    },
    {
        "phone_number": "+555591782822",
        "public_name": "Marcio Cliente Mkt Frente Mar Trabalha Com Bitcoin"
    },
    {
        "phone_number": "+554792005885",
        "public_name": "Filipe Proprietário De Imoveis"
    },
    {
        "phone_number": "+554184035096",
        "public_name": "AT 1.3m Anderson Cliente"
    },
    {
        "phone_number": "+554799470128",
        "public_name": "AT 1M-Cristian Cliente Tem Terreno"
    },
    {
        "phone_number": "+554799883333",
        "public_name": "Corretor Proprietario Mario Quintana"
    },
    {
        "phone_number": "+554796112575",
        "public_name": "Neiva Santos De Souza Cliente Serenity"
    },
    {
        "phone_number": "+554599259380",
        "public_name": "Izabel Cliente Organica"
    },
    {
        "phone_number": "+554299790061",
        "public_name": "Sodenia Cliente Mulher Antonio"
    },
    {
        "phone_number": "+554197030220",
        "public_name": "At 3m Paulo Cliente Frente Mar"
    },
    {
        "phone_number": "+554391116597",
        "public_name": "AT 1.3M- Euclides Cliente"
    },
    {
        "phone_number": "+554788976321",
        "public_name": "Devair Proprietario Lumiere 2601"
    },
    {
        "phone_number": "+554199239966",
        "public_name": "At 5m Marcos Cliente Indicacao Fabio"
    },
    {
        "phone_number": "+556699125199",
        "public_name": "AT 800K - Jean Cliente- Casa"
    },
    {
        "phone_number": "+554799196026",
        "public_name": "AT 800K - Odete Cliente"
    },
    {
        "phone_number": "+556791376610",
        "public_name": "AT 500K - Aliris Cliente Apt"
    },
    {
        "phone_number": "+554791313191",
        "public_name": "AT 2.5m Cisso Schimitz Cliente"
    },
    {
        "phone_number": "+554899883189",
        "public_name": "AT 500K - Lili Matiola Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554291048689",
        "public_name": "Nadia Cliente Orbita"
    },
    {
        "phone_number": "+554796297290",
        "public_name": "At 800K Casa Carlos Barcelos Cliente"
    },
    {
        "phone_number": "+554791240556",
        "public_name": "AT 2M Jailson Silva Cliente"
    },
    {
        "phone_number": "+554899863535",
        "public_name": "At 3m Messias Fernandes Cliente"
    },
    {
        "phone_number": "+554999981959",
        "public_name": "Airton Cliente Vendido Royal"
    },
    {
        "phone_number": "+554796686407",
        "public_name": "At 1.6m Juliana Duarte Cliente"
    },
    {
        "phone_number": "+554799950403",
        "public_name": "AT 800K - Emelize Cliente"
    },
    {
        "phone_number": "+554399579464",
        "public_name": "At 3.5m Antonio Djair Puzzi Cliente"
    },
    {
        "phone_number": "+554792750033",
        "public_name": "At 1.6m Bruno Menegazzo Cliente"
    },
    {
        "phone_number": "+554791617535",
        "public_name": "Taryn De Matos Proprietario Splendia 1401"
    },
    {
        "phone_number": "+554799837530",
        "public_name": "Cap Ferrat Proprietário Oitavo"
    },
    {
        "phone_number": "+554197800170",
        "public_name": "At 500k Adriana Guinter Cliente"
    },
    {
        "phone_number": "+554199770002",
        "public_name": "Wilson Proprietário Italian 2302"
    },
    {
        "phone_number": "+556796720034",
        "public_name": "At 1.6m Nilza Pegoraro Cliente"
    },
    {
        "phone_number": "+554199796679",
        "public_name": "AT 1M - Adriana Cliente Barra Sul"
    },
    {
        "phone_number": "+555499091260",
        "public_name": "AT 800K -Arni Cliente Sarandi"
    },
    {
        "phone_number": "+554796462830",
        "public_name": "AT 500K - Cinara Cliente"
    },
    {
        "phone_number": "+555499311127",
        "public_name": "At 3m José Alceu Cliente"
    },
    {
        "phone_number": "+554488126699",
        "public_name": "GIUSEPPE LEGGI JUNIOR Cliente Investidor"
    },
    {
        "phone_number": "+554788248782",
        "public_name": "Silas Proprietario Area Rural Em Camboriu"
    },
    {
        "phone_number": "+554799020404",
        "public_name": "AT 500K - Airton Deschamps Cliente Mkt -Praia Brava"
    },
    {
        "phone_number": "+554198460656",
        "public_name": "Marco Aurelio Proprietario Mandala Pega Permuta Em CTB"
    },
    {
        "phone_number": "+5511998375439",
        "public_name": "Emerson Sergio Rigotti Cliente Aurora"
    },
    {
        "phone_number": "+554799216520",
        "public_name": "AT 800K - Fatima Cliente"
    },
    {
        "phone_number": "+554791331084",
        "public_name": "Marcus Vinicius De Moraes Proprietario Garden Plaza"
    },
    {
        "phone_number": "+555496801306",
        "public_name": "AT 1.3M- Dilamar Favareto Cliente Tapejara"
    },
    {
        "phone_number": "+554796505382",
        "public_name": "Priscila Proprietario Casa"
    },
    {
        "phone_number": "+555194407050",
        "public_name": "At 2m Marcelo Moraes Cliente"
    },
    {
        "phone_number": "+554799892707",
        "public_name": "At 2m Fabio Benedetti Cliente"
    },
    {
        "phone_number": "+554399236342",
        "public_name": "AT 500K Josi Cardin Cliente Mkt"
    },
    {
        "phone_number": "+554796505404",
        "public_name": "AT 1.6m Luciano Cliente"
    },
    {
        "phone_number": "+554699715991",
        "public_name": "At 5.5m Igor Chiminacio Cliente"
    },
    {
        "phone_number": "+554796047890",
        "public_name": "AT 1.3M -Nivia Pericolo Cliente - Frente Mar"
    },
    {
        "phone_number": "+554791528885",
        "public_name": "Kako Cliente Imperio Das Ondas 22"
    },
    {
        "phone_number": "+555198515349",
        "public_name": "AT 1M Alexandre Garcia Cliente"
    },
    {
        "phone_number": "+554191561938",
        "public_name": "Rafael Caillet Cliente Organica"
    },
    {
        "phone_number": "+554999172046",
        "public_name": "AT 800K - Caio Cliente"
    },
    {
        "phone_number": "+554797470000",
        "public_name": "Marco Emilio Proprietario Luar Biasa 1001"
    },
    {
        "phone_number": "+554799891012",
        "public_name": "Milton Floriani Proprietario Millenium 2450"
    },
    {
        "phone_number": "+554791236500",
        "public_name": "AT 1M- Rodrigo Cliente"
    },
    {
        "phone_number": "+554799128898",
        "public_name": "AT 1.3M Giuliana Cliente"
    },
    {
        "phone_number": "+554799807460",
        "public_name": "At 3.5m Borbinha Borba Cliente"
    },
    {
        "phone_number": "+554796520121",
        "public_name": "Iridete Cliente Miguel Bailak"
    },
    {
        "phone_number": "+554799713133",
        "public_name": "Antonio Conti Cliente"
    },
    {
        "phone_number": "+555496117282",
        "public_name": "At 2.5m Maria Cechin Cliente"
    },
    {
        "phone_number": "+554199299777",
        "public_name": "At 6.5m Rita Gayas Cliente"
    },
    {
        "phone_number": "+554799852690",
        "public_name": "Rosita Benner Cliente Organica"
    },
    {
        "phone_number": "+554197428492",
        "public_name": "Adriano Proprietario Rivera Frente Mar"
    },
    {
        "phone_number": "+554899056287",
        "public_name": "Romualdo Furlan Cliente Investidor"
    },
    {
        "phone_number": "+554199734038",
        "public_name": "Carlos Proprietário Colina Do Sol"
    },
    {
        "phone_number": "+554191578785",
        "public_name": "Edilson Cliente Organica"
    },
    {
        "phone_number": "+554792474816",
        "public_name": "AT 800K - Rodrigo Jose Pereira Cliente - Casa"
    },
    {
        "phone_number": "+554399219093",
        "public_name": "Leonice Cliente Apucarana"
    },
    {
        "phone_number": "+554199204751",
        "public_name": "At 3.5m Giani Amorim Cliente"
    },
    {
        "phone_number": "+554791306835",
        "public_name": "Rogerio Proprietário Salvador Dali 1801"
    },
    {
        "phone_number": "+554888638737",
        "public_name": "AT 800K - Nando Coelho Cliente - Planta"
    },
    {
        "phone_number": "+554198180191",
        "public_name": "At 5m Carlos Garcia Cliente Tem Casa Em Curitiba 3.5m"
    },
    {
        "phone_number": "+555499882824",
        "public_name": "AT 1.6M Claudia Travi Cliente Permuta Canela"
    },
    {
        "phone_number": "+554799748584",
        "public_name": "AT 1.6m Clelia Marta Cliente"
    },
    {
        "phone_number": "+554799330245",
        "public_name": "AT 2.5m Fabianne Caldeira Cliente"
    },
    {
        "phone_number": "+554799811839",
        "public_name": "AT 150 Mil Quer Terreno Joao Cliente Parcelado"
    },
    {
        "phone_number": "+554799991479",
        "public_name": "Rodolfo Cliente"
    },
    {
        "phone_number": "+555499678259",
        "public_name": "AT 500K - Carlos Cliente - Praia Brava"
    },
    {
        "phone_number": "+554991351666",
        "public_name": "AT 1M- Joao Vieira Cliente- Parcelado"
    },
    {
        "phone_number": "+554999963169",
        "public_name": "AT 800K - Maria Cliente"
    },
    {
        "phone_number": "+554799003398",
        "public_name": "Franco Proprietário Frente Mar"
    },
    {
        "phone_number": "+5511945323961",
        "public_name": "Marcelo Xavier Proprietario Cobertura Avangard"
    },
    {
        "phone_number": "+554797119000",
        "public_name": "AT 1.6m Alcina Venturi Cliente"
    },
    {
        "phone_number": "+554899891314",
        "public_name": "Edson Venera Proprietário Lumiere 3701"
    },
    {
        "phone_number": "+554797693505",
        "public_name": "Delfes Proprietario Reno 1001"
    },
    {
        "phone_number": "+554799740319",
        "public_name": "Roberto Cliente Organica"
    },
    {
        "phone_number": "+554799117744",
        "public_name": "AT 800K - Luciana Arouca Cliente Casa"
    },
    {
        "phone_number": "+554792212770",
        "public_name": "Kleber Simões Cliente"
    },
    {
        "phone_number": "+554799220000",
        "public_name": "AT 1M- Flaviano Ramos Cliente"
    },
    {
        "phone_number": "+554792466647",
        "public_name": "AT 1M Alessandro Ferreira Cliente"
    },
    {
        "phone_number": "+554195767991",
        "public_name": "Jovina Campos Cliente"
    },
    {
        "phone_number": "+554196835151",
        "public_name": "At 3m Marcela Ribeiro Cliente"
    },
    {
        "phone_number": "+554199611593",
        "public_name": "AT 800k Cassia Regina Cliente Casa"
    },
    {
        "phone_number": "+555499738865",
        "public_name": "AT 2.5M- Fabiano Boeno Cliente Mkt Lagoa Vermelha"
    },
    {
        "phone_number": "+555499745836",
        "public_name": "Fernando Luiz Marchioretto Cliente 135 Jardins"
    },
    {
        "phone_number": "+554799838977",
        "public_name": "Antonio Ramiro Proprietario Barra Tower"
    },
    {
        "phone_number": "+554288831161",
        "public_name": "AT 500K - Ezequiel Danilo Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554199742133",
        "public_name": "Roberto Cliente Curitiba"
    },
    {
        "phone_number": "+559192630015",
        "public_name": "At 2m Leandro Cliente Investidor"
    },
    {
        "phone_number": "+554799799400",
        "public_name": "AT 1M- Guilherme Cliente"
    },
    {
        "phone_number": "+554199855678",
        "public_name": "AT 1M- Paulo Vinicius Cliente"
    },
    {
        "phone_number": "+554691201234",
        "public_name": "Josiane Scopel Cliente Esposa Do Junior"
    },
    {
        "phone_number": "+5514998610332",
        "public_name": "Dion Andrade Cliente Aurora"
    },
    {
        "phone_number": "+555491563453",
        "public_name": "AT 1.6M- Daniel Nicolodi Cliente"
    },
    {
        "phone_number": "+554799214004",
        "public_name": "Maury Roberto Proprietario Monte Olympos 1604"
    },
    {
        "phone_number": "+554898417228",
        "public_name": "AT 500K -Sandra Cliente  Mkt"
    },
    {
        "phone_number": "+554797070101",
        "public_name": "Wilian Proprietario Bmw"
    },
    {
        "phone_number": "+554792590106",
        "public_name": "Eduardo Cliente Organica (Blumenau)"
    },
    {
        "phone_number": "+554398485145",
        "public_name": "Keitilaine Paszko Cliente Organica"
    },
    {
        "phone_number": "+554991058868",
        "public_name": "At 3m Maria Zancanaro Cliente"
    },
    {
        "phone_number": "+554799833014",
        "public_name": "AT 1.3M- Deize Cliente Tem Lausanne"
    },
    {
        "phone_number": "+554799872837",
        "public_name": "At 2m Henrique Labes Da Fontana Cliente"
    },
    {
        "phone_number": "+554799095222",
        "public_name": "Cleusa Proprietário Torremolinos 2302"
    },
    {
        "phone_number": "+554591489086",
        "public_name": "At 1.6m Sergio Franczak Cliente"
    },
    {
        "phone_number": "+554799118395",
        "public_name": "AT 1.3M- Gabriela Cliente"
    },
    {
        "phone_number": "+554796095446",
        "public_name": "AT 2M Michelle Duarte Cliente"
    },
    {
        "phone_number": "+554799833670",
        "public_name": "Osni Kaester Proprietario Torre Atlantica"
    },
    {
        "phone_number": "+555197832021",
        "public_name": "AT 3M Steffani Costa Cliente"
    },
    {
        "phone_number": "+554796779892",
        "public_name": "At 500K Zila Adur Cliente"
    },
    {
        "phone_number": "+555481180236",
        "public_name": "At 1.6M Felipe Michelin Cliente"
    },
    {
        "phone_number": "+554991225566",
        "public_name": "At 1.2m Gilson Santos Cliente"
    },
    {
        "phone_number": "+554799836665",
        "public_name": "Proprietário Gonzaga Torre Di Lyon 701"
    },
    {
        "phone_number": "+555184242229",
        "public_name": "Daniel Luiz Machado Proprietario Algaleo"
    },
    {
        "phone_number": "+554999853053",
        "public_name": "At 3m Francisco Hilgemberg Cliente"
    },
    {
        "phone_number": "+554884555548",
        "public_name": "At 1.3 João Maurique Cliente"
    },
    {
        "phone_number": "+556696832628",
        "public_name": "At 3.5m Iris Ferreira Cliente"
    },
    {
        "phone_number": "+5519974281856",
        "public_name": "At 5m Ricardo Machado Cliente"
    },
    {
        "phone_number": "+555499262428",
        "public_name": "Victor Cliente Indicacao Mauro Conapique"
    },
    {
        "phone_number": "+554797303900",
        "public_name": "At 3.5m Harley Amaral Cliente"
    },
    {
        "phone_number": "+554197400154",
        "public_name": "AT 800K - Everton Cliente  Parcelado"
    },
    {
        "phone_number": "+554199575299",
        "public_name": "Roberto Zeclhynski Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555591128998",
        "public_name": "At 3.5m Janice Da Silva Cliente"
    },
    {
        "phone_number": "+554197627777",
        "public_name": "AT 500K - Charles Cliente"
    },
    {
        "phone_number": "+554784965836",
        "public_name": "At 3.5m Marli Cliente"
    },
    {
        "phone_number": "+554196778171",
        "public_name": "José Peixoto Cliente Organica"
    },
    {
        "phone_number": "+554187219648",
        "public_name": "At 6m Felipe Magaldi Cliente"
    },
    {
        "phone_number": "+5511996188762",
        "public_name": "Pericles Proprietario Cobertura Nina Shurmann"
    },
    {
        "phone_number": "+554199971038",
        "public_name": "Magnum Cliente Privilegie"
    },
    {
        "phone_number": "+554199260020",
        "public_name": "Vilmar Cliente Indicacao Sergio"
    },
    {
        "phone_number": "+554799714306",
        "public_name": "AT 800K -Junior Cliente Casa"
    },
    {
        "phone_number": "+554784690064",
        "public_name": "Alessandro Oliveira Cliente Investidor"
    },
    {
        "phone_number": "+554888028841",
        "public_name": "AT 2.5m Tadeu Demboski Cliente"
    },
    {
        "phone_number": "+554799598998",
        "public_name": "AT 800K - Anderson Cruz Cliente"
    },
    {
        "phone_number": "+555599991626",
        "public_name": "At 3m Jean Rafael Pinto Cliente"
    },
    {
        "phone_number": "+554898622031",
        "public_name": "Rafael Marido Karina Cliente"
    },
    {
        "phone_number": "+554184165976",
        "public_name": "At 2.5m Emanuel Castelli Ribas Cliente"
    },
    {
        "phone_number": "+554792750765",
        "public_name": "AT 500K - Sergio Cliente Praia Brava"
    },
    {
        "phone_number": "+553182861339",
        "public_name": "At 1.6m GUSTAVOPH Cliente"
    },
    {
        "phone_number": "+554791344763",
        "public_name": "At 1.3m Ana Paula Gross Goncalves Cliente"
    },
    {
        "phone_number": "+554799283800",
        "public_name": "AT 500K - Fabio Dias Cliente Tem Casa De 200 Em Jvl"
    },
    {
        "phone_number": "+554784146992",
        "public_name": "AT 2m Rafaella Schmitt Cliente Praia Brava"
    },
    {
        "phone_number": "+554198620025",
        "public_name": "AT 800K - Anderson Cliente"
    },
    {
        "phone_number": "+554391030102",
        "public_name": "At 3.5m Ana Beatriz Cliente"
    },
    {
        "phone_number": "+554288125100",
        "public_name": "Mario Cliente Olx"
    },
    {
        "phone_number": "+554791898767",
        "public_name": "Luiz Carlos Pomiecinski Cliente Organica"
    },
    {
        "phone_number": "+554791013100",
        "public_name": "AT 2.5 Rovena Cliente"
    },
    {
        "phone_number": "+554799254868",
        "public_name": "Tassi Marques Cliente São Bento Do Sul"
    },
    {
        "phone_number": "+554196757500",
        "public_name": "At 3m Ludmila De Castro Cliente"
    },
    {
        "phone_number": "+554796090854",
        "public_name": "Sabrine Cliente"
    },
    {
        "phone_number": "+554799148289",
        "public_name": "AT 1.6M Samara Fossari Cliente"
    },
    {
        "phone_number": "+554788612471",
        "public_name": "AT 3.5M Neusa Dalmolin Cliente"
    },
    {
        "phone_number": "+554784471156",
        "public_name": "At 3.5m Sandra Volles De Souza Cliente"
    },
    {
        "phone_number": "+554791757481",
        "public_name": "Suelen Finta Aben Cliente"
    },
    {
        "phone_number": "+554188645501",
        "public_name": "AT 500K - Antonio Cliente Curitiba Camboriu"
    },
    {
        "phone_number": "+554888362505",
        "public_name": "Pedro Paulo Poeta Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554788166970",
        "public_name": "Francisco Theiss Proprietario Costa Blanca E Flor De Lotus"
    },
    {
        "phone_number": "+554799779120",
        "public_name": "Marco Galdino Cliente BC"
    },
    {
        "phone_number": "+554799637702",
        "public_name": "At 2m Sandra Candido Cliente Casa Caledonia"
    },
    {
        "phone_number": "+554199155531",
        "public_name": "Alexandre Proprietario Onne Home Invetidor"
    },
    {
        "phone_number": "+554691118791",
        "public_name": "At 2.5m Andreia Guedes Cliente"
    },
    {
        "phone_number": "+554788618638",
        "public_name": "Fabricio Cliente"
    },
    {
        "phone_number": "+554799834659",
        "public_name": "At 5m Marcio Cliente"
    },
    {
        "phone_number": "+554799572211",
        "public_name": "AT 800K - Claudio Cliente BC"
    },
    {
        "phone_number": "+554799411340",
        "public_name": "AT 1.6M- Denilson Sevei Masson Cliente"
    },
    {
        "phone_number": "+554199035995",
        "public_name": "At 5m Wania Ditzel Cliente"
    },
    {
        "phone_number": "+554498361568",
        "public_name": "AT 2M- Jose Carlos Cliente"
    },
    {
        "phone_number": "+59996958133",
        "public_name": "Blanca Colmenares Cliente Paraguai"
    },
    {
        "phone_number": "+554888450656",
        "public_name": "At 3.5m Mine Melo Cliente"
    },
    {
        "phone_number": "+554399945921",
        "public_name": "At 1.6m Abdo M. Cliente"
    },
    {
        "phone_number": "+554991365914",
        "public_name": "Patricia Cliente Organica"
    },
    {
        "phone_number": "+554199656513",
        "public_name": "Neusa Cliente Curitiba"
    },
    {
        "phone_number": "+554799830106",
        "public_name": "Sergio Proprietario Ilha Do Sol 1901"
    },
    {
        "phone_number": "+556499847126",
        "public_name": "At 6m Tânia Pavesi Cliente"
    },
    {
        "phone_number": "+555399749885",
        "public_name": "At 3m Lhoren Ballvartt Cliente"
    },
    {
        "phone_number": "+554999638093",
        "public_name": "Laurence Proprietario Apartameto BC Aluga"
    },
    {
        "phone_number": "+554799214852",
        "public_name": "AT 1.6M- Aloir Pai Cliente"
    },
    {
        "phone_number": "+554791664114",
        "public_name": "At 3.5m Marise Zanella Cliente"
    },
    {
        "phone_number": "+554796441900",
        "public_name": "Carlos Proprietário Leonardo Da Vinci Praia Brava"
    },
    {
        "phone_number": "+554999142180",
        "public_name": "Gustavo Cliente Casa Concórdia Vendido"
    },
    {
        "phone_number": "+554796864015",
        "public_name": "Jackson Proprietario North Shore 802"
    },
    {
        "phone_number": "+554788195588",
        "public_name": "AT 2M Alessandra Badalotti Cliente"
    },
    {
        "phone_number": "+554784645005",
        "public_name": "AT 800K William GR Cliente Casa"
    },
    {
        "phone_number": "+554199583121",
        "public_name": "AT 1.3 M Mari Souza Cliente"
    },
    {
        "phone_number": "+554791017675",
        "public_name": "AT 2M Luiz Eduardo Cliente"
    },
    {
        "phone_number": "+554792573418",
        "public_name": "Felipe Macedo Cliente Permuta Caxias Do Sul"
    },
    {
        "phone_number": "+556992098776",
        "public_name": "AT 500K - Alexandre Nogueira Cliente"
    },
    {
        "phone_number": "+555199463798",
        "public_name": "Renesio Cliente Indicacao Geovane Lageado"
    },
    {
        "phone_number": "+555499845868",
        "public_name": "At 3m Zuleica Haln Cliente"
    },
    {
        "phone_number": "+554599126464",
        "public_name": "Filha Vilson Proprietário Villa Serena 3503"
    },
    {
        "phone_number": "+555599632791",
        "public_name": "AT 800K - Marcelo Reis Cliente - Praia Brava Mkt"
    },
    {
        "phone_number": "+554196221802",
        "public_name": "AT 800k Cristine Mariana Cliente"
    },
    {
        "phone_number": "+5519983834770",
        "public_name": "AT 1M- Marcelo Ferraz Cliente"
    },
    {
        "phone_number": "+554197967067",
        "public_name": "AT 1.6M Jessica Repukna Cliente"
    },
    {
        "phone_number": "+554999876374",
        "public_name": "Renato Mauricio Basso Proprietário Torre Atlantica"
    },
    {
        "phone_number": "+554299875089",
        "public_name": "Ana Paula Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554784670494",
        "public_name": "At 3.5m Junior Da Silva Cliente"
    },
    {
        "phone_number": "+554791684793",
        "public_name": "At 3m Alaércio Tizoni Cliente"
    },
    {
        "phone_number": "+554791291628",
        "public_name": "At 1.6m Gustavo Zaninotti Cliente"
    },
    {
        "phone_number": "+554796051476",
        "public_name": "Darli Cliente Organica"
    },
    {
        "phone_number": "+556699848810",
        "public_name": "At 2.5m Gerson Mattei Cliente"
    },
    {
        "phone_number": "+555481217215",
        "public_name": "Proprietario - Andre Caxias"
    },
    {
        "phone_number": "+554796519183",
        "public_name": "Valmir Proprietário Costa Splendida 1401"
    },
    {
        "phone_number": "+554788369387",
        "public_name": "Levi Proprietario Ville De France"
    },
    {
        "phone_number": "+554799734959",
        "public_name": "AT 2.5m Leoonidás Dias Cliente"
    },
    {
        "phone_number": "+554788496900",
        "public_name": "AT 800K - Marta Cliente"
    },
    {
        "phone_number": "+5521994471775",
        "public_name": "Luiz Claudio Cliente RJ Quer Casa"
    },
    {
        "phone_number": "+554799586641",
        "public_name": "AT 800K -Mayara Cliente"
    },
    {
        "phone_number": "+554791477070",
        "public_name": "Elaine Coelho Cliente Proprietaria Anglo"
    },
    {
        "phone_number": "+554984165084",
        "public_name": "Joaquim Proprietário Ville De France"
    },
    {
        "phone_number": "+554799593729",
        "public_name": "AT 800K - Rodolfo Cliente"
    },
    {
        "phone_number": "+554788095897",
        "public_name": "At 1.6M Davi Soldatelli Cliente"
    },
    {
        "phone_number": "+554198662425",
        "public_name": "AT 1M -Vanessa Galli Cliente"
    },
    {
        "phone_number": "+554298031550",
        "public_name": "At 1.6m Patricia Naiverth Cliente"
    },
    {
        "phone_number": "+554796622087",
        "public_name": "AT 500K - Isabela Cliente Casa"
    },
    {
        "phone_number": "+554498016974",
        "public_name": "AT 1M Cristiano Rodrigues Cliente"
    },
    {
        "phone_number": "+555198418072",
        "public_name": "AT 1.3M -Jair Ribeiro Cliente"
    },
    {
        "phone_number": "+554599722828",
        "public_name": "AT 4.5m Dercio Bonitti Cliente"
    },
    {
        "phone_number": "+554799221676",
        "public_name": "AT 800k Simoni Janning Cliente"
    },
    {
        "phone_number": "+554799837707",
        "public_name": "Nelson Proprietario 901 Gran Vintage"
    },
    {
        "phone_number": "+554799238241",
        "public_name": "Vinicius Cliente BC"
    },
    {
        "phone_number": "+554199850246",
        "public_name": "AT 1M- Manoel Cliente Curitiba  Praia Brava"
    },
    {
        "phone_number": "+5521981017180",
        "public_name": "AT 500K -Taises Figueiredo Cliente"
    },
    {
        "phone_number": "+554799493938",
        "public_name": "Rafael Cliente Vendido"
    },
    {
        "phone_number": "+556999916323",
        "public_name": "At 3.5m Elisangela Cliente"
    },
    {
        "phone_number": "+554391461488",
        "public_name": "AT 1M-Giuseppe Cliente Londrina - Barra Sul"
    },
    {
        "phone_number": "+554699206577",
        "public_name": "Adriano Cliente Organica"
    },
    {
        "phone_number": "+555499179217",
        "public_name": "Fabricio Cliente Caxias Do Sul"
    },
    {
        "phone_number": "+554599381667",
        "public_name": "Silvana Fatima Vigo Cliente Orbita"
    },
    {
        "phone_number": "+554598062467",
        "public_name": "Cassio Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554797051692",
        "public_name": "Áurea Cliente Maringa"
    },
    {
        "phone_number": "+554799834157",
        "public_name": "AT 800K Dani Dalponte Cliente Casa Tem Apt 500k Vila Real"
    },
    {
        "phone_number": "+554891019101",
        "public_name": "Davi Proprietario Cristina 1305"
    },
    {
        "phone_number": "+555491668203",
        "public_name": "AT 2.5M- Renan Lottici Cliente Mkt Marau"
    },
    {
        "phone_number": "+554796194977",
        "public_name": "Leandro Censi Cliente Yachthouse"
    },
    {
        "phone_number": "+554791216182",
        "public_name": "AT 800K - Luis Cliente Centro Norte"
    },
    {
        "phone_number": "+554196260911",
        "public_name": "AT 1M- Vagner Cliente Curitiba"
    },
    {
        "phone_number": "+554891441980",
        "public_name": "AT 800K - Suzana Cliente Bc"
    },
    {
        "phone_number": "+554796619299",
        "public_name": "Renato Cliente"
    },
    {
        "phone_number": "+554899916045",
        "public_name": "AT 500K - Alvaro Cliente"
    },
    {
        "phone_number": "+554199988948",
        "public_name": "Rodrigo Matos Proprietário Brava Beach"
    },
    {
        "phone_number": "+5511982640278",
        "public_name": "Alberto Prado Proprietario Barcelona"
    },
    {
        "phone_number": "+554199227787",
        "public_name": "At 3m Eveline Hasselmann Cliente Admira"
    },
    {
        "phone_number": "+554789144554",
        "public_name": "At 2m Mara Ligia Will Cliente"
    },
    {
        "phone_number": "+554484033181",
        "public_name": "Bruna Cliente Maringa"
    },
    {
        "phone_number": "+554899454496",
        "public_name": "At 2.5m Pedro Paulo Nau Junior Cliente"
    },
    {
        "phone_number": "+554688037023",
        "public_name": "AT 800k André Luiz Coitinho Cliente Mkt"
    },
    {
        "phone_number": "+559285905540",
        "public_name": "Davi Almeida Cliente Organica"
    },
    {
        "phone_number": "+554196429012",
        "public_name": "AT 800K - Lorena Cliente Curitiba"
    },
    {
        "phone_number": "+554199888557",
        "public_name": "AT 800K Fabiano Cliente Curitiba"
    },
    {
        "phone_number": "+5512974093496",
        "public_name": "Kiki Tavolaro Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554699259876",
        "public_name": "Herman Cliente Comprou Hamptons Investidor"
    },
    {
        "phone_number": "+554192728801",
        "public_name": "Lineu Proprietario Costa Esmeralda 802"
    },
    {
        "phone_number": "+554991463486",
        "public_name": "AT 500K - Goetten Cliente"
    },
    {
        "phone_number": "+554188820306",
        "public_name": "Vlademir Proprietario 2901 Argos"
    },
    {
        "phone_number": "+554799575129",
        "public_name": "At 1.3m Margareth Cliente"
    },
    {
        "phone_number": "+554796527375",
        "public_name": "Ivo Proprietario Lumiere 1001 1302"
    },
    {
        "phone_number": "+555199841204",
        "public_name": "AT 2M- Bejamin Bartz Cliente Investidor"
    },
    {
        "phone_number": "+554198012939",
        "public_name": "Tatyane Dall Algnolo Mkt Cliente Frente Mar"
    },
    {
        "phone_number": "+554199741455",
        "public_name": "At 2m Lilian Dominoni Simm Cliente"
    },
    {
        "phone_number": "+555599611182",
        "public_name": "Cliente Passo Fundo"
    },
    {
        "phone_number": "+554899874989",
        "public_name": "AT 1.6M- Marcio Cliente Mkt Tem Permuta Em Florianopolis"
    },
    {
        "phone_number": "+554799586677",
        "public_name": "Michel Cliente"
    },
    {
        "phone_number": "+555591337309",
        "public_name": "AT 500K - Adão Cambraia Cliente Mkt"
    },
    {
        "phone_number": "+554499722087",
        "public_name": "At 3.5m Marcos Gonçalves Cliente"
    },
    {
        "phone_number": "+554195553334",
        "public_name": "Claudio Cliente DS5"
    },
    {
        "phone_number": "+554192666407",
        "public_name": "Vanessa Múrio (Namíta) Cliente"
    },
    {
        "phone_number": "+554491454837",
        "public_name": "Julio Ceola Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554191835140",
        "public_name": "Jozafá Proprietário Torre Di Lyon 2702 Poeta Mario Quintana Diferenciado"
    },
    {
        "phone_number": "+554199327200",
        "public_name": "Wilson Proprietário 3701 Royal Tower"
    },
    {
        "phone_number": "+554796844444",
        "public_name": "AT 1.3M- Andre Reche Cliente"
    },
    {
        "phone_number": "+5521998873200",
        "public_name": "AT 800K - Elena Cliente Rio"
    },
    {
        "phone_number": "+554199580166",
        "public_name": "Vitor Franciosi Proprietario"
    },
    {
        "phone_number": "+554791409009",
        "public_name": "Camila Costa Cliente Organica"
    },
    {
        "phone_number": "+554791389554",
        "public_name": "Zenildo Cliente Brava Beach"
    },
    {
        "phone_number": "+555596252516",
        "public_name": "Paulo Cliente Mkt Boreal Cruz Alta"
    },
    {
        "phone_number": "+554396360257",
        "public_name": "AT 500k Carlos Robinson Cliente Mkt"
    },
    {
        "phone_number": "+554799190909",
        "public_name": "Diogo Proprietario Torre D Lyon"
    },
    {
        "phone_number": "+554999195302",
        "public_name": "Juarez De Oliveira Cliente Ate"
    },
    {
        "phone_number": "+554799278520",
        "public_name": "At 3.5m Isabela Cristiane Cliente"
    },
    {
        "phone_number": "+554799723534",
        "public_name": "AT 1.3m Ney Cliente"
    },
    {
        "phone_number": "+554799229306",
        "public_name": "AT 800K - Rafael De Moura Speroni Cliente"
    },
    {
        "phone_number": "+554799723388",
        "public_name": "Paulo Proprietario Alexandria Vendido"
    },
    {
        "phone_number": "+554792788989",
        "public_name": "Claudio Roberto Paul Cliente Organica"
    },
    {
        "phone_number": "+555199836658",
        "public_name": "AT 1.6M- Paulo Cliente"
    },
    {
        "phone_number": "+554199947576",
        "public_name": "Valentin Proprietário"
    },
    {
        "phone_number": "+556183622911",
        "public_name": "Junior Japa Cliente"
    },
    {
        "phone_number": "+554891075114",
        "public_name": "Daniel Magnelli Cliente Loteamento Terreno"
    },
    {
        "phone_number": "+556699400016",
        "public_name": "AT 500K -Sthefanny Cliente  Mkt"
    },
    {
        "phone_number": "+554391048100",
        "public_name": "Helio Bonafini Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554797031211",
        "public_name": "Clauber Proprietario Melbourne 2001"
    },
    {
        "phone_number": "+5518982000187",
        "public_name": "At 2.5M Sergio Cliente"
    },
    {
        "phone_number": "+554791663445",
        "public_name": "Nonato Cliente Marido Ester Vendido"
    },
    {
        "phone_number": "+554799911628",
        "public_name": "AT 800K - Silvana Cliente"
    },
    {
        "phone_number": "+554591048681",
        "public_name": "Gianni Ramiro Cliente Orbita"
    },
    {
        "phone_number": "+555596142296",
        "public_name": "Fabiano Azeredo Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555199123460",
        "public_name": "At 3m Clair Moa Cliente"
    },
    {
        "phone_number": "+554999924815",
        "public_name": "AT 800K -Luis Carlos Aruda Junior Cliente Mkt"
    },
    {
        "phone_number": "+554184199439",
        "public_name": "AT 1M- Luciano Fedalto Cliente"
    },
    {
        "phone_number": "+554788533454",
        "public_name": "AT 3M Neide Cipriani Cliente"
    },
    {
        "phone_number": "+554796051880",
        "public_name": "Marcelo Marcolla Proprietario Casa Balneario"
    },
    {
        "phone_number": "+555591562443",
        "public_name": "Jardel Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799110984",
        "public_name": "AT 800K - Robson Azevedo Cliente"
    },
    {
        "phone_number": "+554799510953",
        "public_name": "AT 1.3M Maria Angela Cliente BC"
    },
    {
        "phone_number": "+554799013637",
        "public_name": "AT 800K Neoli Sedrez Cliente"
    },
    {
        "phone_number": "+554999669471",
        "public_name": "Mariela Cliente Indicacao Jackes"
    },
    {
        "phone_number": "+554799611518",
        "public_name": "AT 800K -Celso Cliente"
    },
    {
        "phone_number": "+554792312722",
        "public_name": "Jociano Proprietario Phoenix 3501"
    },
    {
        "phone_number": "+554796140007",
        "public_name": "AT 1.6M Irene Belli Cliente"
    },
    {
        "phone_number": "+554196787272",
        "public_name": "Eduardo Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555491600570",
        "public_name": "AT 500K - Celso Bernardi Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554999466233",
        "public_name": "Alencar Agrônomo Cliente Indicacao Jonas"
    },
    {
        "phone_number": "+554799220008",
        "public_name": "Tabaré Aliano Cliente Investidor Reforma E Vende"
    },
    {
        "phone_number": "+554799177000",
        "public_name": "Cristiano Cliente Ponta Grossa"
    },
    {
        "phone_number": "+554991916907",
        "public_name": "At 3.5m Katia Busato M. Derossi Cliente"
    },
    {
        "phone_number": "+554799831324",
        "public_name": "AT 1.3M- Diego Toni Cliente - Permuta Gaspar"
    },
    {
        "phone_number": "+554799187858",
        "public_name": "AT 800K - Aline Sarasol Cliente"
    },
    {
        "phone_number": "+554599447463",
        "public_name": "Junior Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799537098",
        "public_name": "Clovis Floriani Proprietario Acqualina 1502"
    },
    {
        "phone_number": "+555499540709",
        "public_name": "At 3.5m Marines Dalbosco da Silva Cliente Gramado"
    },
    {
        "phone_number": "+555182094092",
        "public_name": "Dan Proprietario Terra E Mar 701/02"
    },
    {
        "phone_number": "+554796587060",
        "public_name": "At 1.6m Rodrigo Cliente"
    },
    {
        "phone_number": "+5519997260036",
        "public_name": "Andre Proprietario"
    },
    {
        "phone_number": "+554488164376",
        "public_name": "Luana Thais Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554599239324",
        "public_name": "Maruam Safa Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554792895656",
        "public_name": "AT 400 K- Nori Cliente Novo Hamburgo"
    },
    {
        "phone_number": "+555496174876",
        "public_name": "At 1.6m Zelinda Cristofari Cliente"
    },
    {
        "phone_number": "+557799614041",
        "public_name": "Vital Anzilheiro Cliente Bahia Indicacao Ronaldo"
    },
    {
        "phone_number": "+555496757575",
        "public_name": "AT 1.6M- Christian Cliente"
    },
    {
        "phone_number": "+554791140090",
        "public_name": "Paulo Proprietário Vernazza 3¤ Mob"
    },
    {
        "phone_number": "+554199172161",
        "public_name": "At 1.6m Rosangela Maria Tuczek Cliente Indicacao Fabio"
    },
    {
        "phone_number": "+5519974063111",
        "public_name": "Everaldo Israel Proprietario Vermont"
    },
    {
        "phone_number": "+13216033000",
        "public_name": "AT 3M Andre Macohin Cliente"
    },
    {
        "phone_number": "+554796127583",
        "public_name": "AT 5M- CASA - Analu Santos Medeiros Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554788093603",
        "public_name": "AT 2M -Soraia Lobe Cliente"
    },
    {
        "phone_number": "+555496943008",
        "public_name": "AT 1.3M -Leonildo Friske Cliente Vendido"
    },
    {
        "phone_number": "+554797705372",
        "public_name": "AT 800K - Lair Cliente Casa Ou Diferenciado"
    },
    {
        "phone_number": "+554797720049",
        "public_name": "AT 1.3M- Andre Gustavo Cliente Permuta"
    },
    {
        "phone_number": "+554797346050",
        "public_name": "AT 800K - Cris Cliente"
    },
    {
        "phone_number": "+556599661234",
        "public_name": "Luciano Martins Cliente Organica"
    },
    {
        "phone_number": "+554498804343",
        "public_name": "At 2.5m Lucas Orsini Cliente"
    },
    {
        "phone_number": "+554796540635",
        "public_name": "Roberto Cliente Olx"
    },
    {
        "phone_number": "+554499764801",
        "public_name": "At 2m Walmor Massaro Cliente Maringa"
    },
    {
        "phone_number": "+554797090123",
        "public_name": "AT 500K - Janaina Cliente"
    },
    {
        "phone_number": "+554784043211",
        "public_name": "Everton Cliente Joenvile"
    },
    {
        "phone_number": "+554799882748",
        "public_name": "AT 1.6M Leandro Cliente"
    },
    {
        "phone_number": "+554799556265",
        "public_name": "AT 1.3M Paty Pellegrini Cliente"
    },
    {
        "phone_number": "+555198994056",
        "public_name": "Geraldo Proprietario 3301 Lumiere"
    },
    {
        "phone_number": "+5511976044805",
        "public_name": "AT 1.6M Paula Moraes Cliente"
    },
    {
        "phone_number": "+554196760347",
        "public_name": "Jorge Cliente"
    },
    {
        "phone_number": "+19546432431",
        "public_name": "Jose Passinato EUA Proprietario Terreno Colinas"
    },
    {
        "phone_number": "+554299569633",
        "public_name": "AT 2.5m  Ana Lopes Cliente 135 Jardins"
    },
    {
        "phone_number": "+554797794330",
        "public_name": "AT 500K - Altair Cliente Mkt"
    },
    {
        "phone_number": "+554799851775",
        "public_name": "Alex Sagala Proprietario Apogee"
    },
    {
        "phone_number": "+555189976020",
        "public_name": "Maria Cristina Medeiros Marques Cliente Orbita"
    },
    {
        "phone_number": "+554791592609",
        "public_name": "Daniel Proprietário Philipos"
    },
    {
        "phone_number": "+555499444977",
        "public_name": "At 500k Luciana Fontana Cliente"
    },
    {
        "phone_number": "+554884147272",
        "public_name": "AT 1.3M - Marcos Cliente"
    },
    {
        "phone_number": "+554791399136",
        "public_name": "Dany Cliente Mkt Boreal"
    },
    {
        "phone_number": "+556184053824",
        "public_name": "AT 1.6M- Cleuber Luis Cliente Investidor"
    },
    {
        "phone_number": "+554199692030",
        "public_name": "Fernando Dissenha Proprietario Saint Tropez"
    },
    {
        "phone_number": "+5511947457393",
        "public_name": "Rogerio Proprietario Celebration"
    },
    {
        "phone_number": "+555193192141",
        "public_name": "AT 500K -Ana Cliente"
    },
    {
        "phone_number": "+555199425990",
        "public_name": "Douglas Silveira Cliente Orbita"
    },
    {
        "phone_number": "+554399742186",
        "public_name": "Jaime Idalgo Proprietario Tour Toyalle"
    },
    {
        "phone_number": "+555193085437",
        "public_name": "Rubia Costa Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799356775",
        "public_name": "AT 1M- Raquelli Cliente Tem Permuta Palermo"
    },
    {
        "phone_number": "+5518997522300",
        "public_name": "Julio Hoch Cliente Indicão Geovane"
    },
    {
        "phone_number": "+554796644566",
        "public_name": "Fernanda Cliente"
    },
    {
        "phone_number": "+554791371414",
        "public_name": "Anderson Proprietario Costa Dos Corais"
    },
    {
        "phone_number": "+554799156412",
        "public_name": "Jamila - Salustiano Proprietario Porto da Barra"
    },
    {
        "phone_number": "+554799698817",
        "public_name": "Elder Cliente BC"
    },
    {
        "phone_number": "+554191049016",
        "public_name": "AT 1.3M Jean Carlos Cliente"
    },
    {
        "phone_number": "+554199113775",
        "public_name": "Carlos Alberto Proprietario Ilha De Saturno"
    },
    {
        "phone_number": "+554799862790",
        "public_name": "At 1.3 Maria Regina Busato Teixeira Cliente"
    },
    {
        "phone_number": "+555199717943",
        "public_name": "Everson Cliente POA"
    },
    {
        "phone_number": "+554799750496",
        "public_name": "Jenice Proprietario Royal Garden E Cala D Volpi"
    },
    {
        "phone_number": "+554791292022",
        "public_name": "At 3.5m Maria Aparecida Bianchezzi Dos Santos Cliente"
    },
    {
        "phone_number": "+554791101798",
        "public_name": "AT 800k Cris Cliente"
    },
    {
        "phone_number": "+554788515553",
        "public_name": "Vinicius Cliente Tem Casa Em Mariscal Permuta"
    },
    {
        "phone_number": "+554599127821",
        "public_name": "Rafaela Oltramari Cliente Cascavel"
    },
    {
        "phone_number": "+554799376899",
        "public_name": "Robson Raimundo Cliente"
    },
    {
        "phone_number": "+554884038223",
        "public_name": "André Athayde Cliente Organica"
    },
    {
        "phone_number": "+554799461633",
        "public_name": "Neiva Cliente 4 Dorm"
    },
    {
        "phone_number": "+554788262285",
        "public_name": "Augustin Cliente Argentina"
    },
    {
        "phone_number": "+554796382283",
        "public_name": "Custodio Proprietario Di Galles 902"
    },
    {
        "phone_number": "+554188187747",
        "public_name": "Ronald Cliente Curitiba"
    },
    {
        "phone_number": "+554199956669",
        "public_name": "At 2.5m Edison Goncalves Cliente"
    },
    {
        "phone_number": "+556281605004",
        "public_name": "Gabriel Leão de Oliveira Cliente Organica"
    },
    {
        "phone_number": "+554988031850",
        "public_name": "Julio Filho Maria Elena Mae Cliente"
    },
    {
        "phone_number": "+554797220008",
        "public_name": "Cesar Proprietário Do Virgínia"
    },
    {
        "phone_number": "+556792746000",
        "public_name": "Sadi Cliente Orbita"
    },
    {
        "phone_number": "+554197515380",
        "public_name": "Cleber Cliente Vendido"
    },
    {
        "phone_number": "+554791558007",
        "public_name": "AT 1.3M Juliana Souza Cliente"
    },
    {
        "phone_number": "+554788179699",
        "public_name": "Regina Marcia Proprietario Torre Atlantica"
    },
    {
        "phone_number": "+555191928706",
        "public_name": "At 3.5m Denise Reis Cliente"
    },
    {
        "phone_number": "+554799931181",
        "public_name": "AT 1.6M- Neuza Maria Cliente"
    },
    {
        "phone_number": "+555496699020",
        "public_name": "Sidney Proprietario Notting Hill 3002"
    },
    {
        "phone_number": "+554499171343",
        "public_name": "Xande Cliente Amigo Marciel"
    },
    {
        "phone_number": "+554788052305",
        "public_name": "AT 800K - Mônica Cliente Sobrado"
    },
    {
        "phone_number": "+554799853300",
        "public_name": "Yamamoto Proprietário Aloha 510"
    },
    {
        "phone_number": "+554298531812",
        "public_name": "Sandra Cliente"
    },
    {
        "phone_number": "+554791748881",
        "public_name": "Sebastian Cliente Brusque Troca"
    },
    {
        "phone_number": "+555491966068",
        "public_name": "Chaiane Cliente Studio 25"
    },
    {
        "phone_number": "+554799704722",
        "public_name": "AT 1M- Ursula Cliente"
    },
    {
        "phone_number": "+554191036221",
        "public_name": "Wilson Proprietário 3302 Royal"
    },
    {
        "phone_number": "+554199556039",
        "public_name": "Caue Cliente Ate 500 Mil Casa"
    },
    {
        "phone_number": "+554799772032",
        "public_name": "Jose Carlos Proprietário Costa Atlantica"
    },
    {
        "phone_number": "+554791141966",
        "public_name": "R Fretta Proprietario"
    },
    {
        "phone_number": "+554184823905",
        "public_name": "Graziele Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554999732773",
        "public_name": "Tiago Proprietário"
    },
    {
        "phone_number": "+554784341466",
        "public_name": "AT 1M Sandra Cliente"
    },
    {
        "phone_number": "+554699105263",
        "public_name": "AT 500K - Osvaldo Cliente"
    },
    {
        "phone_number": "+554791196000",
        "public_name": "Giovani Proprietário torre 02 Brava Home 1102 3. 5k"
    },
    {
        "phone_number": "+554796178060",
        "public_name": "Errol Bogo Proprietário One Tower 26"
    },
    {
        "phone_number": "+554791927300",
        "public_name": "AT 1.3M- Elton Cliente"
    },
    {
        "phone_number": "+554299750813",
        "public_name": "At 1.6m Mara Matos Cliente"
    },
    {
        "phone_number": "+5512997118509",
        "public_name": "Camila Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554888439354",
        "public_name": "AT 2M- Izaia Cliente Vendo Pro Irmao Frente Mar"
    },
    {
        "phone_number": "+556798290809",
        "public_name": "Ana Paula Furlan Proprietario Pacoste Permutante"
    },
    {
        "phone_number": "+554792500855",
        "public_name": "At 3.5m Angelo Cattoni Cliente"
    },
    {
        "phone_number": "+554799189588",
        "public_name": "Marquiotti Proprietário Notting Hill"
    },
    {
        "phone_number": "+554899820064",
        "public_name": "Claudio Proprietario Hamptons"
    },
    {
        "phone_number": "+5511940354373",
        "public_name": "Emerson Cliente Casa Parcelado"
    },
    {
        "phone_number": "+554799384565",
        "public_name": "At 3m Celia Ferreira Daniotti Cliente"
    },
    {
        "phone_number": "+554788689459",
        "public_name": "AT 1.6M Thiago Sanches Cliente"
    },
    {
        "phone_number": "+554896635152",
        "public_name": "AT 800k Valdecir Pantano Cliente"
    },
    {
        "phone_number": "+554788321177",
        "public_name": "Valdeci Pereira Proprietario Mediterranê"
    },
    {
        "phone_number": "+554196112280",
        "public_name": "AT 1M- Mauro Cliente"
    },
    {
        "phone_number": "+554799887605",
        "public_name": "João Valmir Proprietário Maria Luiza 600"
    },
    {
        "phone_number": "+554999520760",
        "public_name": "AT 1.3M -Mauro Cliente"
    },
    {
        "phone_number": "+554991943184",
        "public_name": "AT 1.3M- Nadia Cliente"
    },
    {
        "phone_number": "+5511958036544",
        "public_name": "AT 1M -  Aíssa Cliente"
    },
    {
        "phone_number": "+554788031795",
        "public_name": "Jubiane Cliente Blumenau"
    },
    {
        "phone_number": "+554799257051",
        "public_name": "AT 800K - Felipe Cliente -Casa"
    },
    {
        "phone_number": "+554796013621",
        "public_name": "Luiz Carlos Cliente"
    },
    {
        "phone_number": "+554799792229",
        "public_name": "Adênis Antunes Cliente Organica"
    },
    {
        "phone_number": "+554799838623",
        "public_name": "Alexandre Proprietário Ap 106 Amaralina"
    },
    {
        "phone_number": "+554791995889",
        "public_name": "Edson Suzena Proprietario Mirage 701"
    },
    {
        "phone_number": "+554784062455",
        "public_name": "Guerra Proprietario Skyline FG"
    },
    {
        "phone_number": "+554184111167",
        "public_name": "AT 800K -Elizabeth Cliente"
    },
    {
        "phone_number": "+555596320539",
        "public_name": "Ana Martello Cliente Indicacao Carol (kaue)"
    },
    {
        "phone_number": "+554187791919",
        "public_name": "AT 1M-Georgia Cliente"
    },
    {
        "phone_number": "+554797086666",
        "public_name": "Silvano Proprietario Bmw 320"
    },
    {
        "phone_number": "+559681151763",
        "public_name": "AT 800K - Felipe Passos Cliente Casa"
    },
    {
        "phone_number": "+554499575737",
        "public_name": "AT 2M Diego Cliente Investidor"
    },
    {
        "phone_number": "+555599533544",
        "public_name": "Denis Capital 922 Cliente"
    },
    {
        "phone_number": "+554791016687",
        "public_name": "Mariza Cliente Blumenau"
    },
    {
        "phone_number": "+554799059292",
        "public_name": "Michele Cliente Casa"
    },
    {
        "phone_number": "+554784456955",
        "public_name": "Mirella Cliente"
    },
    {
        "phone_number": "+554784316839",
        "public_name": "AT 800K - Camila Peters Cliente"
    },
    {
        "phone_number": "+554896200805",
        "public_name": "Ivonete Cliente Florianopolis"
    },
    {
        "phone_number": "+554199745710",
        "public_name": "Paulo Cliente Curitiba (Bruna)"
    },
    {
        "phone_number": "+555596438433",
        "public_name": "AT 2M- Anusca Cliente Mkt"
    },
    {
        "phone_number": "+554188560449",
        "public_name": "AT 500K - Edivaldo Cliente Sobrado"
    },
    {
        "phone_number": "+554396209299",
        "public_name": "Nadia Cliente Admira"
    },
    {
        "phone_number": "+554799725114",
        "public_name": "Placido Cliente Investidor"
    },
    {
        "phone_number": "+554788862322",
        "public_name": "AT 2M Denise Staedele Cliente"
    },
    {
        "phone_number": "+554792524771",
        "public_name": "Mílard Zhaf Proprietario Alexandria"
    },
    {
        "phone_number": "+554791054746",
        "public_name": "AT 300K Elina Cliente"
    },
    {
        "phone_number": "+554796189193",
        "public_name": "Cris/Eloi Proprietario Portinax"
    },
    {
        "phone_number": "+554791406562",
        "public_name": "Adao Ademir Almeida Proprietario Seas Tower 2101 Frente Mar"
    },
    {
        "phone_number": "+554791018009",
        "public_name": "AT 800K - Cesar Cliente -Praia Brava"
    },
    {
        "phone_number": "+554791361006",
        "public_name": "Daniel Cliente Casa"
    },
    {
        "phone_number": "+554799872116",
        "public_name": "Marina Cliente BC"
    },
    {
        "phone_number": "+554896069660",
        "public_name": "At 2.5m Adriana Fagundes Cliente"
    },
    {
        "phone_number": "+554797900545",
        "public_name": "AT 1.3M -Patricia Caniver Moriconi Cliente"
    },
    {
        "phone_number": "+554784466188",
        "public_name": "AT 1.6M- Rafaela Cliente"
    },
    {
        "phone_number": "+556981070096",
        "public_name": "At 3m Suzana Carmargo Cliente"
    },
    {
        "phone_number": "+554896986404",
        "public_name": "Proprietario - Andre Caxias"
    },
    {
        "phone_number": "+554796195149",
        "public_name": "Ricardo Proprietário Lorenzo 502"
    },
    {
        "phone_number": "+554791258540",
        "public_name": "Carlos Cliente"
    },
    {
        "phone_number": "+554799192903",
        "public_name": "Fernando Cliente Vendido Casa"
    },
    {
        "phone_number": "+554791460860",
        "public_name": "AT 4.5M Leandro Grah Cliente"
    },
    {
        "phone_number": "+554796122222",
        "public_name": "AT 500k Juliana Martins Cliente"
    },
    {
        "phone_number": "+554588172285",
        "public_name": "Sabrina Cliente Organica"
    },
    {
        "phone_number": "+556492140033",
        "public_name": "Thaynara Cliente Organica"
    },
    {
        "phone_number": "+554199858500",
        "public_name": "AT 2.5M José Henrique Jamur Cliente"
    },
    {
        "phone_number": "+554784369868",
        "public_name": "Carlos Andrade Proprietario Gran Torino"
    },
    {
        "phone_number": "+554784482283",
        "public_name": "Cledinara Coelho Cliente Permuta"
    },
    {
        "phone_number": "+554196813613",
        "public_name": "Felipe Bena Cliente"
    },
    {
        "phone_number": "+554998019595",
        "public_name": "AT 500K - Nei Tesser Cliente Joacaba"
    },
    {
        "phone_number": "+554799855051",
        "public_name": "AT 1M - Arno Cliente Ap Norte"
    },
    {
        "phone_number": "+556699997650",
        "public_name": "At 3.5m Everson Ruffato Cliente"
    },
    {
        "phone_number": "+554788059445",
        "public_name": "AT 1.3M -Robson Cliente Vendido"
    },
    {
        "phone_number": "+554498494140",
        "public_name": "AT 1.6M Junior Cliente"
    },
    {
        "phone_number": "+554699319000",
        "public_name": "Hans Kuerten Cliente Investidor Amigo Do Junior"
    },
    {
        "phone_number": "+554796090840",
        "public_name": "Rafael Proprietário Cobertura San Gennaro"
    },
    {
        "phone_number": "+554584072038",
        "public_name": "Devair Guimarães Cliente"
    },
    {
        "phone_number": "+554691119445",
        "public_name": "AT 3m Fabiana Battisti Cliente"
    },
    {
        "phone_number": "+554184008216",
        "public_name": "Rafael Bin Cliente Italian"
    },
    {
        "phone_number": "+554791782902",
        "public_name": "AT 500K -Bueno Cliente"
    },
    {
        "phone_number": "+554799681335",
        "public_name": "AT 800k -Juari Cliente Blumenau"
    },
    {
        "phone_number": "+554799149205",
        "public_name": "Carlos Eduardo Proprietário Barra Tower 901"
    },
    {
        "phone_number": "+554799120553",
        "public_name": "AT 6M Livia Cliente"
    },
    {
        "phone_number": "+554999050051",
        "public_name": "AT 500K - Vanderley Nordio Cliente Terreno"
    },
    {
        "phone_number": "+554499892117",
        "public_name": "AT 800K - Regis Panceri Cliente -Parcelado Campo Mourão"
    },
    {
        "phone_number": "+555599496862",
        "public_name": "At 3.5m Samira Omran Cliente"
    },
    {
        "phone_number": "+555198553788",
        "public_name": "AT 1.6M- Valdir Cliente"
    },
    {
        "phone_number": "+554599629527",
        "public_name": "AT 1M-Eduardo De França Cliente"
    },
    {
        "phone_number": "+554796076905",
        "public_name": "AT 500K - Valdirene Cliente Chacara"
    },
    {
        "phone_number": "+554999971118",
        "public_name": "AT 2.5M Leandro Briancini Cliente"
    },
    {
        "phone_number": "+554799828118",
        "public_name": "Levi Proprietario Summer Breeze"
    },
    {
        "phone_number": "+555491170095",
        "public_name": "Noemia Silva Cardoso Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554195405709",
        "public_name": "Bruna Angelica Matia Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554791230071",
        "public_name": "AT 800K - Evandro Cliente Casa"
    },
    {
        "phone_number": "+554499445913",
        "public_name": "Rocha Pombo Cliente"
    },
    {
        "phone_number": "+554999876472",
        "public_name": "Tirza Grando Proprietario Uirapuru"
    },
    {
        "phone_number": "+554799199747",
        "public_name": "At 2m Eduardo Loss Cliente"
    },
    {
        "phone_number": "+554791835214",
        "public_name": "AT 1M- Nilto Cliente -Permuta Jaragua"
    },
    {
        "phone_number": "+554791246406",
        "public_name": "Lila Cliente Permuta Blumenau"
    },
    {
        "phone_number": "+554796048191",
        "public_name": "AT 800K - Roberta Cliente Casa"
    },
    {
        "phone_number": "+555599557151",
        "public_name": "Julio Cesar Santa Maria Cliente"
    },
    {
        "phone_number": "+554788566803",
        "public_name": "AT 1M- Jheniffer Luana E Cesar Cliente"
    },
    {
        "phone_number": "+554796120003",
        "public_name": "Dioni Cliente"
    },
    {
        "phone_number": "+554188286204",
        "public_name": "AT 1.6m Maura Gonçalves Cliente"
    },
    {
        "phone_number": "+554896289411",
        "public_name": "At 2m Odilson Lima Cliente"
    },
    {
        "phone_number": "+554899415161",
        "public_name": "At 1.3m Maikon Cliente Permuta São José"
    },
    {
        "phone_number": "+554799650664",
        "public_name": "Fernando Augusto Proprietario Monte Olympos 1203"
    },
    {
        "phone_number": "+555491291826",
        "public_name": "Marcio Truss Cliente Ibiruba"
    },
    {
        "phone_number": "+555181607027",
        "public_name": "Luiza Cliente Poa"
    },
    {
        "phone_number": "+554391838384",
        "public_name": "AT 1m Juliano Cliente"
    },
    {
        "phone_number": "+554191024390",
        "public_name": "Rafael Mansur Proprietário Torre De São Francisco 101"
    },
    {
        "phone_number": "+554199883748",
        "public_name": "At 800k Luiz Carlos Buhrer Cliente"
    },
    {
        "phone_number": "+554799747493",
        "public_name": "AT 500K - Maria Cliente"
    },
    {
        "phone_number": "+556899872737",
        "public_name": "Cristian Diogo Cliente Organica"
    },
    {
        "phone_number": "+554792153001",
        "public_name": "Pedro Telefone Novo Cliente Ouro Brasil"
    },
    {
        "phone_number": "+554199573821",
        "public_name": "Ane Cliente Curitiba"
    },
    {
        "phone_number": "+554799638494",
        "public_name": "Claudia Bauer Cliente"
    },
    {
        "phone_number": "+554791852277",
        "public_name": "Paulo Proprietário Brava Prime 501/02/03"
    },
    {
        "phone_number": "+554899529058",
        "public_name": "AT 1.3M -Guilherme Cliente"
    },
    {
        "phone_number": "+555596141100",
        "public_name": "At 3m Luana Albiero Schetko Cliente"
    },
    {
        "phone_number": "+554796290045",
        "public_name": "AT 800K -Raduan Nobre Cliente - Casa"
    },
    {
        "phone_number": "+554599358937",
        "public_name": "At 2m Ana Paula Bandeira Cliente"
    },
    {
        "phone_number": "+554999831358",
        "public_name": "AT 1.6M- Amilton Cliente Lages"
    },
    {
        "phone_number": "+557192900506",
        "public_name": "At 2.5m Valdemiro Araujo Cliente"
    },
    {
        "phone_number": "+554299857203",
        "public_name": "Gih Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554898260008",
        "public_name": "Adir Proprietario Poeta Mario Quintana"
    },
    {
        "phone_number": "+554891639667",
        "public_name": "Diego Della Cliente Bmw"
    },
    {
        "phone_number": "+554188551445",
        "public_name": "At 3M Marcos Freire Cliente"
    },
    {
        "phone_number": "+34687121475",
        "public_name": "Carlos Masaro Proprietario Cobertura"
    },
    {
        "phone_number": "+556992619611",
        "public_name": "AT 800K - Diego Cliente Rondônia"
    },
    {
        "phone_number": "+554499312016",
        "public_name": "At 3m Edvaldo HA Cliente"
    },
    {
        "phone_number": "+554788720008",
        "public_name": "AT 1.3m Elisabet Kleis Cliente"
    },
    {
        "phone_number": "+554799082419",
        "public_name": "Fernanda Cliente Tem Casa Troca Em Ap"
    },
    {
        "phone_number": "+554288387722",
        "public_name": "At 2m Renato Moecke Cliente"
    },
    {
        "phone_number": "+554499167897",
        "public_name": "Eduardo Cardoso Proprietario Frente Mar Perequê"
    },
    {
        "phone_number": "+554699050897",
        "public_name": "AT 800K - Daniele Kunz Cliente Praia Brava"
    },
    {
        "phone_number": "+554799854470",
        "public_name": "AT 1.3M- Fabio Casini Cliente"
    },
    {
        "phone_number": "+554799372296",
        "public_name": "Jair Proprietário"
    },
    {
        "phone_number": "+554796196666",
        "public_name": "AT 1M -  Angelo Cliente Diego"
    },
    {
        "phone_number": "+5522988023141",
        "public_name": "AT 800K - Cliente Praia Brava"
    },
    {
        "phone_number": "+554791105445",
        "public_name": "AT 2.5M Ale Felini Cliente"
    },
    {
        "phone_number": "+554788239600",
        "public_name": "Alexandre Proprietario 3001 Blue Coast"
    },
    {
        "phone_number": "+554797219223",
        "public_name": "Fabricio Mineiro Cliente Hyde"
    },
    {
        "phone_number": "+555499452225",
        "public_name": "Jo Proprietário Tour Chapelle 2300"
    },
    {
        "phone_number": "+555581214107",
        "public_name": "Argos Irmao Eguimar Proprietario Avangart"
    },
    {
        "phone_number": "+557799482169",
        "public_name": "Beti Flores Freitas Cliente Vendido"
    },
    {
        "phone_number": "+554799599999",
        "public_name": "AT 1M-Augusto Cliente"
    },
    {
        "phone_number": "+554799188203",
        "public_name": "AT 1.3M- Donizetti Cliente"
    },
    {
        "phone_number": "+554196527321",
        "public_name": "At 2m Gabriela Dra Cliente"
    },
    {
        "phone_number": "+554399557400",
        "public_name": "Felipe Filho Proprietario Montreux 1501"
    },
    {
        "phone_number": "+556282411263",
        "public_name": "At 3.5m Alysom Cliente"
    },
    {
        "phone_number": "+554796054999",
        "public_name": "AT 800k Shirley Schneider Cliente"
    },
    {
        "phone_number": "+554198932966",
        "public_name": "AT 500K -Luiz Cliente Sobrado"
    },
    {
        "phone_number": "+557799842090",
        "public_name": "AT 5m Fernando Cliente Bahia Vendido"
    },
    {
        "phone_number": "+554299724410",
        "public_name": "AT 500K - Luis/Beatriz Cliente Paraná"
    },
    {
        "phone_number": "+554199713490",
        "public_name": "AT 1.6M Joao Pequeno Cliente"
    },
    {
        "phone_number": "+554791087187",
        "public_name": "AT 800K - Fernando Cliente- Casa"
    },
    {
        "phone_number": "+554799823231",
        "public_name": "AT 2.5m Delcio Maximiano Cliente"
    },
    {
        "phone_number": "+555597006785",
        "public_name": "At 1m Elaine Cliente"
    },
    {
        "phone_number": "+554199219085",
        "public_name": "Leandro Cliente Comprou"
    },
    {
        "phone_number": "+554799832139",
        "public_name": "Renaldo Cliente"
    },
    {
        "phone_number": "+555591349172",
        "public_name": "Luiz Fernando Machado Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554299237187",
        "public_name": "AT 3M Dinilda Morais Cliente"
    },
    {
        "phone_number": "+554791022265",
        "public_name": "AT 1M-Dody Cliente- Casa"
    },
    {
        "phone_number": "+554796525425",
        "public_name": "AT 1.3M Keila Mara Cliente Comprou"
    },
    {
        "phone_number": "+554799999737",
        "public_name": "Shirley Cliente Esposa Do Beto"
    },
    {
        "phone_number": "+554199358490",
        "public_name": "AT 800K - Natasha Cliente"
    },
    {
        "phone_number": "+554797008847",
        "public_name": "At 800k Maura Cliente"
    },
    {
        "phone_number": "+555499001342",
        "public_name": "At 3m Elisandra Piva Cliente"
    },
    {
        "phone_number": "+554799988820",
        "public_name": "AT 500K Vania Rocha Cliente"
    },
    {
        "phone_number": "+554784742287",
        "public_name": "At 2m Fabio Ferreira Cliente Frente Mar"
    },
    {
        "phone_number": "+554799850385",
        "public_name": "Sergio Nuhs Proprietario Barra Tower 1901"
    },
    {
        "phone_number": "+554799210023",
        "public_name": "Fernando Kraft Proprietário Terreno Meia Praia"
    },
    {
        "phone_number": "+554184038584",
        "public_name": "Proprietario Bmw Gt"
    },
    {
        "phone_number": "+556692062310",
        "public_name": "AT 800K - Arlene Borges Cliente"
    },
    {
        "phone_number": "+554499019140",
        "public_name": "At 600k Carol Pavezi Cliente"
    },
    {
        "phone_number": "+554899613100",
        "public_name": "Newton Proprietário Tropical Summer 1802"
    },
    {
        "phone_number": "+555499349070",
        "public_name": "Marcelo Cliente Tapejara"
    },
    {
        "phone_number": "+554791563485",
        "public_name": "Emidio Lara Cliente Loteamento"
    },
    {
        "phone_number": "+554191048225",
        "public_name": "AT 2.5M Geraldo Lopes Cliente"
    },
    {
        "phone_number": "+554999472257",
        "public_name": "Eduardo Cliente Organica"
    },
    {
        "phone_number": "+554188613601",
        "public_name": "Juarez Proprietario Maria Augusta 802"
    },
    {
        "phone_number": "+554791966004",
        "public_name": "AT 800K - Marcos Cliente"
    },
    {
        "phone_number": "+554797165884",
        "public_name": "Valeria Distefano Cliente"
    },
    {
        "phone_number": "+554796347312",
        "public_name": "AT 3M Shirlei Macelani Cliente"
    },
    {
        "phone_number": "+554999472526",
        "public_name": "At 2M Jane Centenaro Cliente"
    },
    {
        "phone_number": "+554199148685",
        "public_name": "Isabela Cliente Proprietaria Skyline 1102 FG"
    },
    {
        "phone_number": "+554799375999",
        "public_name": "Fernanda Rosin Cliente Sil"
    },
    {
        "phone_number": "+555192129981",
        "public_name": "AT 1.6M- Milene Fernandes Cliente"
    },
    {
        "phone_number": "+554796724742",
        "public_name": "AT 500K - Aline Cipriano Cliente"
    },
    {
        "phone_number": "+554196190666",
        "public_name": "At 2m Carlos Alberto Rodrigues Cliente"
    },
    {
        "phone_number": "+554799579057",
        "public_name": "Joice Cliente Jaragua"
    },
    {
        "phone_number": "+555499761132",
        "public_name": "AT 3M Michel Thomé Cliente"
    },
    {
        "phone_number": "+554788346824",
        "public_name": "Pedro H De Souza Cliente Organica"
    },
    {
        "phone_number": "+554199953146",
        "public_name": "AT 1.3M Maurício Leal Cliente"
    },
    {
        "phone_number": "+555591187789",
        "public_name": "AT 1M- Kamila Cliente Casa"
    },
    {
        "phone_number": "+554799212018",
        "public_name": "AT 1.3M- Cyrus Cliente- Praia brava"
    },
    {
        "phone_number": "+555196661199",
        "public_name": "At 3m Marlete Lopes Cliente"
    },
    {
        "phone_number": "+555599979650",
        "public_name": "At 5m Jaime De Oliveira Cliente Privilege"
    },
    {
        "phone_number": "+553189890696",
        "public_name": "At 2.5m Maria Luiza Cliente"
    },
    {
        "phone_number": "+554899699847",
        "public_name": "Íris Cliente Jurerê"
    },
    {
        "phone_number": "+553184174715",
        "public_name": "At 4m José Calazans Cliente"
    },
    {
        "phone_number": "+555181186077",
        "public_name": "AT 500K - Gislai Cliente Mkt"
    },
    {
        "phone_number": "+554299750808",
        "public_name": "Ragli V.R.M Cliente Italian"
    },
    {
        "phone_number": "+554799772069",
        "public_name": "Lirio Zonta Proprietario Beach Tower 1602"
    },
    {
        "phone_number": "+557399194848",
        "public_name": "Flávio Cliente"
    },
    {
        "phone_number": "+554797403044",
        "public_name": "Marilena Proprietário Porto Veneto 901"
    },
    {
        "phone_number": "+554791269286",
        "public_name": "At 3m Marcinho da Silva Cliente"
    },
    {
        "phone_number": "+554896112642",
        "public_name": "Lauro Proprietario Maria Carolina 201"
    },
    {
        "phone_number": "+554799656818",
        "public_name": "AT 800K - Marcelo Cliente Meia Praia"
    },
    {
        "phone_number": "+554196700298",
        "public_name": "AT 800K -Lysandro Santana Cliente - Praia Brava Mkt"
    },
    {
        "phone_number": "+554792010787",
        "public_name": "Méri Cliente Jaragua"
    },
    {
        "phone_number": "+554691233317",
        "public_name": "Sandra Cliente Investidor Mkt Ftente Mar"
    },
    {
        "phone_number": "+555184661892",
        "public_name": "AT 1M- Wilson Garcia Cliente - Sobrado"
    },
    {
        "phone_number": "+554699119095",
        "public_name": "Robson Cliente Yachthouse"
    },
    {
        "phone_number": "+554899429022",
        "public_name": "AT 1.6M- Marcio Dutra Cliente Tem Tres Lojas"
    },
    {
        "phone_number": "+554396241896",
        "public_name": "At 3m Samir Cliente"
    },
    {
        "phone_number": "+554499209139",
        "public_name": "AT 1m Felippe Teodoro Cliente"
    },
    {
        "phone_number": "+554788198666",
        "public_name": "Artur Proprietário Esquina Dos Açores 702"
    },
    {
        "phone_number": "+554888063656",
        "public_name": "At 2m Jeferson Diel Cliente"
    },
    {
        "phone_number": "+554799772930",
        "public_name": "Moacir Novelletto Proprietario Mar bello 131"
    },
    {
        "phone_number": "+554399150202",
        "public_name": "AT 2M Zé Neto Cliente"
    },
    {
        "phone_number": "+554498398787",
        "public_name": "Paulo Bogda Cliente Organica"
    },
    {
        "phone_number": "+555381341854",
        "public_name": "Huda Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554199944955",
        "public_name": "João Carlos Cliente (Neiva)"
    },
    {
        "phone_number": "+5511996111519",
        "public_name": "AT 2M Roberto Monteiro Maciel Cliente"
    },
    {
        "phone_number": "+554196119151",
        "public_name": "AT 800K - Laura Fausto Cliente"
    },
    {
        "phone_number": "+554799650380",
        "public_name": "Silvio Proprietario Casa No Haras Do Rio Do Ouro"
    },
    {
        "phone_number": "+554796857034",
        "public_name": "Belliani Cliente Tem Casa São João Quer Ap"
    },
    {
        "phone_number": "+554499820242",
        "public_name": "At 5m Ralph Rocha Mardegam Cliente"
    },
    {
        "phone_number": "+554799553410",
        "public_name": "At 3m Lilian Machado Cliente"
    },
    {
        "phone_number": "+554384065000",
        "public_name": "At 2.5m Willian Modesto Cliente"
    },
    {
        "phone_number": "+554784083084",
        "public_name": "Marcelo Proprietario Cristina 1305"
    },
    {
        "phone_number": "+554799121556",
        "public_name": "Guilherme Cliente Lotes"
    },
    {
        "phone_number": "+554399229159",
        "public_name": "AT 800K - Tânia Cliente Apucarana"
    },
    {
        "phone_number": "+554799189006",
        "public_name": "Leonardo Bolsi Cliente Vendido"
    },
    {
        "phone_number": "+554299305566",
        "public_name": "At 3.5m Alandra Cliente"
    },
    {
        "phone_number": "+555499941009",
        "public_name": "At 1m Lucas Aldebrand Cliente Ibirubá"
    },
    {
        "phone_number": "+554799835100",
        "public_name": "Zaga Proprietário Diferenciado Le Parc"
    },
    {
        "phone_number": "+555596743706",
        "public_name": "AT 2.5M Lauri Sanayotto Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554396150700",
        "public_name": "Leonardo Proprietario Meia Praia"
    },
    {
        "phone_number": "+555599266641",
        "public_name": "Jacinto Cliente RS"
    },
    {
        "phone_number": "+554784874707",
        "public_name": "Valdir Virgilio Proprietario Tour Royalle"
    },
    {
        "phone_number": "+554391242200",
        "public_name": "Maria Rosangela Cliente"
    },
    {
        "phone_number": "+554799878880",
        "public_name": "At 2.5m Jorge Cliente Investidor"
    },
    {
        "phone_number": "+554196012358",
        "public_name": "AT 500K - Valdir Cliente"
    },
    {
        "phone_number": "+554791448060",
        "public_name": "At 1.3M Daniela Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555499193606",
        "public_name": "At 3.5m Luciane Sanches Cliente"
    },
    {
        "phone_number": "+555481197978",
        "public_name": "At 8m Aguinaldo Junior Pastre Cliente"
    },
    {
        "phone_number": "+554796561477",
        "public_name": "At 6m Sabrina Dellandréa Cliente"
    },
    {
        "phone_number": "+554199329763",
        "public_name": "AT 1.6M- Junior Cliente Curitiba 4 Quartos"
    },
    {
        "phone_number": "+554199718330",
        "public_name": "Marco Anthero Soullis Cliente Felicita"
    },
    {
        "phone_number": "+554884083609",
        "public_name": "AT 1M- Fernanda Tenfen Cliente Mkt"
    },
    {
        "phone_number": "+554988372922",
        "public_name": "André Cliente Loteamento"
    },
    {
        "phone_number": "+554896330735",
        "public_name": "Proprietário Bmw"
    },
    {
        "phone_number": "+554898673731",
        "public_name": "At 500k Paulinha Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554788494553",
        "public_name": "At 1.3M Klaus Franzner Cliente"
    },
    {
        "phone_number": "+554791056121",
        "public_name": "Zilma Lopes Cliente Site"
    },
    {
        "phone_number": "+554799833598",
        "public_name": "At 1.6m Silvia Cliente"
    },
    {
        "phone_number": "+554796525424",
        "public_name": "Claudir Cliente Marido Da Keila Tem Mirante Do Atlantico"
    },
    {
        "phone_number": "+554799565946",
        "public_name": "AT 500K - Patricia Cliente Sobrado"
    },
    {
        "phone_number": "+554784660617",
        "public_name": "Tiago Junior Lopes Cliente Indicacão Legendario"
    },
    {
        "phone_number": "+554797841414",
        "public_name": "Nilson Cliente Tem San Pietro Quer Casa Na Brava"
    },
    {
        "phone_number": "+5519981660908",
        "public_name": "AT 1M Rudner Brocalhoni Cliente"
    },
    {
        "phone_number": "+554799737679",
        "public_name": "AT 2.5M- Nestor Cliente"
    },
    {
        "phone_number": "+555499946909",
        "public_name": "Edgar Cliente RS Indicação Cristiano"
    },
    {
        "phone_number": "+554198356578",
        "public_name": "At 2M Elaine Caldin Cliente"
    },
    {
        "phone_number": "+555198436696",
        "public_name": "At 3.5m Augusto Cliente"
    },
    {
        "phone_number": "+555499957788",
        "public_name": "At 3m Waleska Walber Cliente"
    },
    {
        "phone_number": "+554797120712",
        "public_name": "At 3m Larissa Brito Cliente"
    },
    {
        "phone_number": "+554797172332",
        "public_name": "Carmem Cliente"
    },
    {
        "phone_number": "+554799964079",
        "public_name": "José Guimarães Cliente"
    },
    {
        "phone_number": "+554198890555",
        "public_name": "AT 800K -Leticia Amorim Cliente Casa"
    },
    {
        "phone_number": "+554191178119",
        "public_name": "At 3m Gisele Cavichiolo Cliente"
    },
    {
        "phone_number": "+554796265621",
        "public_name": "AT 1M- Rodrigo Cliente"
    },
    {
        "phone_number": "+554791400088",
        "public_name": "AT 800K -David Cliente"
    },
    {
        "phone_number": "+554788362708",
        "public_name": "Charles Proprietario Mirante Das Ondas 901"
    },
    {
        "phone_number": "+5521970312397",
        "public_name": "AT 500K - Ricardo Cliente RJ Terreno"
    },
    {
        "phone_number": "+556592560200",
        "public_name": "Fernando Silva Cliente Mkt Boreal Permuta Marmore"
    },
    {
        "phone_number": "+554797030000",
        "public_name": "Rafael Proprietario Casa Haras Do Rio Do Ouro"
    },
    {
        "phone_number": "+554791086844",
        "public_name": "AT 500K - Suziani Cliente Praia Brava"
    },
    {
        "phone_number": "+554499369191",
        "public_name": "AT 1M-Junior Cliente"
    },
    {
        "phone_number": "+554199122164",
        "public_name": "Adriano Silva Nizer Cliente Eberti"
    },
    {
        "phone_number": "+554196501114",
        "public_name": "AT 800K - Paulo Cliente Curitiba"
    },
    {
        "phone_number": "+556183536868",
        "public_name": "At 1.6m Karina Cliente"
    },
    {
        "phone_number": "+554799845571",
        "public_name": "Vili Schiochet Proprietario Notthing 2602"
    },
    {
        "phone_number": "+555195537788",
        "public_name": "Marcelo Proprietario Clemond"
    },
    {
        "phone_number": "+556599037708",
        "public_name": "Heloisa Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555197565546",
        "public_name": "Suellen Schmidt Cliente Organica"
    },
    {
        "phone_number": "+554391571966",
        "public_name": "At 5m Oscar Cliente"
    },
    {
        "phone_number": "+555182602602",
        "public_name": "AT 800K - Cleia Ceni Cliente"
    },
    {
        "phone_number": "+555484471936",
        "public_name": "At 2m Danieli Cliente"
    },
    {
        "phone_number": "+556696854121",
        "public_name": "At 2m Patricia Mota Cliente"
    },
    {
        "phone_number": "+554791134982",
        "public_name": "Edgar H Wegner Proprietario Salas Benvenutti"
    },
    {
        "phone_number": "+554799980154",
        "public_name": "Maikon Proprietario"
    },
    {
        "phone_number": "+554784348455",
        "public_name": "AT 2M Fabio Schulz Cliente"
    },
    {
        "phone_number": "+554799057724",
        "public_name": "Fabio Cliente"
    },
    {
        "phone_number": "+554991078268",
        "public_name": "AT 800K - Priscila Manao Cliente"
    },
    {
        "phone_number": "+554788033440",
        "public_name": "AT 2.5m Luiz Carlos Rocha Cliente"
    },
    {
        "phone_number": "+554899780729",
        "public_name": "Gabriel Peruchi Proprietário Terraco Da Rainha "
    },
    {
        "phone_number": "+555492678166",
        "public_name": "AT 3m Rafael Moraes Cliente"
    },
    {
        "phone_number": "+554791157054",
        "public_name": "Felipe Kapper Cliente Permuta Itapema"
    },
    {
        "phone_number": "+554796006566",
        "public_name": "Marcos Proprietario Arkansas"
    },
    {
        "phone_number": "+554198783399",
        "public_name": "At 3m Nivaldo Carneiro Cliente"
    },
    {
        "phone_number": "+554988292969",
        "public_name": "AT 1M- Renato Cliente - Quadra Mar"
    },
    {
        "phone_number": "+554796281010",
        "public_name": "Wilson Coelho Cliente Loteamento"
    },
    {
        "phone_number": "+554198313541",
        "public_name": "Jean Proprietario Acacias Frente Mar"
    },
    {
        "phone_number": "+554791614794",
        "public_name": "AT 1.3M Alana Mallmann Cliente"
    },
    {
        "phone_number": "+5511998339822",
        "public_name": "Alexandre Cliente SP"
    },
    {
        "phone_number": "+554799826766",
        "public_name": "AT 3M Dani Cliente"
    },
    {
        "phone_number": "+554799191340",
        "public_name": "AT 3.5M Alexandro Cliente"
    },
    {
        "phone_number": "+554791950004",
        "public_name": "AT 1.3M -Robson Cliente"
    },
    {
        "phone_number": "+555496094717",
        "public_name": "Airton Proprietario Torre Atlantica 604"
    },
    {
        "phone_number": "+555481077000",
        "public_name": "Silvio Zanette Cliente Organica"
    },
    {
        "phone_number": "+555496372326",
        "public_name": "AT 4.5M- Marcelo Cliente Frente Mar Passo Fundo"
    },
    {
        "phone_number": "+554784632797",
        "public_name": "AT 500K - Cleuso Cliente"
    },
    {
        "phone_number": "+554791193693",
        "public_name": "Gilvan Proprietario Alameda Jardins 1804"
    },
    {
        "phone_number": "+554792081501",
        "public_name": "Ezidoro Proprietario Cartagena"
    },
    {
        "phone_number": "+554999881192",
        "public_name": "Isabel Milani Cliente Organica"
    },
    {
        "phone_number": "+554699741498",
        "public_name": "At 2m Loraine Corso Sanson Cliente"
    },
    {
        "phone_number": "+554796220807",
        "public_name": "Geva Proprietário Mercedes"
    },
    {
        "phone_number": "+554792541208",
        "public_name": "Cirlene Teixeira Cliente Organica"
    },
    {
        "phone_number": "+554796213167",
        "public_name": "AT 500K - Adrian Cliente"
    },
    {
        "phone_number": "+5511935051600",
        "public_name": "AT 3M Tania Da Silva Cliente"
    },
    {
        "phone_number": "+554499911036",
        "public_name": "AT 1.6 Elder Cliente"
    },
    {
        "phone_number": "+554888154750",
        "public_name": "Marcelo Proprietário Pionner Tower"
    },
    {
        "phone_number": "+554796701190",
        "public_name": "At 1.6m Jarrison Cliente"
    },
    {
        "phone_number": "+554899776688",
        "public_name": "Joao Batista Martins - Proprietario"
    },
    {
        "phone_number": "+554388289701",
        "public_name": "Gilberto Cordovil Cliente Hyde"
    },
    {
        "phone_number": "+5513997335616",
        "public_name": "AT 1.6M House Desing Decor Cliente"
    },
    {
        "phone_number": "+555499860516",
        "public_name": "AT 800K - Celcio Kozen Cliente -Casa"
    },
    {
        "phone_number": "+555484039472",
        "public_name": "Fabio Cliente Erechim"
    },
    {
        "phone_number": "+554799468822",
        "public_name": "Indianara Alves Cliente"
    },
    {
        "phone_number": "+555191146399",
        "public_name": "AT 800K - Vera Dalmanico Cliente"
    },
    {
        "phone_number": "+555596824914",
        "public_name": "Tarso Cliente Tupa RS"
    },
    {
        "phone_number": "+555491425398",
        "public_name": "At 3m Mauricio Mentz Cliente"
    },
    {
        "phone_number": "+554188586313",
        "public_name": "AT 1M-Marcia Rangel Cliente"
    },
    {
        "phone_number": "+5511991117014",
        "public_name": "AT 500k Derocilia Bussing Cliente"
    },
    {
        "phone_number": "+554199867474",
        "public_name": "At 9m Cesar Clauman Cliente"
    },
    {
        "phone_number": "+554792445115",
        "public_name": "AT 800K - Vanise Cliente- Sobrado"
    },
    {
        "phone_number": "+554899279320",
        "public_name": "AT 1M -Thiago Cliente Florianopolis"
    },
    {
        "phone_number": "+554599881027",
        "public_name": "At 3m Leandro Prinz Cliente"
    },
    {
        "phone_number": "+555491121042",
        "public_name": "At 1.6m José Gilberto Vergani Cliente"
    },
    {
        "phone_number": "+554999858080",
        "public_name": "At 3.5m Cézar Leobet Cliente"
    },
    {
        "phone_number": "+554699125453",
        "public_name": "Juari Cliente Organica"
    },
    {
        "phone_number": "+554599608436",
        "public_name": "Anny Muller Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554899111115",
        "public_name": "Saulo Cliente"
    },
    {
        "phone_number": "+554796161111",
        "public_name": "AT 800K - Josiane Cliente Casa"
    },
    {
        "phone_number": "+554133020090",
        "public_name": "Proprietario-Afonso  1501 E 3401 Vision"
    },
    {
        "phone_number": "+554191273737",
        "public_name": "Rafael Proprietario Vista Bella 2602"
    },
    {
        "phone_number": "+554399914253",
        "public_name": "AT 500K -Rosane Reis Cliente Praia Brava"
    },
    {
        "phone_number": "+554384442727",
        "public_name": "At 2m Ana Cliente"
    },
    {
        "phone_number": "+554799199196",
        "public_name": "Rodrigo Proprietario Sobrado Praia Dos Amores 790 Mil"
    },
    {
        "phone_number": "+554399604000",
        "public_name": "At 3m Adriano Contato Cliente"
    },
    {
        "phone_number": "+555399947257",
        "public_name": "Gabriel Yacovazzo Belino Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554784086749",
        "public_name": "Arno Proprietario Costa Tropicale 1201"
    },
    {
        "phone_number": "+554799922761",
        "public_name": "AT 2M Vanderlea Meller Cliente"
    },
    {
        "phone_number": "+555199625600",
        "public_name": "At 1M Paulo Lourenço Rosa Cliente"
    },
    {
        "phone_number": "+5521995636167",
        "public_name": "Fernando Lopes Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799689899",
        "public_name": "AT 2M -Roni Cliente"
    },
    {
        "phone_number": "+554799238330",
        "public_name": "Luis Proprietario Cobertura Baia Dos Golfinhos"
    },
    {
        "phone_number": "+554796214406",
        "public_name": "Louri Cliente"
    },
    {
        "phone_number": "+555596773570",
        "public_name": "AT 1.6M Geraldino De Carli Cliente"
    },
    {
        "phone_number": "+554196440933",
        "public_name": "AT 800K - Fabiano Cliente"
    },
    {
        "phone_number": "+554191435224",
        "public_name": "AT 2M Michel Basso Cliente"
    },
    {
        "phone_number": "+554796470085",
        "public_name": "AT 500K - Cristiane Cliente P/Deixar Alugado"
    },
    {
        "phone_number": "+555599702728",
        "public_name": "Ana Magali Scheeren Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554991275350",
        "public_name": "Fabiana Cliente Oeste"
    },
    {
        "phone_number": "+554199736709",
        "public_name": "Valdecir Miranda Cliente Marido Cristiane"
    },
    {
        "phone_number": "+554591224242",
        "public_name": "Juliano Cliente Cascavel"
    },
    {
        "phone_number": "+554784121416",
        "public_name": "Paulo Alberto Proprietario Diamond Hill"
    },
    {
        "phone_number": "+5519991338392",
        "public_name": "AT 3M Robson Cliente"
    },
    {
        "phone_number": "+554196752828",
        "public_name": "Werlang Cliente Marido Rita"
    },
    {
        "phone_number": "+554188067036",
        "public_name": "Fernando Cliente Comprou"
    },
    {
        "phone_number": "+554796165542",
        "public_name": "AT 3M Carina Lourenço Cliente"
    },
    {
        "phone_number": "+554498007776",
        "public_name": "AT 1M - Alexandre Cliente Quadra Mar"
    },
    {
        "phone_number": "+554799993868",
        "public_name": "Arno Proprietário Frente Mar"
    },
    {
        "phone_number": "+554196440836",
        "public_name": "Perini Proprietario Casa 700 Mil"
    },
    {
        "phone_number": "+554196894363",
        "public_name": "AT 800K Leandro Rodrigues Cliente Casa"
    },
    {
        "phone_number": "+554784252140",
        "public_name": "Silas Proprietario Terra e Mar 602"
    },
    {
        "phone_number": "+554188968361",
        "public_name": "AT 1. 3M - Patricia Stein Lemes Cliente Praia Brava"
    },
    {
        "phone_number": "+554797231532",
        "public_name": "Jose Guimarães Cliente Número Dele"
    },
    {
        "phone_number": "+555496414319",
        "public_name": "At 500k Rayssa Willig Cliente"
    },
    {
        "phone_number": "+554791880900",
        "public_name": "AT 4m Isabel Cliente"
    },
    {
        "phone_number": "+5511981382224",
        "public_name": "Helo Gomes Cliente Ilhas Marianas"
    },
    {
        "phone_number": "+555381123464",
        "public_name": "AT 2M- Maicon Sulivan Cliente Tem Apt No Siri"
    },
    {
        "phone_number": "+5511966018365",
        "public_name": "AT 800K - Roberto Souza Cliente"
    },
    {
        "phone_number": "+555496616513",
        "public_name": "Vera Cliente Organica"
    },
    {
        "phone_number": "+554497549177",
        "public_name": "Daiane Miranda Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554896247021",
        "public_name": "Edson Proprietario Cabortura Iluminatti"
    },
    {
        "phone_number": "+554299910333",
        "public_name": "At 3.5m Denis Sanson Cliente"
    },
    {
        "phone_number": "+554199028211",
        "public_name": "Fabio Cliente Curitiba"
    },
    {
        "phone_number": "+554799447991",
        "public_name": "AT 500K - Cesar Correia Cliente -Praia Brava Mkt"
    },
    {
        "phone_number": "+555196398816",
        "public_name": "Francielli Cliente Mot Boreal"
    },
    {
        "phone_number": "+554799616371",
        "public_name": "Jose Cliente Proprietário Tem Terreno No Morretes Itapema"
    },
    {
        "phone_number": "+554799837337",
        "public_name": "Alfredo Proprietario 400 Torre Di Petra"
    },
    {
        "phone_number": "+554799337228",
        "public_name": "AT 1.6M- Eraldo Cliente  Mkt Tem Jardim Atlantico"
    },
    {
        "phone_number": "+556684610415",
        "public_name": "Eldorado Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554899716565",
        "public_name": "AT 1.6M Ana Luiza Maia Cliente"
    },
    {
        "phone_number": "+554196526150",
        "public_name": "Rafa Schuastz Cliente Organica"
    },
    {
        "phone_number": "+554799830231",
        "public_name": "Rui Leopoldo Hess Proprietario Torre Atlantica"
    },
    {
        "phone_number": "+554791628005",
        "public_name": "AT 1M- Marli Ishida Cliente"
    },
    {
        "phone_number": "+554899928860",
        "public_name": "AT 1M-  Aurelio Cliente"
    },
    {
        "phone_number": "+554788169998",
        "public_name": "Douglas Proprietário Portal De Antares 504"
    },
    {
        "phone_number": "+554599148696",
        "public_name": "Vanderlei Cristovam Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554792310083",
        "public_name": "Fabio Zanon Cliente Orbita"
    },
    {
        "phone_number": "+554191214000",
        "public_name": "Aluisio Cliente Organica"
    },
    {
        "phone_number": "+554799879306",
        "public_name": "AT 500K - Creuza Andrade Cliente - Praia Brava"
    },
    {
        "phone_number": "+555196043009",
        "public_name": "Naira França Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554399550460",
        "public_name": "At 3m Neto Dib Cliente"
    },
    {
        "phone_number": "+554991976111",
        "public_name": "Rose Cliente Indicacao Amilton Lages"
    },
    {
        "phone_number": "+554796633388",
        "public_name": "Junior Proprietario Cepar 83"
    },
    {
        "phone_number": "+555499144433",
        "public_name": "At 2m Maria Lucia Leite Cliente"
    },
    {
        "phone_number": "+554799782210",
        "public_name": "Marcio E Patricia Clientes Blumenau"
    },
    {
        "phone_number": "+5524999181968",
        "public_name": "AT 500K - Rogerio Cliente Sobrado"
    },
    {
        "phone_number": "+554484088906",
        "public_name": "At 3.5m Ricardo Fancelli Cliente"
    },
    {
        "phone_number": "+554498261983",
        "public_name": "At 500k Gabriela Cliente"
    },
    {
        "phone_number": "+554899359198",
        "public_name": "AT 6M Magda Campos Cliente"
    },
    {
        "phone_number": "+554899830080",
        "public_name": "Paulo Cliente Florianopolis Tem Maria Salete 2 Dorm"
    },
    {
        "phone_number": "+554788180355",
        "public_name": "AT 800K - Lisandro Cliente Casa -Parcelado"
    },
    {
        "phone_number": "+554899765141",
        "public_name": "AT 800K - Robe Cliente"
    },
    {
        "phone_number": "+554799021644",
        "public_name": "AT 3.5m Alessandra Fernandes Cliente"
    },
    {
        "phone_number": "+554792241471",
        "public_name": "Alfred Proprietario Acqua Del Mare 901"
    },
    {
        "phone_number": "+554299472023",
        "public_name": "At 1m Érica Vollweiter Cliente"
    },
    {
        "phone_number": "+554796157147",
        "public_name": "Méri Cliente"
    },
    {
        "phone_number": "+554784144658",
        "public_name": "Samili Cliente"
    },
    {
        "phone_number": "+554498129441",
        "public_name": "Marcelo Longhini Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554288633616",
        "public_name": "AT 3.5M Eduardo Rosental Cliente"
    },
    {
        "phone_number": "+555182016368",
        "public_name": "At 3.5m Fabio Darlan Souza Cliente"
    },
    {
        "phone_number": "+554391411415",
        "public_name": "At 3.5m Tania Aquino Cliente"
    },
    {
        "phone_number": "+554796884228",
        "public_name": "Lyz Proprietario Ed Israel"
    },
    {
        "phone_number": "+5521969733273",
        "public_name": "AT 1m Georgea Wernke Cliente"
    },
    {
        "phone_number": "+554199766757",
        "public_name": "Felipe Proprietario"
    },
    {
        "phone_number": "+554599847363",
        "public_name": "AT 2M Thiago Magnabosco Cliente"
    },
    {
        "phone_number": "+554191024232",
        "public_name": "Abdo Proprietário"
    },
    {
        "phone_number": "+555491177241",
        "public_name": "At 8m Karol Diel Cliente"
    },
    {
        "phone_number": "+554796855210",
        "public_name": "AT 1.3M - Tatiana Cliente"
    },
    {
        "phone_number": "+554799713869",
        "public_name": "Eliane Cliente Joenville"
    },
    {
        "phone_number": "+554196145082",
        "public_name": "AT 1.3M -Mauricio Cliente"
    },
    {
        "phone_number": "+555192421792",
        "public_name": "Pati Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554991461095",
        "public_name": "AT 1M- Mariani Cliente-Meia Praia"
    },
    {
        "phone_number": "+554799814299",
        "public_name": "William Cliente Organica"
    },
    {
        "phone_number": "+554796729126",
        "public_name": "At 7m Junior Olevar Cliente"
    },
    {
        "phone_number": "+554792064837",
        "public_name": "Alex Proprietário San Remo 804"
    },
    {
        "phone_number": "+554391938050",
        "public_name": "AT 800K -Helio Cliente"
    },
    {
        "phone_number": "+5491161937856",
        "public_name": "Lukas Cliente Buenos Aires"
    },
    {
        "phone_number": "+554399722829",
        "public_name": "AT 800K - Leonardo Cliente"
    },
    {
        "phone_number": "+554799237766",
        "public_name": "AT 2M Felipe Folchini Cliente"
    },
    {
        "phone_number": "+555491561976",
        "public_name": "Osmar Cliente Ate"
    },
    {
        "phone_number": "+554799890488",
        "public_name": "AT 2M Simone Elisa Venske Cliente"
    },
    {
        "phone_number": "+554797636666",
        "public_name": "Valdir Proprietario Casa Camboriu"
    },
    {
        "phone_number": "+5527992039016",
        "public_name": "Marcos Proprietario Arkansas"
    },
    {
        "phone_number": "+554499559998",
        "public_name": "AT 1.3m Milena Philipp Cliente"
    },
    {
        "phone_number": "+5511968682594",
        "public_name": "At 3.5m Juci Westphal Cliente"
    },
    {
        "phone_number": "+554999834440",
        "public_name": "Arnildo Gerhardt Cliente Pai Do Alexandre"
    },
    {
        "phone_number": "+595985443099",
        "public_name": "At 4m Dhones Cliente Paraguai Frente Mar"
    },
    {
        "phone_number": "+556792757656",
        "public_name": "Maikon Cliente Orbita"
    },
    {
        "phone_number": "+555499410841",
        "public_name": "AT 1M- Gilda Cliente Passo Fundo"
    },
    {
        "phone_number": "+554199118866",
        "public_name": "Francielle Cwikla Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554788040027",
        "public_name": "Simone Filha João Proprietario Maria Eduarda"
    },
    {
        "phone_number": "+554784983147",
        "public_name": "Marlon Pacheco Cliente Ate"
    },
    {
        "phone_number": "+554188315456",
        "public_name": "Jonas Prates Cliente"
    },
    {
        "phone_number": "+5517992121211",
        "public_name": "AT 800K - Marcus Augustu Biffi Cliente Casa"
    },
    {
        "phone_number": "+554799747574",
        "public_name": "AT 2.5M Fabricia da Costa Cliente"
    },
    {
        "phone_number": "+554799696677",
        "public_name": "Gilmar proprietario Casa Aririba"
    },
    {
        "phone_number": "+554799834400",
        "public_name": "Cesar Proprietario Renaissence 302"
    },
    {
        "phone_number": "+554799231311",
        "public_name": "AT 2.5M- Valdir Lartzac Cliente Mkt"
    },
    {
        "phone_number": "+555491299325",
        "public_name": "At 2m Alexandre Contin Cliente"
    },
    {
        "phone_number": "+554891607974",
        "public_name": "Agri Multi Cliente Grade"
    },
    {
        "phone_number": "+554788024912",
        "public_name": "AT 2M- Lucas Cliente"
    },
    {
        "phone_number": "+554792224080",
        "public_name": "AT 1.3M -Willian Cliente"
    },
    {
        "phone_number": "+554199438333",
        "public_name": "Gustavo Dantas Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796622872",
        "public_name": "Eduardo Proprietario Aguas Do Iguassu 1601"
    },
    {
        "phone_number": "+554388292050",
        "public_name": "AT 500K -Silvia Cliente Curitiba"
    },
    {
        "phone_number": "+555181778711",
        "public_name": "At 1m Suelen Lima Cliente"
    },
    {
        "phone_number": "+554991434010",
        "public_name": "AT 1.3M -Helio Cliente"
    },
    {
        "phone_number": "+554788360851",
        "public_name": "AT 500K - Lucas Cliente Camboriu"
    },
    {
        "phone_number": "+554396331655",
        "public_name": "AT 1M- Miquéias Cliente"
    },
    {
        "phone_number": "+555491658775",
        "public_name": "Milton Rinaldo Cliente Orbita"
    },
    {
        "phone_number": "+554796600324",
        "public_name": "AT 2M Paula Cristina Lima Cliente"
    },
    {
        "phone_number": "+554195387005",
        "public_name": "Frank Arruda Cliente Mkt Frente Mar Ate"
    },
    {
        "phone_number": "+554796368566",
        "public_name": "AT 1M- Lidiana Cliente  Olx Tem Permuta"
    },
    {
        "phone_number": "+554799832474",
        "public_name": "Peixoto Proprietário Imperio Das Ondas 3302"
    },
    {
        "phone_number": "+554195948870",
        "public_name": "AT 800K -Joao Cesar Cliente - Casa"
    },
    {
        "phone_number": "+554499909446",
        "public_name": "Maria Virginia Vivi Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796800064",
        "public_name": "Renan Proprietario Sobrado"
    },
    {
        "phone_number": "+554899430222",
        "public_name": "Israel Nasa Cliente Indicação Raul"
    },
    {
        "phone_number": "+554788042203",
        "public_name": "At 2m Antonio Da Silva Cliente"
    },
    {
        "phone_number": "+556596426769",
        "public_name": "AT 800K - Fabiola Cliente"
    },
    {
        "phone_number": "+555596388092",
        "public_name": "Cristiano Da Silva Cliente Marau Mkt Boreal"
    },
    {
        "phone_number": "+554799795205",
        "public_name": "AT 2M Abrahão Alfredo Cliente"
    },
    {
        "phone_number": "+555597247977",
        "public_name": "Kelvin Oliveira Cliente Aurora"
    },
    {
        "phone_number": "+555184596353",
        "public_name": "AT 5M Eduardo Fontana Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796132252",
        "public_name": "AT 800K - Leandro Cliente"
    },
    {
        "phone_number": "+554291161017",
        "public_name": "AT 500K - Angelo Cliente Praia Brava Mkt"
    },
    {
        "phone_number": "+554788513240",
        "public_name": "AT 800K - Thiago Cliente"
    },
    {
        "phone_number": "+555499460046",
        "public_name": "AT 1M-Marcelo Borges Cliente Pf"
    },
    {
        "phone_number": "+554791539969",
        "public_name": "Gilvan Cavalheiro Cliente Barra Velha Loteamento"
    },
    {
        "phone_number": "+554799275903",
        "public_name": "Roberto Proprietario Barra Tower Blumenau"
    },
    {
        "phone_number": "+553898135758",
        "public_name": "At 3.5m Juliana Trevisan Cliente"
    },
    {
        "phone_number": "+554799643038",
        "public_name": "AT 2.5m Erika Hasse Cliente"
    },
    {
        "phone_number": "+555584546218",
        "public_name": "Cleiton Cliente EAG Vendido"
    },
    {
        "phone_number": "+555193118215",
        "public_name": "AT 1.6M- Pablo Werlang Cliente"
    },
    {
        "phone_number": "+554196438618",
        "public_name": "Alfred Proprietário Saint German Diferenciado"
    },
    {
        "phone_number": "+554899627711",
        "public_name": "AT 2M Henrique Cliente"
    },
    {
        "phone_number": "+554792690816",
        "public_name": "AT 500K - Cintia Cliente Praia Brava"
    },
    {
        "phone_number": "+5511993224110",
        "public_name": "AT 800K - Ilson Cliente Casa"
    },
    {
        "phone_number": "+554198419842",
        "public_name": "Rosemar Proprietário Costão Da Barra Torre Central"
    },
    {
        "phone_number": "+554789006715",
        "public_name": "AT 1.6m Ana Cliente"
    },
    {
        "phone_number": "+5511949702080",
        "public_name": "AT 800K - Alessandra Cliente Casa"
    },
    {
        "phone_number": "+554799530310",
        "public_name": "AT 1.6M Denise Cliente"
    },
    {
        "phone_number": "+554199386613",
        "public_name": "AT 800K - Leonilda Rosseti Cliente Casa"
    },
    {
        "phone_number": "+554799673833",
        "public_name": "Juvani Kling Proprietario Monte Olympos 401"
    },
    {
        "phone_number": "+554791921313",
        "public_name": "At 3.5m Dani Cliente"
    },
    {
        "phone_number": "+554188986276",
        "public_name": "AT 4M- Silmara Cliente Frente Mar"
    },
    {
        "phone_number": "+554199740506",
        "public_name": "Emir Proprietario Praia Do Sol"
    },
    {
        "phone_number": "+556984667171",
        "public_name": "Sandro Cliente Indicacao"
    },
    {
        "phone_number": "+554192332564",
        "public_name": "Gil Menezes Cliente Yachthouse"
    },
    {
        "phone_number": "+554799687929",
        "public_name": "AT 1.3 Jessica Gomes Cliente"
    },
    {
        "phone_number": "+554797078151",
        "public_name": "Nilson Proprietario Bc"
    },
    {
        "phone_number": "+554799830665",
        "public_name": "Adulcio Agustini Proprietario Barramares 902"
    },
    {
        "phone_number": "+556191734101",
        "public_name": "Paulo Proprietário 1001 Mentawai"
    },
    {
        "phone_number": "+555199226068",
        "public_name": "At 2m Sergio Luiz Fernandes Cliente"
    },
    {
        "phone_number": "+554797108080",
        "public_name": "Eduardo Proprietario Ana Cunha 203"
    },
    {
        "phone_number": "+554299973113",
        "public_name": "Proprietario George Bizet"
    },
    {
        "phone_number": "+554796215146",
        "public_name": "AT 1M- Ricardo Moraes Cliente"
    },
    {
        "phone_number": "+554699101531",
        "public_name": "Eunice Cliente Admirá"
    },
    {
        "phone_number": "+554799710321",
        "public_name": "Carlos Cliente Casa"
    },
    {
        "phone_number": "+556599080109",
        "public_name": "AT 2.5M- Adriano Collegeo Cliente  Mkt Boreal"
    },
    {
        "phone_number": "+554792061087",
        "public_name": "Yeda Cliente BC"
    },
    {
        "phone_number": "+554791357443",
        "public_name": "At 1.3m Sidnei Cliente"
    },
    {
        "phone_number": "+554188943330",
        "public_name": "AT 3M Silvio Cliente"
    },
    {
        "phone_number": "+554388064858",
        "public_name": "AT 800K - Valdecir Cliente"
    },
    {
        "phone_number": "+554784471112",
        "public_name": "Yeda Cliente BC"
    },
    {
        "phone_number": "+554499161261",
        "public_name": "Irene Dellay Cliente Eberti"
    },
    {
        "phone_number": "+554199531810",
        "public_name": "AT 800K - Volnei Cliente"
    },
    {
        "phone_number": "+554799010368",
        "public_name": "Rose Cliente São Bento Do Oeste"
    },
    {
        "phone_number": "+554399358001",
        "public_name": "AT 1.6M- Junior Cliente  Mkt"
    },
    {
        "phone_number": "+555596412806",
        "public_name": "At 4m Alessandra Fiuza Cliente"
    },
    {
        "phone_number": "+554791818986",
        "public_name": "Paulo Proprietário Felicitá"
    },
    {
        "phone_number": "+555499778989",
        "public_name": "Angelisa Cliente Organica"
    },
    {
        "phone_number": "+554497764689",
        "public_name": "Dayane Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554299251857",
        "public_name": "Itamar Roberto Pereira Cliente Eberti"
    },
    {
        "phone_number": "+555481332231",
        "public_name": "AT 1.6M Jean Roger Cliente"
    },
    {
        "phone_number": "+554784552949",
        "public_name": "Marcos Cliente Olx"
    },
    {
        "phone_number": "+554796191425",
        "public_name": "Suzana Terezinha Ribeiro Cliente"
    },
    {
        "phone_number": "+554791350555",
        "public_name": "AT 1M Renzo Cliente"
    },
    {
        "phone_number": "+554299001069",
        "public_name": "At 1.3 Marcus Vinicius Mesquini Cliente"
    },
    {
        "phone_number": "+554199964243",
        "public_name": "Jorge Cliente Curitiba"
    },
    {
        "phone_number": "+554999146370",
        "public_name": "Analu Mezzomo Valandro Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799276868",
        "public_name": "Alex Cliente Troca Apt Por Casa"
    },
    {
        "phone_number": "+554799870760",
        "public_name": "Salomar Osti Proprietario"
    },
    {
        "phone_number": "+554896127953",
        "public_name": "Ricardo Cliente Loteamento"
    },
    {
        "phone_number": "+554199607711",
        "public_name": "Jeferson Cliente Curitiba"
    },
    {
        "phone_number": "+554196886116",
        "public_name": "Joares Cliente Curitiba"
    },
    {
        "phone_number": "+5518997292253",
        "public_name": "AT 1. 6 M Daniel Marido Fran Cliente"
    },
    {
        "phone_number": "+554799971414",
        "public_name": "AT 800k Shirley Vergara Cliente"
    },
    {
        "phone_number": "+554498356768",
        "public_name": "At 3m Mauro Cliente"
    },
    {
        "phone_number": "+555499833444",
        "public_name": "Ademir Romani Vendido Cliente Marau"
    },
    {
        "phone_number": "+554196119173",
        "public_name": "Fabio Falasque Cliente Organica"
    },
    {
        "phone_number": "+5511985249279",
        "public_name": "Nelson Cliente SP"
    },
    {
        "phone_number": "+554491195757",
        "public_name": "Leandro Cliente"
    },
    {
        "phone_number": "+554799668449",
        "public_name": "At 1m Elis Domingues Cliente Casa Quer Casa Tem Permuta"
    },
    {
        "phone_number": "+554999660282",
        "public_name": "At 3.5m Marcelo Momm Cliente"
    },
    {
        "phone_number": "+554499402751",
        "public_name": "At 3.5m Shirley Ramiro Cliente"
    },
    {
        "phone_number": "+555591685548",
        "public_name": "Rochelli Cliente Esposa Clay"
    },
    {
        "phone_number": "+554199780062",
        "public_name": "4m Arthur Cliente"
    },
    {
        "phone_number": "+554999831150",
        "public_name": "Alexandre Cliente Organica Curitibanos"
    },
    {
        "phone_number": "+554788079996",
        "public_name": "AT 3M Ricardo M Retzem Cliente"
    },
    {
        "phone_number": "+554791021110",
        "public_name": "Marcelo Cliente Camboriu"
    },
    {
        "phone_number": "+554499964121",
        "public_name": "At 1.6m Rafael Soares Cliente"
    },
    {
        "phone_number": "+554799890701",
        "public_name": "Homero Cliente Organica"
    },
    {
        "phone_number": "+554196212131",
        "public_name": "At 3m Fernando Dembiski Cliente"
    },
    {
        "phone_number": "+555497012944",
        "public_name": "Daniel Cliente Serrafina Correa"
    },
    {
        "phone_number": "+554799627596",
        "public_name": "Joao Carlos Proprietário Alameda Provence"
    },
    {
        "phone_number": "+554198593552",
        "public_name": "Tiago Dos Santos Camargo Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554791052204",
        "public_name": "Proprietario Splendia 2101 Rodrigo"
    },
    {
        "phone_number": "+556182179100",
        "public_name": "AT 1M- Marco Cliente"
    },
    {
        "phone_number": "+554192851870",
        "public_name": "At 3.5m Daniela Cliente"
    },
    {
        "phone_number": "+554796342992",
        "public_name": "Proprietário Reggio Di Calebria Caprta"
    },
    {
        "phone_number": "+554599169102",
        "public_name": "AT 500K - Sissi Elisabeth Cliente"
    },
    {
        "phone_number": "+555499985690",
        "public_name": "Mauro Cliente Vendido"
    },
    {
        "phone_number": "+554988329939",
        "public_name": "Gustavo Lolato Proprietario Ap Proedi"
    },
    {
        "phone_number": "+5511971775017",
        "public_name": "Gelson Pilar Cliente Indicacao Ademir"
    },
    {
        "phone_number": "+555181242134",
        "public_name": "AT 500K - Paulo Prass Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554799651211",
        "public_name": "Jorge Proprietario 402 Pablo Neruda"
    },
    {
        "phone_number": "+554199981807",
        "public_name": "Willian Proprietário Porto Vita 1801"
    },
    {
        "phone_number": "+554199637470",
        "public_name": "Talyta Palhano Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799110370",
        "public_name": "AT 5M- Giovano Proprietário Vale Dos Reis 2402"
    },
    {
        "phone_number": "+554998274633",
        "public_name": "Proprietario Apartamento 1.100 Jardim Atlantico"
    },
    {
        "phone_number": "+554788051348",
        "public_name": "Palmira Cliente Pouso Redondo"
    },
    {
        "phone_number": "+554791170951",
        "public_name": "At 2m Eduardo Montandon Cliente"
    },
    {
        "phone_number": "+556796887630",
        "public_name": "AT 1M-Dione Cliente Mkt"
    },
    {
        "phone_number": "+554797191815",
        "public_name": "AT 1m Alaa Cliente"
    },
    {
        "phone_number": "+554791132449",
        "public_name": "Eduardo Kazapi Cliente"
    },
    {
        "phone_number": "+554799762670",
        "public_name": "At 3.5m Vera Guedes Maidana Cliente"
    },
    {
        "phone_number": "+554198590099",
        "public_name": "Alex Cliente Organica"
    },
    {
        "phone_number": "+554791467005",
        "public_name": "Canisio Dias (Pedro) Cliente Eberti"
    },
    {
        "phone_number": "+554797002983",
        "public_name": "Rafael Proprietario Torre De Lyon"
    },
    {
        "phone_number": "+554188356521",
        "public_name": "Gisele Cliente Curitiba"
    },
    {
        "phone_number": "+554195866531",
        "public_name": "Diego Cliente Curitiba Tem Ap La De 1.5"
    },
    {
        "phone_number": "+554799002960",
        "public_name": "Marcelo Oliveira Cliente"
    },
    {
        "phone_number": "+5519981479963",
        "public_name": "Fagner Cliente Sala Comercia Campinas SP"
    },
    {
        "phone_number": "+555584024838",
        "public_name": "AT 1.6M Roberto Tessele Cliente"
    },
    {
        "phone_number": "+554796096539",
        "public_name": "AT 500K - Juliana Cliente Filha Tânia"
    },
    {
        "phone_number": "+554691036866",
        "public_name": "Olacir Francescatto Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799209550",
        "public_name": "João Aloisio Haubert Cliente"
    },
    {
        "phone_number": "+556581267117",
        "public_name": "At 3.5m Jessica Ribeiro Cliente"
    },
    {
        "phone_number": "+555384182858",
        "public_name": "Marcos Proprietario Splendia 1301"
    },
    {
        "phone_number": "+554299252100",
        "public_name": "AT 1.6m Sandra Maria Cliente"
    },
    {
        "phone_number": "+554899566619",
        "public_name": "Gustavo Cliente Orbita"
    },
    {
        "phone_number": "+555599285848",
        "public_name": "Neiva Schardong Cliente Orbita"
    },
    {
        "phone_number": "+554288267005",
        "public_name": "Marina Sacchi  Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554791760292",
        "public_name": "Edison Tomazelli Cliente Eberti"
    },
    {
        "phone_number": "+554799750009",
        "public_name": "Eduardo Wan-dall Cliente Esquadrias"
    },
    {
        "phone_number": "+554799830004",
        "public_name": "Airton Proprietario Summer Breeze"
    },
    {
        "phone_number": "+554891064971",
        "public_name": "At 600m Marilia Guisolffi Cliente"
    },
    {
        "phone_number": "+554784232345",
        "public_name": "AT 500K - Orlando Augusto Cliente"
    },
    {
        "phone_number": "+554499728607",
        "public_name": "AT 1M- Valter Cliente Frente Mar"
    },
    {
        "phone_number": "+554199436261",
        "public_name": "AT 800K - Deolinda Cliente- Tem Apt Ponta Grossa"
    },
    {
        "phone_number": "+554299727200",
        "public_name": "AT 800K - Silney Cliente"
    },
    {
        "phone_number": "+554497677287",
        "public_name": "Ligia Munhoz Cliente Organica"
    },
    {
        "phone_number": "+554799256224",
        "public_name": "Batista Cliente"
    },
    {
        "phone_number": "+556681257161",
        "public_name": "Regina Sofia Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554498508102",
        "public_name": "Sandra Mara Maggioni Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554898450070",
        "public_name": "Dejair Proprietario Malaga 1301"
    },
    {
        "phone_number": "+554796445448",
        "public_name": "AT 2M- Gustavo Jacomini Cliente Frente Mar"
    },
    {
        "phone_number": "+554799117384",
        "public_name": "AT 2M Roseli Zenp Cliente"
    },
    {
        "phone_number": "+555196751027",
        "public_name": "Vanessa Fuchs Cliente POA"
    },
    {
        "phone_number": "+554791197002",
        "public_name": "AT 1.3M -Liliam Cliente Bombas -Praia Brava"
    },
    {
        "phone_number": "+554799234277",
        "public_name": "Eduardo Proprietário Hermosa Beach 501"
    },
    {
        "phone_number": "+554799859257",
        "public_name": "Celso Proprietário Torre D Napoli 501"
    },
    {
        "phone_number": "+555496171734",
        "public_name": "Wilker Lago Cliente MKt Boreal"
    },
    {
        "phone_number": "+554797158008",
        "public_name": "AT 1.3m Gelson Argenta Cliente"
    },
    {
        "phone_number": "+554188213773",
        "public_name": "Samir Proprietario Ilha De Paqueta 403"
    },
    {
        "phone_number": "+554799900878",
        "public_name": "Adriano Dall Olivio Cliente"
    },
    {
        "phone_number": "+554684013798",
        "public_name": "Thiago Parisotto Luquini Cliente Yachthouse"
    },
    {
        "phone_number": "+554791602899",
        "public_name": "At 1.3m Aldo Gumz Jr Cliente"
    },
    {
        "phone_number": "+554684136080",
        "public_name": "Wilson Marcos Lopes Cliente"
    },
    {
        "phone_number": "+5521968109989",
        "public_name": "Ivo Proprietario D Itália 201"
    },
    {
        "phone_number": "+554799430660",
        "public_name": "Zé Alexandre Proprietario Pionner Tower 1101"
    },
    {
        "phone_number": "+554788599818",
        "public_name": "Omar Proprietário Portal De Antares 1003"
    },
    {
        "phone_number": "+554791664734",
        "public_name": "Carol Cliente"
    },
    {
        "phone_number": "+554199959999",
        "public_name": "Heitor Sumida Proprietario Torre Atlantica"
    },
    {
        "phone_number": "+554784180338",
        "public_name": "Henrique Cliente Camboriu"
    },
    {
        "phone_number": "+554791032077",
        "public_name": "Gelson Proprietario Amores Da Brava 801 Torre 4"
    },
    {
        "phone_number": "+554199155056",
        "public_name": "At 6.5m Luiz Antonio Cliente Ilhas Marianas"
    },
    {
        "phone_number": "+554391666530",
        "public_name": "Marcelo Cliente Jacarezinho"
    },
    {
        "phone_number": "+555481152105",
        "public_name": "At 3.5m Carlitos Carlotto Vanz Cliente"
    },
    {
        "phone_number": "+554791937979",
        "public_name": "Gelson Cliente Blumenau"
    },
    {
        "phone_number": "+554799445561",
        "public_name": "Cesar Proprietario Morro Dos Ventos 601"
    },
    {
        "phone_number": "+554591171712",
        "public_name": "AT 500K -Antonio Jair Crestani Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554999832914",
        "public_name": "Margarete Cliente Meia Praia"
    },
    {
        "phone_number": "+554796517272",
        "public_name": "Luciano Cliente Investidor"
    },
    {
        "phone_number": "+554799651692",
        "public_name": "At 1.4m Marcia Santos De Souza Cliente"
    },
    {
        "phone_number": "+554198952020",
        "public_name": "Rafael Proprietario Gran Torino 1001"
    },
    {
        "phone_number": "+554791530397",
        "public_name": "AT 800K - Vanessa Cliente"
    },
    {
        "phone_number": "+554399774277",
        "public_name": "AT 500K - Renato Bonacin Cliente Mkt  Praia Brava"
    },
    {
        "phone_number": "+556892535222",
        "public_name": "Ires Oliveira Cliente Aurora"
    },
    {
        "phone_number": "+554999177048",
        "public_name": "Carol Cliente"
    },
    {
        "phone_number": "+554784823732",
        "public_name": "Maicon De Borba Cliente"
    },
    {
        "phone_number": "+554799632312",
        "public_name": "Anderson Proprietario Piaza Vitoria"
    },
    {
        "phone_number": "+554796115059",
        "public_name": "Germano Hermínio Soares Cliente Organica"
    },
    {
        "phone_number": "+554599451072",
        "public_name": "Fabiane Cristina Adamczuk Cliente Italian"
    },
    {
        "phone_number": "+5514988031764",
        "public_name": "Andrez Cliente Organica"
    },
    {
        "phone_number": "+554591048670",
        "public_name": "Edson Ramiro Cliente Cascavel Vendido"
    },
    {
        "phone_number": "+554796168973",
        "public_name": "Antonio Decker Proprietario Torre D Napoli 1701"
    },
    {
        "phone_number": "+554684030380",
        "public_name": "At 1.6m Angela Maria Langaro Cliente"
    },
    {
        "phone_number": "+554384382828",
        "public_name": "At 1.6m Toninho Cliente"
    },
    {
        "phone_number": "+554799891583",
        "public_name": "Ivanildo Proprietário Rooftop"
    },
    {
        "phone_number": "+554797830083",
        "public_name": "Guilherme Lucci Proprietario Ilha Do Sol 1101"
    },
    {
        "phone_number": "+554199216026",
        "public_name": "AT 1M Anderson Catapan Cliente Investidor"
    },
    {
        "phone_number": "+554498492994",
        "public_name": "Marcelo Marques Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796814000",
        "public_name": "Wilson Proprietario Bosque Belcanto 2202"
    },
    {
        "phone_number": "+555181949383",
        "public_name": "At 3.5m Julio Cliente"
    },
    {
        "phone_number": "+554791710801",
        "public_name": "AT 800K - Manoel Cliente"
    },
    {
        "phone_number": "+554784189502",
        "public_name": "AT 2M Cristhianne Mudrey Cliente"
    },
    {
        "phone_number": "+554792587110",
        "public_name": "AT 800K - Mauricio Cliente Casa"
    },
    {
        "phone_number": "+554799664595",
        "public_name": "AT 2.5M- Matheus Castilho Cliente-Permuta CTB"
    },
    {
        "phone_number": "+554599591011",
        "public_name": "At 2.5m Adriana B Cliente"
    },
    {
        "phone_number": "+554788017878",
        "public_name": "AT 1.3M Ana Cliente"
    },
    {
        "phone_number": "+554799353919",
        "public_name": "At 2m Antonio Afonso Cliente"
    },
    {
        "phone_number": "+555596764430",
        "public_name": "At 1.6m Paulo André Lunardi Cliente"
    },
    {
        "phone_number": "+554799583903",
        "public_name": "Joao Ricardo Proprietario Portal Residence"
    },
    {
        "phone_number": "+554791830944",
        "public_name": "AT 500K -Wilma Cliente"
    },
    {
        "phone_number": "+554799479062",
        "public_name": "Vinitus Proprietario Casa Estaleiro"
    },
    {
        "phone_number": "+556699854292",
        "public_name": "At 4m Jonas Zonta Cliente"
    },
    {
        "phone_number": "+554999732531",
        "public_name": "At 1m Juliana Appel Passos Cliente"
    },
    {
        "phone_number": "+556181043653",
        "public_name": "Igor Proprietário Bmw"
    },
    {
        "phone_number": "+554799178249",
        "public_name": "AT 1M - Alisson Cliente"
    },
    {
        "phone_number": "+554888284547",
        "public_name": "AT 2.5M Jussara Cliente"
    },
    {
        "phone_number": "+554799955612",
        "public_name": "AT 500K - Anderson De Assuncao Cliente"
    },
    {
        "phone_number": "+554799802406",
        "public_name": "Ronaldo Proprietario Summer Breeze 2001"
    },
    {
        "phone_number": "+555199775436",
        "public_name": "Maira Cliente Organica"
    },
    {
        "phone_number": "+554796098382",
        "public_name": "Eloa Evidênce 1302 Proprietario"
    },
    {
        "phone_number": "+555491423013",
        "public_name": "Celso Luis Proprietario Arthur Fischer 1801"
    },
    {
        "phone_number": "+555199958293",
        "public_name": "Fernando Bourscheidt Cliente POA"
    },
    {
        "phone_number": "+555197012588",
        "public_name": "Ester Passing Cliente Orbita"
    },
    {
        "phone_number": "+554396392375",
        "public_name": "Kaue Barreto Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799672007",
        "public_name": "At 800k Maria Helena Borba Cliente"
    },
    {
        "phone_number": "+554799777897",
        "public_name": "AT 500K -Vanessa Pereira Cliente Sobrado"
    },
    {
        "phone_number": "+554799534000",
        "public_name": "AT 800K - Edson Cliente"
    },
    {
        "phone_number": "+554999861105",
        "public_name": "AT 2.5M Claudia Bertoldo Cliente"
    },
    {
        "phone_number": "+554298577906",
        "public_name": "At 3.5m Gilherme Petrechen Cliente"
    },
    {
        "phone_number": "+5522981032248",
        "public_name": "Victor Cliente Up"
    },
    {
        "phone_number": "+554797882525",
        "public_name": "Mônica Cliente Praia Brava"
    },
    {
        "phone_number": "+554791458991",
        "public_name": "AT 4M Sell Muller Cliente"
    },
    {
        "phone_number": "+554197410004",
        "public_name": "AT 1.3M -Joana Maria Cliente"
    },
    {
        "phone_number": "+554299730456",
        "public_name": "Florinda Cliente Ponta Grossa"
    },
    {
        "phone_number": "+555481159341",
        "public_name": "Jones Cliente Lagom"
    },
    {
        "phone_number": "+556791302060",
        "public_name": "AT 500K - Alex Cliente"
    },
    {
        "phone_number": "+554999813077",
        "public_name": "AT 1.6M Deize Roveda Cliente"
    },
    {
        "phone_number": "+554999615550",
        "public_name": "Julian Belotto Cliente Organica"
    },
    {
        "phone_number": "+554799739872",
        "public_name": "Paulo Proprietário Villa Siena nações"
    },
    {
        "phone_number": "+554999962450",
        "public_name": "Janete Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554197311706",
        "public_name": "At 3m Anderson Piovesani Cliente"
    },
    {
        "phone_number": "+554499260089",
        "public_name": "AT 1.3M Gislaine Molina Cliente"
    },
    {
        "phone_number": "+554792412040",
        "public_name": "Bruno Cliente EUA Vendido"
    },
    {
        "phone_number": "+554188596773",
        "public_name": "At 1.6m Wilson Pagnoncelli Cliente"
    },
    {
        "phone_number": "+554195881029",
        "public_name": "Jean Proprietario Frente Mar Acacias"
    },
    {
        "phone_number": "+554799858932",
        "public_name": "Rafael Cliente Joenville"
    },
    {
        "phone_number": "+554184488862",
        "public_name": "Edson Coser Cliente"
    },
    {
        "phone_number": "+554796334127",
        "public_name": "At 2.5m Tallyne Oliveira Cliente"
    },
    {
        "phone_number": "+554799923007",
        "public_name": "AT 800K - Pamella Cliente"
    },
    {
        "phone_number": "+554191399082",
        "public_name": "Marcelo Grad Cliente Organica"
    },
    {
        "phone_number": "+556999037397",
        "public_name": "AT 2m Daniela Scarone Cliente"
    },
    {
        "phone_number": "+5517997364170",
        "public_name": "AT 500k Alan Cliente"
    },
    {
        "phone_number": "+5511991519139",
        "public_name": "Edu Cliente Investidor"
    },
    {
        "phone_number": "+554799039180",
        "public_name": "Mika Cliente BC"
    },
    {
        "phone_number": "+554796664221",
        "public_name": "Joel Eyroff Cliente Organica"
    },
    {
        "phone_number": "+554796365636",
        "public_name": "AT 1M- Fabricio Cliente"
    },
    {
        "phone_number": "+554799450648",
        "public_name": "Marcelo Cliente BC"
    },
    {
        "phone_number": "+554488310442",
        "public_name": "AT 800K - Michelly Cliente Casa"
    },
    {
        "phone_number": "+554891691527",
        "public_name": "Ernani Proprietário Aldebaran"
    },
    {
        "phone_number": "+5521981009492",
        "public_name": "AT 500k Roberto Cliente"
    },
    {
        "phone_number": "+554792555521",
        "public_name": "Bernardo Proprietario Notre Ville 902"
    },
    {
        "phone_number": "+554796052455",
        "public_name": "AT 500K - Mari Borsoi Cliente  Praia Brava Mkt"
    },
    {
        "phone_number": "+554799890012",
        "public_name": "Joao Proprietario Torre Blanca 502 Frente Mar"
    },
    {
        "phone_number": "+554788078817",
        "public_name": "AT 1.3M -Paulo Cliente Blumenau"
    },
    {
        "phone_number": "+554899280074",
        "public_name": "AT 1M- Maicon Cliente - Itapema"
    },
    {
        "phone_number": "+554192553311",
        "public_name": "AT 800K - Edson Cliente Curitiba"
    },
    {
        "phone_number": "+554791941706",
        "public_name": "Jonathan Padilha Cliente Indicacao Lilian"
    },
    {
        "phone_number": "+554191994440",
        "public_name": "At 3.5m Enzo A. Silvestro Cliente"
    },
    {
        "phone_number": "+554792690707",
        "public_name": "Carlos Proprietário Royal Garden 1902"
    },
    {
        "phone_number": "+554184172474",
        "public_name": "AT 1.3M- Felipe Cliente - Praia BRAVA"
    },
    {
        "phone_number": "+554198560005",
        "public_name": "Sena Proprietario"
    },
    {
        "phone_number": "+555399714418",
        "public_name": "At 2m Regis Cliente"
    },
    {
        "phone_number": "+555599815371",
        "public_name": "AT 1M-Olmiro Andrade Cliente Mkt"
    },
    {
        "phone_number": "+556692276640",
        "public_name": "Debora Mendonça Cliente Frente Mar"
    },
    {
        "phone_number": "+554799183642",
        "public_name": "AT 500K -Rangel Cliente"
    },
    {
        "phone_number": "+554792599948",
        "public_name": "Vinicius Proprietario Casa Parcelada"
    },
    {
        "phone_number": "+554891373142",
        "public_name": "AT 800K - Marcelo Cliente - Praia Brava"
    },
    {
        "phone_number": "+554799737056",
        "public_name": "Edmilson Marido Da Dani Cliente"
    },
    {
        "phone_number": "+554799663577",
        "public_name": "Roberto Carlos Coradini Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554999912787",
        "public_name": "Roberto Proprietário Tropical Summer 501"
    },
    {
        "phone_number": "+554796849737",
        "public_name": "At 2m Simone Mendes Cliente"
    },
    {
        "phone_number": "+554792189292",
        "public_name": "At 3.5m Aline Siqueira Cliente"
    },
    {
        "phone_number": "+554792479253",
        "public_name": "Wilson Proprietario Montparnasse 1101"
    },
    {
        "phone_number": "+554796330845",
        "public_name": "AT 500K -Lourenço Cliente Balneario"
    },
    {
        "phone_number": "+554799889828",
        "public_name": "Milo Proprietario 801 Monteserrat"
    },
    {
        "phone_number": "+554898576214",
        "public_name": "AT 3M Mario Sizenando Cliente"
    },
    {
        "phone_number": "+5521998960491",
        "public_name": "Rui Proprietário Dom Pablo 301"
    },
    {
        "phone_number": "+555499121620",
        "public_name": "Ari Cliente Orbita"
    },
    {
        "phone_number": "+554195700005",
        "public_name": "Alessandro Proprietario Diamond Hill E Dolce Vita"
    },
    {
        "phone_number": "+554788278617",
        "public_name": "AT 1M- Giovani Cliente"
    },
    {
        "phone_number": "+554299220432",
        "public_name": "At 3.5m Eduardo Bacila Cliente"
    },
    {
        "phone_number": "+554691026590",
        "public_name": "Adegir Cliente Vendido"
    },
    {
        "phone_number": "+554791668555",
        "public_name": "Fernando Proprietario Via Felice"
    },
    {
        "phone_number": "+554174006395",
        "public_name": "At 2.5m Flávio Pretko Cliente"
    },
    {
        "phone_number": "+554791334067",
        "public_name": "AT 800K - Ricardo Cliente Investidor"
    },
    {
        "phone_number": "+554497171812",
        "public_name": "AT 500K - Ianco Cliente"
    },
    {
        "phone_number": "+554796197004",
        "public_name": "AT 800K - Marianne Cliente Casa"
    },
    {
        "phone_number": "+554792113661",
        "public_name": "At 2m Lara Arruda Cliente"
    },
    {
        "phone_number": "+554784112573",
        "public_name": "Joercir Cliente Bc"
    },
    {
        "phone_number": "+554884484481",
        "public_name": "Rodrigo Proprietário fusion"
    },
    {
        "phone_number": "+554288034557",
        "public_name": "AT 1.3M -Simone Cliente"
    },
    {
        "phone_number": "+554796527761",
        "public_name": "AT 1.6M João Andrietti Cliente"
    },
    {
        "phone_number": "+5511941115152",
        "public_name": "Fabricio Stagliano Cliente"
    },
    {
        "phone_number": "+555196078043",
        "public_name": "Eduardo Poletto Cliente Organica"
    },
    {
        "phone_number": "+554796586359",
        "public_name": "Guilherme Lucci Proprietario Ilha Do Sol 1101"
    },
    {
        "phone_number": "+554799613115",
        "public_name": "Liferson Nacimento Proprietario Sobrado"
    },
    {
        "phone_number": "+554799971228",
        "public_name": "At 1.3m Cibele Cliente"
    },
    {
        "phone_number": "+14075363596",
        "public_name": "Jeni Proprietario"
    },
    {
        "phone_number": "+554799972897",
        "public_name": "Ivan Cliente Investidor Bc"
    },
    {
        "phone_number": "+554799746527",
        "public_name": "Salustiano Proprietário Villa Serena 3203"
    },
    {
        "phone_number": "+554791434444",
        "public_name": "AT 1.3M -Rafael Lira Cliente"
    },
    {
        "phone_number": "+554888324928",
        "public_name": "Fernando Proprietario Maria Raquel 1901 Vendido"
    },
    {
        "phone_number": "+554191988700",
        "public_name": "Rogerio Proprietário Mirage 401 M2"
    },
    {
        "phone_number": "+554799870060",
        "public_name": "Carlos Sabino Proprietario Summer Beach 501 Frente Mar"
    },
    {
        "phone_number": "+554791445664",
        "public_name": "AT 1.6M- Ney Prado Cliente"
    },
    {
        "phone_number": "+554699723376",
        "public_name": "AT 2.5 M Fernando Cliente"
    },
    {
        "phone_number": "+554796067165",
        "public_name": "At 1.3m Rodrigo Vieitez Cliente"
    },
    {
        "phone_number": "+554199939104",
        "public_name": "AT 1M- Roberta Cliente Curitiba"
    },
    {
        "phone_number": "+554791183388",
        "public_name": "AT 1.3M Sonia Cliente"
    },
    {
        "phone_number": "+554799116651",
        "public_name": "Fernando Cliente Indicação Lair"
    },
    {
        "phone_number": "+554499116666",
        "public_name": "Nery Jose Proprietario Diamond Hill"
    },
    {
        "phone_number": "+554191333717",
        "public_name": "AT 1M- Maristela Cliente"
    },
    {
        "phone_number": "+554799320070",
        "public_name": "Doca Laurentino Cliente"
    },
    {
        "phone_number": "+554799853643",
        "public_name": "At 3.5m Victor Leduc Cliente"
    },
    {
        "phone_number": "+554185110422",
        "public_name": "AT 1.6M Fernanda Nunes Corrêa Cliente Mkt"
    },
    {
        "phone_number": "+554199636100",
        "public_name": "AT 1.3M -Horley Cordeiro Cliente"
    },
    {
        "phone_number": "+554799772662",
        "public_name": "Nercy Vargas Proprietário Dif. 701/702 Chateout Mont Martre"
    },
    {
        "phone_number": "+554796245030",
        "public_name": "AT 1.6M Fernando Quintas Cliente"
    },
    {
        "phone_number": "+554199150752",
        "public_name": "AT 800K - Livia Cliente"
    },
    {
        "phone_number": "+554791138974",
        "public_name": "Juliano Cliente Brusque"
    },
    {
        "phone_number": "+554799851633",
        "public_name": "Renato Proprietario Malaga 1501"
    },
    {
        "phone_number": "+555492065661",
        "public_name": "Mauricio Cliente Comprou"
    },
    {
        "phone_number": "+555196865996",
        "public_name": "Cíntia Cliente Mkt Boreal"
    },
    {
        "phone_number": "+556799815223",
        "public_name": "Jose Carlos Santin Proprietario Splendido"
    },
    {
        "phone_number": "+556199858363",
        "public_name": "AT 1.6M- Rogerio Cliente"
    },
    {
        "phone_number": "+554991661133",
        "public_name": "AT 500K - Sinval Cliente  Mkt Tem Sitio"
    },
    {
        "phone_number": "+554784982308",
        "public_name": "Marli Cliente Organica"
    },
    {
        "phone_number": "+556792591172",
        "public_name": "At 3.5m Elmo Fulioto Peres Cliente"
    },
    {
        "phone_number": "+554991200808",
        "public_name": "At 3.5m Domingos Scariot Cliente"
    },
    {
        "phone_number": "+554191170773",
        "public_name": "Vilmar Zapelini Cliente Curitiba"
    },
    {
        "phone_number": "+554191219295",
        "public_name": "Ivo Proprietário Grécia 401"
    },
    {
        "phone_number": "+554796776466",
        "public_name": "AT 500k Geo Cliente Trabalha Com A Mi"
    },
    {
        "phone_number": "+554797480458",
        "public_name": "AT 800K - Daniel Cliente"
    },
    {
        "phone_number": "+554191859990",
        "public_name": "Scheyla Ciruelos Cliente"
    },
    {
        "phone_number": "+554788051722",
        "public_name": "Carlos Proprietário Costa Atlantica 14"
    },
    {
        "phone_number": "+556699853480",
        "public_name": "Ricardo Cliente Sinop"
    },
    {
        "phone_number": "+555198480242",
        "public_name": "Fran Lima Cliente Orbita"
    },
    {
        "phone_number": "+554796340007",
        "public_name": "Sergio Proprietario Citta Di Vinci"
    },
    {
        "phone_number": "+554196846962",
        "public_name": "At 3M Otavio Moura Cliente"
    },
    {
        "phone_number": "+554796813924",
        "public_name": "Romildo Cliente Joinville"
    },
    {
        "phone_number": "+554796492853",
        "public_name": "At 4m Bruno Neves Cliente"
    },
    {
        "phone_number": "+554998061777",
        "public_name": "Youssef Proprietario Falcon 1002"
    },
    {
        "phone_number": "+554799189823",
        "public_name": "Roberto Proprietário Calil Elias 303"
    },
    {
        "phone_number": "+554792626969",
        "public_name": "Cyntia Cliente"
    },
    {
        "phone_number": "+554684027481",
        "public_name": "Djalmo Cliente Eberti"
    },
    {
        "phone_number": "+5511985888830",
        "public_name": "AT 500K - Nelson Santos Cliente SP"
    },
    {
        "phone_number": "+554191930601",
        "public_name": "AT 800k Marcia Ferreira Cliente"
    },
    {
        "phone_number": "+555499132949",
        "public_name": "Eder De Morais Rosa Cliente Mkt Boreal AT 2.0 "
    },
    {
        "phone_number": "+554699807549",
        "public_name": "At 3m Andrey Ribas Cliente"
    },
    {
        "phone_number": "+554799831963",
        "public_name": "Rodolfo Souza Proprietario Royal Tower 602"
    },
    {
        "phone_number": "+554796176814",
        "public_name": "AT 1.3M Nicolas Cliente"
    },
    {
        "phone_number": "+554291019060",
        "public_name": "At 1. 3 M Rosana Ganassoli Cliente"
    },
    {
        "phone_number": "+555591625356",
        "public_name": "Everton Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554799000000",
        "public_name": "AT 800K -Jenifer M Cliente"
    },
    {
        "phone_number": "+554792507711",
        "public_name": "AT 800K -Alexandre Cliente"
    },
    {
        "phone_number": "+554191743333",
        "public_name": "Veronica/João Proprietário Rainha Vitoria 401"
    },
    {
        "phone_number": "+554188432693",
        "public_name": "AT 4M- Ade Peixer Cliente"
    },
    {
        "phone_number": "+554791967007",
        "public_name": "EDUARDO FIGUEIREDO Proprietário Cobertura Magnifique"
    },
    {
        "phone_number": "+5521982034788",
        "public_name": "Luana Cliente RJ"
    },
    {
        "phone_number": "+555499187747",
        "public_name": "At 3.5m Luiz Henrique Ferronato Cliente"
    },
    {
        "phone_number": "+554891325758",
        "public_name": "AT 4m Roger Cliente Balneario"
    },
    {
        "phone_number": "+554799732808",
        "public_name": "AT 1.3 Tatiana Leier Cliente"
    },
    {
        "phone_number": "+554791313044",
        "public_name": "At 2m Silvia Helena Rezini Cliente"
    },
    {
        "phone_number": "+556584656617",
        "public_name": "AT 800K - Shirley Proença Cliente"
    },
    {
        "phone_number": "+554799838803",
        "public_name": "AT 3M Arnaldo De Campos Cliente"
    },
    {
        "phone_number": "+554796387231",
        "public_name": "AT 500K -Renata Cliente"
    },
    {
        "phone_number": "+554499317544",
        "public_name": "AT 1M- Edina Cliente - Casa\\Sobrado"
    },
    {
        "phone_number": "+556781513038",
        "public_name": "At 3.5m CMA Clinica Cliente"
    },
    {
        "phone_number": "+554799714944",
        "public_name": "At 5.5m Erlon Minella Cliente"
    },
    {
        "phone_number": "+5548920006866",
        "public_name": "Emerson Cliente Organica"
    },
    {
        "phone_number": "+554788128227",
        "public_name": "AT 1M- Claudinei Cliente  Praia Brava"
    },
    {
        "phone_number": "+555181895771",
        "public_name": "AT 1.3M -Mayara Zago Cliente"
    },
    {
        "phone_number": "+554999369877",
        "public_name": "At 1m Alda Ossani Cliente"
    },
    {
        "phone_number": "+554791871053",
        "public_name": "AT 3M Alexandre Francisco Cliente"
    },
    {
        "phone_number": "+554598208940",
        "public_name": "AT 1M-Jeferson Woicziekoski Cliente"
    },
    {
        "phone_number": "+554792566617",
        "public_name": "José Dallabrida Cliente Organica Blumenau"
    },
    {
        "phone_number": "+554196162835",
        "public_name": "Rogerio Proprietario Rivera 802 Frente Mar"
    },
    {
        "phone_number": "+554599760569",
        "public_name": "Fabi Cliente Organica"
    },
    {
        "phone_number": "+554188489727",
        "public_name": "Paulo Sergio Cliente Organica"
    },
    {
        "phone_number": "+554699359536",
        "public_name": "Junior Cliente Mkt Boreal"
    },
    {
        "phone_number": "+5512982197530",
        "public_name": "AT 800K Mister Ale Cliente"
    },
    {
        "phone_number": "+555499729709",
        "public_name": "Bianca Maciel Cliente Passo Fundo"
    },
    {
        "phone_number": "+554796210200",
        "public_name": "At 4m Cleiton Cliente"
    },
    {
        "phone_number": "+554788259846",
        "public_name": "Gym Lovers Cliente Praia Brava"
    },
    {
        "phone_number": "+555199858026",
        "public_name": "Sergio Damiani Cliente Poa"
    },
    {
        "phone_number": "+554499418604",
        "public_name": "Eduardo Cliente Permuta Maringa"
    },
    {
        "phone_number": "+554799215193",
        "public_name": "Gabriel Cliente MTS"
    },
    {
        "phone_number": "+554199872997",
        "public_name": "AT 2M -Vanderlei Correa Cliente Mkt"
    },
    {
        "phone_number": "+554388625932",
        "public_name": "Elias Menezes Cliente Organica"
    },
    {
        "phone_number": "+554999187585",
        "public_name": "Aristofolis Proprietario Torre De Lyon 3101"
    },
    {
        "phone_number": "+5517981336020",
        "public_name": "Juliano Proprietário Morada Do Sol"
    },
    {
        "phone_number": "+554991609121",
        "public_name": "Su Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554188211966",
        "public_name": "Vitor Proprietário Mar Azul Ap. 26"
    },
    {
        "phone_number": "+555481118024",
        "public_name": "AT 1M- Marcelo Tilin Cliente"
    },
    {
        "phone_number": "+554792616045",
        "public_name": "AT 1.6M Amanda Cliente"
    },
    {
        "phone_number": "+554791736336",
        "public_name": "AT 1.3M Adilson Carlos Cliente"
    },
    {
        "phone_number": "+555499746046",
        "public_name": "AT 500K - Laura Cliente Passo Fundo"
    },
    {
        "phone_number": "+554788099647",
        "public_name": "Paulo Proprietario Santana"
    },
    {
        "phone_number": "+554788356542",
        "public_name": "Wilmar Proprietario Jardim Atlantico 1001"
    },
    {
        "phone_number": "+554199763001",
        "public_name": "Alcione Proprietário Ap 40 Ed. Lady"
    },
    {
        "phone_number": "+554796614546",
        "public_name": "Proprietario Apartamento"
    },
    {
        "phone_number": "+554185063140",
        "public_name": "AT 6M- Rubia Silva Cliente"
    },
    {
        "phone_number": "+555491062290",
        "public_name": "Rossana Esposa Rogerio Cliente"
    },
    {
        "phone_number": "+554191357755",
        "public_name": "Altivo Cliente Organica"
    },
    {
        "phone_number": "+554591477771",
        "public_name": "At 3m Chadi El Khechen Cliente"
    },
    {
        "phone_number": "+554797571147",
        "public_name": "Wal Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799777588",
        "public_name": "Carine Proprietario Imperio 2501"
    },
    {
        "phone_number": "+554999227227",
        "public_name": "Francisco Proprietario Citta Di Vinci 1501"
    },
    {
        "phone_number": "+554599761445",
        "public_name": "Norlei Bongiolo Cliente Organica"
    },
    {
        "phone_number": "+554796366552",
        "public_name": "At 1.3M Marcos Vasconcelos Cliente"
    },
    {
        "phone_number": "+554999633713",
        "public_name": "AT 1M- Luiz Carlos Cliente"
    },
    {
        "phone_number": "+554792770016",
        "public_name": "Luis Carlos Proprietario Platinum 702"
    },
    {
        "phone_number": "+554399743377",
        "public_name": "At 3m Sandra Villa Cliente Londrina"
    },
    {
        "phone_number": "+554396297473",
        "public_name": "Josiele Cliente Organica"
    },
    {
        "phone_number": "+554799249781",
        "public_name": "AT 800K - Josiele Lopes Cliente Casa"
    },
    {
        "phone_number": "+554399848270",
        "public_name": "AT 800K - Alisson Cliente Arapongas Mkt"
    },
    {
        "phone_number": "+554388017835",
        "public_name": "AT 800K - Marcos Cliente"
    },
    {
        "phone_number": "+555195000259",
        "public_name": "At 3.5m Gilson Cliente"
    },
    {
        "phone_number": "+554499948717",
        "public_name": "At 1.3m Osni Cliente"
    },
    {
        "phone_number": "+554396162839",
        "public_name": "Vilmar Almeida De Araujo Cliente Eberti"
    },
    {
        "phone_number": "+554792768989",
        "public_name": "AT 2M Leandro Guimaraes Cliente"
    },
    {
        "phone_number": "+554891663234",
        "public_name": "Juliano Zeredo Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799169231",
        "public_name": "Paulo Proprietario Gran Torino 602/601"
    },
    {
        "phone_number": "+554799126499",
        "public_name": "Alexandro Proprietario Aconcagua 502"
    },
    {
        "phone_number": "+554799736660",
        "public_name": "Augir Proprietário Atlântis Frente Mar"
    },
    {
        "phone_number": "+554799270541",
        "public_name": "Atalavio Proprietário sobrado Bairro Municípios"
    },
    {
        "phone_number": "+554792265039",
        "public_name": "Rafael Romer Cliente Organica"
    },
    {
        "phone_number": "+554792768400",
        "public_name": "AT 800K - Jonatas Cliente - Casa"
    },
    {
        "phone_number": "+556999533844",
        "public_name": "Natanael Félix Cliente"
    },
    {
        "phone_number": "+554791173616",
        "public_name": "Batista Cliente Permuta"
    },
    {
        "phone_number": "+555193201007",
        "public_name": "Caroline Pesegoginski Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554999410798",
        "public_name": "AT 1M Guido Neuls Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799855967",
        "public_name": "At 1.6m Juarez Felix De Macedo Cliente"
    },
    {
        "phone_number": "+554188030029",
        "public_name": "Juliano Palmiro Proprietario Privilege 1402"
    },
    {
        "phone_number": "+554384072048",
        "public_name": "Jied Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555191619965",
        "public_name": "Tiárlei Cliente Orbita"
    },
    {
        "phone_number": "+554791973020",
        "public_name": "Marcelo Proprietário Terreno Camboriú"
    },
    {
        "phone_number": "+554784262988",
        "public_name": "AT 500K - Jose Cliente"
    },
    {
        "phone_number": "+554791678005",
        "public_name": "AT 1.6m Dany Cliente"
    },
    {
        "phone_number": "+554188026188",
        "public_name": "AT 2 M Luciane Correa Cliente"
    },
    {
        "phone_number": "+556699985120",
        "public_name": "Luiz Alberto P. Fattori Cliente Organica"
    },
    {
        "phone_number": "+554399145153",
        "public_name": "AT 800K -Joceyr Carvalho Guilherme Cliente- Casa"
    },
    {
        "phone_number": "+554796916900",
        "public_name": "Alexandra Proprietário majestic 901"
    },
    {
        "phone_number": "+554999642727",
        "public_name": "Aurelio Proprietario Dolce Vitta 2902"
    },
    {
        "phone_number": "+554599328088",
        "public_name": "Juliana Cliente Organica"
    },
    {
        "phone_number": "+555496698500",
        "public_name": "AT 500K - Patricia Cliente Olx"
    },
    {
        "phone_number": "+554191071489",
        "public_name": "Ney Proprietário Ed. Itajai 402"
    },
    {
        "phone_number": "+554797017611",
        "public_name": "AT 1M- Paty Cliente"
    },
    {
        "phone_number": "+557799718772",
        "public_name": "AT 3M Jean Baldissareella Cliente"
    },
    {
        "phone_number": "+554691039009",
        "public_name": "At 2.5m Rodrigo Galliazzi Cliente"
    },
    {
        "phone_number": "+554799737464",
        "public_name": "Silvio Cliente Tem Casa ITJ"
    },
    {
        "phone_number": "+554291661307",
        "public_name": "Cassiano Mielitz Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554796331164",
        "public_name": "AT 800K - Pauline Folador Cliente- Praia Brava"
    },
    {
        "phone_number": "+554899784885",
        "public_name": "AT 800k Liete Budni Cliente"
    },
    {
        "phone_number": "+554796026971",
        "public_name": "Cliente Meia Praia Tem Casa Quer Apt"
    },
    {
        "phone_number": "+554799128180",
        "public_name": "AT 800k Paulo Cesar Joenck Cliente"
    },
    {
        "phone_number": "+554799021103",
        "public_name": "Augusto Miranda Filho Cliente Serenity"
    },
    {
        "phone_number": "+554799219328",
        "public_name": "Rafaela Cliente Sunset"
    },
    {
        "phone_number": "+554991680605",
        "public_name": "AT 1M- Sandra Cliente"
    },
    {
        "phone_number": "+5518997171155",
        "public_name": "AT 1.6M- Fran Cliente"
    },
    {
        "phone_number": "+5511982673287",
        "public_name": "Marisa Cliente"
    },
    {
        "phone_number": "+554899627505",
        "public_name": "Sílvia Cliente Florianopolis mulher Do Paulo"
    },
    {
        "phone_number": "+554888362608",
        "public_name": "At 1.3m Samira Arruda Cliente"
    },
    {
        "phone_number": "+554199883712",
        "public_name": "AT 800K - Ari Cliente"
    },
    {
        "phone_number": "+554396065623",
        "public_name": "AT 500K - Remilton Prati Cliente"
    },
    {
        "phone_number": "+554791375515",
        "public_name": "Dalila Cliente"
    },
    {
        "phone_number": "+554799474455",
        "public_name": "Gustavo Proprietario Ed Daniela Dif"
    },
    {
        "phone_number": "+5524981153455",
        "public_name": "At 3m Jorge Cunha Cliente"
    },
    {
        "phone_number": "+554999922616",
        "public_name": "Sergio Campos Cliente Eberti"
    },
    {
        "phone_number": "+5511976203088",
        "public_name": "AT 2M Antonio Barbosa Cliente"
    },
    {
        "phone_number": "+556599871901",
        "public_name": "Ieda Cliente Tangara Fa Serra"
    },
    {
        "phone_number": "+554299378511",
        "public_name": "At 3.5m Vera Lucia Chagas Moura Cliente Ponta Grossa"
    },
    {
        "phone_number": "+554791051102",
        "public_name": "AT 800K - Flavio Cliente"
    },
    {
        "phone_number": "+555499112377",
        "public_name": "Laila Martins Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554792860636",
        "public_name": "Thais Venturi Cliente Filha Palmira"
    },
    {
        "phone_number": "+5511996391648",
        "public_name": "Raphael Figueiredo Proprietario Lumiere 3401"
    },
    {
        "phone_number": "+554399874494",
        "public_name": "AT 500K - Cris Zaparoli Cliente Mkt -Praia Brava"
    },
    {
        "phone_number": "+556699570418",
        "public_name": "AT 800k Luciano Fernandes Cliente Sorriso Parcelado"
    },
    {
        "phone_number": "+554797323500",
        "public_name": "AT 1.3m Glenio Cliente Comprou"
    },
    {
        "phone_number": "+554999920995",
        "public_name": "Bruno Proprietario Amores Da Brava 401"
    },
    {
        "phone_number": "+554799616368",
        "public_name": "George (Filho) Proprietário villa Serena 3203"
    },
    {
        "phone_number": "+554499278877",
        "public_name": "Lia Medici Cliente Mkt Boreal"
    },
    {
        "phone_number": "+556599871042",
        "public_name": "At 3.5m Danilo Lima Cliente"
    },
    {
        "phone_number": "+554299770649",
        "public_name": "AT 800K - Antonio Cliente  Parcelado"
    },
    {
        "phone_number": "+554799230380",
        "public_name": "Roberto Proprietario Quebec 102"
    },
    {
        "phone_number": "+554796172324",
        "public_name": "Caio Proprietario Uirapuru"
    },
    {
        "phone_number": "+554792883233",
        "public_name": "AT 1M-Dorateia Cliente"
    },
    {
        "phone_number": "+554797037081",
        "public_name": "Camila Cliente"
    },
    {
        "phone_number": "+554396607707",
        "public_name": "AT 800k Rodrigo Cliente Indicacao Leti"
    },
    {
        "phone_number": "+555491438310",
        "public_name": "Roberson Gambatto Cliente Mkt Frente Mar"
    },
    {
        "phone_number": "+554188532737",
        "public_name": "AT 800K -Ivanor Cliente"
    },
    {
        "phone_number": "+554796019296",
        "public_name": "Thiago Proprietario Casa Aririba"
    },
    {
        "phone_number": "+554788383769",
        "public_name": "At 6m Miranda Cliente"
    },
    {
        "phone_number": "+559192800083",
        "public_name": "Silvany Moura Cliente"
    },
    {
        "phone_number": "+554498383474",
        "public_name": "AT 2.5m Franciely Cliente"
    },
    {
        "phone_number": "+554188891429",
        "public_name": "Andrei Proprietário Frente Mar"
    },
    {
        "phone_number": "+555181483175",
        "public_name": "AT 1M- Guilherme Rabusky Cliente - Praia Brava"
    },
    {
        "phone_number": "+554185043508",
        "public_name": "AT 800K - Diego Oliveira Cliente - Casa"
    },
    {
        "phone_number": "+554192149266",
        "public_name": "AT 2M- Diego Cliente Curitiba"
    },
    {
        "phone_number": "+554199887569",
        "public_name": "Cleber Proprietario Maison Royale 202"
    },
    {
        "phone_number": "+554699298282",
        "public_name": "Marcia Faust Rosseto Cliente Aurora"
    },
    {
        "phone_number": "+556699327753",
        "public_name": "AT 800K - Gilberto Cliente"
    },
    {
        "phone_number": "+554799054234",
        "public_name": "Antonio Proprietario Cobertura 2001 Ilha Sul"
    },
    {
        "phone_number": "+554799810338",
        "public_name": "AT 1M-Daniel Cliente  Sobrado Praia Brava"
    },
    {
        "phone_number": "+554688280109",
        "public_name": "At 3m Geraldo Rodrigues Cliente"
    },
    {
        "phone_number": "+554799235945",
        "public_name": "AT 1.6M Olimpierri Mallmann Cliente"
    },
    {
        "phone_number": "+554797244180",
        "public_name": "AT 500K - Thiago Luis Cliente Investidor"
    },
    {
        "phone_number": "+554784487914",
        "public_name": "At 3.5m Beathriz Santos Cliente"
    },
    {
        "phone_number": "+554191531610",
        "public_name": "Ludwiggilson Proprietario"
    },
    {
        "phone_number": "+555599423270",
        "public_name": "AT 2M Elaine Cliente"
    },
    {
        "phone_number": "+555481590810",
        "public_name": "Katia Cliente Mkt Boreal"
    },
    {
        "phone_number": "+555491581730",
        "public_name": "At 4m Eunice Durante Rodolfo Cliente"
    },
    {
        "phone_number": "+554791922400",
        "public_name": "At 2.5m Luciane Fontelles Cliente"
    },
    {
        "phone_number": "+554796546905",
        "public_name": "AT 500K -Pri Wernke Cliente"
    },
    {
        "phone_number": "+556293914339",
        "public_name": "AT 800K - Nathalia Cliente Casa"
    },
    {
        "phone_number": "+554599715464",
        "public_name": "Gelson Moraes Clientes"
    },
    {
        "phone_number": "+554291254092",
        "public_name": "At 2.5m Fabio Vivian Cliente"
    },
    {
        "phone_number": "+554799408989",
        "public_name": "Luciano Cliente Investidor"
    },
    {
        "phone_number": "+5527998210312",
        "public_name": "Vinicius Bregensk Alves Cliente Italian"
    },
    {
        "phone_number": "+554885001691",
        "public_name": "William Silva Proprietario Discovery Sport"
    },
    {
        "phone_number": "+554791373455",
        "public_name": "Maria Camargi Cliente"
    },
    {
        "phone_number": "+554791179996",
        "public_name": "JA Sedrez Proprietario Carrara"
    },
    {
        "phone_number": "+554788293631",
        "public_name": "AT 3.5M- Joelma Silveira Cliente"
    },
    {
        "phone_number": "+559182985030",
        "public_name": "AT 500K - Nubia Cliente"
    },
    {
        "phone_number": "+554399149177",
        "public_name": "AT 1M- Suellen Cliente Mkt"
    },
    {
        "phone_number": "+557598801623",
        "public_name": "Gilmagno Cliente Brava Vision"
    },
    {
        "phone_number": "+554491517060",
        "public_name": "Vagner G Prado Cliente Italian"
    },
    {
        "phone_number": "+554784487353",
        "public_name": "Alex Fonseca Proprietario Sobrado 450k"
    },
    {
        "phone_number": "+554796215325",
        "public_name": "AT 500K - Thiago Cliente"
    },
    {
        "phone_number": "+554788021908",
        "public_name": "At 1m Diomar Carvalho Cliente"
    },
    {
        "phone_number": "+554799236084",
        "public_name": "AT 500K -Ticiane Elisa Mafra Cliente Mkt Praia Brava"
    },
    {
        "phone_number": "+554591397444",
        "public_name": "Rafael Lengler Proprietario Lumiere 3401"
    },
    {
        "phone_number": "+554799141736",
        "public_name": "AT 2.5M Peterson Oliveira Cliente"
    },
    {
        "phone_number": "+554899118900",
        "public_name": "Rafael Lengler Proprietario Lumiere 3401"
    },
    {
        "phone_number": "+559181268581",
        "public_name": "AT 1.3M -Marco Cliente Belém Investidor"
    },
    {
        "phone_number": "+554799834899",
        "public_name": "Leonardo Bononomi - Proprietario Villa Serena 1602"
    },
    {
        "phone_number": "+554299774013",
        "public_name": "At 3.5m Hilde Reinhofer Cliente"
    },
    {
        "phone_number": "+554799870800",
        "public_name": "AT 500K - Mara Pereira Cliente Mkt - Praia Brava"
    },
    {
        "phone_number": "+554396142273",
        "public_name": "AT 500K - Lilian Scholze Cliente"
    },
    {
        "phone_number": "+554796133290",
        "public_name": "Marlene Mulher Do Batista Cliente"
    },
    {
        "phone_number": "+554791255151",
        "public_name": "Celso Proprietario Torre De San Francisco"
    },
    {
        "phone_number": "+554899935432",
        "public_name": "AT 1.3k Daniel K. Cliente"
    },
    {
        "phone_number": "+554799021440",
        "public_name": "At 1.3m Aldo Gumz Jr Cliente"
    },
    {
        "phone_number": "+554791194664",
        "public_name": "AT 3M Vivian Coelho Cliente"
    },
    {
        "phone_number": "+5511955581978",
        "public_name": "Proprietario Splendia 2101 Rodrigo"
    },
    {
        "phone_number": "+553499711761",
        "public_name": "At 8.5m Ronaldo Cliente"
    },
    {
        "phone_number": "+554799151645",
        "public_name": "AT 1M- Ricardo Cliente Blumenau"
    },
    {
        "phone_number": "+555599635439",
        "public_name": "Claudio Amorim Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554799161094",
        "public_name": "AT 1M-Heraldo Cliente"
    },
    {
        "phone_number": "+554796407126",
        "public_name": "Oliveira Cliente Organica"
    },
    {
        "phone_number": "+554384040820",
        "public_name": "Marcelo Cliente Organica"
    },
    {
        "phone_number": "+554799729330",
        "public_name": "At 700k Denise Figueredo Gomes Cliente"
    },
    {
        "phone_number": "+554797681448",
        "public_name": "Gabriela Ramos Cliente Atmos"
    },
    {
        "phone_number": "+554196556480",
        "public_name": "AT 3M Andreia Campos Cliente"
    },
    {
        "phone_number": "+554796215001",
        "public_name": "AT 1.3M- Beto Cliente - Investidor"
    },
    {
        "phone_number": "+554784051123",
        "public_name": "Frank Cliente Jaragua Do Sul"
    },
    {
        "phone_number": "+554799752242",
        "public_name": "At 3.5m Leticia Cliente"
    },
    {
        "phone_number": "+554799117476",
        "public_name": "Giovana Proprietario Pablo Neruda"
    },
    {
        "phone_number": "+554499841662",
        "public_name": "Fabio Leal Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554788541515",
        "public_name": "3m Salvio Grah Cliente"
    },
    {
        "phone_number": "+554796245180",
        "public_name": "Aguinaldo Toso Cliente Casa"
    },
    {
        "phone_number": "+554198078288",
        "public_name": "Fatima Cliente Curitiba"
    },
    {
        "phone_number": "+554291187090",
        "public_name": "Alcidio Soares Proprietario Maragogy"
    },
    {
        "phone_number": "+554196018877",
        "public_name": "AT 1.3M Berenise Borsari Cliente"
    },
    {
        "phone_number": "+554598216138",
        "public_name": "AT 500k Barbara Souza Cliente"
    },
    {
        "phone_number": "+554192770103",
        "public_name": "Alison Andrei Cliente Investidor"
    },
    {
        "phone_number": "+554498747628",
        "public_name": "At 3.5m Marcelo Neis Cliente"
    },
    {
        "phone_number": "+554991264516",
        "public_name": "AT 800K - Maristella Cliente"
    },
    {
        "phone_number": "+554799948655",
        "public_name": "Luci Ou Marcelo Proprietario Costa Insolaratta 1101"
    },
    {
        "phone_number": "+556593157724",
        "public_name": "Lu Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554896785330",
        "public_name": "AT 3.5M Mario Kobus Cliente"
    },
    {
        "phone_number": "+554791692443",
        "public_name": "Laureci Cliente"
    },
    {
        "phone_number": "+554788467057",
        "public_name": "Thiago Machado Proprietario 1001"
    },
    {
        "phone_number": "+554192345299",
        "public_name": "AT 1M-Cleverson Cliente - Frente Mar"
    },
    {
        "phone_number": "+554599189969",
        "public_name": "Romindo Cliente Foz Do Iguaçu"
    },
    {
        "phone_number": "+554788035663",
        "public_name": "AT 1.6m Solange Bock Cliente"
    },
    {
        "phone_number": "+555197428139",
        "public_name": "Gustavo Borgomann Cliente Vendido"
    },
    {
        "phone_number": "+554896043083",
        "public_name": "AT 800K -Augusto Cliente"
    },
    {
        "phone_number": "+554799744578",
        "public_name": "Zaniolo Cliente Casa Tem Apt Como Permuta"
    },
    {
        "phone_number": "+555399790412",
        "public_name": "Ana Cliente Orbita"
    },
    {
        "phone_number": "+554796523402",
        "public_name": "AT 500K -Eliane Cliente"
    },
    {
        "phone_number": "+554192140474",
        "public_name": "Alex Mildenberger Cliente Italian"
    },
    {
        "phone_number": "+554196131567",
        "public_name": "Eliana Cliente Curitiba"
    },
    {
        "phone_number": "+554299140291",
        "public_name": "Mayrus Gomes Cliente"
    },
    {
        "phone_number": "+5493764350222",
        "public_name": "Augustin Cliente Argentina"
    },
    {
        "phone_number": "+5516997620303",
        "public_name": "Carlos Roberto Cliente Bc"
    },
    {
        "phone_number": "+554788319460",
        "public_name": "AT 2M Marlene Hetterich Cliente"
    },
    {
        "phone_number": "+554799460246",
        "public_name": "AT 800K - Tiago Cliente"
    },
    {
        "phone_number": "+555499320212",
        "public_name": "Osmar Busato Proprietario Monte Olympos 2003"
    },
    {
        "phone_number": "+5516981953344",
        "public_name": "Dini Cliente"
    },
    {
        "phone_number": "+555499848985",
        "public_name": "AT 500K -Scherly Endrizzi Cliente"
    },
    {
        "phone_number": "+554988522626",
        "public_name": "AT 500K - Lisete Cliente  Mkt"
    },
    {
        "phone_number": "+554799831925",
        "public_name": "AT 1.3M- Cezario Prado Cliente  Tem Permuta Em Gaspar"
    },
    {
        "phone_number": "+554797689996",
        "public_name": "AT 800k Zeli Balles De Melo Cliente Ate"
    },
    {
        "phone_number": "+554999295013",
        "public_name": "AT 500K - Marilda Cavalheri Cliente Mot"
    },
    {
        "phone_number": "+554191195511",
        "public_name": "AT 1M-Dulcio Cliente - Tem Permuta Em Itapema"
    },
    {
        "phone_number": "+554796966300",
        "public_name": "Rodrigo Pasqualotto Cliente Tem Permuta De Terreno"
    },
    {
        "phone_number": "+555496473585",
        "public_name": "Mi Zanella Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554797543923",
        "public_name": "Thalles Guilherme Proprietario Spazio Bianco"
    },
    {
        "phone_number": "+554199980636",
        "public_name": "Junior Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554899141437",
        "public_name": "Celso Cliente RS"
    },
    {
        "phone_number": "+554791959391",
        "public_name": "Ariel Proprietario Honorati"
    },
    {
        "phone_number": "+554896896035",
        "public_name": "AT 1M - Alessandro / Rita Chaves Cliente"
    },
    {
        "phone_number": "+554199147300",
        "public_name": "AT 2.5m Luciane Scariot Cliente"
    },
    {
        "phone_number": "+554899575795",
        "public_name": "Silvio Carlos Proprietario Cidade De Padua 1202"
    },
    {
        "phone_number": "+554199087614",
        "public_name": "AT 800K - Roberto Cliente Curitiba"
    },
    {
        "phone_number": "+554199700203",
        "public_name": "AT 1.6M Mesquita Cliente"
    },
    {
        "phone_number": "+554188621282",
        "public_name": "AT 1.3M- Cesar Kinaki Cliente"
    },
    {
        "phone_number": "+554599890854",
        "public_name": "Milton Cliente Cascavel"
    },
    {
        "phone_number": "+554799474511",
        "public_name": "AT 1.6M- Israel Cliente Proprietário Torremolinos 2202"
    },
    {
        "phone_number": "+554499640066",
        "public_name": "Matheus Gomiero Cliente Aurora"
    },
    {
        "phone_number": "+554187479379",
        "public_name": "At 3.5m Igor Alves Cliente"
    },
    {
        "phone_number": "+5521981720055",
        "public_name": "Luis Felipe Cliente Organica"
    },
    {
        "phone_number": "+5511988147063",
        "public_name": "AT 5M Rogui Cliente Proprietário Four Seasons"
    },
    {
        "phone_number": "+556196675346",
        "public_name": "At 6m Alexandre Baptista Cliente"
    },
    {
        "phone_number": "+555496198342",
        "public_name": "AT 500K - Gisele Cliente Pf -A Vista"
    },
    {
        "phone_number": "+554784545333",
        "public_name": "Silvana Proprietario Apt Balneario"
    },
    {
        "phone_number": "+554788706132",
        "public_name": "Lenon Santa Cliente Aurora"
    },
    {
        "phone_number": "+554797320003",
        "public_name": "AT 1M-Marcelo Cliente  Praia Brava"
    },
    {
        "phone_number": "+555199231300",
        "public_name": "At 500K Maytha Cliente"
    },
    {
        "phone_number": "+554796489763",
        "public_name": "Keli Cliente Loteamento"
    },
    {
        "phone_number": "+554799973134",
        "public_name": "Noryan Cliente Sobrado"
    },
    {
        "phone_number": "+554784716612",
        "public_name": "Eduardo Garlert Cliente"
    },
    {
        "phone_number": "+554792155301",
        "public_name": "Pedro Cliente Novo"
    },
    {
        "phone_number": "+5519996921126",
        "public_name": "AT 800K - Amanda Rubia Cliente -Casa"
    },
    {
        "phone_number": "+554188294280",
        "public_name": "Vitor Proprietário Mar Azul Ap. 26"
    },
    {
        "phone_number": "+554491757893",
        "public_name": "Leonardo Cliente Permuta Maringa"
    },
    {
        "phone_number": "+555491062838",
        "public_name": "At 3.5M Rogerio Cliente Erechim"
    },
    {
        "phone_number": "+554799120601",
        "public_name": "AT 3M Maria Zago Cliente"
    },
    {
        "phone_number": "+554291017086",
        "public_name": "Dario Proprietario Ilha Do Campeche 203"
    },
    {
        "phone_number": "+5519994989836",
        "public_name": "AT 1M- Rangel Cliente SP"
    },
    {
        "phone_number": "+554799888230",
        "public_name": "Toni Proprietário Rooftop"
    },
    {
        "phone_number": "+554799619078",
        "public_name": "AT 2.5 Lara De Souza Cliente"
    },
    {
        "phone_number": "+554792812500",
        "public_name": "AT 500K -Andreia Lopes Cliente"
    },
    {
        "phone_number": "+554599655157",
        "public_name": "AT 800K - Patrick Cliente"
    },
    {
        "phone_number": "+554784074142",
        "public_name": "Edson Cliente Indaial"
    },
    {
        "phone_number": "+554799710600",
        "public_name": "Roberto André De Sá Proprietário Porto Di Napoli E Serendipty"
    },
    {
        "phone_number": "+554799461018",
        "public_name": "AT 1M- Erick Cliente Mil Olx- Parcelado"
    },
    {
        "phone_number": "+554988326121",
        "public_name": "Carolina Baldissera Rosset Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554599185682",
        "public_name": "At 7m Elisa Sontagg Cliente"
    },
    {
        "phone_number": "+554791358111",
        "public_name": "AT 800K - Ailton Cliente"
    },
    {
        "phone_number": "+554197111334",
        "public_name": "Isabela Cliente"
    },
    {
        "phone_number": "+554796203000",
        "public_name": "AT 1M-Rafael Chiquetti Cliente"
    },
    {
        "phone_number": "+554797140022",
        "public_name": "At 1m Alecssandra Cliente"
    },
    {
        "phone_number": "+554988436017",
        "public_name": "AT 2M Gustavo Augusto Machado Cliente"
    },
    {
        "phone_number": "+558888210100",
        "public_name": "AT 2.5M Rodrigo Pasqualotto Cliente"
    },
    {
        "phone_number": "+554388131423",
        "public_name": "Raquel Pegoraro Cliente Brava Home"
    },
    {
        "phone_number": "+554791032639",
        "public_name": "At 1.6M Christian Cliente"
    },
    {
        "phone_number": "+554784445903",
        "public_name": "AT 2M Adriana Koch Cliente"
    },
    {
        "phone_number": "+555591641145",
        "public_name": "Edson Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554792221434",
        "public_name": "Ricardo Proprietario Altos Da Brava"
    },
    {
        "phone_number": "+555499232641",
        "public_name": "Gustavo Lucas Pereira Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554199671998",
        "public_name": "Marya Cliente Curitiba"
    },
    {
        "phone_number": "+554796509897",
        "public_name": "Henrique Testoni Cliente Casa Permuta"
    },
    {
        "phone_number": "+554198125004",
        "public_name": "AT 500K -Silvia Cliente Curitiba"
    },
    {
        "phone_number": "+554799654343",
        "public_name": "Cláudio Proprietario Permutante Fischer"
    },
    {
        "phone_number": "+554784047503",
        "public_name": "AT 1.3M -Joao Machado Cliente -Tem Permuta Em Itajai"
    },
    {
        "phone_number": "+554195669414",
        "public_name": "AT 1.3M -Isaura Costa Cliente"
    },
    {
        "phone_number": "+554784207571",
        "public_name": "Cliente Renato Bianchini Proprietario Terreno Perequê"
    },
    {
        "phone_number": "+554197886705",
        "public_name": "AT 1.3 Adilaine Dutra Cliente"
    },
    {
        "phone_number": "+554791222839",
        "public_name": "At 2m Lariane C. Da Silva Cliente"
    },
    {
        "phone_number": "+554891278885",
        "public_name": "Felipe Proprietário Acqua Del Mare 902"
    },
    {
        "phone_number": "+554184079650",
        "public_name": "Jair Bana Cliente Curitiba"
    },
    {
        "phone_number": "+554799837019",
        "public_name": "Odacio Proprietario Holambra 2101"
    },
    {
        "phone_number": "+554788442677",
        "public_name": "Iolanda Cliente Ranking"
    },
    {
        "phone_number": "+554599556175",
        "public_name": "AT 1M-Celio Cliente Praia Brava"
    },
    {
        "phone_number": "+554488354735",
        "public_name": "Wilson Proprietario Otto Schafer Frente 1001"
    },
    {
        "phone_number": "+554784048191",
        "public_name": "Frederico Cliente Joinville Ate 750 Mil"
    },
    {
        "phone_number": "+554891355193",
        "public_name": "AT 500K - Janio Jose Coelho Cliente Praia Brava Mkt"
    },
    {
        "phone_number": "+554792876060",
        "public_name": "AT 800k Irene Hajdesz Cliente"
    },
    {
        "phone_number": "+554399659150",
        "public_name": "At 3m Juliano Weigert Cliente"
    },
    {
        "phone_number": "+554796095485",
        "public_name": "Felipe Vasconcelos Proprietario BMW 2014"
    },
    {
        "phone_number": "+555591724415",
        "public_name": "Rosi Cliente Ijui"
    },
    {
        "phone_number": "+555499766602",
        "public_name": "AT 3M Vera Boff Cliente"
    },
    {
        "phone_number": "+554288125494",
        "public_name": "Carla Cliente"
    },
    {
        "phone_number": "+557181676253",
        "public_name": "Marcos Correia Proprietario Edgar Wegner 2001"
    },
    {
        "phone_number": "+554484059061",
        "public_name": "At 2m Noemia Caetano Cliente"
    },
    {
        "phone_number": "+554797017000",
        "public_name": "AT 1.3M -Julio Ganassin Cliente"
    },
    {
        "phone_number": "+554788483888",
        "public_name": "AT 2.5M- Valdir Lartzac Cliente Mkt"
    },
    {
        "phone_number": "+554791934333",
        "public_name": "At 2m Arthur Bassani Cliente"
    },
    {
        "phone_number": "+554788036271",
        "public_name": "At 5m Marcelo Gripa Cliente"
    },
    {
        "phone_number": "+554288204847",
        "public_name": "Allan M Gonçalves Cliente Perequê"
    },
    {
        "phone_number": "+554199987888",
        "public_name": "Augustinho Proprietário 2002 Privilege"
    },
    {
        "phone_number": "+554999797339",
        "public_name": "AT 500K - Cesar Signor Cliente Mkt - Praia Brava"
    },
    {
        "phone_number": "+554188968748",
        "public_name": "AT 800K - Super Drink Cliente - Casa"
    },
    {
        "phone_number": "+554488598604",
        "public_name": "Ro Paris Cliente"
    },
    {
        "phone_number": "+554799979343",
        "public_name": "Daniel Valerio Cliente Vendido"
    },
    {
        "phone_number": "+554796148716",
        "public_name": "AT 2M Priscila Cliente"
    },
    {
        "phone_number": "+556696249069",
        "public_name": "Josi Cliente Mkt Boreal"
    },
    {
        "phone_number": "+554196182611",
        "public_name": "AT 1M- Jair Cliente"
    },
    {
        "phone_number": "+554499199696",
        "public_name": "Ricardo Hungaro Filho Cliente Organica"
    },
    {
        "phone_number": "+557799741128",
        "public_name": "Thalita Gaban Cliente Organica"
    },
    {
        "phone_number": "+556281281818",
        "public_name": "AT 1.6M- Leonardo Cliente Goiania"
    },
    {
        "phone_number": "+554191892330",
        "public_name": "At 3.5m Bruno Zanini Cliente"
    },
    {
        "phone_number": "+554195193333",
        "public_name": "Joselito Cliente Curitiba"
    },
    {
        "phone_number": "+554791427284",
        "public_name": "AT 2.5m Anne Schmidt Cliente"
    },
    {
        "phone_number": "+554899836592",
        "public_name": "3.5m Paulo Cesar Cordeiro Cliente"
    },
    {
        "phone_number": "+554988321617",
        "public_name": "AT 1M- Allan Feliciani Cliente"
    },
    {
        "phone_number": "+554498981510",
        "public_name": "Leonardo Pasqualli Cliente Orbita"
    },
    {
        "phone_number": "+555499594599",
        "public_name": "AT 1 M Sander Cliente"
    },
    {
        "phone_number": "+554799149285",
        "public_name": "AT 800K - Jair Cliente Casa"
    },
    {
        "phone_number": "+5491141466029",
        "public_name": "Franklin Cliente Buenos Aires"
    },
    {
        "phone_number": "+554184115059",
        "public_name": "Mariana Tomitão Cresto Cliente Admirá"
    },
    {
        "phone_number": "+554399054395",
        "public_name": "Sandra Cliente Orbita"
    },
    {
        "phone_number": "+554797192065",
        "public_name": "Arthur Cliente Organica"
    },
    {
        "phone_number": "+554999295655",
        "public_name": "Adilson Cliente"
    },
    {
        "phone_number": "+554791374807",
        "public_name": "AT 500K - Marcus Vinicius Martim Cliente  Praia Brava"
    },
    {
        "phone_number": "+554899706681",
        "public_name": "Jean Proprietário Fusion"
    },
    {
        "phone_number": "+554791551070",
        "public_name": "At 3.5m Simone Cliente"
    },
    {
        "phone_number": "+554196716240",
        "public_name": "Eduardo Proprietario Palm Beach 2101"
    },
    {
        "phone_number": "+554599124989",
        "public_name": "AT 500K -John Liaw Cliente  Praia Mkt"
    },
    {
        "phone_number": "+554784320383",
        "public_name": "AT 1.6M Fredemar Schmitt Cliente"
    },
    {
        "phone_number": "+555481117633",
        "public_name": "Marcia Cliente Marau"
    },
    {
        "phone_number": "+556592198465",
        "public_name": "AT 2.5M- Lourival Cliente Mkt"
    },
    {
        "phone_number": "+554797408081",
        "public_name": "Gislene Cliente Brava Beach"
    },
    {
        "phone_number": "+554792793131",
        "public_name": "AT 5M André Miranda Cliente"
    },
    {
        "phone_number": "+554792934408",
        "public_name": "Allamo Cliente Serenity"
    },
    {
        "phone_number": "+554184461177",
        "public_name": "Ingrid Proprietário Lago Maggiore 91"
    },
    {
        "phone_number": "+554788094540",
        "public_name": "Nildo Cliente Brusque Mega Motos"
    },
    {
        "phone_number": "+555499657354",
        "public_name": "At 600k Roselene Paludo Cliente"
    },
    {
        "phone_number": "+554999786977",
        "public_name": "AT 1M- Nelci Cliente"
    },
    {
        "phone_number": "+554796022448",
        "public_name": "Fernando Proprietário Casa Condominio"
    },
    {
        "phone_number": "+554198042880",
        "public_name": "Ricardo Lourenço Cliente Hyde"
    }
];

// Função para limpar o nome
function cleanName(publicName) {
    return publicName
    .replace(/\bmil\b/gi, '') // Remove "mil" ou "Mil" quando estiver sozinha
    .replace(/AT\s?\d+\.?\d*\s?[KM]?-?/gi, '') // Remove "AT 2M", "AT 800K", etc.
        .replace(/-/g, '') // Remove qualquer "-"
        .replace(/\./g, '') // Remove qualquer "."
        .replace(/\bat\b/gi, '') // Remove "mil" ou "Mil" quando estiver sozinha
        .replace(/\b\d+\b/g, '')
        .replace(/\b[a-zA-Z]\b(?![áéíóúàèìòùâêîôûäëïöüç])\s*/g, '')// Remove "mil" ou "Mil" quando estiver sozinha
        .replace(/Cliente/gi, '') // Remove "Cliente"
        .replace(/\b\d+(\.\d+)?m\b/gi, '') // Remove números no formato "3.5m", "99.0m", "1m", "8.8m"
        .trim() // Remove espaços extras
        .split(' ')[0]; // Pega somente o primeiro nome
}


const cleanedContacts = contacts.map(contact => ({
    phone_number: contact.phone_number,
    public_name: cleanName(contact.public_name)
}));

function filterInvalidNames(contacts) {
    return contacts.filter(contact => {
        const name = contact.public_name;
        // Regex que permite letras (com acentos), espaços e nega símbolos indesejados
        return /[^a-zA-ZÀ-ÖØ-öø-ÿ\s]/.test(name) || name.length <= 2;
    }).map(contact => [contact.public_name, contact.phone_number]);
}

const fileContent = `const cleanedContacts = ${JSON.stringify(cleanedContacts, null, 4)};\n\nconsole.log(cleanedContacts);`;

fs.writeFileSync('cleaned-contacts.js', fileContent, 'utf8');

console.log(filterInvalidNames(cleanedContacts));
console.log(filterInvalidNames(cleanedContacts).length);
// console.log(filterInvalidNames(cleanedContacts));
