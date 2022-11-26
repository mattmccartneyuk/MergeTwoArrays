def main(array1, array2):
    occurrence_tracker = {}
    
    """
    *******************************************************
    ** The first For Loop adds the occurrences of {array1}
    ** to {occurrence_tracker}, followed by {array2}. This
    ** loop only operates twice.
    *******************************************************

    """
    current_array = array1
    for y in range(2):
        """
        *******************************************************
        ** The second For Loop checks if {current_array} already
        ** exists in the occurence tracker. If it doesn't it
        ** creates a new key/value pair. If the key/value pair
        ** does exist the key's value is incremented by +1.
        *******************************************************
        """
        for i in range(len(current_array)):
            current_number = current_array[i]
            # Checks if {current_number} already exists as a key in {occurrence_tracker}.
            if str(current_number) in occurrence_tracker:
                # .get returns the current value using the key.
                new_occurrence = occurrence_tracker.get(f"{current_number}")
                # Increments value by +1. 
                new_occurrence = str(int(new_occurrence) + 1)
                # .update changes the value held in {occurrence_tracker} using the key.
                occurrence_tracker.update({f"{current_number}": f"{new_occurrence}"})
            else:
                # Creates a new key/value pair in the occurrence tracker where {current_number} is the current_array value being considered.
                occurrence_tracker[f"{current_number}"] = "1"
        current_array = array2

    """
    *******************************************************
    ** Iterates through each entity in {occurrence_tracker},
    ** thereby string formatting based on the number of
    ** occurrences held as a value.
    *******************************************************
    """
    mergeList = []
    for x in range(len(occurrence_tracker)):
        # Retrives the key/value pair based on the array index.
        key = list(occurrence_tracker.keys())[x]
        value = list(occurrence_tracker.values())[x]

        # String formatting.
        string = (key + ", ") * int(value)
        string = string[:-2]

        # .extend creates a single one-dimensional array, as opposed to .append which is multi-dimensional.  
        mergeList.extend(string.split(','))
    
    return mergeList

if __name__ == "__main__":
    a1 = [1, 1, 2, 2, 3]
    a2 = [1, 2, 3, 4, 5, 6] 
   
    print(main(a1, a2))