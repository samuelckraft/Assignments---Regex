#Task 1
import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

def tag_product(description):
    keywords = {
        'Electronics': ['smartphone', 'tablet', 'laptop', 'camera'],
        'Apparel': ['t-shirt', 'shirt', 'jeans', 'dress'],
        'Home and Kitchen': ['knife', 'kitchen', 'utensils', 'appliance']
    }

    for category, category_keywords in keywords.items():
        for keyword in category_keywords:
            if re.search(keyword, description, re.IGNORECASE): #returns none if search turns up nothing
                return category
    return "Uncategorized"


for description in descriptions:
    print(f"{description}: {tag_product(description)}")