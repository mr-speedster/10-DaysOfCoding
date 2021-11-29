def main():
    def firstTest():
        test="First Test"
    def secondTest():
        nonlocal test #just ithil poointer vekkumbol thanne nammakk kanam ath main functionil athayath current functionu veliyile test aan enn athine nonlocal vech akath access akki
        test="Second Test"
    def ThirdTest():
        global test #ithine nammakk main methodinte veliyil vare access akkam
        test="Third Test"
    test="Null"
    print(test)#ippo nammal main functionil declare akkiyath mathram work akum
    firstTest()
    print(test)#ivide nammal kodutha null value olla test thanne work akum becouse aa functionile variabline ath badhichattilla
    secondTest()
    print(test)#ivide nammal kodutha test=null enn variabline nonlocal vech access akkiyatt athile new value koduthu so new value print aayi
    ThirdTest()
    print(test)#ivide current aayitt ulla value thanne print aayi karanam global variable main functionu veliyil aan access akkunne

main()
print(test)