import gpgme

from minitrue.prompt import ask, say, yes_no


class Gpg:
    def __init__(self):
        self.context = gpgme.Context()
        self.__choose_key()

    def __choose_key(self):
        for key in self.context.keylist(
                ask("Which key should we search for?")):
            user = key.uids[0]
            if key.can_encrypt & key.can_sign & key.can_certify:
                say("Keys for %s (%s): %s" %
                    (user.name, user.email, key.subkeys[0].fpr))
                if yes_no("Is this the key you want to use?"):
                    say("imported")
                else:
                    say("messed up")
