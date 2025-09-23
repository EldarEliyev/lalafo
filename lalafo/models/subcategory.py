from django.db import models

class SubCategory(models.Model):
    SNOWBOARDING_EQUIPMENT_CATEGORY = [
        ("helmet",  "Helmet"),
        ("bindings",  "Bindings"),
        ("goggles",  "Goggles"),
        ("snowboard_boots",  "Snowboard Boots"),
        ("snowboard_jacket",  "Snowboard Jacket"),
        ("gloves",  "Gloves"),
        ("snowboard_pants",  "Snowboard pants"),
        ("layers",  "Layers"),
        ("snowboard_googles",  "Snowboard Goggles"),
        ("jacket",  "Jacket"),
        ("backpack",  "Backpack")
    ]

    BOXING_EQUIPMENT_CATEGORY = [
        ("boxing_gloves",  "Boxing Gloves"),
        ("boxing_shoes", "Boxing Shoes"),
        ("hand_wraps",  "Hand Wraps"),
        ("punching_bags",  "Punching bags"),
        ("heavy_bag",  "Heavy Bag"),
        ("jump_rope",  "Jump Rope"),
        ("headgear",  "Headgear"),
        ("speed_bags",  "Speed bags"),
        ("hanging_punch",  "Hanging Punch"),
        ("double_end_bag",  "Double End Bag"),
    ]

    GOLF_EQUIPMENT_CATEGORY = [
        ("putters",  "Putters"),
        ("woods",  "Woods"),
        ("irons",  "Irons"),
        ("hybrids", "Hybrids"),
        ("wedges", "Wedges"),
        ("driver",  "Driver"),
        ("golf_clubs",  "Golf Clubs"),
        ("tees",  "Tees"),
        ("golf_shoes",  "Golf Shoes"),
        ("marker",  "Marker")
    ]

    TENNIS_EQUIPMENT_CATEGORY = [
        ("tennis_racket",  "Tennis Racket"),
        ("tennis_balls",  "Tennis Balls"),
        ("tennis_shoes",  "Tennis Shoes"),
        ("balls",  "Balls"),
        ("racket",  "Racket"),
        ("apparel",  "Apparel"),
        ("tennis_apparel",  "Tennis apparel"),
        ("tennis_grips",  "Tennis grips"),
        ("tennis_strings",  "Tennis strings"),
        ("babolat",  "Babolat")
    ]

    SCHOOL_EQUIPMENT_CATEGORY = [
        ("erasers",  "Erasers"),
        ("backpack",  "Backpack"),
        ("glue_sticks",  "Glue Sticks"),
        ("pencil_sharpener",  "Pencil Sharpener"),
        ("ruler",  "Ruler"),
        ("scissors",  "Scissors"),
        ("crayons",  "Crayons"),
        ("folders",  "Folders"),
        ("highlighters",  "Highlighters"),
        ("markers",  "Markers")
    ]

    FRUIT_CATEGORY = [
        ("apple",  "Apple"),
        ("apricot",  "Apricot"),
        ("banana",  "Banana"),
        ("canary_melon",  "Canary Melon"),
        ("cherry",  "Cherry"),
        ("watermelon",  "Watermelon"),
        ("currants",  "Currants"),
        ("grape",  "Grape"),
        ("kiwi",  "Kiwi"),
        ("dragon_fruit",  "Dragon Fruit")
    ]

    VEGETABLE_CATEGORY = [
        ("carrot",  "Carrot"),
        ("broccoli",  "Broccoli"),
        ("cabbage",  "Cabbage"),
        ("cauliflower",  "Cauliflower"),
        ("spinach",  "Spinach"),
        ("cucumber",  "Cucumber"),
        ("eggplant",  "Eggplant"),
        ("onion",  "Onion"),
        ("peas",  "Peas"),
        ("artichoke",  "Artichoke")
    ]

    snowboard_subcategory = models.CharField(max_length=42, choices=SNOWBOARDING_EQUIPMENT_CATEGORY, default="helmet",  null=True,  blank=True)
    box_equipment_subcategory = models.CharField(max_length=42, choices=BOXING_EQUIPMENT_CATEGORY, default="boxing_gloves",  null=True, blank=True)
    golf_equipment_subcategory = models.CharField(max_length=42, choices=GOLF_EQUIPMENT_CATEGORY, default="putters",  null=True, blank=True)
    tennis_equipment_subcategory = models.CharField(max_length=42, choices=GOLF_EQUIPMENT_CATEGORY, default="tennis_balls",  null=True, blank=True)
    school_equipment_subcategory = models.CharField(max_length=42, choices=SCHOOL_EQUIPMENT_CATEGORY, default="erasers",  null=True, blank=True)
    fruit_subcategory = models.CharField(max_length=42, choices=FRUIT_CATEGORY, default="apple",  null=True, blank=True)
    vegetable_subcategory = models.CharField(max_length=42, choices=VEGETABLE_CATEGORY, default="carrot",  null=True, blank=True)

    def __str__(self):
        return self.snowboard_subcategory or self.box_equipment_subcategory or self.golf_equipment_subcategory or self.tennis_equipment_subcategory or self.school_equipment_subcategory or self.fruit_subcategory or self.vegetable_subcategory
    
