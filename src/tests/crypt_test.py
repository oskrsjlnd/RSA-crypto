# pylint: skip-file
import unittest
from src.crypto import Crypt

class TestCrypt(unittest.TestCase):
    def setUp(self):
        self.crypt = Crypt()
        self.private_key = (59991223314036227864103898334420920341302788766379149242078352396448848446541115225267485475174364270513300770431749186690142211394437971455062652098275571782053568415336097647433990207539737593087182929549937868200186533248541240717471133426949616132974470945643680881251539051116517015103169367127836835949, 5978343217784924610227238964586463078094031057772284720081995201202487590282741406170895030873609915783791863095499548930731018853732615035369549733033822942252570678069995450812400462799983666275982020042166961404238617763676301821465331341944756060824150373697743974725790946855252170072888747481640089941)
        self.public_key = (59991223314036227864103898334420920341302788766379149242078352396448848446541115225267485475174364270513300770431749186690142211394437971455062652098275571782053568415336097647433990207539737593087182929549937868200186533248541240717471133426949616132974470945643680881251539051116517015103169367127836835949, 65537)
        self.string_array = ['bmxkioprrxlmlyhvspelxhsazisqpzlxorunqfgzgstlsrdzbsl',
        'gwqnaxugwbepxrdoywpasilgjtxlxxfxmltpynotmatvrsmjqtgfogvklbbatk',
        'iibakalrehgdmrdlipqjgtdtlpdojwienoumzyrhivmrrrq',
        'elyszxjaekaquspblxrjinsfauanmfaywusvvnzyicrwjlgxtxnbwwypjbdoohnssoocfasd',
        'zcybfeewkvethjmcriddlpixxnhuas',
        'psljkncbjokwzqfwzjrzvefeaapvwcbhivdntbrftmr',
        'wlvugqfpylwpedxrarpsweymyobnstgozmfiqzoztxthhsvswlpulxobwxuarqyxhgvanbenzusukzqxbssultflgtyrqcaevoeqkkixeuqhivdwusnak',
        'nnkkaichxzkfshqruqlrejlttajzvtpoofqfftmrxfuhwnwwytbdkwvlbkuzofafashjgwomnawa',
        'zgdvzgrywxnxrkddsvvjfvhjvqtjmnskuloknfldthlhgcifhkykzeathc',
        'uitnowovfzjgzwtybbeglckcnaxoshikjqqjesvvanmdstcwxfhgijgkgtalgxvyegcoyuzogfthftumqhnzfknrzzagmrtbdnlhwaprjqayrvkygsicifoj',
        'omoqzjoidtdtmksbwysrtxhoklajyvsjpjufujmjmtsihdumowkovujbkeppofvzwzqxjtfv',
        'piycbqwneahvelwpdjxhqeiaxwkljkcriiqfitqdtlckuncfvfivdvjswtvdtkkknohfhkcnrofjogcggultaejjjyktsackfrfcsaydxfrnntdpnftbs',
        'jmpwszgbwpjfhbmmjfjcxjwxgmbnamdln',
        'ipcfeewqzzovdbrtkkxzdaknlmehkkzlxekfyocfofikpwilpyzfcxivletzcloimofak',
        'kqxattgaydqpifnzgvjnbkrzibteojrkjyasgnfdsfuqltafjdczptlyzyntcjhtrhebyowgqhgojgzbwjfqs',
        'tbdiggznxgeflvcjspphtkpygusbgvpfazovleqttchguxlijmgjxxnzzeamenimcqpkynxfcxpdoxkdyod',
        'kqrdejthnnxkukvafcqiufymmkpfazebqsmyeinqzurhjdgdwheokpwapocxxpdylubpfpceqnrjfdzvzkelrmt',
        'whvkrmrflybseawoxmctqlufuocxyeqxhxjdwdlvkqbbhouyxciln',
        'gztskmhpiaaxhrhukeooucmocwvtvruoxgbvantuwkknldwgjai',
        'hmoyjvhytabpjwwiylknhkhumzfqwxlfcacnjgrqqzwklopkkhiwepe',
        'RPQDTCNHUYSKIHBNMYTAAYMYIWRVZMOCLCRRTMTBCHEBSLFWADSVGHSLBTROJKBOOIFVKUILAOGVSZQVFZWLXJNXTBJIYBFHZUCSHPKPVSEANRHPSD',
        'XKOCXIHFCFWQEAWLUXVRHEOPYJIHUHFWBAHWUZRPZYDJOBZTIOKENANFUQGNIBMPSYHVBZDTDJIVEJKUKLZTTXAPJLBATIFDMGLUICMQYHQUULNNUJFMEVTT',
        'AGDJOEBDRQHDHVHPDRXQUXIHMHVQKNUSXRBMOTPOYMHEYAOTVZLXTNSLNKBQDZDUNVVTDHDYZJEMLNQNGAFKPSECM',
        'RJBMZBDPOFKOZIAZTKBOQMVSWICLVKFQAJWOLJYHZMPQXVSFPETINXQLHYITCSEQWKVBANMFINGJIOWQFTZPNTBMHAXWAEW',
        'OFQOIKSDZHRFRZLBEXRRJKVSGZOTMTIXYUIYJBDIATDMGKJJSBIUCMRKBSKBHJNZDKKEBMVYJRVABSSAXABUMATACZFXONXHXPPNKPLPNBDVV',
        'GYJFPUIRQGCMKYBHKARAEKBOIXOVJSNLTCLXVOAHXPUKEZFEHHMECURJLEUULNREZICKNYXI',
        'LUXSAQYQVHYFAHPJSVDIRWEOWIOEBUOCIMZNSHCIXSTSGXXIDKTPSXVFWCFBHOUEICDTLELMIDNVQVXQIOSHLETZIDFODXRSSUAXHRYLTSWZRQ',
        'RJXZWYJZMBXQUUXFZXZBJFHCMHSNNRWMNPBGAETGLSABBCFBZIYOPYVCAATSECVVFDWUBHHHWAAWPDEURIKVVWRGWWEIGVHLOKDGFHUDB', 
        'OVFBHSVZBIXGLZOSLCDANQHFRNOIJHRWAHQSQMYWYAFWSNMSVTLRNNXTBOGQAIAYLDCR', 
        'YMVWLBCAFAOOXJQNHQMLCIIBYZSZIXTJSFQZMSSRYOEZINPVZGPJIDAKJAOOGRXLIFWSUCJUPLABIHMMHDVJUJEPTGVAHXGGQVKSZRMMDSSVGPLK',
        '03215077996814872876736940837334372921901338189047366153392637213608492659157097529340424405276',
        '5452958578345446499170716590468076411271864426882816319443244466196372132308666265937397892267008834179023890566165',
        '577607550367324518706322329764503911687290175598597786858899312504634031944966857721782330799370155599849602456588',
        '82656052723254303662569190218091094403648581257854528910702992777946442485081608589721',
        '7266280284840299303343713129853734653940877275875080682277741673225900719',
        '012158290258851351188629213088440196840041609483285845001964467523162401138432584334752111809372058659224462854',
        '543739471082770461810530965737837956404230446052126881702',
        '867383232076861052647848397698595639631050',
        '85466732704524324342713967721352988',
        '60373465991730050345913640972664198',
        '"#=)="(!=¤()=!(¤=!"(¤=)#%?!"=?"%/!?#%140+',
        '}]@$\@]$\]@$]}\£$]\$]€@€[',
        '}\£]€]€}\@€]\$}]£‚£‚@$]@$\]£€}\$]}[}',
        '&/!"¤&!"(%=)=#!\]$}$\]$^^^^`**.;,.:;|<<|>><']

    def test_str_conversion_to_int_works(self):
        result = self.crypt.str_to_int("This is a test")
        self.assertIsInstance(result, int)

    def test_encrypted_message_is_not_plaintext(self):
        plaintext = """Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, 
        consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. 
        Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet."""
        int_ptext = self.crypt.str_to_int(plaintext)
        cipher = self.crypt.encrypt_message(plaintext, self.public_key)
        ciphertext = cipher[0]
        self.assertNotEqual(ciphertext, int_ptext)

    def test_message_decrypted_right_priv_key_match_original_plaintext(self):
        plaintext = """alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku
        12alkuluku12alkuluku12alkuluk"""
        cipher = self.crypt.encrypt_message(plaintext, self.public_key)
        decrypted_message = self.crypt.decrypt_message(cipher, self.private_key)
        self.assertEqual(plaintext, decrypted_message)

    def test_message_encryption_returns_encrypted_msg_and_size(self):
        for msg in self.string_array:
            cipher = self.crypt.encrypt_message(msg, self.public_key)
            self.assertIsNotNone(cipher)
        
    def test_decrypted_message_equal_to_original(self):
        originals = self.string_array

        list_of_encrypted = []
        for message in originals:
            list_of_encrypted.append(self.crypt.encrypt_message(message, self.public_key))
        
        list_of_decrypted = []
        for encrypted in list_of_encrypted:
            list_of_decrypted.append(self.crypt.decrypt_message(encrypted, self.private_key))
        
        for i in range(len(originals)):
            self.assertEqual(originals[i], list_of_decrypted[i])

    def test_message_decrypted_wrong_private_key_not_matching_original(self):
        plaintext = """alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku12alkuluku
        12alkuluku12alkuluku12"""
        cipher = self.crypt.encrypt_message(plaintext, self.public_key)

        self.wrong_private_key = (self.private_key[0]-1, self.private_key[1])
        decrypted_message = self.crypt.decrypt_message(cipher, self.wrong_private_key)
        self.assertNotEqual(plaintext, decrypted_message)
