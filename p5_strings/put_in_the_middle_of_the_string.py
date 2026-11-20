def make_out_word(out, word):
    return '%s%s%s' % (out[0:2], word, out[2:])

out = input()
word = input()

print(make_out_word(out, word))






# Даден е входящ низ с гарантирана дължина 4, например "<<>>", 
# и една дума. Върнете нов низ, в който думата се намира в 
# средата на входящия низ, например "<<word>>".
