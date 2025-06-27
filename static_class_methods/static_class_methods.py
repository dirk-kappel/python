class LuxuryWatch:
    __watches_created = 0

    def __init__(self, engraving=""):
        LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_watches_created(cls):
        return f"Number of watches created {cls.__watches_created}"

    @staticmethod
    def engrave_watch(engraving):
        if len(engraving) <= 40 and engraving.isalnum():
            return True
        raise Exception

engravings = ["test","test2","test*^&^#$*"]
for i in engravings:
    try:
        LuxuryWatch.engrave_watch(i)
        print("We can use",i,"to create an engraving")
    except:
        print("bad engraving",i)

a=LuxuryWatch("test")
b=LuxuryWatch("test2")

print(LuxuryWatch.get_number_watches_created())
