def deduplicate(input_str):
   words = input_str.split(' ')
   word_freq = {}
   for word in words:
      #word = word.lower()
      if word in word_freq:
          word_freq[word] += 1
      else:
          word_freq[word] = 1
   distinct_words = [] 
   for word in word_freq.keys():
      if word_freq[word] == 1:
          distinct_words.append(word)
   return distinct_words

def sort(input_str_list):
    sorted_str_list = input_str_list
    temp = ""
    for i in range(len(sorted_str_list)):
        for j in range(len(sorted_str_list)):
            if(sorted_str_list[j] > sorted_str_list[i]):
                temp = sorted_str_list[i]
                sorted_str_list[i] = sorted_str_list[j]
                sorted_str_list[j] = temp
    return  sorted_str_list