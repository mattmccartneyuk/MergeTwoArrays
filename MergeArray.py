def main(array1, array2):
    occurrence_tracker = {}
    current_array = array1
    for y in range(2): 
        for i in range(len(current_array)):
            if str(current_array[i]) in occurrence_tracker:
                number = current_array[i]
                #Get current occurrence, then + 1
                new_occurrence = occurrence_tracker.get(f"{number}")
                new_occurrence = str(int(new_occurrence) + 1)
                print(new_occurrence)
                occurrence_tracker.update({f"{number}": f"{new_occurrence}"})
            else:
                number = current_array[i]
                occurrence_tracker[f"{number}"] = "1"
        current_array = array2
    print(occurrence_tracker)
if __name__ == "__main__":
    a1 = [1, 1, 2, 2, 3]
    a2 = [1, 2, 3, 4, 5, 6] 
    # return 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6 main(a1, a2)