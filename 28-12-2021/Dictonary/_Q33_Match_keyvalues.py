#Match key values in two dictionaries.

class Match:
    def match_keys(self):
        aa = {'a': 1, 'c': 3, 'b': 2}
        bb = {'a': 1, 'b': 2}
        for k in aa:
            if k in bb:
                if aa[k] == bb[k]:
                    print("Key and value both matches in aa and bb")

res = Match()
res.match_keys()