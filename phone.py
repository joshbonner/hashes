import hashlib

def generate_phone_numbers(area_codes, numbers_per_code):
    for area_code in area_codes:
        for num in range(numbers_per_code):
            yield f"1{area_code:03d}{num:07d}"

def hash_number(number):
    return hashlib.sha256(number.encode()).hexdigest()

def main():
    area_codes = range(335)  # 335 area codes
    numbers_per_code = 299   # Generate 299 numbers per area code

    with open('phone_numbers_hashes.txt', 'w') as file:
        for number in generate_phone_numbers(area_codes, numbers_per_code):
            hash_value = hash_number(number)
            file.write(f"{hash_value}:{number}\n")

if __name__ == "__main__":
    main()
