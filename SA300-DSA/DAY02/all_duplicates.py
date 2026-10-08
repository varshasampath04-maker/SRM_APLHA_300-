def find_duplicates(nums):

    seen = {}
    duplicates = []
    for num in nuums:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)

            seen.add(num)

        return duplicates
    
