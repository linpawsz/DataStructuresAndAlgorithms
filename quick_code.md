
# Quick Tips and Tricks
 
Making lists and dictionaries  
> str = "abcdefghijklmnopqrstuvwxyz"  
> alphabets = [i for i in list(map(list, enumerate(str)))]  
> key_value_pairs_dict = dict(alphabets)

  