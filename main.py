def main():
	path_to_file = "./books/frankenstein.txt"

	with open(path_to_file) as f:
		file_contents = f.read()

	make_report(path_to_file, file_contents)

def make_report(path_to_file, string):
	print(f"--- Begin report for {path_to_file} ---")
	print(f"{word_count(string)} words found in the document")

	char_dict = char_count(string)
	chars_sorted_list = char_count_to_sorted_list(char_dict)

	for item in chars_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"The '{item['char']}' was found {item['num']} times")
	

	print("--- End report ---")

def char_count_to_sorted_list(char_count_dict):
	sorted_list = []
	for char in char_count_dict:
		sorted_list.append({"char" : char, "num" : char_count_dict[char]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list

def sort_on(d):
    return d["num"]

def word_count(sentence):
	return len(sentence.split())

def char_count(string):
	string = string.lower()
	count_dict = {}
	for char in string:
		if char in count_dict:
			count_dict[char] += 1
		else:
			count_dict[char] = 1
	return count_dict






if __name__ == "__main__":
	main()
