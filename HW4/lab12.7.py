#Student name: Becky Tseng
#Student ID: 2038591

def get_age():
    age = int(input())
    # Raise exception for invalid ages
    if 18 <= age <= 75:
        return age
    raise ValueError("Invalid age.")


# Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7
    return round(heart_rate, 2)


if __name__ == "__main__":
    # Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")

