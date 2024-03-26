
# Implement helper classes here

class LRCMap:
    def __init__(self, build = False):
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING

    def put_data(self, key, data):
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING

    def get_data(self, key): # returns data for that key or None if non-existant
        pass # REMOVE THIS LINE WHEN YOU START IMPLEMENTING


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    tm = LRCMap()
    tm.put_data("lrl", "THIS IS THE DATA FOR KEY lrl")
    tm.put_data("lc", "THIS IS THE DATA FOR KEY lc")
    print(tm.get_data("lrl"))
    print(tm.get_data("lrcclc"))
    print(tm.get_data("lc"))

    tm = LRCMap(True)
    tm.put_data("lrlrccr", "THIS IS THE DATA FOR KEY lrlrccr")
    tm.put_data("lrlrcclc", "THIS IS THE DATA FOR KEY lrlrcclc")
    print(tm.get_data("lrlrcclc"))
    print(tm.get_data("lrlclc"))
    print(tm.get_data("lrlrccr"))
