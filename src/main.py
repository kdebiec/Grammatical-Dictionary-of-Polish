import src.dict.dictionary as dict

if __name__ == '__main__':
    dictionary = dict.Dictionary(["pospolite.txt"])
    print(dictionary.get_children("pies"))
    print(dictionary.get_parent("psa"))
    dictionary.add_gradation_relationship("adj.txt")
    print(dictionary.get_all_relationships())
    print(dictionary.get_parent("największy"))
    print(dictionary.get_word_by_relationship("hst", "największy"))
    #dictionary.add_multisegmented(["WS_tylko_rzecz.txt"])

