# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        field_names=adapter.field_names()
        for field_name in field_names:
            if field_name!='description':
                value=adapter.get(field_name)
                if value:
                    adapter[field_name]=value[0].strip()
        #category & product type->switch to lower case
        lowercase_keys=['category','product_type']
        for lowercase_key in lowercase_keys:
            value=adapter.get(lowercase_key)
            if value:
                adapter[lowercase_key]=value.lower()

        #price->convert to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            if value:
                value = value.replace('£', '').strip()  # Remove the '£' symbol and strip any extra spaces
                try:
                    adapter[price_key] = float(value)  # Convert to float and store in the correct key
                except ValueError:
                    adapter[price_key] = None
        #availability ->extract no of books in strore
        availabilty_string=adapter.get('availabilty')
        split_string_array=availabilty_string.split('(')
        if len(split_string_array)<2:
            adapter['availabilty']=0
        else:
            availabilty_array=split_string_array[1].split(' ')
            adapter['availabilty']=int(availabilty_array[0])
        #reviews=>converting string to integer
        num_reviews_string=adapter.get('num_reviews')
        adapter['num_reviews']=int(num_reviews_string)

        #stars->convert to int
        stars_string=adapter.get('stars')
        split_stars_array=stars_string.split(' ')
        stars_text_value=split_stars_array[1].lower()
        if stars_text_value=="zero":
            adapter['stars']=0
        elif stars_text_value=="one":
            adapter['stars']=1
        elif stars_text_value=="two":
            adapter['stars']=2
        elif stars_text_value=="three":
            adapter['stars']=3
        elif stars_text_value=="four":
            adapter['stars']=4
        elif stars_text_value=="five":
            adapter['stars']
        else:
            adapter['stars']=0
        return item
