from models.saskaita import Saskaita

saskaita = Saskaita()

while True:
    veiksmas = int(input("1 - peržiūrėti, 2 - pridėti pajamas, 3 - pridėti išlaidas, 4 - balansas, 0 - išeiti: "))
    match veiksmas:
        case 1:
            print(saskaita.zurnalas)
        case 2:
            saskaita.prideti_pajamas()
        case 3:
            saskaita.prideti_islaidas()
        case 4:
            saskaita.paskaiciuoti_balansa()
        case 0:
            break

