def sort_string(strings):
   strings.sort()
   strings.sort(key=len)
   return strings

string_list = ["emma", "muideen", "Blessing","Zainab","Richard", "Dami"]


sorted_list = sort_string(string_list)

print(string_list, "string_list")

print(sorted_list, "sorted_list")