def index_containing_substring(the_list, substring):
        for i, s in enumerate(the_list):
                if substring in s:
                            return i
        return -1