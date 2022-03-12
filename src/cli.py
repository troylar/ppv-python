# import arrow
# from notion_client import Client
# from rich.pretty import pprint

# from dates import DateManager

# notion = Client(auth=os.environ["NOTION_KEY"])
# search_db = notion.search(**{
#     'query': "Months",
# 	'property': 'object',
# 	'value': 'database'
# 	}).get('results')
# # pprint(search_db)

# months = notion.search(**{
#     'query': 'Months',
#     'property': 'object',
#     'value': 'page'
# }).get('results')
# id = months[0]["id"]

# pages = notion.databases.query(database_id=id).get("results")
# page_id = pages[0]["id"]
# props = pages[0]["properties"]
# pprint(props["Date"]["date"]["end"])
# props["Date"]["date"]["end"] = '2022-03-15'
# pprint(props)
# notion.pages.update(page_id=page_id, properties={"Date": {'date': {'start': '2022-03-01', 'end': '2022-03-15'}}})
# pages = notion.databases.query(database_id=id).get("results")
# pprint(pages[0]["properties"]["Date"]["date"]["end"])

# dm = DateManager(start_date=arrow.get("2022-03-12"), end_date=arrow.get("2022-09-15"))
# pprint(dm.get_weeks())
