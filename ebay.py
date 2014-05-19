__author__ = 'Jason Crockett'

#username = ""
#password = ""
#authtoken = ""

#from ebaysdk import trading
from ebaysdk.trading import Connection as trading


class EbayUser:
    DevID = 'f48a5c13-dca0-4077-8295-006421d6ed3b'
    AppID = 'MrJasonA-67c2-4711-b4a2-51b534432c67'
    CertID = 'a1ebd7a4-24e4-4a41-b657-03d450fd1fbc'
    AuthToken = 'AgAAAA**AQAAAA**aAAAAA**kRRwUw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wHlYCkD5ODpQmdj6x9nY+seQ**CDoCAA**AAMAAA**BnUgP+TiXiFomd95vhkK0lO5RG9Iid3z+wxS7+vlI1KocnCdjJvsndQLKW0tAPUmtx+0soDNFu5H1RHMTn3IsFquf++DHASQh6rVB8UsXpjeVxgORI4jfykHbnMlo3BKtBhaqNxA5tA7ZyZCpH7D5Isk/JxJ9Ijrr5wZZgoKcM5EX17X0NDKKBo6450LwN22/9P/GGKdnLOW58SxAQhw1ycANgaB0DWtPVLCjo1C+o9zfG3iwQrUGp0jTsCNtuzv7XZfOrPr75P7ReUhZVotUfpj+waBDRD9+P+LMPJ+Qf3xfuIjK6hrTPUp5XCQ6KIgCP6eKUvPQU81wJM/icB++zov7w+i6Vj4HAYViDlcGhUpf3R+EZOL25epQfaModou3I/tu5Ut5dMDbTrgOzElCNqD8OUS7tF/viACe+fvALhB6FmKcNpWPT23tdTqP/OzF1Db/OoWZ14sVIA8JikgIj8IJfeErDYdA4ZV5bENFEOFeZmLEXmei/pSSooNniwnX0N5BJdVTzBf0ewn4Un3b6ldQvY+uOX6nznQ17ZwX2eVWwS+Tnvixn/jr8uFCnGaJMeIAMfx/Og4PGG5La7E6igCKrdomvUX9wjeScqGLdKs4HHjuZVJ9Pptp1kP8zW46T361D2JIFsP8sKyfOpWgdVqPGK1ZEz6z9KSEQezcPuQ6bHsJZdV4fXWFP/kJBNfS/Dh7HOXAWrHsQP0xqtK2npDuCVyDSzPDPrp834LzFPh+v+Fm4jXJdx4YpKzlWaB'

    def setAsSandboxUser(self):
        self.DevID = 'f48a5c13-dca0-4077-8295-006421d6ed3b'
        self.AppID = 'MrJasonA-67c2-4711-b4a2-51b534432c67'
        self.CertID = 'a1ebd7a4-24e4-4a41-b657-03d450fd1fbc'
        self.AuthToken = 'AgAAAA**AQAAAA**aAAAAA**kRRwUw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wHlYCkD5ODpQmdj6x9nY+seQ**CDoCAA**AAMAAA**BnUgP+TiXiFomd95vhkK0lO5RG9Iid3z+wxS7+vlI1KocnCdjJvsndQLKW0tAPUmtx+0soDNFu5H1RHMTn3IsFquf++DHASQh6rVB8UsXpjeVxgORI4jfykHbnMlo3BKtBhaqNxA5tA7ZyZCpH7D5Isk/JxJ9Ijrr5wZZgoKcM5EX17X0NDKKBo6450LwN22/9P/GGKdnLOW58SxAQhw1ycANgaB0DWtPVLCjo1C+o9zfG3iwQrUGp0jTsCNtuzv7XZfOrPr75P7ReUhZVotUfpj+waBDRD9+P+LMPJ+Qf3xfuIjK6hrTPUp5XCQ6KIgCP6eKUvPQU81wJM/icB++zov7w+i6Vj4HAYViDlcGhUpf3R+EZOL25epQfaModou3I/tu5Ut5dMDbTrgOzElCNqD8OUS7tF/viACe+fvALhB6FmKcNpWPT23tdTqP/OzF1Db/OoWZ14sVIA8JikgIj8IJfeErDYdA4ZV5bENFEOFeZmLEXmei/pSSooNniwnX0N5BJdVTzBf0ewn4Un3b6ldQvY+uOX6nznQ17ZwX2eVWwS+Tnvixn/jr8uFCnGaJMeIAMfx/Og4PGG5La7E6igCKrdomvUX9wjeScqGLdKs4HHjuZVJ9Pptp1kP8zW46T361D2JIFsP8sKyfOpWgdVqPGK1ZEz6z9KSEQezcPuQ6bHsJZdV4fXWFP/kJBNfS/Dh7HOXAWrHsQP0xqtK2npDuCVyDSzPDPrp834LzFPh+v+Fm4jXJdx4YpKzlWaB'

    def getUserInfo(self):
        api = trading(appid=self.AppID, devid=self.DevID, certid=self.CertID, token=self.AuthToken)
        api.execute('GetUser', {})
        print api.response_dict()
        return api.response_dict()


class ItemsForSale(EbayUser):
    DevID = EbayUser.DevID
    AppID = EbayUser.AppID
    CertID = EbayUser.CertID
    AuthToken = EbayUser.CertID

    def getDict(self, Verbose=False):
        api = trading(appid=self.AppID, devid=self.DevID, certid=self.CertID, token=self.AuthToken)
        api.execute('GetMyeBaySelling', {})
        if Verbose:
            print api.response_dict()
        return api.response_dict()

    def getJson(self, Verbose=False):
        api = trading(appid=self.AppID, devid=self.DevID, certid=self.CertID, token=self.AuthToken)
        api.execute('GetMyeBaySelling', {})
        if Verbose:
            print api.response_json()
        return api.response_json()

    def getObjects(self, Verbose=False):
        api = trading(appid=self.AppID, devid=self.DevID, certid=self.CertID, token=self.AuthToken)
        api.execute('GetMyeBaySelling', {})
        if Verbose:
            print api.response_obj()
        return api.response_obj()

    def getItemDict(self,ItemName):
        Inventory = self.getJson()
        Item = Inventory[ItemName]
        return Item

    def getItemNames(self):
        Inventory = self.getJson()




class EbayItem(ItemsForSale):
    ItemsForSale



##getItemsForSale(DevID,AppID,CertID,AuthToken)
print(len(AuthToken))