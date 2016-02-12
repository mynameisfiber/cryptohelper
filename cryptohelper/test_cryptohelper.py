from . import cryptohelper as ch
import random
import string

def test_import_export():
    share_threshold = 2
    # generate a random passphrase and split it into shares
    passphrase = ch.generate_passphrase(6)
    shares = ch.split_passphrase(passphrase, share_threshold=share_threshold,
                                 num_shares=3)

    # generate public/private keys with passphrase and encrypt some data
    pub, priv = ch.create_keypair(passphrase=passphrase, length=1024)
    pubkey = ch.import_key(pub)
    data = "".join(random.choice(string.ascii_letters) for _ in range(2))
    enc_data = ch.encrypt_blob(pubkey, data)

    # recover passphrase using a subset of the shares and import priv key
    share_partial = random.sample(shares, share_threshold)
    rec_passphrase = ch.recover_passphrase(share_partial)

    # load priv key using the recovered passphrase and decrypt the data
    privkey = ch.import_key(priv, rec_passphrase)
    rec_data = ch.decrypt_blob(privkey, enc_data)

    assert(data == rec_data)



