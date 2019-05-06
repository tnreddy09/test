from simplecrypt import encrypt, decrypt

### Mongo Constants
class Constants():
    def __init__(self, decrypt_key):
        self.decryption_key = decrypt_key
        decrypted_string = self.decrypt_credentials()
        values_list = decrypted_string.split(' ')
        self.mongo_username = values_list[0]
        self.mongo_password = values_list[1]
        self.mongo_external_ip = values_list[2]
        self.mongo_db_name = values_list[3]
        self.mongo_tweets_collection_name = values_list[4]
        self.mongo_stocks_collection_name = values_list[5]
        self.kibanalogger = values_list[6]


    def decrypt_credentials(self):
        return decrypt(self.decryption_key,
                       b'sc\x00\x02}d\x7f\x00\xc6R\x17~\x9f\x87\xe4\xd8l\x07\xdbT6\xdcX\x8eq\xc0\xf4Y\x00\x93\xd2\x06\\\xe2k\x93s.\x01\xae\xaem\x9b]\xb18\x05i\x11\x96\xa3#\xdd\xc1H3\x90Y\xfdoI\xf6\x188Wu\xa6\x90\xbe\x99s\xcb\xfc\x11\x9am\xae\x14\x10\x91\x0b#"\xe1d7\xf3b\xc1\x13\x8e\xec\x17\x9c\xbf\xa8\xae<\xbf\x18\x96\xc2n\xc6\xd9\xf0\x92\xf0\xfd\x96\x80\xf2\x06\x07\xf1\x08_\x89v\xd3\xb3\xa2\xef\x19\xf7z)\x0b\xffM9\xa23@\x0fJ\x15\x8d\x0b\xaa'
                       ).decode('utf-8')


if __name__ == "__main__":
    constants = Constants('Wrong Password')
    print('yes')