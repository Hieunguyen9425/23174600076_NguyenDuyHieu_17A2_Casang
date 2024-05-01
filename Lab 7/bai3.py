text = '''The dog The cow my school my house my teacher A morning walk A rainy day my best friend my neighbor(a good man) my neighbor(a bad man) my father my mother my sister my brother myself Grandparents My principal Diwali Person I like the most my aim in life my grandfather my grandmother Holi visit to zoo cricket Mahatama Gandhi My country Picnic The elephant The horse The donkey The book I like the most A cricket match My school garden My school peon The policeman A hot day A cold day The postman A marriage party Chacha Nehru Sardar Patel My city My village My parents My uncle My pet animal My daily routine My watch My classroom'''

text = text.replace(".", " ")
text = text.replace(",", " ")
text = text.replace("'s", " ")
text = text.lower()

word_list = text.split()
word_count = {}

for i in range(len(word_list)):
    count = 0
    for j in range(len(word_list)):
        if word_list[i] == word_list[j]:
            count += 1
    word_count[word_list[i]] = count
print("Tần suất xuất hiện của các từ trong đoạn văn là:")
print(word_count)

most_common_word = max(word_count, key=word_count.get)
most_common_count = word_count[most_common_word]
print("Từ xuất hiện nhiều nhất là '{}' với {} lần xuất hiện.".format(most_common_word, most_common_count))

least_common_word = min(word_count, key=word_count.get)
least_common_count = word_count[least_common_word]
print("Từ xuất hiện ít nhất là '{}' với {} lần xuất hiện.".format(least_common_word, least_common_count))
