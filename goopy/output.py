TITLE = "\033[4m\033[94m"
GREEN = "\033[32m"
END = "\033[0m"

def print_results(results):
    for result in results:
        print_result(result)

def print_result(result):
    print_format(result.title, TITLE)
    print_format(result.display_link, GREEN)
    print result.snippet
    print

def print_format(text, format):
    print "%s%s%s" % (format, text, END)