class NumberList:
    def __init__(self):
        self.mylist = []  # Boş siyahı yaradılır

    def add_numbers(self, numbers):
        """Rəqəmləri siyahıya əlavə et."""
        self.mylist.extend(numbers)  # Verilən siyahını mövcud siyahıya əlavə edirik

    def find_target_sum(self, target):
        """Verilən hədəf üçün iki rəqəmin cəmini tap."""
        # Cütləri tapmaq üçün istifadə ediləcək lüğət
        num_index = {}

        # Siyahı üzərində keçərək cütləri tapırıq
        for index, num in enumerate(self.mylist):
            # Hədəfə çatmaq üçün lazım olan tamamlayıcı rəqəm
            complement = target - num

            # Əgər tamamlayıcı rəqəm artıq lüğətdə varsa, cüt tapılıb
            if complement in num_index:
                return [num_index[complement], index]

            # Əks halda cari rəqəmi lüğətə əlavə edirik
            num_index[num] = index

        # Əgər heç bir cüt tapılmazsa, -1 qaytarırıq
        return -1


# İstifadə nümunəsi:
# Boş NumberList obyektini yaradın
nl = NumberList()

# Siyahıya rəqəmləri əlavə edin
nl.add_numbers([1, 2, 3, 4, 5])

# İstənilən hədəf üçün cütləri tapın
target = 7  # Misal üçün 7 hədəfi
result = nl.find_target_sum(target)  # Bu halda, [1, 4] indekslərini qaytarmalıdır (2 və 5 cütü)

print("Nəticə:", result)  # Çıxış: Nəticə: [1, 4]

# Başqa bir hədəf üçün cütləri yoxlayın
target = 10  # 10 hədəfi üçün -1 qaytarır
result = nl.find_target_sum(target)

print("Nəticə:", result)  # Çıxış: Nəticə: -1
