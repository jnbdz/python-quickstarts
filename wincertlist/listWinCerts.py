import wincertstore

f = open("wincert.cer", "w")

for storename in ("CA", "ROOT"):
        with wincertstore.CertSystemStore(storename) as store:
                for cert in store.itercerts(usage=wincertstore.SERVER_AUTH):
                        f.write(cert.get_name())
                        f.write("\n")
                        f.write(cert.get_pem())

f.close()
